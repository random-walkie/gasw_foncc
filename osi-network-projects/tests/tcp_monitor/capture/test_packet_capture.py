import unittest
from unittest.mock import Mock, patch
from tcp_monitor.capture.packet_capture import PacketCapture

class TestPacketCapture(unittest.TestCase):
    """Test suite for the PacketCapture class.
    """

    @patch('scapy.sendrecv.AsyncSniffer')
    def setUp(self, mock_async_sniffer):
        """Set up test environment before each test case."""
        # Mock the AsyncSniffer class
        self.mock_sniffer_instance = Mock()
        mock_async_sniffer.return_value = self.mock_sniffer_instance
        self.mock_sniffer_instance.results = [Mock(), Mock()]  # Mock captured packets

        # Create a sample packet for testing
        self.sample_packet = Mock()
        self.sample_packet.summary.return_value = "TCP 192.168.1.1:12345 > 10.0.0.1:80"

        # Create a PacketCapture instance
        self.packet_capture = PacketCapture()

    def test_initialization(self):
        """Test that a new PacketCapture instance is properly initialized."""
        # Check public properties
        self.assertEqual(self.packet_capture.packet_count, 0)
        self.assertFalse(self.packet_capture.is_running)
        self.assertIsNone(self.packet_capture.interface)

        # Check public attributes
        self.assertEqual(self.packet_capture.protocols, ["tcp"])
        self.assertIsNone(self.packet_capture.packet_callback)

    def test_interface_property(self):
        """Test interface property setter with validation."""
        # Test valid interface
        self.packet_capture.interface = "eth0"
        self.assertEqual(self.packet_capture.interface, "eth0")

        # Test invalid interface
        with self.assertRaises(ValueError):
            self.packet_capture.interface = ""

    def test_packet_count_readonly(self):
        """Test that packet_count is a read-only property."""
        with self.assertRaises(AttributeError):
            self.packet_capture.packet_count = 100

    def test_is_running_readonly(self):
        """Test that is_running is a read-only property."""
        with self.assertRaises(AttributeError):
            self.packet_capture.is_running = True

    def test_build_filter_string_comprehensive(self):
        """Test the _build_filter_string method with various filter combinations."""
        # Test with empty/default configuration
        self.packet_capture.protocols = ["tcp"]  # Default
        self.assertEqual(self.packet_capture._build_filter_string(), "(tcp)")

        # Test with single protocol
        self.packet_capture.protocols = ["udp"]
        self.assertEqual(self.packet_capture._build_filter_string(), "(udp)")

        # Test with multiple protocols
        self.packet_capture.protocols = ["tcp", "udp", "icmp"]
        self.assertEqual(self.packet_capture._build_filter_string(), "(tcp or udp or icmp)")

        # Test with port filter only
        self.packet_capture.protocols = ["tcp"]  # Reset to simpler case
        self.packet_capture.set_filters(port=80)
        self.assertEqual(self.packet_capture._build_filter_string(), "(tcp) and port 80")

        # Test with IP filter only
        self.packet_capture.set_filters(ip="192.168.1.1")
        self.assertEqual(self.packet_capture._build_filter_string(), "(tcp) and host 192.168.1.1")

        # Test with both port and IP filter
        self.packet_capture.set_filters(port=443, ip="10.0.0.1")
        self.assertEqual(self.packet_capture._build_filter_string(),
                         "(tcp) and port 443 and host 10.0.0.1")

        # Test with comprehensive configuration
        self.packet_capture.protocols = ["tcp", "udp"]
        self.packet_capture.set_filters(port=8080, ip="172.16.0.1")
        self.assertEqual(self.packet_capture._build_filter_string(),
                         "(tcp or udp) and port 8080 and host 172.16.0.1")

    @patch('tcp_monitor.capture.packet_capture.AsyncSniffer')
    def test_filter_construction_via_start_capture(self, mock_async_sniffer):
        """Test filter string construction by checking AsyncSniffer parameters."""
        # Setup for each test
        def reset_and_configure():
            mock_async_sniffer.reset_mock()
            self.packet_capture = PacketCapture()
            self.packet_capture.interface = "eth0"

        # Test default TCP filter
        reset_and_configure()
        self.packet_capture.start_capture()
        mock_async_sniffer.assert_called_with(
            iface="eth0",
            filter="(tcp)",
            prn=self.packet_capture._process_packet,
            count=100,
            timeout=60,
            store=False
        )

        # Test with port filter
        reset_and_configure()
        self.packet_capture.set_filters(port=80)
        self.packet_capture.start_capture()
        mock_async_sniffer.assert_called_with(
            iface="eth0",
            filter="(tcp) and port 80",
            prn=self.packet_capture._process_packet,
            count=100,
            timeout=60,
            store=False
        )

        # Test with IP filter
        reset_and_configure()
        self.packet_capture.set_filters(ip="192.168.1.1")
        self.packet_capture.start_capture()
        mock_async_sniffer.assert_called_with(
            iface="eth0",
            filter="(tcp) and host 192.168.1.1",
            prn=self.packet_capture._process_packet,
            count=100,
            timeout=60,
            store=False
        )

        # Test with multiple protocols
        reset_and_configure()
        self.packet_capture.set_filters(protocols=["tcp", "udp"])
        self.packet_capture.start_capture()
        mock_async_sniffer.assert_called_with(
            iface="eth0",
            filter="(tcp or udp)",
            prn=self.packet_capture._process_packet,
            count=100,
            timeout=60,
            store=False
        )

        # Test with all filters
        reset_and_configure()
        self.packet_capture.set_filters(port=443, ip="192.168.1.1", protocols=["tcp", "udp"])
        self.packet_capture.start_capture()
        mock_async_sniffer.assert_called_with(
            iface="eth0",
            filter="(tcp or udp) and port 443 and host 192.168.1.1",
            prn=self.packet_capture._process_packet,
            count=100,
            timeout=60,
            store=False
        )

    @patch('tcp_monitor.capture.packet_capture.AsyncSniffer')
    def test_start_capture(self, mock_async_sniffer):
        """Test starting packet capture with default parameters."""
        # Setup
        mock_sniffer = Mock()
        mock_async_sniffer.return_value = mock_sniffer

        # Execute the method being tested
        self.packet_capture.interface = "eth0"
        self.packet_capture.start_capture()

        # Verify the method had the expected effects
        self.assertTrue(self.packet_capture.is_running)
        self.assertEqual(mock_async_sniffer.call_count, 1)
        mock_sniffer.start.assert_called_once()

        # Check the arguments (with less strict comparison)
        args, kwargs = mock_async_sniffer.call_args
        self.assertEqual(kwargs['iface'], "eth0")
        self.assertEqual(kwargs['filter'], "(tcp)")
        self.assertEqual(kwargs['count'], 100)
        self.assertEqual(kwargs['timeout'], 60)
        self.assertEqual(kwargs['store'], False)

    @patch('tcp_monitor.capture.packet_capture.AsyncSniffer')
    def test_start_capture_with_custom_parameters(self, mock_async_sniffer):
        """Test starting packet capture with custom parameters."""
        # Configure capture with custom settings
        self.packet_capture.interface = "eth0"
        self.packet_capture.set_filters(port=80, ip="192.168.1.1", protocols=["tcp", "udp"])
        self.packet_capture.set_output_file("capture.pcap")

        # Start capture with custom duration and count
        self.packet_capture.start_capture(duration=120, count=1000)

        # Verify correct parameters were passed to AsyncSniffer
        mock_async_sniffer.assert_called_with(
            iface="eth0",
            filter="(tcp or udp) and port 80 and host 192.168.1.1",
            prn=self.packet_capture._process_packet,
            count=1000,
            timeout=120,
            store=True  # Should store packets because output file is set
        )

    def test_start_capture_errors(self):
        """Test error handling when starting capture."""
        # Test starting without configuring interface
        with self.assertRaises(ValueError):
            self.packet_capture.start_capture()

        # Configure interface
        self.packet_capture.interface = "eth0"

        # Set running state and test starting when already running
        # We need to patch is_running property because we can't directly set private attributes
        with patch.object(self.packet_capture, '_is_running', True):
            with self.assertRaises(ValueError):
                self.packet_capture.start_capture()

    @patch('tcp_monitor.capture.packet_capture.AsyncSniffer')
    def test_start_capture_exception(self, mock_async_sniffer):
        """Test exception handling during capture start."""
        # Setup mock to raise exception
        mock_sniffer_instance = mock_async_sniffer.return_value
        mock_sniffer_instance.start.side_effect = Exception("Capture error")

        # Configure interface
        self.packet_capture.interface = "eth0"

        # Start capture should raise the exception
        with self.assertRaises(Exception):
            self.packet_capture.start_capture()

        # State should reset - verify through is_running property
        self.assertFalse(self.packet_capture.is_running)

    @patch('tcp_monitor.capture.packet_capture.wrpcap')
    def test_stop_capture(self, mock_wrpcap):
        """Test stopping a capture without output file."""
        # Setup: We need to patch internal state
        with patch.object(self.packet_capture, '_is_running', True):
            # We need to set _sniffer but can't access it directly, so use a context manager
            with patch.object(self.packet_capture, '_sniffer', self.mock_sniffer_instance):
                # Stop capture
                self.packet_capture.stop_capture()

                # Verify sniffer was stopped
                self.mock_sniffer_instance.stop.assert_called_once()
                mock_wrpcap.assert_not_called()

    @patch('tcp_monitor.capture.packet_capture.wrpcap')
    def test_stop_capture_with_output(self, mock_wrpcap):
        """Test stopping capture with output file."""
        # Setup: We need to patch internal state
        with patch.object(self.packet_capture, '_is_running', True):
            # We need to set up _sniffer and _output_file without direct access
            with patch.object(self.packet_capture, '_sniffer', self.mock_sniffer_instance):
                # Set output file
                self.packet_capture.set_output_file("capture.pcap")

                # Stop capture
                self.packet_capture.stop_capture()

                # Verify sniffer was stopped and wrpcap was called
                self.mock_sniffer_instance.stop.assert_called_once()
                mock_wrpcap.assert_called_once()
                # Check first argument is the filename
                self.assertEqual(mock_wrpcap.call_args[0][0], "capture.pcap")
                # Check second argument is the results
                self.assertEqual(mock_wrpcap.call_args[0][1], self.mock_sniffer_instance.results)

    def test_stop_capture_not_running(self):
        """Test stopping capture when not running."""
        # Make sure is_running returns False
        with patch.object(self.packet_capture, '_is_running', False):
            # Stop capture - should not raise exception
            self.packet_capture.stop_capture()

    def test_process_packet(self):
        """Test packet processing callback."""
        # Setup mock callback
        callback_mock = Mock()
        self.packet_capture.packet_callback = callback_mock

        # Process a packet
        self.packet_capture._process_packet(self.sample_packet)

        # Verify packet was processed - we check packet_count through property
        self.assertEqual(self.packet_capture.packet_count, 1)
        callback_mock.assert_called_once_with(self.sample_packet)

        # Process another packet
        self.packet_capture._process_packet(self.sample_packet)

        # Verify count increased and callback called again
        self.assertEqual(self.packet_capture.packet_count, 2)
        self.assertEqual(callback_mock.call_count, 2)

    def test_process_packet_no_callback(self):
        """Test packet processing without a callback."""
        # Setup - no callback
        self.packet_capture.packet_callback = None

        # Process a packet
        self.packet_capture._process_packet(self.sample_packet)

        # Verify packet count was incremented without error
        self.assertEqual(self.packet_capture.packet_count, 1)
