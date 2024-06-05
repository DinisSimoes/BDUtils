from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def GenerateKey(password: str, salt: bytes) -> bytes:
    """
    Gera uma chave de criptografia a partir de uma senha e um salt.

    Args:
    password (str): A senha utilizada para gerar a chave.
    salt (bytes): O salt utilizado para gerar a chave.

    Returns:
    bytes: A chave de criptografia.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key