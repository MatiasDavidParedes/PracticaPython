"""Breve descripción de la fuente.
"""

import tkinter as tk
from services.login_services import LoginManager

# Crear la ventana principal y pasarla a la clase LoginManager
root = tk.Tk()
Login_Manager = LoginManager(root)
root.mainloop()

# Después de cerrar la ventana principal de Tkinter, puedes verificar el estado del login así:
if Login_Manager.login_successful:
    print(
        "El usuario ha iniciado sesión correctamente."
    )  # Nos vamos al siguiente paso de la aplicacion
else:
    print(
        "Inicio de sesión fallido o ventana cerrada sin iniciar sesión."
    )  # Mostramos error.
