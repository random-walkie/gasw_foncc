from time import time
class TCPConnection:
    """
    Represents a TCP connection and its state machine.

    This class provides the functionality to model a TCP connection,
    including various states and transitions of the state machine according
    to the TCP protocol. It can be used to simulate or manage real-world
    TCP communication scenarios.
    """

    def __init__(self, src_ip, dst_ip, src_port, dst_port) -> None:
        """Initialize a TCPConnection object."""

        # Store connection identifiers
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port

        # Initialize TCP state
        self.state = 'CLOSED'

        # Initialize sequence tracking
        self.seq_num = 0
        self.ack_num = 0

        # Initialize statistics
        self.bytes_sent = 0
        self.bytes_received = 0
        self.packets_sent = 0
        self.packets_received = 0
        self.payload_bytes_sent = 0
        self.payload_bytes_received = 0

        # Initialize timing information
        self.start_time = time()
        self.last_activity = time()

    def get_connection_key(self) -> str:
        """
        Generate a unique string that represents this TCP connection.

        The connection key is formed by concatenating the source IP, source port,
        destination IP, and destination port in the following format:
        'src_ip:src_port-dst_ip:dst_port'.

        Returns:
            str: A string representing the connection key.
        """
        return f"{self.src_ip}:{self.src_port}-{self.dst_ip}:{self.dst_port}"

    def get_reversed_connection_key(self) -> str:
        """
        Generate a connection key with reversed source and destination values.

        This method creates a unique identifier for the TCP connection where
        the source and destination IP addresses and ports are swapped compared
        to the original connection key.

        Returns:
            str: A string representing the reversed connection key.
        """
        return f"{self.dst_ip}:{self.dst_port}-{self.src_ip}:{self.src_port}"

    def update_state(self, flags=None, is_source=True) -> None:
        """
        Update the state of the TCP connection based on the provided flags.

        This method processes TCP flags to determine the state transition 
        of the connection according to the TCP protocol. It also updates 
        the sequence and acknowledgment numbers if applicable.

        Args:
            flags (dict): A dictionary of TCP flags, such as 'SYN', 'ACK', 
                          'FIN', etc., where the keys are flag names and 
                          the values are booleans indicating whether the flag 
                          is set.
            is_source (bool): A boolean indicating whether the flags are 
                              from the source side of the connection. 
                              If True, it represents the source; otherwise, 
                              it represents the destination.

        Returns:
            None
        """
        if flags is None:
            flags = {
                'syn': False,
                'ack': False,
                'fin': False,
                'rst': False
            }

        # Handle RST flag specially - always goes to CLOSED
        if flags.get("rst"):
            self.state = "CLOSED"

        # Handle state transitions based on the current state and packet direction
        if self.state == "CLOSED":
            # Client (source) initiates connection with SYN
            if flags.get("syn") and not flags.get("ack") and is_source:
                self.state = "SYN_SENT"
            # Server (destination) initiates connection (simultaneous open)
            elif flags.get("syn") and flags.get("ack") and not is_source:
                self.state = "SYN_RECEIVED"

        elif self.state == "SYN_SENT":
            # Server responds with SYN-ACK
            if flags.get("syn") and flags.get("ack") and not is_source:
                self.state = "SYN_RECEIVED"
            # Simultaneous open - both sides sent SYN
            elif flags.get("syn") and not flags.get("ack") and not is_source:
                self.state = "SYN_RECEIVED"

        elif self.state == "SYN_RECEIVED":
            if flags.get("ack") and not flags.get("fin") and not flags.get("syn") and is_source:
                # Client completes three-way handshake with ACK
                self.state = "ESTABLISHED"
            elif flags.get("ack") and not flags.get("syn") and not flags.get("fin") and not is_source:
                # Server acknowledges in simultaneous open
                self.state = "ESTABLISHED"

        elif self.state == "ESTABLISHED":
            # Client initiates close with FIN
            if flags.get("fin") and is_source:
                self.state = "FIN_WAIT_1"


        elif self.state == "FIN_WAIT_1":
            # Server acknowledges FIN
            if flags.get("ack") and not flags.get("fin") and not flags.get("syn") and not is_source:
                self.state = "FIN_WAIT_2"
            # Both sides send FIN simultaneously
            elif flags.get("fin") and not flags.get("ack") and not flags.get("syn") and not is_source:
                self.state = "CLOSING"

        elif self.state == "FIN_WAIT_2":
            # Client acknowledges server's FIN
            if flags.get("ack") and not flags.get("fin") and not flags.get("syn") and is_source:
                self.state = "TIME_WAIT"
            # Server sends its own FIN
            elif flags.get("fin") and not flags.get("ack") and not flags.get("syn") and not is_source:
                self.state = "TIME_WAIT"

        elif self.state == "CLOSING":
            # Both sides acknowledge the FIN
            if flags.get("ack") and not flags.get("fin") and not flags.get("syn") and not is_source:
                self.state = "TIME_WAIT"
                
    def update_statistics(self, packet_size=0, payload_size=0, is_source=True) -> None:

        """
        Update the statistics of the TCP connection.

        This method updates various statistical attributes of the 
        TCP connection, such as the number of bytes and packets sent
        and received, as well as the amount of payload data transferred.

        It uses the information from the current state of the connection
        to compute these values. This method can be called periodically 
        to track the performance and activity of the connection.
        
        Args:
            packet_size (int): The size of the entire packet, including headers and data.
            payload_size (int): The amount of actual application data in the packet.
            is_source (bool): Indicates whether the statistics update is for the source side
                              of the connection (True) or the destination side (False).
        
        Returns:
            None
        """
        if is_source:
            self.bytes_sent += packet_size
            self.payload_bytes_sent += payload_size
            self.packets_sent += 1
        else:
            self.bytes_received += packet_size
            self.payload_bytes_received += payload_size
            self.packets_received += 1
            
    def update_sequence_numbers(self, seq_num=0, ack_num=0, payload_size=0, is_source=True):
        
        """
        Update the sequence and acknowledgment numbers for the TCP connection.

        This method updates the sequence and acknowledgment numbers based on
        the provided values. It also accounts for the payload size to adjust
        the sequence number for transmitted data.

        Args:
            seq_num (int): The sequence number to be updated. It represents
                           the current sequence number in the data transfer.
            ack_num (int): The acknowledgment number to be updated. It indicates
                           the next expected sequence number from the other side.
            payload_size (int): The size of the payload data being sent or received.
                                This is used to adjust the sequence number for
                                transmitted data.
            is_source (bool): A boolean indicating whether the update is for the 
                              source side of the connection. If True, the source 
                              values are updated; otherwise, the destination values 
                              are updated.

        Returns:
            None
        """
        if is_source:
            self.seq_num = seq_num + payload_size
            self.ack_num = ack_num
        else:
            self.seq_num = ack_num
            self.ack_num = seq_num + payload_size

    def get_duration(self) -> float:

        """
        Calculate the duration of the TCP connection.

        This method computes the total time elapsed since the 
        creation of the TCP connection based on its start time.

        Returns:
            float: The duration of the connection in seconds, 
                   represented as a floating-point number.
        """
        return self.last_activity - self.start_time
    
    def get_idle_time(self) -> float:
        """
        Calculate the idle time of the TCP connection.

        This method calculates the amount of time the connection has been idle 
        since the last recorded activity.

        Returns:
            float: The idle time of the connection in seconds, represented 
                   as a floating-point number.
        """
        return self.start_time - self.last_activity
    
    def get_send_throughput(self) -> float:

        """
        Calculate the send throughput of the TCP connection.

        This method computes the data transfer rate for transmitted data, 
        by evaluating the total payload bytes sent by the connection and 
        dividing it by the elapsed time.

        Returns:
            float: The send throughput in bytes per second, represented 
                   as a floating-point number. If the connection duration 
                   is 0, the throughput is considered to be 0 to avoid 
                   division by zero.
        """
        return self.bytes_sent / self.get_duration() if self.get_duration() > 0 else 0
    
    def get_receive_throughput(self):
        """
        Calculate the receive throughput of the TCP connection.

        This method computes the data transfer rate for received data,
        by evaluating the total payload bytes received by the connection and
        dividing it by the elapsed time.

        Returns:
            float: The receive throughput in bytes per second, represented
                   as a floating-point number. If the connection duration
                   is 0, the throughput is considered to be 0 to avoid
                   division by zero.
        """
        return self.bytes_received / self.get_duration() if self.get_duration() > 0 else 0

    def is_active(self) -> bool:

        """
        Check if the TCP connection is still active.

        This method determines whether the TCP connection is currently 
        active based on its state. A connection is considered active if 
        it is not in the "CLOSED" or "TIME_WAIT" state.

        Returns:
            bool: True if the connection is active, False otherwise.
        """
        return False if self.state == "CLOSED" or self.state == "TIME_WAIT" else True

    def to_dict(self) -> dict:

        """
        Convert the TCP connection details to a dictionary representation.

        This method consolidates the TCP connection's attributes, such as 
        source and destination information, state, data transfer statistics, 
        and time-related metrics, into a dictionary structure. This is useful 
        for logging, debugging, or exporting the connection's information in 
        a serialized format.

        Returns:
            dict: A dictionary containing TCP connection details with keys like
                  'src_ip', 'dst_ip', 'src_port', 'dst_port', 'state', 
                  'bytes_sent', 'bytes_received', 'packets_sent', 
                  'packets_received', 'duration', and 'idle_time'.
        """
        return {
            'src_ip': self.src_ip,
            'dst_ip': self.dst_ip,
            'src_port': self.src_port,
            'dst_port': self.dst_port,
            'state': self.state,
            'bytes_sent': self.bytes_sent,
            'bytes_received': self.bytes_received,
            'packets_sent': self.packets_sent,
            'packets_received': self.packets_received,
            'duration': self.get_duration(),
            'idle_time': self.get_idle_time()
        }

    def get_service(self) -> str:
        """
        Determine the service associated with the destination port.

        This method analyzes the destination port of the TCP connection 
        and maps it to a commonly known service protocol (e.g., HTTP, FTP, SSH).
        If the destination port does not match any predefined service, it
        returns "UNKNOWN".

        Returns:
            str: The name of the service associated with the destination port,
                 such as "HTTP", "HTTPS", "FTP", etc. If no service matches, 
                 it returns "UNKNOWN".
        """
        if self.dst_port == 80:
            return "HTTP"
        elif self.dst_port == 443:
            return "HTTPS"
        elif self.dst_port == 21:
            return "FTP"
        elif self.dst_port == 22:
            return "SSH"
        elif self.dst_port == 23:
            return "TELNET"
        elif self.dst_port == 25:
            return "SMTP"
        elif self.dst_port == 53:
            return "DNS"
        else:
            return "UNKNOWN"

    def __str__(self):
        return (f"The source address is: {self.src_ip}\n"
                f"The destination address is: {self.dst_ip}\n"
                f"The source port is: {self.src_port}\n"
                f"The destination port is: {self.dst_port}\n"
                f"The connection is: {self.state}")