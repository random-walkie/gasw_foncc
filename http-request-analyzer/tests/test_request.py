import unittest
from src.http_analyzer.request import HTTPRequest

class TestHTTPRequest(unittest.TestCase):
    """Test suite for the HTTPRequest class.

    These tests verify that the HTTPRequest class correctly handles
    HTTP request creation, URL parsing, and request formatting according
    to HTTP protocol specifications.
    """

    def test_request_initialization_basic(self):
        """Test that a request is properly initialized with minimal parameters."""
        # Create a simple GET request
        request = HTTPRequest("GET", "http://example.com/path")

        # Verify basic properties
        self.assertEqual(request.method, "GET")
        self.assertEqual(request.url, "http://example.com/path")
        self.assertEqual(request.scheme, "http")
        self.assertEqual(request.host, "example.com")
        self.assertEqual(request.path, "/path")
        self.assertEqual(request.query, "")

        # Default headers should be set
        self.assertEqual(request.headers["Host"], "example.com")

        # Body should be None by default
        self.assertIsNone(request.body)

    def test_format_request_get_simple(self):
        """Test formatting a simple GET request with no query parameters or body."""
        request = HTTPRequest("GET", "http://example.com/index.html")

        formatted = request.format_request()

        # Check that the request line is properly formatted
        self.assertTrue(formatted.startswith("GET /index.html HTTP/1.1\r\n"))

        # Verify the Host header is included
        self.assertIn("Host: example.com\r\n", formatted)

        # The request should end with an empty line (headers-body separator)
        self.assertTrue(formatted.endswith("\r\n\r\n"))

        # No body should be present for a GET request
        self.assertEqual(formatted.count("\r\n\r\n"), 1, "There should be exactly one headers-body separator")



if __name__ == '__main__':
    unittest.main()
