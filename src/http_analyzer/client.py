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

            # Read the response with better timeout handling
            response_data = b""
            sock.settimeout(timeout)  # Ensure timeout is set for receiving

            # Read until we have a complete HTTP message or timeout
            while True:
                try:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response_data += chunk

                    # Optional: Check if we have a complete HTTP message
                    if b"\r\n\r\n" in response_data:
                        # If we've received headers, try to determine content length
                        headers_end = response_data.find(b"\r\n\r\n") + 4
                        headers = response_data[:headers_end]

                        # Check if we have Content-Length header
                        content_length_match = b"Content-Length: " in headers
                        if content_length_match:
                            # Extract content length value
                            header_start = headers.find(b"Content-Length: ") + 16
                            header_end = headers.find(b"\r\n", header_start)
                            content_length = int(headers[header_start:header_end])

                            # If we've received the complete message, break
                            if len(response_data) >= headers_end + content_length:
                                break

                except socket.timeout:
                    # If we've received some data but timed out before completion,
                    # we'll still try to parse what we have
                    if response_data:
                        break
                    else:
                        raise TimeoutError("Request timed out - no data received")

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