import unittest
from struct import pack
from tcp_monitor.analyzers.tcp_analyzer import TCPAnalyzer

class TestTCPAnalyzer(unittest.TestCase):
    """Test suite for the TCPAnalyzer class.

    These tests verify that the TCPAnalyzer class correctly extracts
    and interprets TCP segment data from raw packet bytes.
    """

    def setUp(self):
        """Set up test environment before each test case."""
        self.analyzer = TCPAnalyzer()

        # Create a sample TCP segment (header + payload)
        # Source port: 52800 (0xCE40)
        # Destination port: 80 (0x0050)
        # Sequence number: 1000 (0x000003E8)
        # Acknowledgment number: 2000 (0x000007D0)
        # Header length: 5 words (20 bytes), flags: ACK
        # Window size: 8192 (0x2000)
        # Checksum: 0x1234 (dummy value for test)
        # Urgent pointer: 0
        self.tcp_header = (
            b"\xCE\x40"  # Source port: 52800
            b"\x00\x50"  # Destination port: 80
            b"\x00\x00\x03\xE8"  # Sequence number: 1000
            b"\x00\x00\x07\xD0"  # Acknowledgment number: 2000
            b"\x50\x10"  # Data offset: 5 (0x5), flags: ACK (0x10)
            b"\x20\x00"  # Window size: 8192
            b"\x12\x34"  # Checksum: 0x1234
            b"\x00\x00"  # Urgent pointer: 0
        )

        # Sample TCP payload
        self.tcp_payload = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

        # Complete TCP segment
        self.tcp_segment = self.tcp_header + self.tcp_payload

    def test_parse_tcp_header_basic(self):
        """Test basic parsing of TCP header fields."""
        tcp_info = self.analyzer.analyze_segment(self.tcp_segment)

        # Check that all expected fields are present
        self.assertIn('src_port', tcp_info)
        self.assertIn('dst_port', tcp_info)
        self.assertIn('seq_num', tcp_info)
        self.assertIn('ack_num', tcp_info)
        self.assertIn('header_length', tcp_info)
        self.assertIn('window_size', tcp_info)
        self.assertIn('checksum', tcp_info)
        self.assertIn('urgent_ptr', tcp_info)
        self.assertIn('flags', tcp_info)

        # Check field values
        self.assertEqual(tcp_info['src_port'], 52800)
        self.assertEqual(tcp_info['dst_port'], 80)
        self.assertEqual(tcp_info['seq_num'], 1000)
        self.assertEqual(tcp_info['ack_num'], 2000)
        self.assertEqual(tcp_info['header_length'], 20)  # 5 words × 4 bytes
        self.assertEqual(tcp_info['window_size'], 8192)
        self.assertEqual(tcp_info['checksum'], 0x1234)
        self.assertEqual(tcp_info['urgent_ptr'], 0)

    def test_parse_tcp_flags(self):
        """Test parsing of TCP flags field."""
        tcp_info = self.analyzer.analyze_segment(self.tcp_segment)

        # Verify flags dictionary
        self.assertIn('flags', tcp_info)
        flags = tcp_info['flags']

        # Check individual flags (only ACK should be set in our test header)
        self.assertFalse(flags['fin'])
        self.assertFalse(flags['syn'])
        self.assertFalse(flags['rst'])
        self.assertFalse(flags['psh'])
        self.assertTrue(flags['ack'])
        self.assertFalse(flags['urg'])

    def test_parse_tcp_payload(self):
        """Test extraction of TCP payload data."""
        tcp_info = self.analyzer.analyze_segment(self.tcp_segment)

        # Check payload extraction
        self.assertIn('payload', tcp_info)
        self.assertEqual(tcp_info['payload'], self.tcp_payload)

        # Check payload size calculation
        self.assertIn('payload_size', tcp_info)
        self.assertEqual(tcp_info['payload_size'], len(self.tcp_payload))

    def test_parse_tcp_with_options(self):
        """Test parsing TCP header with options present."""
        # Create a header with data offset of 6 words (24 bytes) indicating presence of options
        # Adding 4 bytes of options after the standard 20-byte header
        # Options: MSS (kind=2, length=4, value=1460)
        tcp_header_with_options = (
            b"\xCE\x40"  # Source port: 52800
            b"\x00\x50"  # Destination port: 80
            b"\x00\x00\x03\xE8"  # Sequence number: 1000
            b"\x00\x00\x07\xD0"  # Acknowledgment number: 2000
            b"\x60\x10"  # Data offset: 6 (0x6), flags: ACK (0x10)
            b"\x20\x00"  # Window size: 8192
            b"\x12\x34"  # Checksum: 0x1234
            b"\x00\x00"  # Urgent pointer: 0
            b"\x02\x04\x05\xB4"  # Option: MSS=1460
        )

        tcp_segment_with_options = tcp_header_with_options + self.tcp_payload

        tcp_info = self.analyzer.analyze_segment(tcp_segment_with_options)

        # Check header length is correctly parsed (6 words = 24 bytes)
        self.assertEqual(tcp_info['header_length'], 24)

        # Check that options field is present
        self.assertIn('options', tcp_info)
        self.assertEqual(tcp_info['options'], 'MSS=1460')

        # Check payload is correctly extracted after the options
        self.assertEqual(tcp_info['payload'], self.tcp_payload)

    def test_parse_all_flags_set(self):
        """Test parsing TCP segment with all flags set."""
        # Modified header with all flags set (0x3F)
        all_flags_header = (
            b"\xCE\x40"  # Source port: 52800
            b"\x00\x50"  # Destination port: 80
            b"\x00\x00\x03\xE8"  # Sequence number: 1000
            b"\x00\x00\x07\xD0"  # Acknowledgment number: 2000
            b"\x50\x3F"  # Data offset: 5 (0x5), all flags set (0x3F)
            b"\x20\x00"  # Window size: 8192
            b"\x12\x34"  # Checksum: 0x1234
            b"\x00\x00"  # Urgent pointer: 0
        )

        all_flags_segment = all_flags_header + self.tcp_payload

        tcp_info = self.analyzer.analyze_segment(all_flags_segment)

        # Verify all flags are set
        flags = tcp_info['flags']
        self.assertTrue(flags['fin'])
        self.assertTrue(flags['syn'])
        self.assertTrue(flags['rst'])
        self.assertTrue(flags['psh'])
        self.assertTrue(flags['ack'])
        self.assertTrue(flags['urg'])

    def test_parse_empty_segment(self):
        """Test parsing TCP segment with no payload."""
        # TCP segment with just the header and no payload
        empty_segment = self.tcp_header

        tcp_info = self.analyzer.analyze_segment(empty_segment)

        # Check payload is empty
        self.assertEqual(tcp_info['payload'], b"")
        self.assertEqual(tcp_info['payload_size'], 0)

    def test_parse_segment_too_short(self):
        """Test handling of TCP segment that's too short to be valid."""
        # Create a segment that's shorter than the minimum TCP header size
        short_segment = self.tcp_header[:10]  # Only 10 bytes, not the 20+ required
        # Should return an error indicator
        result = self.analyzer.analyze_segment(short_segment)
        # Verify the result indicates an error
        self.assertIn('error', result)

    def test_get_service_name(self):
        """Test identification of well-known services by port number."""
        # Test well-known ports
        self.assertEqual(self.analyzer.get_service_name(80), "HTTP")
        self.assertEqual(self.analyzer.get_service_name(443), "HTTPS")
        self.assertEqual(self.analyzer.get_service_name(22), "SSH")
        self.assertEqual(self.analyzer.get_service_name(25), "SMTP")

        # Test unknown port
        unknown_port = 12345
        self.assertEqual(self.analyzer.get_service_name(unknown_port), f"PORT-{unknown_port}")

    def test_is_control_packet(self):
        """Test identification of TCP control packets (SYN, FIN, RST)."""
        # Create analyzer instances with different flags
        syn_segment = self._create_segment_with_flags(syn=True)
        fin_segment = self._create_segment_with_flags(fin=True)
        rst_segment = self._create_segment_with_flags(rst=True)
        ack_segment = self._create_segment_with_flags(ack=True)

        # Parse segments
        syn_info = self.analyzer.analyze_segment(syn_segment)
        fin_info = self.analyzer.analyze_segment(fin_segment)
        rst_info = self.analyzer.analyze_segment(rst_segment)
        ack_info = self.analyzer.analyze_segment(ack_segment)

        # Check control packet identification
        self.assertTrue(self.analyzer.is_control_packet(syn_info))
        self.assertTrue(self.analyzer.is_control_packet(fin_info))
        self.assertTrue(self.analyzer.is_control_packet(rst_info))
        self.assertTrue(self.analyzer.is_control_packet(ack_info))

    def _create_segment_with_flags(self, fin=False, syn=False, rst=False,
                                   psh=False, ack=False, urg=False):
        """Helper method to create TCP segments with specific flags set."""
        # Calculate flags byte
        flags = 0
        if fin: flags |= 0x01
        if syn: flags |= 0x02
        if rst: flags |= 0x04
        if psh: flags |= 0x08
        if ack: flags |= 0x10
        if urg: flags |= 0x20

        # Create header with specified flags
        tcp_header = (
                b"\xCE\x40"  # Source port: 52800
                b"\x00\x50"  # Destination port: 80
                b"\x00\x00\x03\xE8"  # Sequence number: 1000
                b"\x00\x00\x07\xD0"  # Acknowledgment number: 2000
                + pack("!B", 0x50)           # Data offset: 5 (bits 4-7) with reserved bits (0-3) set to 0
                + pack("!B", flags & 0x3F)   # Flags
                + b"\x20\x00"  # Window size: 8192
                b"\x12\x34"  # Checksum: 0x1234
                b"\x00\x00"  # Urgent pointer: 0
        )

        return tcp_header + self.tcp_payload


if __name__ == '__main__':
    unittest.main()