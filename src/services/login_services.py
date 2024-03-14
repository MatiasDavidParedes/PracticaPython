import tkinter as tk
from tkinter import messagebox


class LoginManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de sesión")

        # Establece el tamaño y la posición de la ventana
        self.master.geometry("400x300")  # Ajusta a tus necesidades

        # Configurar colores y estilo
        self.master.configure(bg="#f0f0f0")  # Color de fondo

        # Crear el frame contenedor
        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Campo de texto para el usuario
        self.user_label = tk.Label(self.frame, text="Usuario:", bg="#f0f0f0")
        self.user_label.grid(row=0, column=0, pady=(0, 5))
        self.user_entry = tk.Entry(self.frame)
        self.user_entry.grid(row=0, column=1, pady=(0, 5))

        # Campo de texto para la contraseña
        self.password_label = tk.Label(self.frame, text="Contraseña:", bg="#f0f0f0")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # Botón para enviar
        self.submit_button = tk.Button(
            self.frame, text="Iniciar sesión", command=self.validate_login
        )
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=(5, 0))

        # Enlaces para recordar contraseña y olvidó contraseña
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

        # Atributo para almacenar el estado del inicio de sesión
        self.login_successful = None

    def validate_login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        if user == "David" and password == "Setia":
            self.login_successful = True
            messagebox.showinfo("Login exitoso", "Bienvenido David")
        else:
            self.login_successful = False
            messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

        # Aquí puedes cerrar la ventana o realizar otra acción
        # self.master.destroy()  # Descomentar si deseas cerrar la ventana automáticamente


# Crear la ventana principal y pasarla a la clase LoginManager
root = tk.Tk()
app = LoginManager(root)
root.mainloop()

# Después de cerrar la ventana principal de Tkinter, puedes verificar el estado del login así:
if app.login_successful:
    print("El usuario ha iniciado sesión correctamente.")
else:
    print("Inicio de sesión fallido o ventana cerrada sin iniciar sesión.")
