"""
Es una clase que no podemos instanciar, es como una plantilla. Una clase que usamos para crear otras clases.
Es como herencia, pero mas complejo. Aumenta la claridad y define metodos que todas las subclases si o si deben tener , forzando a que sea mas sintetico.
"""

from abc import ABC, abstractmethod # El módulo abc (Abstract Base Class) sirve para crear clases abstractas.

#Los metodos que deben ser implementados por las clases hijas se marcan con el decorador @abstractmethod

# Definir una clase abstracta
class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass  # Este método debe ser implementado por las clases hijas

# Clase concreta que hereda de Animal
class Perro(Animal):
    def sonido(self):
        return "Guau"

# Otra clase concreta que hereda de Animal
class Gato(Animal):
    def sonido(self):
        return "Miau"

# No puedes crear una instancia de la clase abstracta
# animal = Animal()  # Esto dará error

# Puedes crear instancias de las clases que implementan los métodos abstractos
perro = Perro()
gato = Gato()

print(perro.sonido())  # Guau
print(gato.sonido())   # Miau

"""
Explicación:

    Clase abstracta (Animal): Define un método abstracto sonido(). Esta clase no puede ser instanciada directamente.
    Clases concretas (Perro, Gato): Heredan de Animal y deben implementar el método sonido().
    Uso: Al crear un objeto de las clases hijas (Perro, Gato), se puede llamar al método sonido() que fue definido específicamente en cada clase concreta.

Este diseño asegura que cualquier clase que herede de Animal debe definir su propio método sonido().
"""