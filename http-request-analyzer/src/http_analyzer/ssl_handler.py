import ssl
import socket
from dateutil import parser
from datetime import datetime, timezone

class SSLHandler:
    """Handles SSL/TLS encryption for HTTPS connections.

    This class demonstrates the Presentation Layer (Layer 6) security
    functions by handling the encryption and decryption of data.
    """

    @staticmethod
    def wrap_socket(sock, hostname):
        """Wrap a socket with SSL/TLS encryption.

        Args:
            sock: Plain TCP socket
            hostname: Target hostname for certificate validation

        Returns:
            Encrypted SSL socket
        """
        # Create SSL context with secure defaults
        context = ssl.create_default_context()

        # Configure context with appropriate security settings
        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Disable older TLS versions
        context.set_ciphers('HIGH:!aNULL:!eNULL')  # Strong ciphers only

        # Wrap the socket with SSL/TLS
        ssl_socket = context.wrap_socket(sock, server_hostname=hostname)

        # Return the wrapped socket
        return ssl_socket
        

    @staticmethod
    def get_certificate_info(ssl_socket):
        """Extract certificate information from an SSL socket.

        This method can be used to analyze the SSL/TLS connection
        security properties for educational purposes.

        Args:
            ssl_socket: An SSL-wrapped socket

        Returns:
            Dictionary of certificate information
        """
        certificate_info = {
            'issuer': '',
            'subject': '',
            'valid_from': '',
            'valid_until': '',
            'cipher': '',
            'protocol': '',
            'key_size': '',
            'alt_names': ''
        }
        # Extract certificate from socket using getpeercert()
        certificate = ssl_socket.getpeercert()
        cipher, protocol, key_size = ssl_socket.cipher()
        # Parse certificate fields (issuer, subject, expiration)
        certificate_info['issuer'] = SSLHandler.format_cert_field(field=certificate['issuer'],
                                                                  function=lambda pattern: 'Name' in pattern)
        certificate_info['subject'] = SSLHandler.format_cert_field(field=certificate['subject'],
                                                                   function=lambda pattern: 'Name' in pattern)
        certificate_info['valid_until'] = SSLHandler.parse_cert_date(certificate['notAfter'])
        certificate_info['valid_from'] = SSLHandler.parse_cert_date(certificate['notBefore'])
        # Extract cipher information
        certificate_info['cipher'] = cipher
        # Determine protocol version
        certificate_info['protocol'] = protocol
        # Check certificate validation status
        certificate_info['alt_names'] = SSLHandler.format_cert_field(field=certificate['subjectAltName'],
                                                                     function=lambda pattern: 'DNS' in pattern)
        # Return dictionary with formatted certificate information
        return certificate_info

    # @staticmethod
    # def get_security_assessment(cert_info):
    #     """Assess the security of the SSL/TLS connection.
    #
    #     This method demonstrates how to evaluate the security aspects
    #     of the Presentation Layer encryption.
    #
    #     Args:
    #         cert_info: Certificate information dictionary
    #
    #     Returns:
    #         Dictionary with security assessment details
    #     """
    #
    #     # Initialize the assessment dictionary
    #     assessment = {
    #         'certificate_validity': '',
    #         'trusted_issuer': '',
    #         'cipher_strength': '',
    #         'protocol_security': '',
    #         'details': []
    #     }
    #
    #     # Check certificate validity
    #     now = datetime.now(timezone.utc)
    #     valid_from = cert_info['valid_from']
    #     valid_until = cert_info['valid_until']
    #     if valid_from <= now <= valid_until:
    #         assessment['certificate_validity'] = 'Valid'
    #     elif now < valid_from:
    #         assessment['certificate_validity'] = 'Not yet valid'
    #         assessment['details'].append('The certificate is not valid until {}'.format(valid_from))
    #     else:
    #         assessment['certificate_validity'] = 'Expired'
    #         assessment['details'].append('The certificate expired on {}'.format(valid_until))
    #
    #     # Verify trusted issuer (simplified; actual implementation may involve checking against a trusted CA list)
    #     trusted_issuers = ['Let\'s Encrypt', 'DigiCert', 'GlobalSign', 'Sectigo']  # Example trusted issuers
    #     issuer_common_name = cert_info['issuer']
    #     if any(trusted_issuer in issuer_common_name for trusted_issuer in trusted_issuers):
    #         assessment['trusted_issuer'] = 'Trusted'
    #     else:
    #         assessment['trusted_issuer'] = 'Untrusted'
    #         assessment['details'].append('Issuer "{}" is not trusted'.format(issuer_common_name))
    #
    #     # Evaluate cipher strength
    #     strong_ciphers = ['AES256', 'CHACHA20']
    #     cipher = cert_info['cipher']
    #     if any(strong_cipher in cipher.upper() for strong_cipher in strong_ciphers):
    #         assessment['cipher_strength'] = 'Strong'
    #     else:
    #         assessment['cipher_strength'] = 'Weak'
    #
    #     # Assess TLS protocol version security
    #     secure_protocols = ['TLSv1.3', 'TLSv1.2']
    #     protocol = cert_info['protocol']
    #     if protocol not in secure_protocols:
    #         assessment['protocol_security'] = 'Protocol "{}" is outdated or insecure'.format(protocol)
    #
    #     # Return the assessment dictionary
    #     return assessment

    @staticmethod
    def format_cert_field(field: dict, function=None) -> str:
        """Format certificate subject information in a readable format.

        Args:
            field: Certificate field (typically a tuple of tuples)
            function: Function to apply as filter.

        Returns:
            Formatted string representation
        """
        # Extract common name, organization, etc.
        names = SSLHandler.extract_cert_fields(field, function)
        # Format extracted information in a readable string
        formatted_names = ', '.join(names.values())
        # Return formatted string
        return formatted_names

    @staticmethod
    def extract_cert_fields(cert_field, filter_func=None):
        """
        Extract fields from a certificate structure with an optional filter.

        Args:
            cert_field: A nested tuple structure from a certificate
            filter_func: Optional lambda function to filter fields by name

        Returns:
            Dictionary mapping field names to their values
        """
        # Function to extract name-value pairs
        result = {}
        def process_item(item):
            if isinstance(item, tuple):
                if len(item) == 2 and isinstance(item[0], str):
                    # This looks like a name-value pair
                    name, value = item
                    if filter_func is None or filter_func(name):
                        if name in result:
                            result[name] = result.get(name) + ', ' + value
                        else:
                            result[name] = value
                else:
                    # This is a container, process each item
                    for sub_item in item:
                        process_item(sub_item)

        # Start processing the field
        process_item(cert_field)
        return result

    @staticmethod
    def parse_cert_date(cert_date):
        """Convert certificate date to Python datetime object.

        Args:
            cert_date: Date string in ASN.1 format

        Returns:
            datetime object
        """
        return parser.parse(cert_date)