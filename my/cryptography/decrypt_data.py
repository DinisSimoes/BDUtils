from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from Cryptography.aux_generate_key import GenerateKey

def DecryptData(encrypted_data: bytes, password: str, salt: bytes, iv: bytes) -> str:
    """
    Descriptografa dados criptografados usando AES.

    Args:
    encrypted_data (bytes): Os dados criptografados.
    password (str): A senha utilizada para gerar a chave de descriptografia.
    salt (bytes): O salt utilizado para gerar a chave.
    iv (bytes): O vetor de inicialização utilizado na criptografia.

    Returns:
    str: Os dados descriptografados.
    """
    key = GenerateKey(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data.decode()
