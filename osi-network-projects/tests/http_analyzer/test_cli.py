import unittest
import sys
from io import StringIO
from unittest.mock import patch, MagicMock

from http_analyzer.cli import HTTPAnalyzerCLI

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

    @patch('http_analyzer.session.HTTPSession.get')
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

        # Debug: Print out the actual patch target
        print("Patch target:", mock_get._mock_new_name)

        # Run the CLI
        exit_code = self.cli.run(argv)

        # Print diagnostics
        output = self.held_output.getvalue()
        error = self.held_error.getvalue()

        print("STDOUT:", output)
        print("STDERR:", error)
        print("Exit Code:", exit_code)

        # Print out the mock call details
        print("Mock method call count:", mock_get.call_count)
        print("Mock method calls:", mock_get.call_args_list)

        # Check that get was called with correct timeout
        mock_get.assert_called_once_with(
            'https://httpbin.org/get',
            headers={},
            timeout=5.0
        )

if __name__ == '__main__':
    unittest.main()