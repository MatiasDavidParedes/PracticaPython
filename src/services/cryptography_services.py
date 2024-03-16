"""Breve descripción de la fuente.
"""

from cryptography.fernet import Fernet
from decouple import config


class cryptography_manager:
    """Breve descripción de la clase."""

    def __init__(self):
        self.Key = ""
        self.clave_encriptada = ""

    def encriptar_password(self, Password):
        """Breve descripción del metodo."""
        pass
        self.Key = Fernet(config("SECRET_PASSWORD_KEY") + "==")
        self.clave_encriptada = self.Key.encrypt(str.encode(Password))
        print(self.clave_encriptada)


# End-of-file (EOF)
