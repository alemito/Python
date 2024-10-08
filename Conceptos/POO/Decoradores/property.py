"""
Son Getter, Setter y Deletter
"""
# Forma clasica
class Persona_prueba:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self.__edad


persona1 = Persona_prueba("Ale",22)
print(persona1.get_edad()) # 22

# Forma con decorador property

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.__edad = edad

    @property # Decorador especial, que le indica que es un Getter.
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self.__edad

# SETTER

    @nombre.setter #Nombre de la propiedad.
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

# DELETTER
    @nombre.deleter
    def nombre(self):
        del self._nombre


# Ahora puedo invocarlo como una propiedad, sin los () y enmascarar el nombre, ya no es _nombre sino que la llamamos como si fuera "nombre"
persona2 = Persona("Kiko",80)
print(persona2.nombre) # Kiko

#Sobreescribir
persona2.nombre = "PepeLuis"
print(persona2.nombre) # PepeLuis
print(persona2.edad) # 80

#Borrar
del persona2.nombre
# print(persona2.nombre) # Da error , ya no existe
