"""
Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
Persona y Estudiante. La clase Persona tendrá los atributos de Nombre y Edad y un metodo que imprima el nombre y la edad de la persona.
La clase Estudiante heredará de la clase Persona y tambien tendrá un atributo adicional: Grado y un metodo que imprima el grado del estudiante.

Deberás utilizar super en el metodo de inicializacion (init) para reutilizar el codigo de la clase padre (Persona). Luego crea una instancia
de la clase Estudiante e imprime sus atributos y utiliza sus metodos para asegurarte de que todo funciona correctamente.

"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre.capitalize() # se pueden pasar metodos a la variable, por mas que no lo autocomplete
        self.edad = edad

    def mostrar_datos(self):
        print(f"{self.nombre} tiene {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Esta en {self.grado} grado")

alumno = Estudiante("ale",55,8)
alumno.mostrar_datos()
alumno.mostrar_grado()
