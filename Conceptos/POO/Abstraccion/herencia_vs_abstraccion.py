"""
as clases abstractas y la herencia de clases son conceptos relacionados, pero se utilizan en situaciones diferentes según lo que quieras lograr. Aquí te explico cuándo y por qué usar clases abstractas en lugar de simplemente usar herencia directa.
Herencia de clases

Cuando usas herencia directa, una clase hija hereda los métodos y atributos de una clase padre, y tiene la opción de sobrescribir (modificar) algunos de estos métodos. Sin embargo, la clase padre puede ser instanciada, y no hay obligación de sobrescribir los métodos heredados.
Clases abstractas

Las clases abstractas se utilizan cuando quieres asegurarte de que todas las clases hijas implementen ciertos métodos específicos, pero sin definir una implementación genérica en la clase padre. Además, las clases abstractas no pueden ser instanciadas directamente, lo que asegura que solo se trabajará con las clases hijas concretas que implementen los métodos necesarios.
¿Por qué usar clases abstractas?

    Diseño estructurado: Con una clase abstracta, puedes definir un "contrato" que las clases hijas deben cumplir. Esto es útil para asegurarte de que todas las clases hijas implementen ciertos métodos.

    No instanciable: Una clase abstracta asegura que no puedas crear objetos de ella. Esto es útil cuando tienes una clase general que no debería existir por sí sola, pero que debe ser la base de otras clases más específicas.

    Flexibilidad: Te permite establecer un esqueleto para futuras clases sin definir completamente los detalles, dejando que las clases hijas concreten lo que necesiten.

Diferencia clave con la herencia simple

Con la herencia simple, puedes heredar métodos de una clase base, pero no tienes control sobre si las clases hijas están obligadas a implementar o modificar esos métodos. Con una clase abstracta, obligas a que ciertas funcionalidades específicas sean definidas en las clases hijas.
"""

# Herencia Simple
class Animal:
    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    pass  # No tiene obligación de sobrescribir el método sonido()

perro = Perro()
print(perro.sonido())  # Imprime "Sonido genérico"

# Clases Abstractas
from abc import ABC, abstractmethod

class Animal2(ABC):
    @abstractmethod
    def sonido(self):
        pass  # Las clases hijas deben definir este método

class Perro(Animal2):
    def sonido(self):
        return "Guau"

# animal = Animal2()  # Esto dará error, no se puede instanciar una clase abstracta
perro = Perro()
print(perro.sonido())  # Imprime "Guau"
