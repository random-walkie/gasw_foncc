import socket
from urllib.parse import urlparse
from http_analyzer.response import HTTPResponse
from http_analyzer.ssl_handler import SSLHandler

from http_analyzer.request import HTTPRequest


class HTTPClient:
    """Handles the low-level HTTP communication.

    This class is responsible for establishing connections,
    sending requests, and receiving responses.
    """

    def __init__(self):
        """Initialize the HTTP client."""
        # Initialize connection tracking
        # Dictionary to store persistent connections
        self.connections = {}

    def send_request(self, request: HTTPRequest, timeout=10):
        """Send an HTTP request and return the response.

        Args:
            request: HTTPRequest object containing the request details
            timeout: Socket timeout in seconds

        Returns:
            HTTPResponse: The response from the server
        """
        # Extract connection details from the request URL
        # Parse URL to get scheme, host, port
        parsed_url = urlparse(request.url)
        scheme = parsed_url.scheme
        host = parsed_url.hostname
        port = parsed_url.port or (443 if scheme == "https" else 80)

        # Determine if we should use an existing connection
        # Create a connection identifier
        connection_id = f"{host}:{port}"
        # Check Connection header to see if keep-alive is requested
        reuse_connections = request.headers.get("Connection", "").lower() == "keep-alive"
        # Look for an existing connection in self.connections
        sock = None
        if reuse_connections and connection_id in self.connections:
            sock = self.connections[connection_id]

        # Create a new connection if needed
        # Create socket
        if sock is None or sock._closed:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                # Connect to host:port
                sock.connect((host, port))
                # For HTTPS, wrap with SSL
                if scheme == "https":
                  sock = SSLHandler.wrap_socket(sock, host)

                # Store for reuse if keep-alive
                if reuse_connections:
                    self.connections[connection_id] = sock

            except Exception as e:
                # Make sure to close the socket before re-raising as ConnectionError
                sock.close()
                raise ConnectionError(f"Error connecting to {host}:{port}: {e}")

        try:
            # Format and send the request
            # Get the fully formatted request string from the request object
            formatted_request = request.format_request().encode("utf-8")
            # Send it over the socket
            sock.sendall(formatted_request)

            # Read the response
            # Read the raw response bytes from the socket
            response_data = b""
            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response_data += chunk

            # Parse response into HTTPResponse object
            response = HTTPResponse(response_data)

            # Handle connection management
            # If Connection: close header found, close the socket
            connection_header = response.headers.get("Connection", "")
            if connection_header and connection_header[0].lower() == "close" or not reuse_connections:
                sock.close()
                # Otherwise keep it open for reuse
                if connection_id in self.connections:
                    del self.connections[connection_id]
            # Return the response object
            return response

        except Exception as e:
            sock.close()
            if connection_id in self.connections:
                del self.connections[connection_id]
            raise e

    def close(self):
        """Close all open connections."""
        # Close all open socket connections
        # Iterate through connections dictionary
        for sock in self.connections.values():
            try:
                # Close each socket
                sock.close()
            except:
                pass
        # Clear the dictionary
        self.connections.clear()

    def __del__(self):
        """Destructor to ensure connections are closed."""
        # Call close() method
        self.close()