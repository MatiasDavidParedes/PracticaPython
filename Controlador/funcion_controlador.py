"""Breve descripción de la fuente.
"""
from ..Tools.db_Connector import dbconnection
from ..Tools.login_manager import Loginmanager

class Controlador():
    """Breve descripción de la clase.
    """
    def saludo_inicial(self):
        """Breve descripción del metodo.
        """
        print("Bienvenido a mi primer programa de Python.")

        logeousuario = Loginmanager()
        logeousuario.logeo_usuario()


        InstanciaBaseDeDatos = dbconnection()
        InstanciaBaseDeDatos.connection_dba()

        InstanciaBaseDeDatos.SentenciaSQL='select * from pruebas.users'

        InstanciaBaseDeDatos.ejecute_SQL()

        print(InstanciaBaseDeDatos.RowSQL)

        InstanciaBaseDeDatos.close_connection()

# End-of-file (EOF)
