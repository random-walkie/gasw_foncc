import unittest
from src.http_analyzer.content import ContentHandler


class TestContentHandler(unittest.TestCase):
    def test_decode_content(self):
        response_content = ContentHandler.decode_content(b'{"key": "value"}', 'application/json')
        self.assertIsInstance(response_content, dict)
        self.assertEqual(response_content, {"key": "value"})

        response_content = ContentHandler.decode_content(b'\xc3\xa9', 'text/plain', 'utf-8')
        self.assertIsInstance(response_content, str)
        self.assertEqual(response_content, 'é')

    def test_encode_content(self):
        encoded_content, updated_content_type = ContentHandler.encode_content({"key": "value"}, 'application/json')
        self.assertIsInstance(encoded_content, bytes)
        self.assertEqual(encoded_content, b'{"key": "value"}')
        self.assertEqual(updated_content_type, 'application/json; charset=utf-8')

    def test_decode_form_data(self):
        response_content = ContentHandler.decode_form_data(b'key=value&key2=value2')
        self.assertIsInstance(response_content, dict)
        self.assertEqual(response_content, {'key': 'value', 'key2': 'value2'})


    # def test_handle_compression(self):
    #     decompressed_content = ContentHandler.handle_compression(
    #         b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\x0b\xf9\xcf\x0c\x02\x00\x00\x00\xff\xff\x01\x00\x00\xff\xff\x03\x00\xca\x57\xc8\xc1\x0c\x00\x00\x00',
    #         'gzip')
    #     self.assertIsInstance(decompressed_content, bytes)
    #     self.assertEqual(decompressed_content, b'Hello World!\n')


if __name__ == "__main__":
    unittest.main()
