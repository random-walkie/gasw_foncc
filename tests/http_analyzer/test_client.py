import unittest
from unittest.mock import Mock, patch
import socket
from http_analyzer.client import HTTPClient
from http_analyzer.request import HTTPRequest
from http_analyzer.response import HTTPResponse

class TestHTTPClient(unittest.TestCase):
    """Test suite for the HTTPClient class.

    These tests verify that the HTTPClient class correctly establishes
    connections, sends requests, and handles responses.
    """

    def setUp(self):
        """Set up test environment before each test case."""
        # Create a client for testing
        self.client = HTTPClient()

        # Create a sample request
        self.test_request = HTTPRequest("GET", "http://example.com/test")

        # Create a sample raw response
        self.raw_response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nTest response"

    @patch('socket.socket')
    def test_send_request_http(self, mock_socket_class):
        """Test sending a basic HTTP request."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup socket.recv to return our test response and then empty to signal end
        mock_socket.recv.side_effect = [self.raw_response, b""]

        # Call send_request
        response = self.client.send_request(self.test_request)

        # Verify socket was created with right params
        mock_socket_class.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)

        # Verify connection was established
        mock_socket.connect.assert_called_with(("example.com", 80))

        # Verify request was sent
        mock_socket.sendall.assert_called_once()

        # Verify response was received and parsed
        self.assertIsInstance(response, HTTPResponse)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body, b"Test response")

    @patch('socket.socket')
    @patch('http_analyzer.ssl_handler.SSLHandler.wrap_socket')
    def test_send_request_https(self, mock_wrap_socket, mock_socket_class):
        """Test sending a request over HTTPS."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup SSL socket
        mock_ssl_socket = Mock()
        mock_ssl_socket._closed = False
        mock_wrap_socket.return_value = mock_ssl_socket

        # Setup socket.recv to return our test response and then empty
        mock_ssl_socket.recv.side_effect = [self.raw_response, b""]

        # Create an HTTPS request
        https_request = HTTPRequest("GET", "https://example.com/test")

        # Call send_request
        response = self.client.send_request(https_request)

        # Verify socket was created
        mock_socket_class.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)

        # Verify connection was established
        mock_socket.connect.assert_called_with(("example.com", 443))

        # Verify socket was wrapped with SSL
        mock_wrap_socket.assert_called_with(mock_socket, "example.com")

        # Verify request was sent on SSL socket
        mock_ssl_socket.sendall.assert_called_once()

        # Verify response was received and parsed
        self.assertIsInstance(response, HTTPResponse)
        self.assertEqual(response.status_code, 200)

    @patch('socket.socket')
    def test_connection_reuse(self, mock_socket_class):
        """Test that connections are reused when appropriate."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup socket.recv to return our test response and then empty
        mock_socket.recv.side_effect = [
            self.raw_response,  # First request response
            b"",                # End of first response
            self.raw_response,  # Second request response
            b""                 # End of second response
        ]

        # Create a request with Connection: keep-alive
        keep_alive_request = HTTPRequest("GET", "http://example.com/test",
                                         headers={"Connection": "keep-alive"})

        # First request - should create a new connection
        self.client.send_request(keep_alive_request)

        # Reset the mock to track new calls
        mock_socket.reset_mock()

        # Second request to same host - should reuse connection
        self.client.send_request(keep_alive_request)

        # Verify socket.connect was NOT called again
        mock_socket.connect.assert_not_called()

        # But sendall should have been called for the second request
        mock_socket.sendall.assert_called_once()

    @patch('socket.socket')
    def test_connection_close(self, mock_socket_class):
        """Test that connections are closed when requested."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup response with Connection: close header
        close_response = b"HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nTest response"
        mock_socket.recv.side_effect = [close_response, b""]

        # Create a request
        request = HTTPRequest("GET", "http://example.com/test")

        # Send request
        self.client.send_request(request)

        # Verify socket was closed
        mock_socket.close.assert_called_once()

        # Verify connection was removed from tracked connections
        self.assertNotIn("example.com:80", self.client.connections)

    @patch('socket.socket')
    def test_connection_error(self, mock_socket_class):
        """Test handling of connection errors."""
        # Setup mock socket to raise error on connect
        mock_socket = Mock()
        mock_socket.connect.side_effect = socket.error("Connection failed")
        mock_socket_class.return_value = mock_socket

        # Attempt to send request
        with self.assertRaises(ConnectionError):
            self.client.send_request(self.test_request)

        # Verify socket was closed
        mock_socket.close.assert_called_once()

    @patch('socket.socket')
    def test_send_error(self, mock_socket_class):
        """Test handling of send errors."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup socket to raise error on sendall
        mock_socket.sendall.side_effect = socket.error("Send failed")

        # Attempt to send request
        with self.assertRaises(Exception):
            self.client.send_request(self.test_request)

        # Verify socket was closed
        mock_socket.close.assert_called_once()

        # Verify connection was removed from tracked connections
        self.assertNotIn("example.com:80", self.client.connections)

    def test_close_all_connections(self):
        """Test closing all connections."""
        # Setup mock connections
        mock_sock1 = Mock()
        mock_sock2 = Mock()
        self.client.connections = {
            "example.com:80": mock_sock1,
            "example.org:443": mock_sock2
        }

        # Call close method
        self.client.close()

        # Verify all sockets were closed
        mock_sock1.close.assert_called_once()
        mock_sock2.close.assert_called_once()

        # Verify connections dictionary was cleared
        self.assertEqual(len(self.client.connections), 0)

    def test_connection_error_handling(self):
        """Test that errors during close are handled gracefully."""
        # Setup mock connection that raises error on close
        mock_sock = Mock()
        mock_sock.close.side_effect = Exception("Close error")
        self.client.connections = {"example.com:80": mock_sock}

        # Call close method - should not raise exception
        try:
            self.client.close()
            # If we get here, no exception was raised - test passes
            self.assertTrue(True)
        except:
            # If we get here, an exception was raised - test fails
            self.fail("close() raised an exception when it should have handled it")

        # Verify connections dictionary was cleared despite error
        self.assertEqual(len(self.client.connections), 0)

    @patch('socket.socket')
    def test_custom_port(self, mock_socket_class):
        """Test connection to non-standard port."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup socket.recv
        mock_socket.recv.side_effect = [self.raw_response, b""]

        # Create request with custom port
        custom_port_request = HTTPRequest("GET", "http://example.com:8080/test")

        # Call send_request
        self.client.send_request(custom_port_request)

        # Verify connection used correct port
        mock_socket.connect.assert_called_with(("example.com", 8080))

    @patch('socket.socket')
    def test_timeout_parameter(self, mock_socket_class):
        """Test that timeout parameter is applied to socket."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup socket.recv
        mock_socket.recv.side_effect = [self.raw_response, b""]

        # Call send_request with custom timeout
        self.client.send_request(self.test_request, timeout=30)

        # Verify timeout was set on socket
        mock_socket.settimeout.assert_called_with(30)

    @patch('socket.socket')
    def test_recv_timeout(self, mock_socket_class):
        """Test handling of socket timeout during receive."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup socket.recv to raise timeout
        mock_socket.recv.side_effect = socket.timeout("Receive timed out")

        # Attempt to send request - should raise an exception
        with self.assertRaises(Exception):
            self.client.send_request(self.test_request)

        # Verify socket was closed
        mock_socket.close.assert_called_once()

    @patch('socket.socket')
    def test_incomplete_response(self, mock_socket_class):
        """Test handling of incomplete HTTP response."""
        # Setup mock socket
        mock_socket = Mock()
        mock_socket._closed = False
        mock_socket_class.return_value = mock_socket

        # Setup socket.recv to return incomplete response
        incomplete_response = b"HTTP/1.1 200 OK\r\nContent-"
        mock_socket.recv.side_effect = [incomplete_response, b""]

        # Send request - should still try to parse what it received
        response = self.client.send_request(self.test_request)

        # Verify we got a response object
        self.assertIsInstance(response, HTTPResponse)

    def test_destructor(self):
        """Test that destructor calls close."""
        # Mock close method
        self.client.close = Mock()

        # Call destructor
        self.client.__del__()

        # Verify close was called
        self.client.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()