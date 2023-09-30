class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            return f"Se vendieron {cantidad_vendida} {self.nombre}(s)."
        else:
            return f"No hay suficiente stock de {self.nombre}."

    def agregar_stock(self, cantidad_agregada):
        self.cantidad += cantidad_agregada
        return f"Se agregaron {cantidad_agregada} {self.nombre}(s) al stock."

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        return f"El precio de {self.nombre} ha sido cambiado a {nuevo_precio}."

# Ejemplo de uso
articulo1 = Articulo("Camiseta", 10, 20)
print()
print(articulo1.vender(5))
print()
print(articulo1.agregar_stock(3))
print()
print(articulo1.cambiar_precio(25))
print()
print(articulo1.vender(8))
