from ipaddress import IPv4Address, IPv6Address, ip_address

class IPAnalyzer:
    """
    A class to analyze and extract details from IP packets.

    The IPAnalyzer class provides static methods to analyze and parse
    both IPv4 and IPv6 packet headers, determine packet features, and
    interpret various details such as IP protocol version, header flags,
    source and destination IP addresses, and more.

    Attributes:
        ip_packet (bytes): The raw IP packet to be analyzed. Default is None.

    Methods:
        analyze_packet(ip_packet: bytes) -> dict:
            Analyzes the IP packet, identifies its version, and processes the appropriate header.
        
        analyze_ipv4_packet_header(ipv4_packet: bytes) -> dict:
            Extracts and interprets details from an IPv4 packet header.
        
        analyze_ipv6_packet_header(ipv6_packet: bytes) -> dict:
            Extracts and interprets details from an IPv6 packet header.
        
        analyze_packet_payload(ip_packet: bytes, ip_results: dict) -> dict:
            Extracts the payload from the given IP packet based on the version.

        protocol_name(protocol: int) -> str:
            Returns the name of the protocol based on the protocol number,
            e.g., ICMP, TCP, UDP, etc.
    """
    def __init__(self) -> None:
        """
        Initializes an instance of the IPAnalyzer class.

        Since this class contains only static methods, this initializer
        does not perform any specific setup or hold any instance-specific
        data. It exists for potential extension or instantiation needs.
        """

    @staticmethod
    def analyze_packet(ip_packet: bytes) -> dict:
        """
        Analyzes the provided IP packet and determines its IP version.

        This method examines the first byte of the provided IP packet to determine
        whether it is IPv4 or IPv6. It delegates the analysis of the packet to the
        appropriate method based on the version and processes the packet's payload.

        Args:
            ip_packet (bytes): Raw bytes of the IP packet to analyze.

        Returns:
            dict: A dictionary containing the parsed details of the IP packet, 
            including version, header details, payload information, and errors 
            if any occur during analysis.
        """
        # Extract 1st byte of packet header
        # Shift the value right by 4 bits, extracting the first 4 bits of the byte
        ip_results = {}
        if len(ip_packet) < 20:
            ip_results['error'] = "IP packet too short to contain a valid header."
            return ip_results
        else:
            version = ip_packet[0] >> 4
            if version == 4:
                ip_results = IPAnalyzer.analyze_ipv4_packet_header(ip_packet)
            elif version == 6:
                ip_results = IPAnalyzer.analyze_ipv6_packet_header(ip_packet)
            else:
                ip_results['error'] = f"Invalid IP version: {version}. Only IPv4 and IPv6 are supported."
                return ip_results

            ip_results['version'] = version
            return IPAnalyzer.analyze_packet_payload(ip_packet, ip_results)

    @staticmethod
    def analyze_ipv4_packet_header(ipv4_packet: bytes) -> dict:
        """
        Analyzes the header of an IPv4 packet and extracts detailed information.

        This method processes the fields of an IPv4 packet header, including 
        the version, header length, type of service, total length, flags, 
        fragment offset, time to live, protocol, checksum, source IP, destination IP, and options.

        It performs bitwise operations to decode specific fields such as flags 
        and fragment information. Additionally, it handles IP header options 
        by parsing them based on their type, length, and associated data.

        Args:
            ipv4_packet (bytes): A byte string representing the raw IPv4 packet.

        Returns:
            dict: A dictionary containing parsed details from the IPv4 header, 
            including:
                - ihl: Internet Header Length (int).
                - header_length: Total header length in bytes (int).
                - tos: Type of Service field (int).
                - total_length: Total length of the IP packet in bytes (int).
                - id: Packet identification field (int).
                - flags: A dictionary with 'df' (Don't Fragment) and 'mf' (More Fragments) flags (bool).
                - is_fragment: True if the packet is a fragment (bool).
                - fragment_offset: Offset of the fragment in the original data (int).
                - ttl: Time-to-Live value in hops (int).
                - protocol: Protocol number (int).
                - protocol_name: Human-readable name of the protocol (str).
                - checksum: Header checksum (int).
                - src_ip: Source IPv4 address (str).
                - dst_ip: Destination IPv4 address (str).
                - options: A list of parsed options containing type, length, and data.

        Raises:
            ValueError: If an unexpected value is found in the flag bits or if 
            the first bit of the flags segment is not zero.
        """
        # Here I am extracting the last 4 bits, by performing a bitwise AND operation with
        # 0x0F, which corresponds the binary number 0000 1111
        ihl = ipv4_packet[0] & 0x0F
        header_length = ihl * 4
        tos = ipv4_packet[1]
        total_length = ipv4_packet[2] + ipv4_packet[3]
        identification = ipv4_packet[4] + ipv4_packet[5] # not verified here

        # Extract the 3 most significant bits of byte 6:
        # Shift right by 5 and mask with 0x07 (binary 0000 0111)
        binary_flags = format((ipv4_packet[6] >> 5) & 0x07, '03b')
        flags = {
            'df': False,
            'mf': False
        }

        if binary_flags[0] != '0':
            raise ValueError("Bit 0 of Flags section should be 0.")

        if binary_flags[1] == '0':
            flags['df'] = False
        elif binary_flags[1] == '1':
            flags['df'] = True
        else:
            # Handle unexpected value
            raise ValueError("Invalid DF flag value.")

        if binary_flags[2] == '0':
            flags['mf'] = False
        elif binary_flags[2] == '1':
            flags['mf'] = True
        else:
            # Handle unexpected value
            raise ValueError("Invalid MF flag value.")

        is_fragment = flags['mf']
        # Get the last 3 bits of byte 6 and shift them left by 8 positions
        high_bits = ipv4_packet[6] & 0x1F << 8
        fragment_offset = ( high_bits + ipv4_packet[7] ) * 8
        time_to_live = ipv4_packet[8]
        protocol = ipv4_packet[9]
        protocol_name = IPAnalyzer.protocol_name(protocol)
        checksum = ipv4_packet[10] + ipv4_packet[11]
        src_ip = IPv4Address(ipv4_packet[12:16]).__str__()
        dst_ip = IPv4Address(ipv4_packet[16:20]).__str__()

        # Parsing Options
        offset = 20  # Start at the end of the standard header
        options = []

        while offset < header_length:
            option_type = ipv4_packet[offset]

            # Handle special single-byte options
            if option_type == 0:  # End of Option List
                break
            elif option_type == 1:  # No Operation
                options.append({'type': 1})
                offset += 1
                continue

            # Normal TLV options
            option_length = ipv4_packet[offset + 1]
            option_data = ipv4_packet[offset + 2:offset + option_length]

            options.append({
                'type': option_type,
                'length': option_length,
                'data': option_data
            })

            offset += option_length


        return {
            'ihl': ihl,
            'header_length': header_length,
            'tos': tos,
            'total_length': total_length,
            'id': identification,
            'flags': flags,
            'is_fragment': is_fragment,
            'fragment_offset': fragment_offset,
            'ttl': time_to_live,
            'protocol': protocol,
            'protocol_name': protocol_name,
            'checksum': checksum,
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'options': options,
        }

    @staticmethod
    def protocol_name(protocol: int) -> str:
        """
        Returns the human-readable name of a protocol based on its numeric identifier.

        Args:
            protocol (int): The numeric identifier of the protocol as defined in IP headers.

        Returns:
            str: The human-readable name of the protocol. Known values include:
                - 'ICMP' for protocol number 1
                - 'TCP' for protocol number 6
                - 'UDP' for protocol number 17
                - 'Reserved' for protocol number 255
                - 'Unknown' for any other value
        """
        if protocol == 1:
            return 'ICMP'
        elif protocol == 6:
            return 'TCP'
        elif protocol == 17:
            return 'UDP'
        elif protocol == 255:
            return 'Reserved'
        else:
            return 'Unknown'

    @staticmethod
    def analyze_ipv6_packet_header(ipv6_packet: bytes) -> dict:
        """
        Analyzes the header of an IPv6 packet and extracts its components.

        This method interprets the IPv6 header fields, including traffic class,
        flow label, payload length, next header, hop limit, source IP, 
        and destination IP addresses. It provides a dictionary with all the extracted details.

        Args:
            ipv6_packet (bytes): The raw bytes of the IPv6 packet header to be analyzed.

        Returns:
            dict: A dictionary containing the following keys:
                - 'traffic_class' (int): The 8-bit traffic class field.
                - 'flow_label' (int): The 20-bit flow label field.
                - 'payload_length' (int): The total length of the payload in bytes.
                - 'next_header' (int): The identifier for the next header's protocol type.
                - 'protocol_name' (str): The human-readable name of the next header's protocol.
                - 'hop_limit' (int): The hop limit for the packet.
                - 'src_ip' (str): The source IP address as a string.
                - 'dst_ip' (str): The destination IP address as a string.
        """
        # Traffic Class: 4 bits from byte 0 (shifted left) + 4 bits from byte 1
        traffic_class = ((ipv6_packet[0] & 0x0F) << 4) + ((ipv6_packet[1] & 0xF0) >> 4)
        # Flow Label: 4 bits from byte 1 + all 8 bits from byte 2 + all 8 bits from byte 3
        flow_label = ((ipv6_packet[1] & 0x0F) << 16) + (ipv6_packet[2] << 8) + ipv6_packet[3]
        payload_length = ipv6_packet[4] + ipv6_packet[5]
        next_header = ipv6_packet[6]
        protocol_name = IPAnalyzer.protocol_name(next_header)
        hop_limit = ipv6_packet[7]
        src_ip = IPv6Address(ipv6_packet[8:24]).__str__()
        dst_ip = IPv6Address(ipv6_packet[24:40]).__str__()

        return {
            'traffic_class': traffic_class,
            'flow_label': flow_label,
            'payload_length': payload_length,
            'next_header': next_header,
            'protocol_name': protocol_name,
            'hop_limit': hop_limit,
            'src_ip': src_ip,
            'dst_ip': dst_ip
        }

    @staticmethod
    def analyze_packet_payload(ip_packet: bytes, ip_results: dict) -> dict:
        """
        Extracts and analyzes the payload of an IP packet.

        Depending on the IP version (IPv4 or IPv6), this method locates 
        the payload, determines its size, and appends the payload details 
        to the provided IP header analysis results.

        Args:
            ip_packet (bytes): The full raw bytes of the IP packet.
            ip_results (dict): A dictionary containing the analysis of the 
                               IP header, including fields such as version 
                               and header length.

        Returns:
            dict: The updated `ip_results` dictionary, including these additional keys:
                - 'payload' (bytes): The raw payload data extracted from the IP packet.
                - 'payload_size' (int): The size of the extracted payload in bytes.
        """
        payload = b''
        payload_size = 0
        if ip_results['version'] == 4:
            payload = ip_packet[ip_results['header_length']:]
            payload_size = len(payload)

        if ip_results['version'] == 6:
            payload = ip_packet[40:] # IPv6 header is always 40-bytes
            payload_size = len(payload)

        ip_results.update({'payload': payload, 'payload_size': payload_size})
        return ip_results

    @staticmethod
    def get_ip_address_type(ip_addr: str) -> str:
        """
        Determines the type of a given IP address.

        This method categorizes an IP address as loopback, broadcast, private, 
        multicast, reserved, unspecified, link-local, or public based on its attributes.

        Args:
            ip_addr (str): The IP address to analyze as a string.

        Returns:
            str: A string representing the type of the IP address. Possible values are:
                - 'loopback': The address is a loopback address (e.g., 127.0.0.1 or ::1).
                - 'broadcast': The address is a broadcast address (e.g., 255.255.255.255).
                - 'private': The address belongs to a private network range.
                - 'multicast': The address is within a multicast range.
                - 'reserved': The address is a reserved IP address.
                - 'unspecified': The address is unspecified.
                - 'link-local': The address is a link-local address.
                - 'public': The address is a public IP address, i.e., not matching any of the above categories.
        """
        if ip_address(ip_addr).is_loopback:
            return 'loopback'
        elif '255.255.255.255' in ip_addr:
            return 'broadcast'
        elif ip_address(ip_addr).is_private:
            return 'private'
        elif ip_address(ip_addr).is_multicast:
            return 'multicast'
        elif ip_address(ip_addr).is_reserved:
            return 'reserved'
        elif ip_address(ip_addr).is_unspecified:
            return 'unspecified'
        elif ip_address(ip_addr).is_link_local:
            return 'link-local'
        else:
            return 'public'
