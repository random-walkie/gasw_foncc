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
from http_analyzer.ssl_handler import SSLHandler


class HTTPAnalyzerCLI:
    """Command-line interface for HTTP Request Analyzer."""

    def __init__(self):
        """Initialize the CLI with argument parser."""
        self.parser = self._create_argument_parser()
        self.logger = self._configure_logger()

    def _create_argument_parser(self):
        """Create and configure the argument parser."""
        parser = argparse.ArgumentParser(
            description='HTTP Request Analyzer - Explore Network Protocols',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''\
                Examples:
                  http-analyzer https://example.com
                  http-analyzer -m POST -d '{"key":"value"}' https://api.example.com
                  http-analyzer -v --analyze-ssl https://secure.example.com
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

        return parser

    def _configure_logger(self):
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

    def display_response(self, response, verbose=False):
        """Display HTTP response with appropriate formatting.

        Args:
            response: HTTPResponse object
            verbose: Whether to show detailed information
        """
        # Status line
        print(f"Status: {response.status_code} {response.status_message}")

        # Headers
        if verbose:
            print("\nHeaders:")
            for name, values in response.headers.items():
                print(f"{name}: {', '.join(values)}")

        # Body
        try:
            body = response.get_decoded_body()

            # Basic content formatting
            content_type = response.get_content_type()
            if content_type and 'application/json' in content_type[0]:
                # Pretty-print JSON
                print("\nBody:")
                print(json.dumps(body, indent=2))
            elif content_type and 'text/' in content_type[0]:
                # For text content, wrap long lines
                print("\nBody:")
                print(textwrap.fill(str(body), width=80))
            else:
                # For binary or unknown content types
                print(f"\nBody (length: {len(str(body))} bytes)")
                if len(str(body)) > 0:
                    print(body)
        except Exception as e:
            self.logger.error(f"Error decoding response body: {e}")
            print("\nBody decoding failed. Raw body:")
            print(response.body)

    def analyze_security(self, session, url):
        """Analyze and display security information about the connection.

        Args:
            session: HTTPSession object
            url: Original request URL
        """
        if not url.startswith('https'):
            print("SSL/TLS analysis is only available for HTTPS connections.")
            return

        try:
            # Send a request to populate the client
            session.get(url)

            # This is hypothetical and would require modifications to the current implementation
            # The goal is to demonstrate the security analysis concept
            ssl_socket = session.client.get_last_socket()  # Hypothetical method

            if ssl_socket:
                cert_info = SSLHandler.get_certificate_info(ssl_socket)
                security_assessment = SSLHandler.get_security_assessment(cert_info)

                print("\nSSL/TLS Security Assessment:")
                for key, value in security_assessment.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("Could not retrieve SSL socket information.")

        except Exception as e:
            self.logger.error(f"SSL analysis failed: {e}")

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

            # Display response
            self.display_response(response, args.verbose)

            # Perform SSL analysis if requested
            if args.analyze_ssl:
                self.analyze_security(session, args.url)

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