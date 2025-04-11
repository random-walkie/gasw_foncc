"""Security analysis utilities for HTTP Analyzer CLI.

This module provides functions for analyzing SSL/TLS connections.
"""

import logging
from http_analyzer.ssl_handler import SSLHandler
from http_analyzer.formatters.terminal_colors import Colors

logger = logging.getLogger(__name__)


class SecurityAnalyzer:
    """Analyzes security aspects of HTTP connections."""

    @staticmethod
    def analyze_ssl(session, url, use_color=True):
        """Analyze and format SSL/TLS security information.

        Args:
            session: HTTPSession object
            url: Target URL
            use_color: Whether to use colored output

        Returns:
            List of formatted output lines, or empty list if analysis failed
        """
        output = []

        if not url.startswith('https'):
            output.append("SSL/TLS analysis is only available for HTTPS connections.")
            return output

        try:
            # Send a request to populate the client connections
            session.get(url)

            # Try to get the SSL socket - this would need to be implemented in the client
            ssl_socket = None

            # Look for an existing connection to the host in the session's client
            for conn_id, socket in session.client.connections.items():
                if url.split('//')[1].split('/')[0] in conn_id:
                    ssl_socket = socket
                    break

            if ssl_socket:
                cert_info = SSLHandler.get_certificate_info(ssl_socket)
                security_assessment = SSLHandler.get_security_assessment(cert_info)

                if use_color:
                    output.append(f"\n{Colors.BOLD}SSL/TLS Security Assessment:{Colors.RESET}")
                else:
                    output.append("\nSSL/TLS Security Assessment:")

                for key, value in security_assessment.items():
                    # Color-code based on security level
                    if use_color:
                        color = Colors.GREEN
                        if 'poor' in value.lower() or 'weak' in value.lower() or 'expired' in value.lower():
                            color = Colors.RED
                        elif 'moderate' in value.lower():
                            color = Colors.YELLOW

                        output.append(f"{key.replace('_', ' ').title()}: {color}{value}{Colors.RESET}")
                    else:
                        output.append(f"{key.replace('_', ' ').title()}: {value}")

                # Add certificate details
                if use_color:
                    output.append(f"\n{Colors.BOLD}Certificate Information:{Colors.RESET}")
                else:
                    output.append("\nCertificate Information:")

                for key, value in cert_info.items():
                    if key != 'alt_names':  # Skip alt_names as they can be lengthy
                        if use_color:
                            output.append(f"{Colors.CYAN}{key.replace('_', ' ').title()}:{Colors.RESET} {value}")
                        else:
                            output.append(f"{key.replace('_', ' ').title()}: {value}")
            else:
                output.append("Could not retrieve SSL socket information.")

        except Exception as e:
            logger.error(f"SSL analysis failed: {e}")
            output.append(f"SSL analysis failed: {e}")

        return output