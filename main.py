"""Breve descripción de la fuente.
"""
from Tools.login_manager import Loginmanager

class Main():
    """Breve descripción de la clase.
    """
    def saludo_inicial(self):
        """Breve descripción del metodo.
        """
        print("Bienvenido a mi primer programa de Python.")


startprogram = Main()
startprogram.saludo_inicial()

logeousuario = Loginmanager()
logeousuario.logeo_usuario()
# End-of-file (EOF)
