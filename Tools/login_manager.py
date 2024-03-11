"""Breve descripción de la clase.
"""

class Loginmanager():
    """Breve descripción de la clase.
    """

    def __init__(self):

         self.__login = False
         self.__usuario = ""
         self.__password = ""

    def logeo_usuario(self):
        """Breve descripción de la clase.
        """
        self.__usuario = input("Ingrese usuario: ")
        self.__password = input("Ingrese pasword: ")
