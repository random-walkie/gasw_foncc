import unittest
from unittest.mock import Mock
from http_analyzer.session import HTTPSession
from http_analyzer.request import HTTPRequest

class TestHTTPSession(unittest.TestCase):
    """Test suite for the HTTPSession class.

    These tests verify that the HTTPSession class correctly manages cookies,
    builds proper requests, and correctly processes responses.
    """

    def setUp(self):
        """Set up test environment before each test case."""
        # Create a session for testing
        self.session = HTTPSession()

        # Mock the client for testing without actual HTTP calls
        self.session.client = Mock()

        # Create a sample response for the mocked client to return
        # Instead of using Mock(spec=HTTPResponse), create a more complete mock:
        self.mock_response = Mock()
        self.mock_response.status_code = 200
        self.mock_response.headers = {}
        self.mock_response.body = b"Test response"
        self.session.client.send_request.return_value = self.mock_response

    def test_post_basic(self):
        """Test a basic POST request with no special headers or body."""
        # Call the post method
        response = self.session.post("http://example.com/api")

        # Verify client.send_request was called
        self.session.client.send_request.assert_called_once()

        # Get the request that was passed to send_request
        request = self.session.client.send_request.call_args[0][0]

        # Verify request properties
        self.assertEqual(request.method, "POST")
        self.assertEqual(request.url, "http://example.com/api")
        self.assertEqual(request.host, "example.com")

        # Verify default headers are present
        self.assertIn("User-Agent", request.headers)
        self.assertEqual(request.headers["User-Agent"], "HTTPAnalyzer/1.0")

        # Verify the response is what we expected
        self.assertEqual(response, self.mock_response)

    def test_post_with_json(self):
        """Test POST request with JSON data."""
        # Set up test data
        test_json = {"name": "test", "value": 123}

        # Call post with JSON
        self.session.post("http://example.com/api", json=test_json)

        # Get the request that was passed to send_request
        request = self.session.client.send_request.call_args[0][0]

        # Verify Content-Type header is set correctly
        self.assertIn("Content-Type", request.headers)
        self.assertIn("application/json", request.headers["Content-Type"])

        # Verify body contains the JSON data
        self.assertIsNotNone(request.body)

    def test_post_with_form_data(self):
        """Test POST request with form data."""
        # Set up test data
        test_data = {"username": "testuser", "password": "testpass"}

        # Call post with data dict
        self.session.post("http://example.com/login", data=test_data)

        # Get the request that was passed to send_request
        request = self.session.client.send_request.call_args[0][0]

        # Verify Content-Type header is set correctly
        self.assertIn("Content-Type", request.headers)
        self.assertEqual(request.headers["Content-Type"], "application/x-www-form-urlencoded")

        # Verify body contains the form data
        self.assertIsNotNone(request.body)
        body_str = request.body.decode('utf-8')
        # Check that each key-value pair is in the form data
        for key, value in test_data.items():
            self.assertIn(f"{key}={value}", body_str)

    def test_post_with_custom_headers(self):
        """Test POST request with custom headers."""
        # Set up test headers
        test_headers = {
            "X-API-Key": "testapikey123",
            "Accept": "application/json"
        }

        # Call post with custom headers
        self.session.post("http://example.com/api", headers=test_headers)

        # Get the request that was passed to send_request
        request = self.session.client.send_request.call_args[0][0]

        # Verify custom headers are included
        self.assertIn("X-API-Key", request.headers)
        self.assertEqual(request.headers["X-API-Key"], "testapikey123")
        self.assertEqual(request.headers["Accept"], "application/json")

    def test_post_with_cookies(self):
        """Test that cookies are included in request headers."""
        # Set up some cookies for the session
        self.session.cookies = {
            "example.com": {
                "sessionid": "abc123",
                "user": "testuser"
            }
        }

        # Call post method
        self.session.post("http://example.com/api")

        # Get the request that was passed to send_request
        request = self.session.client.send_request.call_args[0][0]

        # Verify Cookie header is included and properly formatted
        self.assertIn("Cookie", request.headers)
        # Cookies should be in format "name1=value1; name2=value2"
        # But we don't guarantee order, so check parts separately
        cookie_header = request.headers["Cookie"]
        self.assertIn("sessionid=abc123", cookie_header)
        self.assertIn("user=testuser", cookie_header)

    def test_cookie_handling_from_response(self):
        """Test that cookies from response are stored in session."""
        # Set up mock response with Set-Cookie headers
        self.mock_response.headers = {
            "Set-Cookie": ["sessionid=xyz789; Path=/", "user=newuser; Path=/"]
        }

        # Call post method
        self.session.post("http://example.com/api")

        # Verify cookies were extracted and stored
        self.assertIn("example.com", self.session.cookies)
        self.assertEqual(self.session.cookies["example.com"]["sessionid"], "xyz789")
        self.assertEqual(self.session.cookies["example.com"]["user"], "newuser")

    def test_request_history(self):
        """Test that request and response are added to history."""
        # Call post method
        self.session.post("http://example.com/api")

        # Verify request/response pair was added to history
        self.assertEqual(len(self.session.history), 1)
        request, response = self.session.history[0]
        self.assertIsInstance(request, HTTPRequest)
        self.assertEqual(response, self.mock_response)

    def test_session_close(self):
        """Test that close method properly closes client."""
        # Call close method
        self.session.close()

        # Verify client.close was called
        self.session.client.close.assert_called_once()

    def test_content_handler_integration(self):
        """Test integration with ContentHandler for JSON encoding."""
        # Create a mock ContentHandler
        mock_content_handler = Mock()
        mock_content_handler.encode_content.return_value = (b'{"data":"test"}', "application/json; charset=utf-8")

        # Inject the mock into the session
        self.session.content_handler = mock_content_handler

        # Call post with JSON
        self.session.post("http://example.com/api", json={"data": "test"})

        # Verify ContentHandler.encode_content was called
        mock_content_handler.encode_content.assert_called_once()

    def test_error_handling_data_and_json(self):
        """Test error handling when both data and json are provided."""
        # Call post with both data and json, should raise ValueError
        with self.assertRaises(ValueError):
            self.session.post("http://example.com/api",
                              data={"form": "data"},
                              json={"json": "data"})

    def test_get_method(self):
        """Test the GET method works correctly."""
        # Call get method
        response = self.session.get("http://example.com/resource")

        # Verify client.send_request was called
        self.session.client.send_request.assert_called_once()

        # Get the request that was passed to send_request
        request = self.session.client.send_request.call_args[0][0]

        # Verify request method is GET
        self.assertEqual(request.method, "GET")

        # Verify the response is what we expected
        self.assertEqual(response, self.mock_response)

    def test_session_cookies_across_requests(self):
        """Test that cookies are maintained across multiple requests."""
        # Set up initial response with cookies
        self.mock_response.headers = {
            "Set-Cookie": ["sessionid=abc123; Path=/"]
        }

        # Make first request to get cookies
        self.session.post("http://example.com/login")

        # Reset mock and response headers for second request
        self.session.client.reset_mock()
        self.mock_response.headers = {}

        # Make second request
        self.session.get("http://example.com/profile")

        # Verify the cookie was sent with the second request
        request = self.session.client.send_request.call_args[0][0]
        self.assertIn("Cookie", request.headers)
        self.assertIn("sessionid=abc123", request.headers["Cookie"])

    def test_timeout_parameter(self):
        """Test that timeout parameter is passed to client."""
        # Call post with custom timeout
        self.session.post("http://example.com/api", timeout=30)

        # Verify timeout was passed to client.send_request
        self.session.client.send_request.assert_called_with(
            unittest.mock.ANY,  # We don't need to verify the request object again
            timeout=30
        )

    def test_different_domain_cookies(self):
        """Test that cookies are domain-specific."""
        # Set up cookies for example.com
        self.session.cookies = {
            "example.com": {"sessionid": "example-session"}
        }

        # Make request to different domain
        self.session.get("http://other-domain.com/resource")

        # Verify that cookies for example.com weren't sent
        request = self.session.client.send_request.call_args[0][0]
        self.assertNotIn("Cookie", request.headers)

    def test_url_parsing(self):
        """Test that URLs are correctly parsed."""
        # Call with a complex URL
        self.session.get("https://example.com:8443/path/to/resource?query=value#fragment")

        # Get the request that was passed to send_request
        request = self.session.client.send_request.call_args[0][0]

        # Verify URL components were correctly parsed
        self.assertEqual(request.scheme, "https")
        self.assertEqual(request.host, "example.com:8443")
        self.assertEqual(request.path, "/path/to/resource")
        self.assertEqual(request.query, "query=value")

    def test_destructor(self):
        """Test that the destructor calls close."""
        # Setup a mock for close method
        self.session.close = Mock()

        # Call destructor
        self.session.__del__()

        # Verify close was called
        self.session.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()