import unittest
from response import HTTPResponse

class TestHTTPResponse(unittest.TestCase):
    """Test suite for the HTTPResponse class.

    These tests verify that the HTTPResponse class correctly parses
    and analyzes HTTP responses according to protocol specifications.
    """

    def test_basic_response_parsing(self):
        """Test parsing of a basic HTTP response with a simple status line and headers."""
        response = HTTPResponse(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 13\r\n\r\nHello, World!")

        # Verify status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_message, "OK")

        # Verify headers
        self.assertEqual(response.headers["Content-Type"], ["text/plain"])
        self.assertEqual(response.headers["Content-Length"], ["13"])

        # Verify body
        self.assertEqual(response.body, b"Hello, World!")

    def test_response_without_body(self):
        """Test parsing a response that has no body."""
        response = HTTPResponse(b"HTTP/1.1 204 No Content\r\nServer: TestServer\r\nDate: Mon, 01 Jan 2023 12:00:00 GMT\r\n\r\n")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.status_message, "No Content")
        self.assertEqual(response.body, b"")

    def test_response_with_multiple_headers(self):
        """Test parsing a response with multiple headers."""
        response = HTTPResponse((
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: 2\r\n"
            b"Cache-Control: max-age=3600\r\n"
            b"Server: TestServer\r\n"
            b"Set-Cookie: session=abc123; Path=/\r\n"
            b"\r\n"
            b"{}"
        ))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.headers), 5)
        self.assertEqual(response.headers["Cache-Control"], ["max-age=3600"])
        self.assertEqual(response.headers["Set-Cookie"], ["session=abc123; Path=/"])

    def test_error_response(self):
        """Test parsing an error response (4xx status code)."""
        response = HTTPResponse(b"HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 9\r\n\r\nNot Found")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.status_message, "Not Found")
        self.assertEqual(response.body, b"Not Found")
        self.assertFalse(response.is_success())

    def test_redirect_response(self):
        """Test parsing a redirect response (3xx status code)."""
        response = HTTPResponse(b"HTTP/1.1 302 Found\r\nLocation: https://example.com/new-location\r\n\r\n")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.status_message, "Found")
        self.assertEqual(response.headers["Location"], ["https://example.com/new-location"])
        self.assertFalse(response.is_success())

    def test_incomplete_response(self):
        """Test parsing an incomplete response."""
        # Missing the \r\n\r\n separator and body
        response = HTTPResponse(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 13")

        # The parser should still extract what it can
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], ["text/plain"])
        self.assertEqual(response.body, b"")

    def test_malformed_status_line(self):
        """Test handling of a malformed status line."""
        # Missing status message
        response = HTTPResponse(b"HTTP/1.1 200\r\nContent-Type: text/plain\r\n\r\nHello")

        # Should still parse the status code correctly
        self.assertEqual(response.status_code, 200)
        # Status message might be empty, but not None
        self.assertIsNotNone(response.status_message)

    def test_is_success_with_success_status(self):
        response = HTTPResponse(b"HTTP/1.1 200\r\nContent-Type: text/plain\r\n\r\nHello")
        self.assertTrue(response.is_success())

    def test_is_success_with_not_success_status(self):
        response = HTTPResponse(b"HTTP/1.1 404 Not Found\r\nContent-Length: 9\r\n\r\nNot Found")
        self.assertFalse(response.is_success())

    def test_is_success_with_boundary_status(self):
        response = HTTPResponse(b"HTTP/1.1 300 Multiple Choices\r\nContent-Length: 15\r\n\r\nMultiple Choices")
        self.assertFalse(response.is_success())

        response = HTTPResponse(b"HTTP/1.1 199 OK\r\nContent-Length: 2\r\n\r\nOK")
        self.assertFalse(response.is_success())

    def test_get_content_type(self):
        """Test the get_content_type helper method."""
        raw_response = b"HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n{}"

        response = HTTPResponse(raw_response)

        self.assertEqual(response.get_content_type(), ["application/json; charset=utf-8"])

    def test_get_content_length(self):
        """Test the get_content_length helper method."""
        raw_response = b"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!"

        response = HTTPResponse(raw_response)

        self.assertEqual(response.get_content_length(), 13)

        # Test when Content-Length header is missing
        raw_response = b"HTTP/1.1 200 OK\r\n\r\nHello, World!"
        response = HTTPResponse(raw_response)

        # Should fall back to the actual body length
        self.assertEqual(response.get_content_length(), 13)

    def test_get_session_info(self):
        """Test extraction of session information from response."""
        response = HTTPResponse(
            b"HTTP/1.1 200 OK\r\n"
            b"Set-Cookie: session=abc123; Path=/; HttpOnly\r\n"
            b"Set-Cookie: user=john; Path=/account\r\n"
            b"Cache-Control: private, max-age=3600\r\n"
            b"\r\n")
        session_info = response.get_session_info()

        # Check that cookies were extracted
        self.assertIn('cookies', session_info)
        self.assertEqual(len(session_info['cookies']), 2)
        self.assertIn('session=abc123; Path=/; HttpOnly', session_info['cookies'])

        # Check that cache control was extracted
        self.assertEqual(session_info['cache_control'], ['private, max-age=3600'])

    def test_get_decoded_body_success_json(self):
        # Given a HTTP response with JSON content
        response = HTTPResponse(b'HTTP/1.1 200 OK\r\n' \
                                b'Content-Length: 17\r\n' \
                                b'Content-Type: application/json\r\n' \
                                b'\r\n' \
                                b'{ "Key": "Value" }')
        expected_decoded_body = {"Key": "Value"}

        # When get_decoded_body() method is called
        decoded_body = response.get_decoded_body()

        # Then the decoded body should match the expected decoded body
        self.assertEqual(expected_decoded_body, decoded_body)

    def test_get_decoded_body_success_text(self):
        # Given a HTTP response with plain text content
        raw_response = b'HTTP/1.1 200 OK\r\n' \
                       b'Content-Length: 4\r\n' \
                       b'Content-Type: text/plain\r\n' \
                       b'\r\n' \
                       b'Test'
        response = HTTPResponse(raw_response)
        expected_decoded_body = "Test"

        # When get_decoded_body() method is called
        decoded_body = response.get_decoded_body()

        # Then the decoded body should match the expected decoded body
        self.assertEqual(expected_decoded_body, decoded_body)

    def test_get_decoded_body_unknown_content_type(self):
        # Given a HTTP response with an unknown content type
        raw_response = b'HTTP/1.1 200 OK\r\n' \
                       b'Content-Length: 4\r\n' \
                       b'Content-Type: unknown/dummy\r\n' \
                       b'\r\n' \
                       b'Data'
        response = HTTPResponse(raw_response)
        expected_message = b"Data"

        # When get_decoded_body() method is called
        decoded_body = response.get_decoded_body()

        # Then the returned value should be the raw response
        self.assertEqual(decoded_body, expected_message)