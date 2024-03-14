"""Breve descripción de la fuente.
"""

import psycopg2
from decouple import config


class dbconnection:
    """Breve descripción de la clase."""

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.SentenciaSQL = " "
        self.RowSQL = " "

    def connection_dba(self):
        """Breve descripción del metodo."""

        try:
            self.connection = psycopg2.connect(
                host=config("DBA_HOST"),
                user=config("DBA_USER"),
                password=config("DBA_PASSWORD"),
                database=config("DBA_ESQUEMA"),
            )
            print(
                "Coneccion exitosa a la base de datos {0}.{1} con el usuario {2}".format(
                    config("DBA_HOST"), config("DBA_ESQUEMA"), config("DBA_USER")
                )
            )
        except Exception as ex:
            print("Error de coneccion a la base de datos.")

    def ejecute_SQL(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.SentenciaSQL)
        self.RowSQL = self.cursor.fetchall()

    def close_connection(self):
        """Breve descripción del metodo."""
        self.connection.close()
        print("Seccion de base de datos finalizada")


# End-of-file (EOF)
