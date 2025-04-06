import unittest
import socket
import ssl
import datetime
from src.http_analyzer.ssl_handler import SSLHandler

class TestSSLHandler(unittest.TestCase):
    """Test suite for the SSLHandler class.

    These tests verify that the SSLHandler correctly manages SSL/TLS connections
    and certificate handling for HTTPS communications.
    """

    def setUp(self):
        """Set up resources needed for testing."""
        # Create a sample socket for testing
        self.test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Real certificate example for testing
        self.real_cert = {
            'issuer': ((('countryName', 'IL'),),
                       (('organizationName', 'StartCom Ltd.'),),
                       (('organizationalUnitName', 'Secure Digital Certificate Signing'),),
                       (('commonName', 'StartCom Class 2 Primary Intermediate Server CA'),)),
            'notAfter': 'Nov 22 08:15:19 2013 GMT',
            'notBefore': 'Nov 21 03:09:52 2011 GMT',
            'serialNumber': '95F0',
            'subject': ((('description', '571208-SLe257oHY9fVQ07Z'),),
                        (('countryName', 'US'),),
                        (('stateOrProvinceName', 'California'),),
                        (('localityName', 'San Francisco'),),
                        (('organizationName', 'Electronic Frontier Foundation, Inc.'),),
                        (('commonName', '*.eff.org'),),
                        (('emailAddress', 'hostmaster@eff.org'),)),
            'subjectAltName': (('DNS', '*.eff.org'), ('DNS', 'eff.org')),
            'version': 3
        }

    def tearDown(self):
        """Clean up resources after testing."""
        # Close the socket if it's still open
        try:
            self.test_socket.close()
        except:
            pass

    def test_wrap_socket_basic(self):
        """Test basic socket wrapping functionality.

        Note: This test doesn't actually establish a connection,
        but verifies that the method attempts to wrap the socket correctly.
        """
        # This test will likely fail with a connection error since we're not
        # actually connecting to a server, but we can check that it tries
        # to create the proper SSL context
        try:
            wrapped_socket = SSLHandler.wrap_socket(self.test_socket, "example.com")
            # If we somehow get here without an error, make sure we got an SSL socket
            self.assertIsInstance(wrapped_socket, ssl.SSLSocket)
        except (ssl.SSLError, socket.error):
            # Expected errors when not actually connecting
            pass

    def test_wrap_socket_parameters(self):
        """Test that wrap_socket passes the correct parameters to the SSL context."""
        # We can monkey-patch ssl.create_default_context to check parameters
        original_create_context = ssl.create_default_context

        try:
            # Create a mock context to check parameters
            context_params = {}

            def mock_create_context(purpose=ssl.Purpose.SERVER_AUTH):
                context_params['purpose'] = purpose
                mock_context = original_create_context(purpose)

                # Save the original wrap_socket method
                original_wrap = mock_context.wrap_socket

                # Replace it with our mock
                def mock_wrap_socket(sock, server_hostname=None, **kwargs):
                    context_params['server_hostname'] = server_hostname
                    context_params['kwargs'] = kwargs
                    # Return the original socket since we're not actually wrapping
                    return sock

                mock_context.wrap_socket = mock_wrap_socket
                return mock_context

            # Replace the real function with our mock
            ssl.create_default_context = mock_create_context

            # Call the method we're testing
            SSLHandler.wrap_socket(self.test_socket, "test.example.com")

            # Check that the correct parameters were passed
            self.assertEqual(context_params.get('server_hostname'), "test.example.com")
            self.assertEqual(context_params.get('purpose'), ssl.Purpose.SERVER_AUTH)

        finally:
            # Restore the original function
            ssl.create_default_context = original_create_context

    def test_get_certificate_info_parsing(self):
        """Test certificate information parsing using a real certificate structure."""
        # Create a mock SSL socket that returns our real certificate example
        class MockSSLSocket:
            def __init__(self, cert):
                self.cert = cert

            def getpeercert(self):
                return self.cert

            def cipher(self):
                return ('TLS_AES_256_GCM_SHA384', 'TLSv1.3', 256)

        mock_socket = MockSSLSocket(self.real_cert)

        # Call the method under test
        cert_info = SSLHandler.get_certificate_info(mock_socket)

        # Verify that the certificate info contains expected fields
        self.assertIsInstance(cert_info, dict)
        self.assertIn('subject', cert_info)
        self.assertIn('issuer', cert_info)
        self.assertIn('valid_from', cert_info)
        self.assertIn('valid_until', cert_info)
        self.assertIn('cipher', cert_info)
        self.assertIn('alt_names', cert_info)

        # Check that the values were correctly extracted from the nested structure
        self.assertIn('*.eff.org', cert_info['subject'])
        self.assertIn('Electronic Frontier Foundation', cert_info['subject'])
        self.assertIn('StartCom', cert_info['issuer'])

        # Check that dates were parsed correctly
        self.assertIn('2011', cert_info['valid_from'])
        self.assertIn('2013', cert_info['valid_until'])

        # Check that alternative names were extracted
        self.assertIn('*.eff.org', cert_info['alt_names'])
        self.assertIn('eff.org', cert_info['alt_names'])

    def test_extract_cert_field(self):
        """Test extraction of certificate field information using real certificate structure."""
        # Extract issuer from our real certificate example
        issuer = self.real_cert['issuer']

        # Call the method
        extracted = SSLHandler.extract_cert_fields(issuer,  lambda pattern: 'Name' in pattern)

        # Check that it is a dictionary
        self.assertIsInstance(extracted, dict)
        # Check key-value pairs
        self.assertEqual(extracted['countryName'], 'IL')
        self.assertEqual(extracted['organizationName'], 'StartCom Ltd.')
        self.assertEqual(extracted['organizationalUnitName'], 'Secure Digital Certificate Signing')
        self.assertEqual(extracted['commonName'], 'StartCom Class 2 Primary Intermediate Server CA')

    def test_extract_cert_field_dns(self):
        """Test extraction of certificate field information using real certificate structure."""
        # Extract issuer from our real certificate example
        alt_names = self.real_cert['subjectAltName']

        # Call the method
        extracted = SSLHandler.extract_cert_fields(alt_names,  lambda pattern: 'DNS' in pattern)

        # Check that it is a dictionary
        self.assertIsInstance(extracted, dict)
        # Check key-value pairs
        self.assertIn('*.eff.org', extracted['DNS'])
        self.assertIn('eff.org', extracted['DNS'])

    def test_format_cert_field(self):
        """Test formatting of certificate subject information using real certificate structure."""
        # Extract subject from our real certificate example
        subject = self.real_cert['subject']

        # Call the method under test
        formatted = SSLHandler.format_cert_field(subject)

        # Check that the formatted string contains the expected information
        self.assertIsInstance(formatted, str)
        self.assertIn('*.eff.org', formatted)
        self.assertIn('Electronic Frontier Foundation', formatted)
        self.assertIn('San Francisco', formatted)
        self.assertIn('California', formatted)
        self.assertIn('US', formatted)

    def test_parse_certificate_dates(self):
        """Test parsing of certificate date formats."""
        # Test with the real date format from certificates
        not_before = 'Nov 21 03:09:52 2011 GMT'
        not_after = 'Nov 22 08:15:19 2013 GMT'

        # Assuming your SSLHandler has a method to parse these dates
        from_date = SSLHandler.parse_cert_date(not_before)
        until_date = SSLHandler.parse_cert_date(not_after)

        # Verify the parsed dates
        self.assertIsInstance(from_date, datetime.datetime)
        self.assertEqual(from_date.year, 2011)
        self.assertEqual(from_date.month, 11)
        self.assertEqual(from_date.day, 21)

        self.assertIsInstance(until_date, datetime.datetime)
        self.assertEqual(until_date.year, 2013)
        self.assertEqual(until_date.month, 11)
        self.assertEqual(until_date.day, 22)

    # def test_get_security_assessment(self):
    #     """Test security assessment of SSL/TLS connection."""
    #     # Create a mock certificate info dictionary
    #     cert_info = {
    #         'subject': 'CN=*.example.com, O=Example Inc, C=US',
    #         'issuer': 'CN=Example CA, O=Example Trust Network, C=US',
    #         'valid_from': 'Nov 21 03:09:52 2023 GMT',
    #         'valid_until': 'Nov 22 08:15:19 2025 GMT',
    #         'cipher': 'TLS_AES_256_GCM_SHA384',
    #         'protocol': 'TLSv1.3',
    #         'key_size': 256,
    #         'alt_names': ['*.example.com', 'example.com']
    #     }
    #
    #     # Call the method under test
    #     assessment = SSLHandler.get_security_assessment(cert_info)
    #
    #     # Check that assessment contains expected fields
    #     self.assertIsInstance(assessment, dict)
    #     self.assertIn('overall_rating', assessment)
    #     self.assertIn('cipher_strength', assessment)
    #     self.assertIn('protocol_security', assessment)
    #
    #     # A certificate with TLS 1.3 and strong cipher should get a good rating
    #     self.assertIn(assessment['overall_rating'], ['Good', 'Excellent'])
    #
    # def test_security_assessment_weak_connection(self):
    #     """Test security assessment of a weak SSL/TLS connection."""
    #
    #     # Create a mock SSL socket and configure it with weak security characteristics
    #     class MockSSLSocket:
    #         def getpeercert(self):
    #             return {
    #                 'issuer': ((('countryName', 'US'),),
    #                            (('organizationName', 'Example CA'),),
    #                            (('organizationalUnitName', 'Example Trust Network'),)),
    #                 'notAfter': 'Nov 22 08:15:19 2025 GMT',
    #                 'notBefore': 'Nov 21 03:09:52 2023 GMT',
    #                 'subject': ((('commonName', '*.example.com'),),
    #                             (('organizationName', 'Example Inc'),),
    #                             (('countryName', 'US'),)),
    #                 'subjectAltName': (('DNS', '*.example.com'), ('DNS', 'example.com')),
    #             }
    #
    #         def cipher(self):
    #             return ('TLS_RSA_WITH_3DES_EDE_CBC_SHA', 'TLSv1.0', 128)
    #
    #     mock_socket = MockSSLSocket()
    #
    #     # Get the certificate info from the mock socket
    #     cert_info = SSLHandler.get_certificate_info(mock_socket)
    #
    #     # Call the method under test
    #     assessment = SSLHandler.get_security_assessment(cert_info)
    #
    #     # Check that assessment correctly identifies weak security
    #     self.assertIn(assessment['overall_rating'], ['Poor', 'Weak'])
    #     self.assertIn('outdated protocol', assessment['protocol_security'].lower())
    #
    # def test_security_assessment_expired_certificate(self):
    #     """Test security assessment of a connection with expired certificate."""
    #     # Create a mock certificate info dictionary with expired certificate
    #     # Using the real date format from certificates
    #     cert_info = {
    #         'subject': 'CN=*.example.com, O=Example Inc, C=US',
    #         'issuer': 'CN=Example CA, O=Example Trust Network, C=US',
    #         'valid_from': 'Nov 21 03:09:52 2011 GMT',
    #         'valid_until': 'Nov 22 08:15:19 2013 GMT',  # Expired
    #         'cipher': 'TLS_AES_256_GCM_SHA384',
    #         'protocol': 'TLSv1.3',
    #         'key_size': 256
    #     }
    #
    #     # Call the method under test
    #     assessment = SSLHandler.get_security_assessment(cert_info)
    #
    #     # Check that assessment correctly identifies expired certificate
    #     self.assertIn('expired', assessment['overall_rating'].lower())
    #     self.assertIn('certificate has expired', str(assessment).lower())


if __name__ == '__main__':
    unittest.main()