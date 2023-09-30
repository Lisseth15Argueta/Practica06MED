class CuentaUsuario:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Se depositaron {cantidad} unidades en la cuenta de {self.nombre}."

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Se retiraron {cantidad} unidades de la cuenta de {self.nombre}."
        else:
            return f"No hay suficiente saldo en la cuenta de {self.nombre}."

# Ejemplo de uso
cuenta1 = CuentaUsuario("Juan", 1000)
print()
print(cuenta1.depositar(500))
print()
print(cuenta1.retirar(2000))
print()
print(cuenta1.retirar(500))
