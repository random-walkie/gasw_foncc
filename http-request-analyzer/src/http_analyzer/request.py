from urllib.parse import urlparse

class HTTPRequest:
    """Represents an HTTP request with all its components.

    This class handles the Application Layer (Layer 7) aspects of HTTP,
    specifically the formatting and parameters of HTTP requests.
    """

    def __init__(self, method, url, headers=None, body=None):
        """Initialize an HTTP request object.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: Full URL for the request
            headers: None or dictionary of HTTP headers
            body: Optional request body
        """
        # Initialize basic properties
        self.method = method.upper()
        self.url = url

        # Use a new dictionary instead of modifying the provided one
        # This ensures no side effects on the input headers
        self.headers = {} if headers is None else headers.copy()

        self.body = body

        # Parse URL components using urllib.parse
        parsed_url = urlparse(url)
        self.scheme = parsed_url.scheme
        self.host = parsed_url.netloc
        self.path = parsed_url.path or '/'
        self.query = parsed_url.query

        # Add default headers if not present
        if 'Host' not in self.headers:
            self.headers['Host'] = self.host

        # Set content length if body is provided
        if self.body is not None and 'Content-Length' not in self.headers:
            self.headers['Content-Length'] = str(len(self.body))

    def format_request(self):
        """Format the HTTP request as it would appear on the wire."""

        # Build the request line (METHOD PATH)
        request_line = f"{self.method} {self.path}"
        # Check if query is present, add if yes
        if self.query:
            request_line += f"?{self.query}"

        request_line += f" HTTP/1.1\r\n"
        
        # Format headers as Name: Value
        headers = ""
        for name, value in self.headers.items():
            headers += f"{name}: {value}\r\n"

        # Add empty line and body if present
        body = "" if self.body is None else self.body
        request = f"{request_line}{headers}\r\n{body}"
        return request

    def get_content_type(self):
        """Get the Content-Type header if set."""
        # Implement content type retrieval
        if self.headers.get('Content-Type'):
            return self.headers.get('Content-Type')


    def get_session_info(self):
        """Extract session information (cookies, etc.)."""
        # TODO: Extract and return cookie and authorization info
        pass