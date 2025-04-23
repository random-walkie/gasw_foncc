import unittest
from tcp_monitor.analyzers.ip_analyzer import IPAnalyzer

class TestIPAnalyzer(unittest.TestCase):
    """Test suite for the IPAnalyzer class.

    These tests verify that the IPAnalyzer class correctly parses
    and analyzes IP packets according to RFC 791 (IPv4) and RFC 8200 (IPv6).
    """

    def setUp(self):
        """Set up test environment before each test case."""
        self.analyzer = IPAnalyzer()

        # Sample IPv4 packet (20 bytes header, no options, 4 bytes payload)
        # Version: 4, IHL: 5 (20 bytes), TOS: 0, Total Length: 24
        # ID: 0x1234, Flags: 0, Fragment Offset: 0
        # TTL: 64, Protocol: 6 (TCP), Header Checksum: 0x1234 (not verified here)
        # Source IP: 192.168.1.1, Destination IP: 10.0.0.1
        # Payload: "data"
        self.ipv4_packet = bytearray([
            0x45, 0x00, 0x00, 0x18,  # Version, IHL, TOS, Total Length
            0x12, 0x34, 0x00, 0x00,  # ID, Flags, Fragment Offset
            0x40, 0x06, 0x12, 0x34,  # TTL, Protocol, Header Checksum
            0xc0, 0xa8, 0x01, 0x01,  # Source IP
            0x0a, 0x00, 0x00, 0x01,  # Destination IP
            0x64, 0x61, 0x74, 0x61   # Payload "data"
        ])

        # Sample IPv6 packet (40 bytes header, 4 bytes payload)
        # Version: 6, Traffic Class: 0, Flow Label: 0
        # Payload Length: 4, Next Header: 6 (TCP), Hop Limit: 64
        # Source IP: 2001:db8::1, Destination IP: 2001:db8::2
        # Payload: "data"
        self.ipv6_packet = bytearray([
            0x60, 0x00, 0x00, 0x00,  # Version, Traffic Class, Flow Label
            0x00, 0x04, 0x06, 0x40,  # Payload Length, Next Header, Hop Limit
            0x20, 0x01, 0x0d, 0xb8,  # Source IP (part 1)
            0x00, 0x00, 0x00, 0x00,  # Source IP (part 2)
            0x00, 0x00, 0x00, 0x00,  # Source IP (part 3)
            0x00, 0x00, 0x00, 0x01,  # Source IP (part 4)
            0x20, 0x01, 0x0d, 0xb8,  # Destination IP (part 1)
            0x00, 0x00, 0x00, 0x00,  # Destination IP (part 2)
            0x00, 0x00, 0x00, 0x00,  # Destination IP (part 3)
            0x00, 0x00, 0x00, 0x02,  # Destination IP (part 4)
            0x64, 0x61, 0x74, 0x61   # Payload "data"
        ])

    def test_analyze_ipv4_packet(self):
        """Test analysis of a basic IPv4 packet."""
        # Analyze the IPv4 packet
        result = self.analyzer.analyze_packet(bytes(self.ipv4_packet))

        # Verify basic IPv4 header fields
        self.assertEqual(result['version'], 4)
        self.assertEqual(result['header_length'], 20)
        self.assertEqual(result['total_length'], 24)
        self.assertEqual(result['ttl'], 64)
        self.assertEqual(result['protocol'], 6)  # TCP

        # Verify IP addresses
        self.assertEqual(result['src_ip'], '192.168.1.1')
        self.assertEqual(result['dst_ip'], '10.0.0.1')

        # Verify fragment information
        self.assertEqual(result['flags'], {'df': False, 'mf': False})
        self.assertEqual(result['fragment_offset'], 0)

        # Verify payload extraction
        self.assertEqual(len(result['payload']), 4)
        self.assertEqual(result['payload'], b'data')

    def test_analyze_ipv6_packet(self):
        """Test analysis of a basic IPv6 packet."""
        # Analyze the IPv6 packet
        result = self.analyzer.analyze_packet(bytes(self.ipv6_packet))

        # Verify basic IPv6 header fields
        self.assertEqual(result['version'], 6)
        self.assertEqual(result['payload_length'], 4)
        self.assertEqual(result['next_header'], 6)  # TCP
        self.assertEqual(result['hop_limit'], 64)

        # Verify IP addresses
        self.assertEqual(result['src_ip'], '2001:db8::1')
        self.assertEqual(result['dst_ip'], '2001:db8::2')

        # Verify payload extraction
        self.assertEqual(len(result['payload']), 4)
        self.assertEqual(result['payload'], b'data')

    def test_fragmented_ipv4_packet(self):
        """Test analyzing a fragmented IPv4 packet."""
        # Create a fragmented IPv4 packet (MF flag set)
        fragmented_packet = bytearray(self.ipv4_packet)
        fragmented_packet[6] = 0x20  # Set MF flag
        fragmented_packet[7] = 0x05  # Fragment offset: 40 bytes (5 * 8)

        # Analyze the fragmented packet
        result = self.analyzer.analyze_packet(bytes(fragmented_packet))

        # Verify fragmentation fields
        self.assertEqual(result['flags']['mf'], True)
        self.assertEqual(result['flags']['df'], False)
        self.assertEqual(result['fragment_offset'], 40)
        self.assertTrue(result['is_fragment'])

    def test_ip_protocol_mapping(self):
        """Test mapping of IP protocol numbers to protocol names."""
        # Test common protocol numbers
        test_cases = [
            (1, 'ICMP'),
            (6, 'TCP'),
            (17, 'UDP'),
            (255, 'Reserved')
        ]

        for protocol_num, expected_name in test_cases:
            # Change the protocol field in the IPv4 packet
            modified_packet = bytearray(self.ipv4_packet)
            modified_packet[9] = protocol_num

            # Analyze the packet
            result = self.analyzer.analyze_packet(bytes(modified_packet))

            # Verify the protocol name
            self.assertEqual(result['protocol_name'], expected_name)

    def test_ipv4_options(self):
        """Test parsing of IPv4 header options."""
        # Create a packet with options (IHL=6, so header is 24 bytes)
        packet_with_options = bytearray(self.ipv4_packet)
        packet_with_options[0] = 0x46  # Version 4, IHL 6
        # Increase total length by 4 (one option word)
        packet_with_options[2] = 0x00
        packet_with_options[3] = 0x1C  # 28 bytes total
        # Insert a simple option after the header (Record Route Option - Type 7)
        packet_with_options.insert(20, 0x07)  # Option type
        packet_with_options.insert(21, 0x04)  # Option length
        packet_with_options.insert(22, 0x00)  # Pointer
        packet_with_options.insert(23, 0x00)  # Padding

        # Analyze the packet
        result = self.analyzer.analyze_packet(bytes(packet_with_options))

        # Verify the header length was parsed correctly
        self.assertEqual(result['header_length'], 24)

        # Verify options were parsed
        self.assertIn('options', result)
        self.assertEqual(len(result['options']), 1)
        self.assertEqual(result['options'][0]['type'], 7)  # Record Route
        self.assertEqual(result['options'][0]['length'], 4)

    def test_get_ip_address_type(self):
        """Test classification of IP address types."""
        # Test IPv4 address types
        test_cases = [
            ('127.0.0.1', 'loopback'),
            ('10.0.0.1', 'private'),
            ('172.16.0.1', 'private'),
            ('192.168.1.1', 'private'),
            ('8.8.8.8', 'public'),
            ('224.0.0.1', 'multicast'),
            ('255.255.255.255', 'broadcast')
        ]

        for ip_address, expected_type in test_cases:
            # Call the address type classifier method
                addr_type = self.analyzer.get_ip_address_type(ip_address)
                self.assertEqual(addr_type, expected_type)

    def test_parse_invalid_packet(self):
        """Test handling of invalid or malformed IP packets."""
        # Test with a too-short packet
        short_packet = bytes([0x45, 0x00, 0x00, 0x05])

        # This should not raise an exception but return an error indication
        result = self.analyzer.analyze_packet(short_packet)

        # Verify the result indicates an error
        self.assertIn('error', result)

        # Test with invalid version
        invalid_version = bytearray(self.ipv4_packet)
        invalid_version[0] = 0x95  # Version 9, IHL 5

        result = self.analyzer.analyze_packet(bytes(invalid_version))
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()