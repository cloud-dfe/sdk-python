import json
import base64
import time
import hmac
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class Webhook:

    @staticmethod
    def is_valid(token: str, payload: str) -> bool:
        std = json.loads(payload)

        def convert_key(token: str) -> bytes:
            # Converte o token para uma chave de 16 bytes
            key = token[:16].ljust(16, '0')
            return key.encode('utf-8')

        def decrypt_time(ciphertext_raw: bytes, token: bytes, iv: bytes) -> float:
            # Decifra o tempo original
            cipher = AES.new(token, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext_raw)
            decrypted = unpad(decrypted, AES.block_size)
            return float(decrypted.decode('utf-8'))

        if not std:
            raise ValueError('Payload incorreto.')

        if 'signature' not in std:
            raise ValueError('Payload incorreto não contêm a assinatura.')

        if not token:
            raise ValueError('Token vazio.')

        key = convert_key(token)
        c = base64.b64decode(std['signature'])

        ivlen = 16
        iv = c[:ivlen]
        hmac_signature = c[ivlen:ivlen + 32]
        ciphertext_raw = c[48:]

        original_time = decrypt_time(ciphertext_raw, key, iv)

        calcmac = hmac.new(token.encode('utf-8'), ciphertext_raw, hashlib.sha256).digest()

        if hmac.compare_digest(hmac_signature, calcmac):
            current_time = int(time.time())
            dif = current_time - original_time

            if dif < 300:
                return True
            raise ValueError('Assinatura expirou.')

        raise ValueError('Token ou assinatura incorreta.')