"""Breve descripción de la fuente.
"""

class Loginmanager():
    """Breve descripción de la clase.
    """

    def __init__(self):

         self.login = False
         self.usuario = ""
         self.password = ""

    def logeo_usuario(self):
        """Breve descripción del metodo.
        """
        self.usuario = input("Ingrese usuario: ")
        self.password = input("Ingrese pasword: ")
# End-of-file (EOF)
