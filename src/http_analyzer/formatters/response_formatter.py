"""Response formatting utilities for HTTP Analyzer CLI.

This module provides functions for formatting HTTP responses for display.
"""

import textwrap
from http_analyzer.formatters.terminal_colors import Colors
from http_analyzer.formatters.html_formatter import HTMLFormatter
from http_analyzer.formatters.json_formatter import format_json


class ResponseFormatter:
    """Formats HTTP responses for terminal display."""

    @staticmethod
    def format_response(response, verbose=False, pretty_html=False, use_color=True):
        """Format an HTTP response for display.

        Args:
            response: HTTPResponse object
            verbose: Whether to show detailed information
            pretty_html: Whether to format HTML responses
            use_color: Whether to use colored output

        Returns:
            List of formatted output lines
        """
        output = []

        # Status line
        if use_color:
            output.append(f"Status: {Colors.BOLD}{response.status_code} {response.status_message}{Colors.RESET}")
        else:
            output.append(f"Status: {response.status_code} {response.status_message}")

        # Headers
        if verbose:
            if use_color:
                output.append(f"\n{Colors.BOLD}Headers:{Colors.RESET}")
            else:
                output.append("\nHeaders:")

            for name, values in response.headers.items():
                if use_color:
                    output.append(f"{Colors.CYAN}{name}:{Colors.RESET} {', '.join(values)}")
                else:
                    output.append(f"{name}: {', '.join(values)}")

        # Body
        try:
            # Check if it's an HTML response and pretty-html is enabled
            content_type = response.get_content_type()
            is_html = content_type and ('text/html' in content_type[0] or 'application/xhtml+xml' in content_type[0])

            if pretty_html and is_html:
                # Use our HTML formatter
                formatted_html = HTMLFormatter.format_html(response.body, color=use_color)
                output.append("\nBody (formatted HTML):")
                output.append(formatted_html)
            else:
                # Regular body display
                body = response.get_decoded_body()

                # Basic content formatting
                if content_type and 'application/json' in content_type[0]:
                    # Format JSON
                    output.append("\nBody:")
                    output.append(format_json(body, color=use_color))
                elif content_type and 'text/' in content_type[0]:
                    # For text content, wrap long lines
                    output.append("\nBody:")
                    output.append(textwrap.fill(str(body), width=80))
                else:
                    # For binary or unknown content types
                    output.append(f"\nBody (length: {len(str(body))} bytes)")
                    if len(str(body)) > 0:
                        output.append(str(body))
        except Exception as e:
            output.append(f"\nError decoding response body: {e}")
            output.append("\nRaw body:")
            output.append(str(response.body))

        return output