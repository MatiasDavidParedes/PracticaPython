"""Clase ejemplo para encriptar una contraseña y luego validar que sea valida, metodo werkzeug.security
"""

from passlib.context import CryptContext

Contexto=CryptContext(
    schemes={"pb"}
)