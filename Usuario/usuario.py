"""Este módulo contiene la definición de la clase Usuario"""

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0
    def hacer_deposito(self, cantidad):
        self.balance += cantidad
    def hacer_retiro(self, cantidad):
        self.balance -= cantidad
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")
    def transferir_dinero(self, otro_usuario, cantidad):
        self.hacer_retiro(cantidad)
        otro_usuario.hacer_deposito(cantidad)

usuario1 = Usuario("Guido van Rossum")
usuario2 = Usuario("Linus Torvalds")
usuario3 = Usuario("Richard Stallman")

usuario1.hacer_deposito(100)
usuario1.hacer_deposito(50)
usuario1.hacer_deposito(30)
usuario1.hacer_retiro(20)
usuario1.mostrar_balance_usuario()

usuario2.hacer_deposito(200)
usuario2.hacer_deposito(50)
usuario2.hacer_retiro(70)
usuario2.hacer_retiro(25)
usuario2.mostrar_balance_usuario()

usuario3.hacer_deposito(300)
usuario3.hacer_retiro(50)
usuario3.hacer_retiro(80)
usuario3.hacer_retiro(30)
usuario3.mostrar_balance_usuario()

#Bonus
usuario1.transferir_dinero(usuario3, 50)

usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()
