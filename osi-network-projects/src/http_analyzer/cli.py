"""
Command-line interface for HTTP Request Analyzer.

This module provides the CLI argument parsing and high-level workflow
for the HTTP Request Analyzer application.
"""

import argparse
import json
import logging
import textwrap
from urllib.parse import urlparse

from http_analyzer.session import HTTPSession
from http_analyzer.formatters.response_formatter import ResponseFormatter
from http_analyzer.security.security_analyzer import SecurityAnalyzer


class HTTPAnalyzerCLI:
    """Command-line interface for HTTP Request Analyzer."""

    def __init__(self):
        """Initialize the CLI with argument parser."""
        self.parser = HTTPAnalyzerCLI._create_argument_parser()
        self.logger = HTTPAnalyzerCLI._configure_logger()

    @staticmethod
    def _create_argument_parser():
        """Create and configure the argument parser."""
        parser = argparse.ArgumentParser(
            description='HTTP Request Analyzer - Explore Network Protocols',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''\
                Examples:
                  http-analyzer https://example.com
                  http-analyzer -m POST -d '{"key":"value"}' https://api.example.com
                  http-analyzer -v --analyze-ssl https://secure.example.com
                  http-analyzer --pretty-html https://example.com
                ''')
        )

        # Required URL argument
        parser.add_argument('url', help='URL to send request to')

        # Optional arguments
        parser.add_argument(
            '-m', '--method',
            choices=['GET', 'POST'],
            default='GET',
            help='HTTP method to use (default: GET)'
        )
        parser.add_argument(
            '-f', '--follow-redirects',
            action='store_true',
            help='Follow HTTP redirects'
        )
        parser.add_argument(
            '-v', '--verbose',
            action='store_true',
            help='Show detailed output'
        )
        parser.add_argument(
            '-d', '--data',
            help='Request body data for POST/PUT requests'
        )
        parser.add_argument(
            '-j', '--json',
            help='JSON data to send with request'
        )
        parser.add_argument(
            '-H', '--header',
            action='append',
            help='Custom HTTP headers (can be used multiple times)'
        )
        parser.add_argument(
            '-o', '--output',
            help='Save response body to a file'
        )
        parser.add_argument(
            '-t', '--timeout',
            type=float,
            default=10,
            help='Request timeout in seconds (default: 10)'
        )
        parser.add_argument(
            '--analyze-ssl',
            action='store_true',
            help='Perform SSL/TLS security analysis for HTTPS'
        )
        parser.add_argument(
            '--pretty-html',
            action='store_true',
            help='Format HTML responses for better readability'
        )
        parser.add_argument(
            '--no-color',
            action='store_true',
            help='Disable colored output'
        )

        return parser

    @staticmethod
    def _configure_logger():
        """Configure and return a logger instance."""
        return logging.getLogger(__name__)

    def parse_headers(self, header_strings):
        """Parse header strings into a dictionary.

        Args:
            header_strings: List of header strings in "Name: Value" format

        Returns:
            Dictionary of headers
        """
        if not header_strings:
            return {}

        headers = {}
        for header in header_strings:
            try:
                name, value = header.split(':', 1)
                headers[name.strip()] = value.strip()
            except ValueError:
                self.logger.warning(f"Malformed header: {header}. Skipping.")

        return headers

    def run(self, argv=None):
        """Execute the CLI workflow.

        Args:
            argv: Command-line arguments (optional, for testing)

        Returns:
            Exit code (0 for success, non-zero for error)
        """
        # Parse arguments
        try:
            args = self.parser.parse_args(argv)
        except SystemExit as e:
            return e.code

        # Configure logging based on verbosity
        logging.basicConfig(
            level=logging.DEBUG if args.verbose else logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

        # Determine if color should be used
        use_color = not args.no_color

        # Validate input
        try:
            parsed_url = urlparse(args.url)
            if not parsed_url.scheme or not parsed_url.netloc:
                raise ValueError("Invalid URL format")

            # Prevent both data and json being provided
            if args.data and args.json:
                raise ValueError("Cannot provide both 'data' and 'json'")

        except ValueError as e:
            self.logger.error(str(e))
            return 1

        # Create HTTP session
        session = HTTPSession()

        try:
            # Prepare headers
            headers = self.parse_headers(args.header)

            # Prepare request body
            data = None
            json_data = None
            if args.json:
                try:
                    json_data = json.loads(args.json)
                except json.JSONDecodeError:
                    self.logger.error("Invalid JSON data")
                    return 1
            elif args.data:
                data = args.data

            # Send request based on method
            if args.method == 'GET':
                response = session.get(
                    args.url,
                    headers=headers,
                    timeout=args.timeout
                )
            elif args.method == 'POST':
                response = session.post(
                    args.url,
                    data=data,
                    json=json_data,
                    headers=headers,
                    timeout=args.timeout
                )
            else:
                # This should not happen due to argparse choices, but include for safety
                raise ValueError(f"Unsupported HTTP method: {args.method}")

            # Format and display response
            formatted_output = ResponseFormatter.format_response(
                response,
                verbose=args.verbose,
                pretty_html=args.pretty_html,
                use_color=use_color
            )

            # Print each line of the formatted output
            for line in formatted_output:
                print(line)

            # Perform SSL analysis if requested
            if args.analyze_ssl:
                ssl_output = SecurityAnalyzer.analyze_ssl(
                    session,
                    args.url,
                    use_color=use_color
                )

                # Print each line of the SSL analysis output
                for line in ssl_output:
                    print(line)

            # Save to output file if specified
            if args.output:
                try:
                    with open(args.output, 'wb') as f:
                        f.write(response.body)
                    self.logger.info(f"Response body saved to {args.output}")
                except IOError as e:
                    self.logger.error(f"Failed to write to output file: {e}")
                    return 1

            return 0

        except Exception as e:
            self.logger.error(f"Request failed: {e}")
            return 1

        finally:
            # Always close the session
            session.close()