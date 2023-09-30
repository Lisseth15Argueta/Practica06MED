class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

# Ejemplo de uso
estudiante1 = Estudiante("Juan", "Perez", "20210001", "Ingeniería Informática")
print(estudiante1.nombre, estudiante1.apellido, estudiante1.carnet, estudiante1.carrera)

estudiante1.actualizar_nombre("Pedro")
estudiante1.actualizar_carrera("Ingeniería Industrial")
print(estudiante1.nombre, estudiante1.apellido, estudiante1.carnet, estudiante1.carrera)
