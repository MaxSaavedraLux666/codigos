# pip install cryptography

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os


# Función para generar una clave derivada de una contraseña usando PBKDF2
def generate_key(password):
    """_summary_

    Args:
        password (_type_): _description_

    Returns:
        _type_: _description_
    """
    salt = os.urandom(16)  # Utilizamos un valor de sal aleatorio
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key


def encrypt(message, key):
    """

    Args:
        message (_type_): _description_
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    iv = os.urandom(16)  # Vector de inicialización único para cada mensaje
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv),
                    backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return base64.urlsafe_b64encode(iv + ciphertext)


def decrypt(ciphertext, key):
    """_summary_

    Args:
        ciphertext (_type_): _description_
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = base64.urlsafe_b64decode(ciphertext)
    iv = data[:16]  # Extraer el vector de inicialización
    ciphertext = data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv),
                    backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode()


# Ejemplo de uso
password = "contraseña_secreta"
message = "Hola, este es un mensaje secreto."

# Generar clave
key = generate_key(password)

# Cifrar mensaje
ciphertext = encrypt(message, key)
print("Mensaje cifrado:", ciphertext.decode())

# Descifrar mensaje
decrypted_message = decrypt(ciphertext, key)
print("Mensaje descifrado:", decrypted_message)
