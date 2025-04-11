import unittest

from http_analyzer.formatters.html_formatter import HTMLFormatter


class TestHTMLFormatter(unittest.TestCase):
    def setUp(self):
        self.html_content = "<html><head><title>Test Site</title></head><body><h1>Welcome to Test Site</h1></body></html>"
        self.formatter = HTMLFormatter()

    def test_format_html(self):
        formatted = self.formatter.format_html(self.html_content)
        self.assertIn("Test Site", formatted)
        self.assertIn("Welcome to Test Site", formatted)

    def test_pretty_print_html(self):
        formatted = self.formatter.pretty_print_html(self.html_content)
        self.assertIn("<html>", formatted.strip().split("\n")[0])
        self.assertIn("</html>", formatted.strip().split("\n")[-1])

    def test_pretty_print_html_with_indentation(self):
        indentation = 4
        formatted = self.formatter.pretty_print_html(self.html_content, indent_size=indentation)
        self.assertEqual(len(formatted.strip().split("\n")[1]) - len(formatted.strip().split("\n")[1].lstrip()),
                         indentation)

    def test_pretty_print_html_with_color(self):
        color = True
        formatted = self.formatter.pretty_print_html(self.html_content, color=color)
        self.assertTrue("\033[" in formatted)
        color = False
        formatted = self.formatter.pretty_print_html(self.html_content, color=color)
        self.assertFalse("\033[" in formatted)

    def test_format_html_with_color(self):
        color = True
        formatted = self.formatter.format_html(self.html_content, color=color)
        self.assertTrue("\033[" in formatted)
        color = False
        formatted = self.formatter.format_html(self.html_content, color=color)
        self.assertFalse("\033[" in formatted)


if __name__ == "__main__":
    unittest.main()
