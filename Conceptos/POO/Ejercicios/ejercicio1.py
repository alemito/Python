"""
Crear la clase estudiante, que tenga los atributos nombre, edad y grado.
Agregar metodo estudiar, que imprima el mensaje "el estudiante (nombre del estudiante) está estudiando"
Se debe interactuar con el usuario y que este brinde los atributos.
Al escribir "estudiar" se debe invocar al metodo estudiar creado en el punto 2 (no case sensitive)
"""

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")


# test = Estudiante("Carlos", 39, 3)
# print(test.grado)
# test.estudiar()

nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

alumno = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ALUMNO: \n\n
      Nombre: {alumno.nombre} \n
      Edad: {alumno.edad} \n
      Grado: {alumno.grado} \n
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        alumno.estudiar()

