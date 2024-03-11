class Login():
    login = False
    usuario = " "
    password = " " 
    
    def solicitarusuario(self):
        self.usuario = input("Ingrese usuario: ")
        self.password = input("Ingrese pasword: ")
    
procesologin = Login()

procesologin.solicitarusuario()