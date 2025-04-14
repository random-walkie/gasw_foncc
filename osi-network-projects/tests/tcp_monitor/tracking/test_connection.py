import unittest
from time import time

from tcp_monitor.tracking.connection import TCPConnection


class TestTCPConnection(unittest.TestCase):
    """Test suite for the TCPConnection class.

    These tests verify that the TCPConnection class correctly manages
    TCP connection state and statistics according to RFC 793.
    """

    def setUp(self):
        """Set up test environment before each test case."""
        # Create a sample connection
        self.connection = TCPConnection(
            src_ip="192.168.1.10",
            dst_ip="93.184.216.34",  # example.com
            src_port=52800,
            dst_port=80
        )

    def test_initial_state(self):
        """Test that a new connection is properly initialized."""
        # Verify initial attributes
        self.assertEqual(self.connection.src_ip, "192.168.1.10")
        self.assertEqual(self.connection.dst_ip, "93.184.216.34")
        self.assertEqual(self.connection.src_port, 52800)
        self.assertEqual(self.connection.dst_port, 80)

        # Verify initial state
        self.assertEqual(self.connection.state, "CLOSED")
        self.assertEqual(self.connection.bytes_sent, 0)
        self.assertEqual(self.connection.bytes_received, 0)
        self.assertEqual(self.connection.packets_sent, 0)
        self.assertEqual(self.connection.packets_received, 0)

        # Verify sequence numbers start at expected values
        self.assertEqual(self.connection.seq_num, 0)
        self.assertEqual(self.connection.ack_num, 0)

    def test_connection_key(self):
        """Test that the connection key is properly generated."""
        # The key should be a string that uniquely identifies this connection
        expected_key = "192.168.1.10:52800-93.184.216.34:80"
        self.assertEqual(self.connection.get_connection_key(), expected_key)

    def test_connection_reversed_key(self):
        """Test that the reversed connection key is properly generated."""
        # The reversed key is for identifying packets in the reverse direction
        expected_reversed_key = "93.184.216.34:80-192.168.1.10:52800"
        self.assertEqual(self.connection.get_reversed_connection_key(), expected_reversed_key)

    def test_three_way_handshake(self):
        """Test the TCP 3-way handshake state transitions."""
        # Initial state
        self.assertEqual(self.connection.state, "CLOSED")

        # Step 1: Client sends SYN
        self.connection.update_state({
            'syn': True,
            'ack': False,
            'fin': False,
            'rst': False
        }, is_source=True)
        self.assertEqual(self.connection.state, "SYN_SENT")

        # Step 2: Server responds with SYN-ACK
        self.connection.update_state({
            'syn': True,
            'ack': True,
            'fin': False,
            'rst': False
        }, is_source=False)
        self.assertEqual(self.connection.state, "SYN_RECEIVED")

        # Step 3: Client sends ACK
        self.connection.update_state({
            'syn': False,
            'ack': True,
            'fin': False,
            'rst': False
        }, is_source=True)
        self.assertEqual(self.connection.state, "ESTABLISHED")

    def test_connection_termination(self):
        """Test normal TCP connection termination (4-way handshake)."""
        # Setup: Get to ESTABLISHED state
        self._establish_connection()

        # Step 1: Client initiates close with FIN
        self.connection.update_state({
            'syn': False,
            'ack': False,
            'fin': True,
            'rst': False
        }, is_source=True)
        self.assertEqual(self.connection.state, "FIN_WAIT_1")

        # Step 2: Server acknowledges FIN
        self.connection.update_state({
            'syn': False,
            'ack': True,
            'fin': False,
            'rst': False
        }, is_source=False)
        self.assertEqual(self.connection.state, "FIN_WAIT_2")

        # Step 3: Server sends its own FIN
        self.connection.update_state({
            'syn': False,
            'ack': False,
            'fin': True,
            'rst': False
        }, is_source=False)
        self.assertEqual(self.connection.state, "TIME_WAIT")

        # Step 4: Client acknowledges server's FIN
        self.connection.update_state({
            'syn': False,
            'ack': True,
            'fin': False,
            'rst': False
        }, is_source=True)
        # After TIME_WAIT timeout, state becomes CLOSED, but we don't simulate that here
        self.assertEqual(self.connection.state, "TIME_WAIT")

    def test_connection_reset(self):
        """Test connection reset using RST flag."""
        # Setup: Get to ESTABLISHED state
        self._establish_connection()

        # Server sends RST
        self.connection.update_state({
            'syn': False,
            'ack': False,
            'fin': False,
            'rst': True
        }, is_source=False)
        self.assertEqual(self.connection.state, "CLOSED")

    def test_simultaneous_close(self):
        """Test the TCP simultaneous close scenario."""
        # Setup: Get to ESTABLISHED state
        self._establish_connection()

        # Both sides send FIN simultaneously
        self.connection.update_state({
            'syn': False,
            'ack': False,
            'fin': True,
            'rst': False
        }, is_source=True)
        self.assertEqual(self.connection.state, "FIN_WAIT_1")

        self.connection.update_state({
            'syn': False,
            'ack': False,
            'fin': True,
            'rst': False
        }, is_source=False)
        self.assertEqual(self.connection.state, "CLOSING")

        # Both sides acknowledge the FIN
        self.connection.update_state({
            'syn': False,
            'ack': True,
            'fin': False,
            'rst': False
        }, is_source=False)
        self.connection.update_state({
            'syn': False,
            'ack': True,
            'fin': False,
            'rst': False
        }, is_source=True)
        self.assertEqual(self.connection.state, "TIME_WAIT")

    def test_update_statistics(self):
        """Test that connection statistics are properly updated."""
        # Setup: Get to ESTABLISHED state
        self._establish_connection()

        # Update with packet data
        self.connection.update_statistics(
            packet_size=1460,  # Standard Ethernet MTU - headers
            payload_size=1400,
            is_source=True  # From client to server
        )

        # Check updated values
        self.assertEqual(self.connection.packets_sent, 1)
        self.assertEqual(self.connection.packets_received, 0)
        self.assertEqual(self.connection.bytes_sent, 1460)
        self.assertEqual(self.connection.bytes_received, 0)
        self.assertEqual(self.connection.payload_bytes_sent, 1400)
        self.assertEqual(self.connection.payload_bytes_received, 0)

        # Update with packet in other direction
        self.connection.update_statistics(
            packet_size=1460,
            payload_size=1400,
            is_source=False  # From server to client
        )

        # Check updated values
        self.assertEqual(self.connection.packets_sent, 1)
        self.assertEqual(self.connection.packets_received, 1)
        self.assertEqual(self.connection.bytes_sent, 1460)
        self.assertEqual(self.connection.bytes_received, 1460)
        self.assertEqual(self.connection.payload_bytes_sent, 1400)
        self.assertEqual(self.connection.payload_bytes_received, 1400)

    def test_update_sequence_numbers(self):
        """Test updating TCP sequence and acknowledgment numbers."""
        # Initialize sequence numbers
        self.connection.seq_num = 1000
        self.connection.ack_num = 2000

        # Update with a packet from client to server
        self.connection.update_sequence_numbers(
            seq_num=1000,
            ack_num=2000,
            payload_size=100,
            is_source=True
        )

        # Sequence number should increment by payload size
        self.assertEqual(self.connection.seq_num, 1100)
        self.assertEqual(self.connection.ack_num, 2000)

        # Update with a packet from server to client
        self.connection.update_sequence_numbers(
            seq_num=2000,
            ack_num=1100,  # Acknowledges the previous packet
            payload_size=200,
            is_source=False
        )

        # Both numbers should be updated
        self.assertEqual(self.connection.seq_num, 1100)
        self.assertEqual(self.connection.ack_num, 2200)

    def test_connection_duration(self):
        """Test calculation of connection duration."""
        # Set initial start time
        initial_time = time()
        self.connection.start_time = initial_time

        # Set last activity time to simulate some time passing
        self.connection.last_activity = initial_time + 10.5

        # Duration should be close to 10.5 seconds
        self.assertAlmostEqual(self.connection.get_duration(), 10.5, delta=0.1)

    def test_connection_idle_time(self):
        """Test calculation of idle time."""
        # Set last activity time to 5 seconds ago
        current_time = time()
        self.connection.last_activity = current_time - 5

        # Idle time should be close to 5 seconds
        self.assertAlmostEqual(self.connection.get_idle_time(), 5, delta=0.1)

    def test_connection_throughput(self):
        """Test calculation of connection throughput."""
        # Setup: Get to ESTABLISHED state and set start time
        self._establish_connection()
        self.connection.start_time = time() - 10  # 10 seconds ago

        # Add some traffic
        self.connection.bytes_sent = 1000000  # 1 MB
        self.connection.bytes_received = 5000000  # 5 MB

        # Calculate throughput
        send_rate = self.connection.get_send_throughput()  # Should be around 100 KB/s
        recv_rate = self.connection.get_receive_throughput()  # Should be around 500 KB/s

        # Check if throughput calculations are reasonable
        self.assertAlmostEqual(send_rate, 100000, delta=1000)  # ~100 KB/s
        self.assertAlmostEqual(recv_rate, 500000, delta=5000)  # ~500 KB/s

    def test_is_active(self):
        """Test the active status of a connection."""
        # A connection in ESTABLISHED state should be active
        self._establish_connection()
        self.assertTrue(self.connection.is_active())

        # A connection in CLOSED state should not be active
        self.connection.state = "CLOSED"
        self.assertFalse(self.connection.is_active())

        # A connection in TIME_WAIT should not be considered fully active
        self.connection.state = "TIME_WAIT"
        self.assertFalse(self.connection.is_active())

    def test_to_dict(self):
        """Test conversion of connection to dictionary."""
        # Setup: Get to ESTABLISHED state
        self._establish_connection()

        # Add some statistics
        self.connection.bytes_sent = 1000
        self.connection.bytes_received = 2000
        self.connection.packets_sent = 10
        self.connection.packets_received = 20
        self.connection.start_time = time() - 30
        self.connection.last_activity = time() - 5

        # Convert to dictionary
        conn_dict = self.connection.to_dict()

        # Check dictionary contents
        self.assertEqual(conn_dict['src_ip'], "192.168.1.10")
        self.assertEqual(conn_dict['dst_ip'], "93.184.216.34")
        self.assertEqual(conn_dict['src_port'], 52800)
        self.assertEqual(conn_dict['dst_port'], 80)
        self.assertEqual(conn_dict['state'], "ESTABLISHED")
        self.assertEqual(conn_dict['bytes_sent'], 1000)
        self.assertEqual(conn_dict['bytes_received'], 2000)
        self.assertEqual(conn_dict['packets_sent'], 10)
        self.assertEqual(conn_dict['packets_received'], 20)
        self.assertIn('duration', conn_dict)
        self.assertIn('idle_time', conn_dict)

    def test_service_identification(self):
        """Test identification of common services by port."""
        # Test well-known port
        http_conn = TCPConnection("192.168.1.10", "93.184.216.34", 12345, 80)
        self.assertEqual(http_conn.get_service(), "HTTP")

        # Test HTTPS
        https_conn = TCPConnection("192.168.1.10", "93.184.216.34", 12345, 443)
        self.assertEqual(https_conn.get_service(), "HTTPS")

        # Test SSH
        ssh_conn = TCPConnection("192.168.1.10", "93.184.216.34", 12345, 22)
        self.assertEqual(ssh_conn.get_service(), "SSH")

        # Test unknown port
        unknown_conn = TCPConnection("192.168.1.10", "93.184.216.34", 12345, 54321)
        self.assertEqual(unknown_conn.get_service(), "UNKNOWN")

    def test_format_connection_string(self):
        """Test the string representation of a connection."""
        # Format connection as string
        conn_str = str(self.connection)

        # Should contain key information
        self.assertIn("192.168.1.10", conn_str)
        self.assertIn("93.184.216.34", conn_str)
        self.assertIn("52800", conn_str)
        self.assertIn("80", conn_str)
        self.assertIn("CLOSED", conn_str)

    # Helper methods - specific to this test class
    def _establish_connection(self):
        """Helper to get a connection to ESTABLISHED state."""
        # Simulate 3-way handshake
        self.connection.update_state({'syn': True, 'ack': False, 'fin': False, 'rst': False}, is_source=True)
        self.connection.update_state({'syn': True, 'ack': True, 'fin': False, 'rst': False}, is_source=False)
        self.connection.update_state({'syn': False, 'ack': True, 'fin': False, 'rst': False}, is_source=True)


if __name__ == '__main__':
    unittest.main()