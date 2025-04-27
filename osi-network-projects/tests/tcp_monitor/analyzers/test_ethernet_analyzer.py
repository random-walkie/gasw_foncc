import unittest
from tcp_monitor.analyzers.ethernet_analyzer import EthernetAnalyzer

class TestEthernetAnalyzer(unittest.TestCase):
    """Test suite for the EthernetAnalyzer class.

    These tests verify that the EthernetAnalyzer class correctly parses
    and analyzes Ethernet frames according to IEEE 802.3 standards.
    """

    def setUp(self):
        """Set up test environment before each test case."""
        # Sample Ethernet frame (header + payload)
        # Destination MAC: 00:1A:2B:3C:4D:5E
        # Source MAC: 5F:4E:3D:2C:1B:0A
        # EtherType: 0x0800 (IPv4)
        # Payload: 'Sample payload'
        self.eth_header = (
            b"\x00\x1A\x2B\x3C\x4D\x5E"  # Destination MAC
            b"\x5F\x4E\x3D\x2C\x1B\x0A"  # Source MAC
            b"\x08\x00"                  # EtherType (IPv4)
        )
        self.eth_payload = b"Sample payload"
        self.eth_frame = self.eth_header + self.eth_payload

    def test_analyze_ethernet_frame_basic(self):
        """Test basic parsing of Ethernet frame fields."""
        # This test verifies that the analyzer correctly extracts
        # the basic fields from an Ethernet frame
        eth_info = EthernetAnalyzer.analyze_frame(self.eth_frame)

        # Check basic field values
        self.assertEqual(eth_info['dst_mac'], '00:1a:2b:3c:4d:5e')
        self.assertEqual(eth_info['src_mac'], '5f:4e:3d:2c:1b:0a')
        self.assertEqual(eth_info['ethertype'], 0x0800)  # IPv4
        self.assertEqual(eth_info['ethertype_name'], 'IPv4')

        # Check payload extraction
        self.assertEqual(eth_info['payload'], self.eth_payload)
        self.assertEqual(eth_info['payload_size'], len(self.eth_payload))

    def test_analyze_ethernet_frame_ipv6(self):
        """Test parsing of Ethernet frame with IPv6 EtherType."""
        # Create a frame with IPv6 EtherType (0x86DD)
        ipv6_header = (
            b"\x00\x1A\x2B\x3C\x4D\x5E"  # Destination MAC
            b"\x5F\x4E\x3D\x2C\x1B\x0A"  # Source MAC
            b"\x86\xDD"                  # EtherType (IPv6)
        )
        ipv6_frame = ipv6_header + self.eth_payload

        eth_info = EthernetAnalyzer.analyze_frame(ipv6_frame)

        # Check EtherType-specific fields
        self.assertEqual(eth_info['ethertype'], 0x86DD)  # IPv6
        self.assertEqual(eth_info['ethertype_name'], 'IPv6')

    def test_analyze_ethernet_frame_arp(self):
        """Test parsing of Ethernet frame with ARP EtherType."""
        # Create a frame with ARP EtherType (0x0806)
        arp_header = (
            b"\x00\x1A\x2B\x3C\x4D\x5E"  # Destination MAC
            b"\x5F\x4E\x3D\x2C\x1B\x0A"  # Source MAC
            b"\x08\x06"                  # EtherType (ARP)
        )
        arp_frame = arp_header + self.eth_payload

        eth_info = EthernetAnalyzer.analyze_frame(arp_frame)

        # Check EtherType-specific fields
        self.assertEqual(eth_info['ethertype'], 0x0806)  # ARP
        self.assertEqual(eth_info['ethertype_name'], 'ARP')

    def test_broadcast_frame(self):
        """Test detection of broadcast Ethernet frames."""
        # Create a frame with broadcast destination MAC (FF:FF:FF:FF:FF:FF)
        broadcast_header = (
            b"\xFF\xFF\xFF\xFF\xFF\xFF"  # Broadcast Destination MAC
            b"\x5F\x4E\x3D\x2C\x1B\x0A"  # Source MAC
            b"\x08\x00"                  # EtherType (IPv4)
        )
        broadcast_frame = broadcast_header + self.eth_payload

        eth_info = EthernetAnalyzer.analyze_frame(broadcast_frame)

        # Check broadcast detection
        self.assertTrue(eth_info['is_broadcast'])
        self.assertEqual(eth_info['dst_mac'], 'ff:ff:ff:ff:ff:ff')

    def test_multicast_frame(self):
        """Test detection of multicast Ethernet frames."""
        # Create a frame with multicast destination MAC (first byte has least significant bit set)
        multicast_header = (
            b"\x01\x00\x5E\x00\x00\x01"  # Multicast Destination MAC (IPv4 multicast)
            b"\x5F\x4E\x3D\x2C\x1B\x0A"  # Source MAC
            b"\x08\x00"                  # EtherType (IPv4)
        )
        multicast_frame = multicast_header + self.eth_payload

        eth_info = EthernetAnalyzer.analyze_frame(multicast_frame)

        # Check multicast detection
        self.assertTrue(eth_info['is_multicast'])
        self.assertEqual(eth_info['dst_mac'], '01:00:5e:00:00:01')

    def test_get_ethertype_name(self):
        """Test mapping of EtherType values to protocol names."""
        # Define expected mappings for common EtherTypes
        ethertypes = {
            0x0800: 'IPv4',
            0x0806: 'ARP',
            0x86DD: 'IPv6',
            0x8100: '802.1Q',
            0x8847: 'MPLS',
            0x8863: 'PPPoE Discovery',
            0x8864: 'PPPoE Session',
            0x9999: 'Unknown'  # Made-up value for testing
        }

        # Test each EtherType
        for ethertype, expected_name in ethertypes.items():
            name = EthernetAnalyzer.get_ethertype_name(ethertype)
            self.assertEqual(name, expected_name)

    def test_malformed_frame(self):
        """Test handling of malformed Ethernet frames."""
        # Create a frame that's too short to be valid
        short_frame = self.eth_header[:10]  # Only 10 bytes, not the 14+ required

        result = EthernetAnalyzer.analyze_frame(short_frame)

        # Check that error was detected and reported
        self.assertIn('error', result)

    def test_format_mac_address(self):
        """Test formatting of MAC addresses."""
        # Raw MAC address bytes
        mac_bytes = b"\x00\x1A\x2B\x3C\x4D\x5E"

        formatted_mac = EthernetAnalyzer.format_mac_address(mac_bytes)

        # Check formatting
        self.assertEqual(formatted_mac, '00:1a:2b:3c:4d:5e')

    def test_analyze_vlan_tagged_frame(self):
        """Test parsing of 802.1Q VLAN tagged Ethernet frames."""
        # Create a frame with 802.1Q VLAN tag (EtherType 0x8100)
        # After the VLAN tag comes the actual EtherType (0x0800 for IPv4)
        vlan_header = (
            b"\x00\x1A\x2B\x3C\x4D\x5E"  # Destination MAC
            b"\x5F\x4E\x3D\x2C\x1B\x0A"  # Source MAC
            b"\x81\x00"                  # EtherType (802.1Q VLAN tag)
            b"\x00\x64"                  # VLAN ID 100 (0x0064)
            b"\x08\x00"                  # Inner EtherType (IPv4)
        )
        vlan_frame = vlan_header + self.eth_payload

        eth_info = EthernetAnalyzer.analyze_frame(vlan_frame)

        # Check VLAN-specific fields
        self.assertTrue(eth_info['is_vlan_tagged'])
        self.assertEqual(eth_info['vlan_id'], 100)
        self.assertEqual(eth_info['inner_ethertype'], 0x0800)
        self.assertEqual(eth_info['inner_ethertype_name'], 'IPv4')

if __name__ == '__main__':
    unittest.main()