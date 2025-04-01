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

        request = HTTPRequest("GET", "http://example.com/path", body="body")

        # Content-Length header should equal body length, if body is not None
        self.assertEqual(request.headers["Content-Length"], "4")

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

    def test_format_request_with_query_parameters(self):
        """Test formatting a request with query parameters in the URL."""
        request = HTTPRequest("GET", "http://api.example.com/search?q=python&sort=relevance")

        formatted = request.format_request()

        # The path should include the query string
        self.assertTrue(formatted.startswith("GET /search?q=python&sort=relevance HTTP/1.1\r\n"))

        # The Host header should match the domain
        self.assertIn("Host: api.example.com\r\n", formatted)

    def test_format_request_post_with_body(self):
        """Test formatting a POST request with a body."""
        body = "name=test&message=hello"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        request = HTTPRequest("POST", "http://example.com/submit", headers=headers, body=body)

        formatted = request.format_request()

        # Check request line
        self.assertTrue(formatted.startswith("POST /submit HTTP/1.1\r\n"))

        # Verify all headers are included
        self.assertIn("Host: example.com\r\n", formatted)
        self.assertIn("Content-Type: application/x-www-form-urlencoded\r\n", formatted)

        # Content-Length should be added automatically
        self.assertIn(f"Content-Length: {len(body)}\r\n", formatted)

        # Body should be included after the headers
        self.assertTrue(formatted.endswith(f"\r\n\r\n{body}"))

    def test_format_request_with_multiple_headers(self):
            """Test formatting a request with multiple custom headers."""
            headers = {
                "User-Agent": "MyClient/1.0",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9",
                "Authorization": "Bearer token123"
            }

            request = HTTPRequest("GET", "http://api.example.com/resource", headers=headers)

            formatted = request.format_request()

            # Check that all headers are included
            for name, value in headers.items():
                self.assertIn(f"{name}: {value}\r\n", formatted)

            # And the default Host header should still be there
            self.assertIn("Host: api.example.com\r\n", formatted)

    def test_format_request_with_json_body(self):
        """Test formatting a request with a JSON body."""
        json_body = '{"name": "test", "message": "hello"}'
        headers = {
            "Content-Type": "application/json"
        }

        request = HTTPRequest("POST", "http://api.example.com/data", headers=headers, body=json_body)

        formatted = request.format_request()

        # Check content type and length headers
        self.assertIn("Content-Type: application/json\r\n", formatted)
        self.assertIn(f"Content-Length: {len(json_body)}\r\n", formatted)

        # The JSON body should be included verbatim
        self.assertTrue(formatted.endswith(f"\r\n\r\n{json_body}"))

    def test_format_request_preserves_header_case(self):
        """Test that the original header case is preserved in formatting."""
        headers = {
            "Content-Type": "text/plain",
            "X-Custom-Header": "value"
        }

        request = HTTPRequest("GET", "http://example.com", headers=headers)

        formatted = request.format_request()

        # Headers should keep their original case
        self.assertIn("Content-Type: text/plain\r\n", formatted)
        self.assertIn("X-Custom-Header: value\r\n", formatted)

    def test_format_request_root_path(self):
        """Test formatting a request to the root path."""
        request = HTTPRequest("GET", "http://example.com")

        formatted = request.format_request()

        # The path should be '/' when none is specified
        self.assertTrue(formatted.startswith("GET / HTTP/1.1\r\n"))

    def test_format_request_http_version(self):
        """Test that the HTTP version is correctly specified."""
        request = HTTPRequest("GET", "http://example.com")

        formatted = request.format_request()

        # Make sure we're using HTTP/1.1
        self.assertIn(" HTTP/1.1\r\n", formatted)

    def test_format_request_edge_cases(self):
        """Test formatting requests with various edge cases."""

        # Test with an unusual HTTP method
        request = HTTPRequest("OPTIONS", "http://example.com")
        formatted = request.format_request()
        self.assertTrue(formatted.startswith("OPTIONS / HTTP/1.1\r\n"))

        # Test with a URL that has a fragment (which should be ignored in the request)
        request = HTTPRequest("GET", "http://example.com/page#section")
        formatted = request.format_request()
        self.assertTrue(formatted.startswith("GET /page HTTP/1.1\r\n"))
        self.assertNotIn("#section", formatted)

        # Test with a URL that includes authentication information
        request = HTTPRequest("GET", "http://user:pass@example.com")
        formatted = request.format_request()
        self.assertIn("Host: user:pass@example.com\r\n", formatted)

    def test_get_content_type(self):
        """Test that get_content_type correctly retrieves the Content-Type header."""

        # Test with no Content-Type header
        request = HTTPRequest("GET", "http://example.com")
        self.assertIsNone(request.get_content_type(),
                          "Should return None when no Content-Type header exists")

        # Test with a simple Content-Type header
        headers = {"Content-Type": "text/html"}
        request = HTTPRequest("GET", "http://example.com", headers=headers)
        self.assertEqual(request.get_content_type(), "text/html",
                         "Should return the exact Content-Type value")

        # Test with a Content-Type that includes parameters
        headers = {"Content-Type": "application/json; charset=utf-8"}
        request = HTTPRequest("GET", "http://example.com", headers=headers)
        self.assertEqual(request.get_content_type(), "application/json; charset=utf-8",
                         "Should return the full Content-Type including parameters")

        # Test with multiple headers
        headers = {
            "Content-Type": "application/xml",
            "Accept": "application/json",
            "User-Agent": "TestClient/1.0"
        }
        request = HTTPRequest("GET", "http://example.com", headers=headers)
        self.assertEqual(request.get_content_type(), "application/xml",
                         "Should correctly find Content-Type among multiple headers")

    def test_get_session_info_empty(self):
        """Test session info extraction when no session-related headers are present."""
        request = HTTPRequest("GET", "http://example.com")

        session_info = request.get_session_info()

        # Even with no session headers, the method should return a dictionary
        self.assertIsInstance(session_info, dict, "Session info should always be a dictionary")

        # Dictionary should have expected keys, even if their values are empty
        self.assertIn('cookies', session_info, "Session info should include 'cookies' key")
        self.assertIn('authorization', session_info, "Session info should include 'authorization' key")

        # Values should be empty or None for non-existent headers
        self.assertFalse(session_info['cookies'], "Cookies should be empty when no Cookie header exists")
        self.assertFalse(session_info['authorization'], "Authorization should be empty when no Authorization header exists")

    def test_get_session_info_with_cookies(self):
        """Test session info extraction when Cookie header is present."""
        # Create a request with a Cookie header
        headers = {"Cookie": "sessionid=abc123; user=john"}
        request = HTTPRequest("GET", "http://example.com", headers=headers)

        session_info = request.get_session_info()

        # The cookies value should match the Cookie header
        self.assertEqual(session_info['cookies'], "sessionid=abc123; user=john",
                         "Cookies value should match the Cookie header exactly")

        # Authorization should still be empty
        self.assertFalse(session_info['authorization'], "Authorization should be empty when no Authorization header exists")

    def test_get_session_info_with_authorization(self):
        """Test session info extraction when Authorization header is present."""
        # Create a request with an Authorization header
        headers = {"Authorization": "Bearer token123"}
        request = HTTPRequest("GET", "http://example.com", headers=headers)

        session_info = request.get_session_info()

        # The authorization value should match the Authorization header
        self.assertEqual(session_info['authorization'], "Bearer token123",
                         "Authorization value should match the Authorization header exactly")

        # Cookies should still be empty
        self.assertFalse(session_info['cookies'], "Cookies should be empty when no Cookie header exists")

    def test_get_session_info_with_both(self):
        """Test session info extraction when both Cookie and Authorization headers are present."""
        # Create a request with both Cookie and Authorization headers
        headers = {
            "Cookie": "sessionid=abc123; user=john",
            "Authorization": "Bearer token123"
        }
        request = HTTPRequest("GET", "http://example.com", headers=headers)

        session_info = request.get_session_info()

        # Both values should match their respective headers
        self.assertEqual(session_info['cookies'], "sessionid=abc123; user=john",
                         "Cookies value should match the Cookie header exactly")
        self.assertEqual(session_info['authorization'], "Bearer token123",
                         "Authorization value should match the Authorization header exactly")

    def test_get_session_info_case_insensitivity(self):
        """Test that session info extraction works regardless of header case."""
        # Create a request with differently-cased headers
        headers = {
            "cookie": "sessionid=abc123",  # lowercase
            "AUTHORIZATION": "Basic dXNlcjpwYXNz"  # uppercase
        }
        request = HTTPRequest("GET", "http://example.com", headers=headers)

        session_info = request.get_session_info()

        # The method should be case-insensitive when looking for headers
        self.assertEqual(session_info['cookies'], "sessionid=abc123",
                         "Cookies should be found regardless of header case")
        self.assertEqual(session_info['authorization'], "Basic dXNlcjpwYXNz",
                         "Authorization should be found regardless of header case")

if __name__ == '__main__':
    unittest.main()
