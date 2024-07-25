# Imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

mapping = {
    '''You Map Items Here'''
}

def generate_key():
    return os.urandom(32)

def aes_encrypt(plaintext, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    padded_plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

def encode(cadena, key):
    encrypted_cadena = aes_encrypt(cadena, key)
    xor_cadena = encrypted_cadena.hex()
    nueva_cadena = ""
    for caracter in xor_cadena:
        if caracter in mapping:
            nueva_cadena += mapping[caracter]
        else:
            nueva_cadena += caracter
    return nueva_cadena

def decode(cadena, key):
    map_inv = {v: k for k, v in mapping.items()}
    xor_cadena = ""
    for caracter in cadena:
        if caracter in map_inv:
            xor_cadena += map_inv[caracter]
        else:
            xor_cadena += caracter
    encrypted_cadena = bytes.fromhex(xor_cadena)
    decrypted_cadena = aes_decrypt(encrypted_cadena, key)
    return decrypted_cadena