"""Breve descripción de la fuente.
"""

import tkinter as tk
from tkinter import messagebox


class RegisterManager:
    """Clase para gestionar el registro de usuarios."""

    def __init__(self, master):
        self.master = master
        self.master.title("Registro de usuario")
        self.master.geometry("400x500")  # Ajuste el tamaño para acomodar más campos
        self.master.configure(bg="#f0f0f0")

        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.place(
            relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8
        )

        # Definir los widgets para cada campo de datos del usuario
        self.entries = {}
        self.labels = {
            "Usuario": "Usuario:",
            "Password": "Contraseña:",
            "Nombre": "Nombre:",
            "Apellido": "Apellido:",
            "Edad": "Edad:",
            "Fecha de nacimiento": "Fecha de nacimiento:",
            "Dirección 1": "Dirección 1:",
            "Dirección 2": "Dirección 2:",
            "Localidad": "Localidad:",
            "Provincia": "Provincia:",
            "Pais": "País:",
        }

        row = 0
        for field, label in self.labels.items():
            tk.Label(self.frame, text=label, bg="#f0f0f0").grid(
                row=row, column=0, pady=2, sticky="w"
            )
            entry = tk.Entry(self.frame)
            entry.grid(row=row, column=1, pady=2)
            self.entries[field] = entry
            row += 1

        # Botón para enviar el formulario de registro
        self.submit_button = tk.Button(
            self.frame, text="Registrarse", command=self.register_user
        )
        self.submit_button.grid(row=row, column=0, columnspan=2, pady=10)

    def register_user(self):
        """Recolectar los datos del formulario y realizar el registro."""
        # Verificar que ninguno de los campos esté vacío
        if any(entry.get().strip() == "" for entry in self.entries.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return  # Detiene la función si algún campo está vacío

        # Aquí iría la lógica para recoger los datos y registrar al usuario.
        user_data = {field: entry.get() for field, entry in self.entries.items()}
        messagebox.showinfo(
            "Registro", "Usuario registrado exitosamente. \n" + str(user_data)
        )
        self.master.destroy()


# End-of-file (EOF)
