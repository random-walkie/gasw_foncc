from struct import unpack
from struct import error as StructError
from logging import getLogger
logger = getLogger(__name__)

class TCPAnalyzer:
    
    def __init__(self, tcp_header: bytes = None, tcp_payload: bytes = None):
        self.tcp_header = tcp_header
        self.tcp_payload = tcp_payload

    @staticmethod
    def analyze_segment(tcp_segment: bytes) -> dict:
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
            tcp_results = TCPAnalyzer.analyze_header(tcp_segment)

        tcp_results['header_length'] = header_length
        tcp_results.update(TCPAnalyzer.analyze_payload(tcp_segment, header_length=header_length))

        return tcp_results

    @staticmethod
    def analyze_header(tcp_segment: bytes) -> dict:
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
    def analyze_payload(tcp_segment: bytes, header_length: int) -> dict:
        payload = tcp_segment[header_length:]
        payload_size = len(payload)

        return {
            'payload': payload,
            'payload_size': payload_size
        }

    @staticmethod
    def analyze_header_with_options(tcp_segment: bytes) -> dict:
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
        if tcp_info['flags']['syn'] or tcp_info['flags']['fin'] or tcp_info['flags']['rst'] \
                or tcp_info['flags']['urg'] or tcp_info['flags']['ack'] or tcp_info['flags']['psh']:
            return True
        else:
            return False





