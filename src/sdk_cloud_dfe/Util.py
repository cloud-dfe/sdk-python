import base64
import zlib

class Util:
    
    @staticmethod
    def encode(data):
        
        encoded_bytes = base64.b64encode(data.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    
    @staticmethod
    def decode(data):

        decoded_bytes = base64.b64decode(data.encode('utf-8'))
        try:

            decompressed = zlib.decompress(decoded_bytes, 16+zlib.MAX_WBITS)
            return decompressed.decode('utf-8')
        except zlib.error:

            return decoded_bytes.decode('utf-8')
    
    @staticmethod
    def readFile(file):

        with open(file, 'r', encoding='utf-8') as f:
            return f.read()

