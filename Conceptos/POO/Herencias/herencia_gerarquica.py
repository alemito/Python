# Una clase padre y muchas clases hijas

class Persona: # SUPERCLASE
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Yo {self.nombre} estoy hablando...")

    def saludar(self):
        print(f"Hola querido!...")

class Empleado(Persona): # SUBCLASE 1
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def saludar(self):
        print(f"JAMAS!...")


class Estudiante(Persona): # SUBCLASE 2
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

    def saludar(self):
        print(f"Hola Director...")

alem = Empleado("Ale",88,"Zaracatunga","Programador",15)
alem.hablar() # Yo Ale estoy hablando...
print(alem.trabajo) # Programador
alem.saludar() # En lugar de "Hola querido!..." imprime "JAMAS!..." , ya que este metodo se sobreescribio en la clase Empleado.

hori = Estudiante("Horacio",20,"Sucutrule",3,"De la calle")
hori.hablar() # Yo Horacio estoy hablando...
print(hori.universidad) # De la calle
hori.saludar() # En lugar de "Hola querido!..." o "JAMAS!..." , imprime "Hola Director" ya que este metodo se sobreescribio en la clase Empleado.