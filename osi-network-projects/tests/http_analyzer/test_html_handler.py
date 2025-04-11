"""
Test suite for the HTMLHandler and HTMLFallbackParser classes.
"""

import unittest
import sys
from unittest import mock

from http_analyzer.html_handler import HTMLHandler, BS4_AVAILABLE
from http_analyzer.html_fallback_parser import HTMLFallbackParser

# Skip BeautifulSoup specific tests if it's not available
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


class TestHTMLHandler(unittest.TestCase):
    """Test suite for the HTMLHandler class."""

    def setUp(self):
        """Set up test data."""
        self.basic_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Page</title>
            <meta name="description" content="A test page">
        </head>
        <body>
            <h1>Hello World</h1>
            <p>This is a test.</p>
        </body>
        </html>
        """

        self.metadata_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Metadata</title>
            <meta name="description" content="A page with metadata">
            <meta name="keywords" content="test, metadata, html">
            <meta property="og:title" content="Open Graph Title">
        </head>
        <body>
            <a href="https://example.com">Example Link</a>
            <a href="/relative/path">Relative Link</a>
        </body>
        </html>
        """

        self.forms_html = """
        <!DOCTYPE html>
        <html>
        <body>
            <form action="/submit" method="post">
                <input type="text" name="username" value="">
                <input type="password" name="password">
                <textarea name="comments">Default text</textarea>
                <select name="country">
                    <option value="us">United States</option>
                    <option value="ca">Canada</option>
                </select>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
        """

    def test_parse_html_returns_proper_type(self):
        """Test that parse_html returns the expected type based on available libraries."""
        parsed = HTMLHandler.parse_html(self.basic_html)

        if BS4_AVAILABLE:
            self.assertIsInstance(parsed, BeautifulSoup)
        else:
            self.assertIsInstance(parsed, HTMLFallbackParser)

    def test_parse_html_with_bytes(self):
        """Test parsing HTML from bytes."""
        byte_html = self.basic_html.encode('utf-8')
        parsed = HTMLHandler.parse_html(byte_html)

        # Should handle bytes regardless of parser
        if BS4_AVAILABLE:
            self.assertIsInstance(parsed, BeautifulSoup)
        else:
            self.assertIsInstance(parsed, HTMLFallbackParser)

    def test_extract_metadata_basic(self):
        """Test basic metadata extraction."""
        metadata = HTMLHandler.extract_metadata(self.metadata_html)

        # Basic assertions that should work with both real and fallback parser
        self.assertIsInstance(metadata, dict)
        self.assertIn('title', metadata)
        self.assertEqual(metadata['title'], "Test Metadata")
        self.assertIn('meta_tags', metadata)
        self.assertIn('description', metadata['meta_tags'])
        self.assertEqual(metadata['meta_tags']['description'], "A page with metadata")

        # Open Graph tags
        self.assertIn('og:title', metadata['meta_tags'])
        self.assertEqual(metadata['meta_tags']['og:title'], "Open Graph Title")

        # Links
        self.assertIn('links', metadata)
        self.assertEqual(len(metadata['links']), 2)

        # Verify specific links
        links_by_text = {link['text']: link['href'] for link in metadata['links']}
        self.assertEqual(links_by_text['Example Link'], 'https://example.com')
        self.assertEqual(links_by_text['Relative Link'], '/relative/path')

    def test_extract_forms(self):
        """Test extraction of form information."""
        forms = HTMLHandler.extract_forms(self.forms_html)

        # Basic assertions
        self.assertIsInstance(forms, list)
        self.assertEqual(len(forms), 1)

        # Check form properties
        form = forms[0]
        self.assertEqual(form['action'], '/submit')
        self.assertEqual(form['method'], 'POST')

        # Check fields
        self.assertEqual(len(form['fields']), 5)

        # Find specific fields by name
        fields_by_name = {field['name']: field for field in form['fields']}

        # Check username field
        self.assertIn('username', fields_by_name)
        self.assertEqual(fields_by_name['username']['type'], 'text')

        # Check password field
        self.assertIn('password', fields_by_name)
        self.assertEqual(fields_by_name['password']['type'], 'password')

        # Check comments field
        self.assertIn('comments', fields_by_name)
        self.assertEqual(fields_by_name['comments']['type'], 'textarea')
        self.assertEqual(fields_by_name['comments']['value'], 'Default text')

        # Check select field
        self.assertIn('country', fields_by_name)
        self.assertEqual(fields_by_name['country']['type'], 'select')

    @unittest.skipIf(not BS4_AVAILABLE, "BeautifulSoup not available")
    def test_beautifulsoup_specific_features(self):
        """Test features specific to BeautifulSoup (skipped if not available)."""
        # Parse with BeautifulSoup
        parsed = HTMLHandler.parse_html(self.basic_html)

        # BeautifulSoup-specific assertions
        self.assertEqual(parsed.h1.text, "Hello World")
        self.assertEqual(parsed.find('p').text, "This is a test.")

    def test_fallback_parser_extraction(self):
        """Test direct use of the fallback parser."""
        parser = HTMLFallbackParser(self.metadata_html)
        metadata = parser.extract_metadata()

        # Check basic metadata
        self.assertEqual(metadata['title'], "Test Metadata")
        self.assertIn('description', metadata['meta_tags'])

        # Check form extraction
        parser = HTMLFallbackParser(self.forms_html)
        forms = parser.extract_forms()

        self.assertEqual(len(forms), 1)
        self.assertEqual(forms[0]['method'], 'POST')

    @unittest.skipIf(not BS4_AVAILABLE, "BeautifulSoup not available")
    def test_bs4_unavailable_fallback(self):
        """Test that the fallback parser is used when BeautifulSoup fails."""
        # Simulate BeautifulSoup failure but still being available
        # The key is to patch where BeautifulSoup is actually used in the HTMLHandler module
        with mock.patch('http_analyzer.html_handler.BeautifulSoup',
                        side_effect=Exception("Simulated BS4 failure")):
            parsed = HTMLHandler.parse_html(self.basic_html)
            self.assertIsInstance(parsed, HTMLFallbackParser)

            # Should still be able to extract metadata
            metadata = HTMLHandler.extract_metadata(parsed)
            self.assertEqual(metadata['title'], "Test Page")


if __name__ == '__main__':
    unittest.main()