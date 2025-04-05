from json import loads
from json import dumps
class ContentHandler:
    """Handles the transformation, encoding, and formatting of HTTP content.

    This class demonstrates the Presentation Layer (Layer 6) functions by:
    - Converting between different data formats (JSON, XML, form data)
    - Handling character encoding and decoding
    - Processing compression/decompression
    - Interpreting content based on MIME types
    """

    @staticmethod
    def decode_content(content_bytes: bytes, content_type: dict, encoding=None):
        """Decode content bytes based on Content-Type header.

        Args:
            content_bytes: Raw bytes from HTTP response
            content_type: Value of Content-Type header (dict of list values)
            encoding: Character encoding override

        Returns:
            Decoded content in appropriate Python type (dict, str, bytes)
        """
        # Parse content_type to extract MIME type and parameters
        separate_content = content_type.split(";")
        mime = separate_content[0]
        # Extract charset from content_type if present and encoding not provided
        charset = separate_content[1].split("=")[1] if len(separate_content) > 1 and encoding is None else encoding
        # TODO: Handle decompression here
        # Delegate to appropriate decoder method based on MIME type
        if mime == "application/json":
            return loads(content_bytes)
        elif "text/" in mime or mime == "application/xml" or mime == "application/xhtml+xml":
            return content_bytes.decode(charset or "utf-8")
        else:
            return content_bytes

    @staticmethod
    def encode_content(data, mime) -> tuple:
        """Encode Python data into bytes for HTTP transmission.

        Args:
            data: Python object to encode (dict, str, etc.)
            mime: Target Content-Type for encoding

        Returns:
            Tuple of (bytes, updated_content_type)
        """
        #  Select encoder based on content_type
        updated_content_type = mime
        if mime == "application/json":
            encoded_content = dumps(data).encode("utf-8")
        else:
            encoded_content = data.encode("utf-8")
        # Set charset parameter in content_type if not present
        if "charset=" not in mime:
            updated_content_type = mime + "; charset=utf-8"
        # Return encoded bytes and possibly updated content_type
        return encoded_content, updated_content_type

    @staticmethod
    def decode_form_data(content_bytes, encoding='utf-8'):
        """Decode application/x-www-form-urlencoded content."""
        # Decode bytes to string
        decoded_content = content_bytes.decode(encoding)
        # Split string by & to separate key-value pairs
        pairs = decoded_content.split("&")
        # Split each pair by = to separate keys and values
        form_data = {}
        for pair in pairs:
            key, value = pair.split("=")
            form_data[key] = value
        # Return dictionary of form data
        return form_data

    # @staticmethod
    # def handle_compression(content_bytes, content_encoding):
    #     """Decompress content based on Content-Encoding header.
    #
    #     Args:
    #         content_bytes: Compressed content
    #         content_encoding: Value of Content-Encoding header
    #
    #     Returns:
    #         Decompressed content bytes
    #     """
    #     # TODO: Check for supported compression methods in content_encoding
    #     # TODO: Handle 'gzip' compression using gzip module
    #     # TODO: Handle 'deflate' compression using zlib module
    #     # TODO: Handle 'br' (Brotli) compression if available
    #     # TODO: Return decompressed bytes or original bytes if no compression
    #     pass