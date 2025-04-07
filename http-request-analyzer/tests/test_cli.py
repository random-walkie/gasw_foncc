import unittest
import sys
from io import StringIO
from unittest.mock import patch, MagicMock

from src.http_analyzer.cli import HTTPAnalyzerCLI

class TestHTTPAnalyzerCLI(unittest.TestCase):
    """Test suite for the HTTP Request Analyzer CLI."""

    def setUp(self):
        """Set up test environment."""
        self.cli = HTTPAnalyzerCLI()
        # Capture stdout and stderr
        self.held_output = StringIO()
        self.held_error = StringIO()
        self.orig_stdout = sys.stdout
        self.orig_stderr = sys.stderr
        sys.stdout = self.held_output
        sys.stderr = self.held_error

    def tearDown(self):
        """Restore stdout and stderr."""
        sys.stdout = self.orig_stdout
        sys.stderr = self.orig_stderr

    @patch('src.http_analyzer.session.HTTPSession.get')
    def test_get_request_httpbin(self, mock_get):
        """Test a basic GET request to httpbin."""
        # Create a mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.status_message = 'OK'
        mock_response.body = b'Test body'
        mock_response.headers = {'Content-Type': ['application/json']}
        mock_response.get_decoded_body.return_value = {'origin': '127.0.0.1'}
        mock_get.return_value = mock_response

        # Simulate CLI arguments
        argv = ['https://httpbin.org/get']

        # Run the CLI
        exit_code = self.cli.run(argv)

        # Print diagnostics if test fails
        output = self.held_output.getvalue()
        error = self.held_error.getvalue()

        print("STDOUT:", output)
        print("STDERR:", error)

        # Check exit code and output
        self.assertEqual(exit_code, 0, f"Exit code is not 0. Output: {output}, Error: {error}")
        self.assertIn('Status:', output)
        self.assertIn('200', output)

    @patch('src.http_analyzer.session.HTTPSession.post')
    def test_post_request_httpbin(self, mock_post):
        """Test a POST request to httpbin."""
        # Create a mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.status_message = 'OK'
        mock_response.body = b'Test body'
        mock_response.headers = {'Content-Type': ['application/json']}
        mock_response.get_decoded_body.return_value = {
            'json': {'test': 'value'},
            'origin': '127.0.0.1'
        }
        mock_post.return_value = mock_response

        # Simulate CLI arguments for POST with JSON
        argv = [
            '-m', 'POST',
            '-j', '{"test":"value"}',
            'https://httpbin.org/post'
        ]

        # Run the CLI
        exit_code = self.cli.run(argv)

        # Print diagnostics if test fails
        output = self.held_output.getvalue()
        error = self.held_error.getvalue()

        print("STDOUT:", output)
        print("STDERR:", error)

        # Check exit code and output
        self.assertEqual(exit_code, 0, f"Exit code is not 0. Output: {output}, Error: {error}")
        self.assertIn('Status:', output)
        self.assertIn('200', output)  # HTTP 200 OK status

    @patch('src.http_analyzer.session.HTTPSession.get')
    def test_verbose_output(self, mock_get):
        """Test verbose output mode."""
        # Create a mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.status_message = 'OK'
        mock_response.body = b'Test body'
        mock_response.headers = {
            'Content-Type': ['application/json'],
            'Server': ['test-server'],
            'X-Custom-Header': ['test-value']
        }
        mock_response.get_decoded_body.return_value = {'origin': '127.0.0.1'}
        mock_get.return_value = mock_response

        # Simulate CLI arguments with verbose flag
        argv = ['-v', 'https://httpbin.org/get']

        # Run the CLI
        exit_code = self.cli.run(argv)

        # Print diagnostics if test fails
        output = self.held_output.getvalue()
        error = self.held_error.getvalue()

        print("STDOUT:", output)
        print("STDERR:", error)

        # Check exit code and output
        self.assertEqual(exit_code, 0, f"Exit code is not 0. Output: {output}, Error: {error}")
        self.assertIn('Status:', output)
        self.assertIn('Headers:', output)

    def test_invalid_url(self):
        """Test handling of invalid URL."""
        # Simulate CLI arguments with invalid URL
        argv = ['not-a-valid-url']

        # Run the CLI
        exit_code = self.cli.run(argv)

        # Print diagnostics
        output = self.held_output.getvalue()
        error = self.held_error.getvalue()

        print("STDOUT:", output)
        print("STDERR:", error)

        # Check exit code
        self.assertEqual(exit_code, 1)

    def test_data_and_json_conflict(self):
        """Test handling of conflicting data arguments."""
        # Simulate CLI arguments with both data and JSON
        argv = [
            '-d', 'test=value',
            '-j', '{"test":"value"}',
            'https://httpbin.org/post'
        ]

        # Run the CLI
        exit_code = self.cli.run(argv)

        # Print diagnostics
        output = self.held_output.getvalue()
        error = self.held_error.getvalue()

        print("STDOUT:", output)
        print("STDERR:", error)

        # Check exit code
        self.assertEqual(exit_code, 1)

    @patch('src.http_analyzer.session.HTTPSession.get')
    def test_timeout_parameter(self, mock_get):
        """Test timeout parameter is passed correctly."""
        # Create a mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.status_message = 'OK'
        mock_response.body = b'Test body'
        mock_response.headers = {'Content-Type': ['application/json']}
        mock_response.get_decoded_body.return_value = {'origin': '127.0.0.1'}
        mock_get.return_value = mock_response

        # Simulate CLI arguments with custom timeout
        argv = ['-t', '5', 'https://httpbin.org/get']

        # Run the CLI
        exit_code = self.cli.run(argv)

        # Print diagnostics
        output = self.held_output.getvalue()
        error = self.held_error.getvalue()

        print("STDOUT:", output)
        print("STDERR:", error)

        # Check that get was called with correct timeout
        mock_get.assert_called_once()
        # Check the timeout argument
        self.assertEqual(mock_get.call_args.kwargs['timeout'], 5.0)

        # Additional exit code check
        self.assertEqual(exit_code, 0)

if __name__ == '__main__':
    unittest.main()