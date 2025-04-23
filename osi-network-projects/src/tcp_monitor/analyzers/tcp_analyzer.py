from struct import unpack
from struct import error as StructError
from logging import getLogger
logger = getLogger(__name__)

class TCPAnalyzer:
    """
    TCPAnalyzer is a utility class designed to process and analyze Transmission Control 
    Protocol (TCP) segments. It provides functionalities to inspect headers, payloads, 
    options, and control packet flags. The class is implemented with several static 
    methods to accommodate the non-instantaneous nature of TCP segment analysis.

    Attributes:
        tcp_header (bytes): The TCP header provided during its instantiation, defaults to None.
        tcp_payload (bytes): The TCP payload provided during its instantiation, defaults to None.

    Methods:
        analyze_segment(tcp_segment: bytes) -> dict:
            Analyzes an entire TCP segment, extracting and interpreting both the header 
            and payload information.

        analyze_header(tcp_segment: bytes) -> dict:
            Parses the TCP header, extracting fields such as source port, 
            destination port, sequence and acknowledgment numbers, flags, 
            and other metadata.

        analyze_payload(tcp_segment: bytes, header_length: int) -> dict:
            Extracts and interprets the payload of a TCP segment starting after the header.

        analyze_header_with_options(tcp_segment: bytes) -> dict:
            Parses TCP header options (if present) and returns their details.

        get_service_name(port: int) -> str:
            Maps a well-known port number to its corresponding service name.

        is_control_packet(tcp_info: dict) -> bool:
            Determines if a TCP segment contains control information using its flags.
    """
    def __init__(self, tcp_header: bytes = None, tcp_payload: bytes = None) -> None:
        """
        Initializes the TCPAnalyzer instance with optional TCP header and payload data.

        Args:
            tcp_header (bytes, optional): The TCP header data. Defaults to None.
            tcp_payload (bytes, optional): The TCP payload data. Defaults to None.

        Attributes:
            self.tcp_header (bytes): Stores the provided TCP header data.
            self.tcp_payload (bytes): Stores the provided TCP payload data.
        """
        self.tcp_header = tcp_header
        self.tcp_payload = tcp_payload

    @staticmethod
    def analyze_segment(tcp_segment: bytes) -> dict:
        """
        Analyzes a complete TCP segment, extracting the header length, parsing the header,
        and interpreting the payload data.

        The method first determines the length of the TCP header by extracting the header
        length information from the TCP segment. Based on the header length, it analyzes
        the header information, and if additional options are present, they are also processed.
        Finally, it extracts and decodes the payload of the TCP segment.

        Args:
            tcp_segment (bytes): A byte sequence representing the entire TCP segment.

        Returns:
            dict: A dictionary containing the parsed header information (including flags, 
                  ports, sequence and acknowledgment numbers, etc.), computed header length, 
                  and payload data with its size.

        Raises:
            ValueError: If the TCP header length is invalid (shorter than 20 bytes).
        """
        binary_header_length = '0'
        try:
            # Extract 13th byte at index 12; unpack into integer; shift bits 4 positions to the right
            binary_header_length = format(unpack('>B', tcp_segment[12:13])[0] >> 4, '04b')
        except StructError:
            logger.error("Error unpacking buffer, when analyzing TCP segment.")

        header_length = int(binary_header_length, 2) * 4

        if header_length < 20:
            raise ValueError("TCP header shorter than 20 bytes.")
        elif header_length > 20:
            tcp_results = TCPAnalyzer.analyze_header_with_options(tcp_segment)
        else:
            tcp_results = TCPAnalyzer.analyze_tcp_header(tcp_segment)

        tcp_results['header_length'] = header_length
        tcp_results.update(TCPAnalyzer.analyze_tcp_payload(tcp_segment, header_length=header_length))

        return tcp_results

    @staticmethod
    def analyze_tcp_header(tcp_segment: bytes) -> dict:
        """
        Parses the TCP header of a given segment and extracts essential information.

        The method extracts fields such as source port, destination port, 
        sequence and acknowledgment numbers, flags (controls bits), window 
        size, checksum, and the urgent pointer from the header.

        Args:
            tcp_segment (bytes): A byte sequence representing the TCP segment.

        Returns:
            dict: A dictionary containing the parsed TCP header information, including:
                  - `src_port` (int): Source port number.
                  - `dst_port` (int): Destination port number.
                  - `seq_num` (int): Sequence number.
                  - `ack_num` (int): Acknowledgment number.
                  - `flags` (dict): Control flags ('urg', 'ack', 'psh', 'rst', 'syn', 'fin') with boolean values.
                  - `window_size` (int): Size of the TCP window.
                  - `checksum` (int): TCP checksum value.
                  - `urgent_ptr` (int): Urgent pointer value.
        """
        src_prt = unpack('>H', tcp_segment[:2])[0]
        dst_prt = unpack('>H', tcp_segment[2:4])[0]
        seq_num = unpack('>I', tcp_segment[4:8])[0]
        ack_num = unpack('>I', tcp_segment[8:12])[0]
        window_size = unpack('>H', tcp_segment[14:16])[0]
        checksum = unpack('>H', tcp_segment[16:18])[0]
        urgent_ptr = unpack('>H', tcp_segment[18:20])[0]

        # Extract control bits from lowest 6 bits of second byte
        binary_flags = format(unpack('>B', tcp_segment[13:14])[0], '06b')

        flags = {
            'urg': False,
            'ack': False,
            'psh': False,
            'rst': False,
            'syn': False,
            'fin': False
        }

        if binary_flags[0] == '1':
            flags['urg'] = True
        if binary_flags[1] == '1':
            flags['ack'] = True
        if binary_flags[2] == '1':
            flags['psh'] = True
        if binary_flags[3] == '1':
            flags['rst'] = True
        if binary_flags[4] == '1':
            flags['syn'] = True
        if binary_flags[5] == '1':
            flags['fin'] = True

        return {
            'src_port': src_prt,
            'dst_port': dst_prt,
            'seq_num': seq_num,
            'ack_num': ack_num,
            'flags': flags,
            'window_size': window_size,
            'checksum': checksum,
            'urgent_ptr': urgent_ptr
        }
    
    @staticmethod
    def analyze_tcp_payload(tcp_segment: bytes, header_length: int) -> dict:
        """
        Extracts and processes the payload data from a given TCP segment.

        This method slices the TCP segment using the provided header length to isolate
        the payload. It then calculates the size of the payload in bytes and packages 
        the relevant information into a dictionary.

        Args:
            tcp_segment (bytes): A byte sequence representing the TCP segment.
            header_length (int): The length of the TCP header in bytes.

        Returns:
            dict: A dictionary containing:
                  - `payload` (bytes): The extracted payload data.
                  - `payload_size` (int): The size of the payload in bytes.
        """
        payload = tcp_segment[header_length:]
        payload_size = len(payload)

        return {
            'payload': payload,
            'payload_size': payload_size
        }

    @staticmethod
    def analyze_header_with_options(tcp_segment: bytes) -> dict:
        """
        Parses the TCP header with options of a given segment.

        This method extracts and interprets TCP options found in the header beyond the standard 
        20-byte length. It identifies the option type, translates it to its corresponding code,
        and retrieves the associated value.

        Args:
            tcp_segment (bytes): A byte sequence representing the TCP segment.

        Returns:
            dict: A dictionary containing:
                  - `options` (str): A string representation of the TCP option in the format 
                    `<option_code>=<option_value>`. Common option codes include:
                    - `EOO` (End of Option List)
                    - `NOP` (No Operation)
                    - `MSS` (Maximum Segment Size)
                    - `WSCALE` (Window Scale)
                    - `SACKOK` (Selective Acknowledgment Permitted)
                    - `SACK` (Selective Acknowledgment)
                    If the option is unrecognized, the code will be `UNKNOWN`.
        """
        option_number = unpack('>B', tcp_segment[20:21])[0]
        option_value = unpack('>H', tcp_segment[22:24])[0]
        option_code = 'UNKNOWN'

        if option_number == 0:
            option_code = 'EOO'
        if option_number == 1:
            option_code = 'NOP'
        if option_number == 2:
            option_code = 'MSS'
        if option_number == 3:
            option_code = 'WSCALE'
        if option_number == 4:
            option_code = 'SACKOK'
        if option_number == 5:
            option_code = 'SACK'

        return {
            'options': f"{option_code}={option_value}"
        }

    @staticmethod
    def get_service_name(port: int) -> str:
        """
        Maps a given port number to its corresponding service name.

        This method takes a port number as an argument and returns a string
        representing the associated service name. If the port number is not
        recognized, it returns a generic string format `PORT-<port_number>`.

        Commonly mapped port numbers include:
        - 80: HTTP
        - 21: FTP
        - 22: SSH
        - 23: Telnet
        - 25: SMTP
        - 53: DNS
        - 443: HTTPS
        - 3306: MySQL
        - 3389: RDP
        - 5985 and 5986: WSMan

        Args:
            port (int): The port number to map to a service name.

        Returns:
            str: The service name associated with the port, or `PORT-<port_number>` if not recognized.
        """
        if port == 80:
            return 'HTTP'
        elif port == 21:
            return 'FTP'
        elif port == 22:
            return 'SSH'
        elif port == 23:
            return 'Telnet'
        elif port == 25:
            return 'SMTP'
        elif port == 53:
            return 'DNS'
        elif port == 443:
            return 'HTTPS'
        elif port == 3306:
            return 'MySQL'
        elif port == 3389:
            return 'RDP'
        elif port == 5985:
            return 'WSMan'
        elif port == 5986:
            return 'WSMan'
        else:
            return f'PORT-{port}'

    @staticmethod
    def is_control_packet(tcp_info: dict) -> bool:
        """
        Determines if the provided TCP information corresponds to a control packet.

        This method checks the flags in the TCP header to determine whether the packet is 
        a control packet. Control packets are identified by the presence of any of the 
        following flags: SYN, FIN, RST, URG, ACK, or PSH.

        Args:
            tcp_info (dict): A dictionary containing parsed TCP header information. It is 
            expected to have a `flags` key that maps to another dictionary with specific 
            control flags as keys and their boolean states as values.

        Returns:
            bool: `True` if the packet is a control packet, `False` otherwise.
        """
        if tcp_info['flags']['syn'] or tcp_info['flags']['fin'] or tcp_info['flags']['rst'] \
                or tcp_info['flags']['urg'] or tcp_info['flags']['ack'] or tcp_info['flags']['psh']:
            return True
        else:
            return False





