# utils.py
from .Caesaer_script import CaesarCipher

def get_cipher(string, key=None, encrypt=True):
    cipher = CaesarCipher(key)
    if encrypt:
        return cipher.encrypt_string(string)
    else:
        return cipher.decrypt_string(string)
