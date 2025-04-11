"""
Module for handling HTML content parsing and analysis.
"""

import logging
from http_analyzer.html_fallback_parser import HTMLFallbackParser

logger = logging.getLogger(__name__)

# Try to import BeautifulSoup, but don't fail if it's not available
BS4_AVAILABLE = False
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    logger.warning("BeautifulSoup library not available. Using fallback HTML parsing.")


class HTMLHandler:
    """Handles the parsing and analysis of HTML content."""

    @staticmethod
    def parse_html(content, encoding='utf-8'):
        """Parse HTML content into a structured object.
        
        Args:
            content: HTML content as string or bytes
            encoding: Character encoding for bytes content
            
        Returns:
            BeautifulSoup object or HTMLFallbackParser object
        """
        # Handle bytes input
        if isinstance(content, bytes):
            try:
                content = content.decode(encoding)
            except UnicodeDecodeError:
                content = content.decode(encoding, errors='replace')

        # Try BeautifulSoup first if available
        if BS4_AVAILABLE:
            try:
                return BeautifulSoup(content, 'html.parser')
            except Exception as e:
                logger.warning(f"BeautifulSoup parsing failed: {e}. Falling back to HTMLFallbackParser")
                # Fall back to our parser if BeautifulSoup fails
                return HTMLFallbackParser(content, encoding)
        else:
            # BeautifulSoup not available, use our fallback parser
            return HTMLFallbackParser(content, encoding)

    @staticmethod
    def extract_metadata(html):
        """Extract metadata from HTML content.

        Args:
            html: HTML content as string, bytes, BeautifulSoup, or HTMLFallbackParser

        Returns:
            Dictionary with metadata (title, meta tags, links)
        """
        # If it's a string or bytes, parse it first
        if isinstance(html, (str, bytes)):
            html = HTMLHandler.parse_html(html)

        # Check if the parsed result is None
        if html is None:
            return {'title': None, 'meta_tags': {}, 'links': []}

        # Now delegate to the appropriate parser
        if isinstance(html, HTMLFallbackParser):
            # Our fallback parser
            return html.extract_metadata()

        try:
            if BS4_AVAILABLE and isinstance(html, BeautifulSoup):
                # Use BeautifulSoup methods
                metadata = {
                    'title': html.title.text.strip() if html.title else None,
                    'meta_tags': {},
                    'links': []
                }

                # Extract meta tags
                for meta in html.find_all('meta'):
                    if meta.get('name'):
                        metadata['meta_tags'][meta.get('name')] = meta.get('content')
                    elif meta.get('property'):
                        metadata['meta_tags'][meta.get('property')] = meta.get('content')

                # Extract links
                for link in html.find_all('a', href=True):
                    metadata['links'].append({
                        'text': link.text.strip(),
                        'href': link['href']
                    })

                return metadata
        except Exception as e:
            logger.error(f"Error extracting HTML metadata: {e}")

        # If we get here, something went wrong - return minimal metadata
        return {'title': None, 'meta_tags': {}, 'links': []}

    @staticmethod
    def extract_forms(html):
        """Extract form information from HTML content.

        Args:
            html: HTML content as string, bytes, BeautifulSoup, or HTMLFallbackParser

        Returns:
            List of form dictionaries
        """
        # If it's a string or bytes, parse it first
        if isinstance(html, (str, bytes)):
            html = HTMLHandler.parse_html(html)

        # Check if the parsed result is None
        if html is None:
            return []

        # Now delegate to the appropriate parser
        if isinstance(html, HTMLFallbackParser):
            # Our fallback parser
            return html.extract_forms()

        try:
            if BS4_AVAILABLE and isinstance(html, BeautifulSoup):
                forms = []
                for form in html.find_all('form'):
                    form_data = {
                        'action': form.get('action', ''),
                        'method': form.get('method', 'get').upper(),
                        'fields': []
                    }

                    # Process input fields
                    for input_field in form.find_all('input'):
                        field = {
                            'name': input_field.get('name', ''),
                            'type': input_field.get('type', 'text'),
                            'value': input_field.get('value', '')
                        }
                        form_data['fields'].append(field)

                    # Process textarea fields
                    for textarea in form.find_all('textarea'):
                        field = {
                            'name': textarea.get('name', ''),
                            'type': 'textarea',
                            'value': textarea.string if textarea.string else ''
                        }
                        form_data['fields'].append(field)

                    # Process select fields
                    for select in form.find_all('select'):
                        field = {
                            'name': select.get('name', ''),
                            'type': 'select',
                            'value': ''  # Could extract options but keeping it simple
                        }
                        form_data['fields'].append(field)

                    forms.append(form_data)

                return forms
        except Exception as e:
            logger.error(f"Error extracting HTML forms: {e}")

        # If we get here, something went wrong - return empty list
        return []