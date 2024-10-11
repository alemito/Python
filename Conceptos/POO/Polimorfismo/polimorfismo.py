class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"

animal1 = Gato()
animal2 = Perro()
"""
Esto es polimorfismo , un mismo metodo cambia segun que objeto lo invoque.
"""
print(animal1.sonido())
print(animal2.sonido())

"""
Otro tipo de polimorfismo valido, el polimorfismo de funcion. Misma funcion,pero cambia el argumento.
Cambia el parametro, no la funcion.
"""

def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(animal1) # o hacer_sonido(Gato())
hacer_sonido(animal2) # o hacer_sonido(Perro())
