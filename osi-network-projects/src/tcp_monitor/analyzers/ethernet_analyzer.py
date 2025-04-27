class EthernetAnalyzer:
    """
    The EthernetAnalyzer class provides static methods for analyzing Ethernet frames.
    It includes functionality to:

    - Analyze an Ethernet frame and extract its header and payload details.
    - Determine properties like broadcast, multicast, or VLAN tagging.
    - Decode the Ethertype and map it to its corresponding protocol name.
    - Format MAC addresses into a human-readable form.

    Methods:
        analyze_frame(frame: bytes) -> dict:
            Analyzes a complete Ethernet frame, returning information about both the header and payload.

        analyze_ethernet_header(frame: bytes) -> dict:
            Extracts and analyzes the Ethernet frame header, identifying MAC addresses,
            Ethertype, and VLAN tagging details.

        analyze_ethernet_payload(frame: bytes) -> dict:
            Analyzes the Ethernet frame payload and provides its size and raw content.

        format_mac_address(mac: bytes) -> str:
            Formats a MAC address from raw bytes into a human-readable string with colon separators.

        get_ethertype_name(ethertype: int) -> str:
            Maps an Ethertype value to its corresponding protocol name (e.g., IPv4, IPv6, etc.).
    """
    def __init__(self) -> None:
        """
        Initializes an instance of the EthernetAnalyzer class.
        
        Since this class contains only static methods, this initializer
        does not perform any specific setup or hold any instance-specific
        data. It exists for potential extension or instantiation needs.
        """
        pass

    @staticmethod
    def analyze_frame(frame: bytes) -> dict:
        """
        Analyzes a complete Ethernet frame, extracting and combining information 
        about the Ethernet header and payload.

        This method performs the following tasks:
        - Validates the length of the given Ethernet frame.
        - Extracts and processes header details such as MAC addresses, Ethertype, 
          broadcast/multicast status, and VLAN tagging if present.
        - Extracts and analyzes the payload content and its size.

        Args:
            frame (bytes): A byte sequence representing the raw Ethernet frame 
            to be analyzed.

        Returns:
            dict: A dictionary containing combined details from both the Ethernet 
            header and payload analysis. Also includes an error key if the frame 
            is too short to be valid.
        """
        # Check if the frame is too short
        if len(frame) < 14:
            return {'error': 'Frame too short to be a valid Ethernet frame'}

        # Get both header and payload information
        header_info = EthernetAnalyzer.analyze_ethernet_header(frame)
        payload_info = EthernetAnalyzer.analyze_ethernet_payload(frame)

        return {**header_info, **payload_info}

    @staticmethod
    def analyze_ethernet_header(frame: bytes) -> dict:
        """
        Analyzes the Ethernet header of a given Ethernet frame.

        The method decodes details about the destination and source MAC addresses,
        identifies whether they indicate a broadcast or multicast frame, and checks
        for VLAN tagging. It also determines the Ethertype, maps it to its respective
        protocol name, and handles cases specific to VLAN-tagged frames by extracting
        VLAN tag details and the inner Ethertype.

        Args:
            frame (bytes): A byte sequence containing the Ethernet frame.

        Returns:
            dict: A dictionary with the following keys:
                - dst_mac (str): The destination MAC address.
                - is_broadcast (bool): Whether the frame is a broadcast frame.
                - is_multicast (bool): Whether the frame is a multicast frame.
                - src_mac (str): The source MAC address.
                - ethertype (int): The Ethertype in the Ethernet header.
                - ethertype_name (str): The protocol name corresponding to the Ethertype.
                - is_vlan_tagged (bool): Indicates if VLAN tagging is present.
                - vlan_id (int or None): The VLAN ID, if tagging is present.
                - inner_ethertype (int or None): Inner Ethertype for VLAN-tagged frames.
                - inner_ethertype_name (str): Protocol name for the inner Ethertype.
        """
        dst_mac = EthernetAnalyzer.format_mac_address(frame[0:6])
        is_broadcast = False
        is_multicast = False
        if dst_mac == 'ff:ff:ff:ff:ff:ff':
            is_broadcast = True
        # Multicast destination MAC (first byte has least significant bit set)
        elif dst_mac[0:2] == '01':
            is_multicast = True
        src_mac = EthernetAnalyzer.format_mac_address(frame[6:12])
        ethertype = (frame[12] << 8) + frame[13]
        ethertype_name = EthernetAnalyzer.get_ethertype_name(ethertype)

        is_vlan_tagged = False
        vlan_id = None
        inner_ethertype = None
        inner_ethertype_name = ''
        if ethertype ==  0x8100:
            is_vlan_tagged = True
            vlan_id = (frame[14] << 8) + frame[15]
            inner_ethertype = (frame[16] << 8) + frame[17]
            inner_ethertype_name = EthernetAnalyzer.get_ethertype_name(inner_ethertype)

        return {'dst_mac': dst_mac,
                'is_broadcast': is_broadcast,
                'is_multicast': is_multicast,
                'src_mac': src_mac,
                'ethertype': ethertype,
                'ethertype_name': ethertype_name,
                'is_vlan_tagged': is_vlan_tagged,
                'vlan_id': vlan_id,
                'inner_ethertype': inner_ethertype,
                'inner_ethertype_name': inner_ethertype_name}

    @staticmethod
    def analyze_ethernet_payload(frame: bytes) -> dict:
        """
        Analyzes the payload of an Ethernet frame.

        This method extracts the payload portion of the given Ethernet frame,
        calculating its size and returning the raw content as bytes.

        Args:
            frame (bytes): A byte sequence representing the Ethernet frame 
            to extract the payload from.

        Returns:
            dict: A dictionary containing:
                - payload (bytes): The raw payload data of the Ethernet frame.
                - payload_size (int): The size of the extracted payload in bytes.
        """
        payload = frame[14:]
        payload_size = len(payload)
        return {'payload': payload, 'payload_size': payload_size}

    @staticmethod
    def format_mac_address(mac: bytes) -> str:
        """
        Formats a MAC address into a human-readable string.

        This method takes a MAC address represented as raw bytes and converts
        it into a string format separated by colons (e.g., '00:1A:2B:3C:4D:5E').

        Args:
            mac (bytes): A 6-byte sequence representing the MAC address.

        Returns:
            str: A formatted MAC address string in colon-separated format.
        """
        return ':'.join(mac.hex()[i:i+2] for i in range(0,12,2))

    @staticmethod
    def get_ethertype_name(ethertype: int) -> str:
        """
        Maps an Ethertype value to its corresponding protocol name.

        This method takes an integer representing the Ethertype value from an Ethernet frame 
        and returns a human-readable string describing the corresponding protocol. It covers 
        common Ethertype values such as IPv4, IPv6, ARP, VLAN tagging, MPLS, and PPPoE protocols. 
        If the provided Ethertype does not match any known protocol, 'Unknown' is returned.

        Args:
            ethertype (int): An integer representing the Ethertype value.

        Returns:
            str: The name of the protocol corresponding to the Ethertype value, 
            or 'Unknown' if the Ethertype is not recognized.
        """
        if ethertype == 0x0800:
            return 'IPv4'
        elif ethertype == 0x86dd:
            return 'IPv6'
        elif ethertype == 0x0806:
            return 'ARP'
        elif ethertype == 0x8100:
            return '802.1Q'
        elif ethertype == 0x8847:
            return 'MPLS'
        elif ethertype == 0x8863:
            return 'PPPoE Discovery'
        elif ethertype == 0x8864:
            return 'PPPoE Session'
        else:
            return 'Unknown'
