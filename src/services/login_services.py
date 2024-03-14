"""Breve descripción de la fuente.
"""

import tkinter as tk
from tkinter import messagebox


class LoginManager:
    """Breve descripción de la clase."""

    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de sesión")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f0f0")

        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.user_label = tk.Label(self.frame, text="Usuario:", bg="#f0f0f0")
        self.user_label.grid(row=0, column=0, pady=(0, 5))
        self.user_entry = tk.Entry(self.frame)
        self.user_entry.grid(row=0, column=1, pady=(0, 5))

        self.password_label = tk.Label(self.frame, text="Contraseña:", bg="#f0f0f0")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # Botón para iniciar sesión
        self.submit_button = tk.Button(
            self.frame, text="Iniciar sesión", command=self.validate_login
        )
        self.submit_button.grid(row=2, column=0, pady=(5, 0))

        # Botón de registro, colocado al lado del botón de inicio de sesión
        self.register_button = tk.Button(
            self.frame, text="Registrarse", command=self.register_user
        )
        self.register_button.grid(row=2, column=1, pady=(5, 0))

        self.remember_me_check = tk.Checkbutton(
            self.frame, text="Recordarme", bg="#f0f0f0"
        )
        self.remember_me_check.grid(row=3, column=0, columnspan=2, pady=(5, 0))

        self.forgot_password_link = tk.Label(
            self.frame,
            text="¿Olvidaste la contraseña?",
            bg="#f0f0f0",
            fg="blue",
            cursor="hand2",
        )
        self.forgot_password_link.grid(row=4, column=0, columnspan=2)

        self.login_successful = None

    def validate_login(self):
        """Breve descripción de la clase."""
        user = self.user_entry.get()
        password = self.password_entry.get()
        if user == "David" and password == "Setia":
            self.login_successful = True
            messagebox.showinfo("Login exitoso", "Bienvenido David")
        else:
            self.login_successful = False
            messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

    def register_user(self):
        """Breve descripción de la clase."""
        # Aquí podrías implementar la lógica para registrar a un nuevo usuario
        messagebox.showinfo(
            "Registro", "La funcionalidad de registro aún no está implementada."
        )
