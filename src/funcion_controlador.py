"""Breve descripción de la fuente.
"""

from services.login_services import Loginmanager
from services.db_services import dbconnection


class Controlador:
    """Breve descripción de la clase."""

    def saludo_inicial(self):
        """Breve descripción del metodo."""
        print("Bienvenido a mi primer programa de Python.")

        # Crear la ventana principal y pasarla a la clase Loginmanager

    root = tk.Tk()
    app = LoginManager(root)
    root.mainloop()


# End-of-file (EOF)
