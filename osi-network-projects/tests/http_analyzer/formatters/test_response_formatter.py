# File: test_response_formatter.py

import unittest
from unittest.mock import Mock

from http_analyzer.formatters.response_formatter import ResponseFormatter


class HTTPResponseMock:
    status_code = 200
    status_message = "OK"
    headers = {
        "Content-Type": ["text/html"]
    }
    body = "<html><body><h1>Hello, World!</h1></body></html>"

    def get_content_type(self):
        return self.headers.get("Content-Type", [])

    def get_decoded_body(self):
        return self.body


class TestResponseFormatter(unittest.TestCase):

    def setUp(self):
        self.response = HTTPResponseMock()

    def test_format_response_uses_color(self):
        output = ResponseFormatter.format_response(self.response, use_color=True)
        self.assertIn("Status: \033[1m200 OK\033[0m", output[0])

    def test_format_response_no_color(self):
        output = ResponseFormatter.format_response(self.response, use_color=False)
        self.assertIn("Status: 200 OK", output[0])

    def test_format_response_verbose_headers(self):
        output = ResponseFormatter.format_response(self.response, verbose=True)
        self.assertIn("Headers:", output[1])
        self.assertIn(f"Content-Type:\x1b[0m {self.response.headers['Content-Type'][0]}", output[2])

    def test_format_response_normal_mode_body(self):
        output = ResponseFormatter.format_response(self.response, pretty_html=False)
        self.assertIn("Body:", output[1])
        self.assertIn(self.response.get_decoded_body(), output[2])

    def test_format_response_pretty_html_body(self):
        # assume HTMLFormatter is working correctly
        output = ResponseFormatter.format_response(self.response, pretty_html=True)
        self.assertIn("Body (formatted HTML):", output[1])

    def test_format_response_error_decoding_body(self):
        bad_response = Mock()
        bad_response.get_decoded_body = Mock(side_effect=Exception("Decoding error"))

        output = ResponseFormatter.format_response(bad_response)

        self.assertIn("Error decoding response body:", output[1])
        self.assertIn("Raw body:", output[2])

    def test_format_response_regular_body_display(self):
        output = ResponseFormatter.format_response(self.response)
        self.assertIn("Body:", output[1])
        self.assertIn('<html><body><h1>Hello, World!</h1></body></html>', output[2])


if __name__ == '__main__':
    unittest.main()
