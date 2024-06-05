from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
from Cryptography.aux_generate_key import GenerateKey

def EncryptData(data: str, password: str) -> tuple:
    """
    Criptografa dados usando AES.

    Args:
    data (str): Os dados a serem criptografados.
    password (str): A senha utilizada para gerar a chave de criptografia.

    Returns:
    tuple: Um tupla contendo os dados criptografados, o salt e o IV.
    """
    salt = os.urandom(16)
    key = GenerateKey(password, salt)
    iv = os.urandom(16)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data, salt, iv