"""
Funcion como la venia utilizando hasta ahora, sin respetar si era privado o no
"""
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad


persona1 = Persona("Ale",55)
print(persona1._nombre) # Funciona, pero no estoy respetando la cualidad de privado que le quisieron dar al atributo.


"""
Genero un metodo especifico de get, para retornar el atributo nombre del objeto creado.
funciona para privados y muy privados
"""

class Persona2:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self.__edad

persona2 = Persona2("Mito",20)
print(persona2.get_nombre())
print(persona2.get_edad())

"""
Genero un metodo especifico de set, para retornar el atributo nombre del objeto creado y modificado.
funciona para privados y muy privados
"""

class Persona3:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self.__edad

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

persona3 = Persona3("Sis",45)
print(persona3.get_nombre()) # Imprime Sis
print(persona3.get_edad()) # Imprime 45

persona3.set_nombre("Alemitosis") # Sobreescribo el atributo _nombre del objeto persona3
persona3.set_edad(37) # Sobreescribo el atributo __edad del objeto persona3

print(persona3.get_nombre()) # Imprime Alemitosis
print(persona3.get_edad()) # Imprime 37