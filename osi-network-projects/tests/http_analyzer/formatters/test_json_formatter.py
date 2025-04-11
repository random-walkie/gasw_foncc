import json
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../osi-network-projects/src/http_analyzer/formatters/")
from http_analyzer.formatters.json_formatter import format_json


class TestJsonFormatter(unittest.TestCase):
    def test_format_json_with_color(self):
        test_json = {"key":"value", "number": 123, "bool": True, "null": None}
        expected = '{\n  \x1b[33m"key"\x1b[0m: \x1b[32m"value"\x1b[0m,\n  \x1b[33m"number"\x1b[0m: \x1b[36m123\x1b[0m,\n  \x1b[33m"bool"\x1b[0m: \x1b[35mtrue\x1b[0m,\n  \x1b[33m"null"\x1b[0m: \x1b[35mnull\x1b[0m\n}'
        self.assertEqual(expected, format_json(test_json))

    def test_format_json_without_color(self):
        test_json = {"key":"value", "number": 123, "bool": True, "null": None}
        expected = json.dumps(test_json, indent=2)
        self.assertEqual(format_json(test_json, color=False), expected)

    def test_format_json_with_indent(self):
        test_json = {"key":"value"}
        expected = "{\n     \"key\": \"value\"\n}"
        self.assertEqual(expected, format_json(test_json, color=False, indent=5))

    def test_format_json_with_string(self):
        test_string = '{"key":"value"}'
        expected = '{\n  \x1b[33m"key"\x1b[0m: \x1b[32m"value"\x1b[0m\n}'
        self.assertIn(format_json(test_string), expected)

    def test_format_json_with_invalid_string(self):
        test_string = 'not valid json'
        self.assertEqual(test_string, format_json(test_string))


if __name__ == "__main__":
    unittest.main()
