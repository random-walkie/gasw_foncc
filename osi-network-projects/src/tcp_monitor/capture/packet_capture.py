from scapy.sendrecv import AsyncSniffer
from scapy.utils import wrpcap

class PacketCapture:
    """
    A class for capturing network packets using Scapy's AsyncSniffer.
    
    The `PacketCapture` class provides capabilities to configure network interfaces, 
    apply filters, and capture network packets based on specified criteria. 
    It supports capturing packets for a specified duration or count and can optionally 
    write the captured data to a file.
    
    Attributes:
        interface (str): The network interface to capture packets from.
        packet_count (int): The number of packets captured so far.
        is_running (bool): Indicates whether the packet capture is currently active.
        protocols (list): A list of protocols to filter during capture. Defaults to ["tcp"].
        packet_callback (callable): A callback function to process each captured packet.
    
    Methods:
        set_filters(port=None, ip=None, protocols=None):
            Configures port, IP, and protocol filters for packet capture.
    
        set_output_file(file_path=None):
            Specifies the file where captured packets should be saved.
    
        start_capture(duration=60, count=100):
            Starts capturing packets based on the configured settings.
    
        stop_capture():
            Stops the packet capture and saves the captured packets if an output file is specified.
    
        _build_filter_string():
            Constructs a string representing the filter configuration for packet capture.
    
        _process_packet(packet=None):
            Internal method to handle captured packets and invoke the packet callback if defined.
    """
    def __init__(self) -> None:
        """
        Initializes the PacketCapture instance with default values.

        This constructor sets up the initial state of the PacketCapture object. 
        Default protocol is set to "tcp", and the packet count starts from 0. 
        Other attributes like interface, port filter, and IP filter are initialized to None. 
        The sniffer is also not active by default.

        Attributes initialized:
            _interface (str): The network interface to capture packets from. Initially None.
            _packet_count (int): Counter for the number of packets captured. Starts at 0.
            _is_running (bool): Indicates the state of the packet capturing process. Initially False.
            _port_filter (str): Filter for specific port(s). Initially None.
            _ip_filter (str): Filter for specific IP(s). Initially None.
            _output_file (str): Path for the output file to save captured packets. Initially None.
            _sniffer (AsyncSniffer): Sniffer instance used for capturing packets. Initially None.
            protocols (list of str): List of protocols to filter during capture. Default is ["tcp"].
            packet_callback (callable): A callback function to process each packet captured. Initially None.
        """
        self._interface = None
        self._packet_count = 0
        self._is_running = False
        self._port_filter = None
        self._ip_filter = None
        self._output_file = None
        self._sniffer = None
        self.protocols = ["tcp"]
        self.packet_callback = None

    @property
    def interface(self) -> str:
        """
        Gets the configured network interface for packet capture.

        This property allows retrieving the name of the network interface 
        that has been set for capturing packets.

        Returns:
            str: The name of the network interface configured for packet capture.
        """
        return self._interface

    @property
    def packet_count(self) -> int:
        """
        Retrieves the current count of packets captured.

        This property provides access to the number of packets that have been
        captured since the packet capture started. It is automatically updated
        during the packet capture process.

        Returns:
            int: The total number of packets captured.
        """
        return self._packet_count

    @property
    def is_running(self) -> bool:
        """
        Checks if the packet capture process is currently active.

        This property provides a way to determine whether the packet 
        capturing process is running. It can be used to verify the state 
        of the capture operation before performing actions like starting 
        or stopping a capture.

        Returns:
            bool: True if the packet capture is currently active, False otherwise.
        """
        return self._is_running

    @interface.setter
    def interface(self, value) -> None:
        """
        Sets the network interface for packet capture.

        This setter method allows configuration of the network interface 
        used for capturing packets. It ensures that a valid (non-empty) 
        interface value is provided.

        Args:
            value (str): The name of the network interface to be set.

        Raises:
            ValueError: If the provided interface value is empty.
        """
        if not value:
            raise ValueError("Interface cannot be empty.")
        self._interface = value

    # Method-based configurations
    def set_filters(self, port=None, ip=None, protocols=None) -> None:
        """
        Configures filters for packet capture.

        This method allows configuring port, IP, and protocol filters
        that will be applied during the packet capture process. These
        filters determine which network packets will be captured based
        on the specified criteria.

        Args:
            port (int, optional): The port number to filter the packets. Default is None.
            ip (str, optional): The IP address to filter the packets. Default is None.
            protocols (list of str, optional): A list of protocols to filter. For example, ["tcp", "udp"].
                If not provided, the default value set in the `protocols` attribute will be used.

        Returns:
            None
        """
        self._port_filter = port
        self._ip_filter = ip
        if protocols:
            self.protocols = protocols

    def set_output_file(self, file_path) -> None:
        """
        Sets the file path for saving captured packets.

        This method allows configuring a file path where the captured packets 
        will be saved after the packet capture process is stopped. If no file 
        path is provided, captured packets will not be saved.

        Args:
            file_path (str): The path to the file where captured packets will
                             be stored. If None, packets will not be saved.

        Returns:
            None
        """
        self._output_file = file_path

    def _build_filter_string(self) -> str:
        """
        Constructs a filter string for use in packet capturing.

        This method constructs a filter string based on the current filter 
        settings such as protocols, port filter, and IP filter. The generated 
        string is compatible with packet capturing tools and determines which 
        packets will be captured during the process.

        Returns:
            str: A string that represents the constructed filter for the capture.
        """
        filters = []

        protocol_filter = " or ".join(self.protocols)
        filters.append(f"({protocol_filter})")

        if self._port_filter:
            filters.append(f"port {self._port_filter}")

        if self._ip_filter:
            filters.append(f"host {self._ip_filter}")

        return " and ".join(filters)

    def _process_packet(self, packet) -> None:
        """
        Processes a captured packet.

        This internal method is invoked whenever a packet is captured during
        the packet sniffing process. It increments the packet count and applies
        the user-defined packet callback (if any) for additional processing.

        Args:
            packet (scapy.packet.Packet): The packet object captured during sniffing.

        Returns:
            None
        """
        
        self._packet_count += 1
        if self.packet_callback:
            self.packet_callback(packet)

    def start_capture(self, duration=60, count=100) -> None:
        """
        Starts the packet capture process.

        This method begins the capture of network packets on the configured
        network interface. It applies any specified filters and processes
        each captured packet using an internal method or a user-defined
        callback. The capture runs for the specified duration or until the
        specified count of packets is reached, whichever comes first.

        Args:
            duration (int, optional): The capture duration in seconds. Default is 60 seconds.
            count (int, optional): The maximum number of packets to capture. Default is 100 packets.

        Raises:
            ValueError: If the packet capture is already running or if the
                        network interface is not configured.
            Exception: If an error occurs during the packet capture initialization.

        Returns:
            None
        """
        if self._is_running:
            raise ValueError("Packet capture is already running")

        if not self._interface:
            raise ValueError("Network interface must be configured before starting capture")

        try:
            filters = self._build_filter_string()

            self._sniffer = AsyncSniffer(iface=self._interface,
                                         filter=filters,
                                         prn=self._process_packet,
                                         count=count,
                                         timeout=duration,
                                         store=bool(self._output_file))
            self._sniffer.start()
            self._is_running = True

        except Exception as e:
            self._is_running = False
            self._sniffer = None
            raise e

    def stop_capture(self) -> None:
        """
        Stops the packet capture process.

        This method halts the ongoing packet capturing process if it is currently
        active. It ensures that captured packets are finalized and saved to the
        configured output file (if any). After stopping the capture, the state
        of the capture process is updated to reflect that it is no longer running.

        Returns:
            None
        """
        if not self._is_running or not self._sniffer:
            return None

        self._sniffer.stop()

        if self._output_file:
            wrpcap(self._output_file, self._sniffer.results, append=True)

        self._is_running = False
