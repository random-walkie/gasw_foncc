from json import loads
import re

class HTTPResponse:
    """Represents an HTTP response with parsing and analysis capabilities."""

    def __init__(self, raw_response: bytes) -> None:
        """Initialize a response object from raw HTTP response data.

        Args:
            raw_response: The raw bytes of the HTTP response
        """
        # Store raw response
        self.raw_response = raw_response
        # Initialize properties (status_code, headers, body, etc.)
        self.status_code = None
        self.status_message = None
        self.headers = {}
        self.body = None
        # Parse the response
        self.parse_response()

    def parse_response(self) -> None:
        """Parse the raw HTTP response into components."""
        # Split headers and body (separated by \r\n\r\n)
        boundary_idx = self.raw_response.find(b"\r\n\r\n")

        if boundary_idx >= 0:
            headers = self.raw_response[0:boundary_idx]
            self.body = self.raw_response[boundary_idx+4:]
        else:
            headers = self.raw_response
            self.body = b""

        header_lines = headers.split(b"\r\n")

        # Parse status line to get status code and message
        status_line = header_lines[0]
        status_parts = status_line.split(b" ")
        self.status_code = int(status_parts[1])
        self.status_message = b" ".join(status_parts[2:]).decode("utf-8")
        print(self.status_message)

        # Parse header lines into a dictionary
        for line in header_lines[1:]:
            if len(line) > 0:
                parts = line.split(b": ")
                # I have to do this, because we may have repeated header names, such as Set-Cookies
                self.headers.setdefault(parts[0].decode("utf-8"), []).append(parts[1].decode("utf-8"))

    def is_success(self) -> bool:
        """Check if the response indicates success (2xx status)."""
        # Implement success check
        if 200 <= self.status_code < 300:
            return True
        else:
            return False

    def get_content_type(self) -> str:
        """Get the Content-Type of the response."""
        # Implement content type retrieval
        return self.headers.get('Content-Type')

    def get_content_length(self) -> int:
        """Get the Content-Length of the response."""
        # Implement content length retrieval
        if self.headers.get('Content-Length') is None:
            return len(self.body)
        else:
            return int(self.headers.get('Content-Length')[0])

    def get_session_info(self) -> dict:
        """Extract session information from response."""
        # Extract and return cookies and other session-related headers
        session_info = {'cookies': self.headers.get('Set-Cookie'), 'cache_control': self.headers.get('Cache-Control')}

        return session_info

    def get_decoded_body(self):
        """Attempt to decode the response body based on Content-Type."""
        # Handle different content types:
        # - application/json: parse as JSON
        # - text/*: decode as text with appropriate charset
        # - image/* or other binary: indicate binary data
        text_type_regex = re.compile(r'text/*')
        if "application/json" in self.get_content_type():
            return loads(self.body)
        elif any((match := text_type_regex.search(item)) for item in self.get_content_type()):
            return self.body.decode("utf-8")
        else:
            return "Binary data"