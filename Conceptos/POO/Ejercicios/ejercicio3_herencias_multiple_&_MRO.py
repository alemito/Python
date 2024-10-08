"""
Ejercicio de herencia múltiple y MRO:

Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal", "Mamífero" y "Ave". La clase "Animal" debe tener un método llamado "comer".
La clase "Mamífero" debe tener un método llamado "amamantar" y la clase "Ave" un método llamado "volar".
Ahora, crea una clase "Murciélago" que herede de "Mamífero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", además de "comer".
Finalmente, juega con el orden de herencia de la clase "Murciélago" y observa cómo cambia el MRO y el comportamiento de los métodos al usar super().

Evidentemente esta mal redactado

"""
class Animal:
    def comer(self):
        print("El animal está comiendo")

class Mamifero:
    def amamantar(self):
        print("El animal está amamantando")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Murcielago(Mamifero, Ave):
    pass
print("Murcielago")
murcielago = Murcielago()
murcielago.comer()
murcielago.volar()
murcielago.amamantar()
print("Ave")
ave = Ave()
ave.volar()
print("MRO")
print(Murcielago.mro())