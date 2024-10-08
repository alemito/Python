# class Persona:
#     def __init__(self, nombre, edad, nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionalidad = nacionalidad

#     def hablar(self):
#         print(f"Yo {self.nombre} estoy hablando...")


# #Para decir que Empleado es Hijo de Persona, basta con colocar a su Padre dentro de los parentesis.
# class Empleado(Persona):
#     pass

# #Prueba de como Empleado hereda el metodo constructor de Persona
# test = Empleado("Ale",88,"Zaracatunga")
# print(test.nacionalidad) # Zaracatunga
# test.hablar() # Yo Ale estoy hablando...

class Persona: # SUPERCLASE
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Yo {self.nombre} estoy hablando...")

    def saludar(self):
        print(f"Hola querido!...")

class Empleado(Persona): # SUBCLASE
    """No esta preparado para agregar algo nuevo al padre de esta manera, esto fallara
    def __init__(self, trabajo, salario):
        self.trabajo = trabajo
        self.salario = salario
    """
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): # Definimos los atributos con los que vamos a trabajar, tanto del padre como de la clase hija.
        super().__init__(nombre, edad, nacionalidad)  # Con super() indicamos qué atributos heredamos de la clase padre.
        self.trabajo = trabajo
        self.salario = salario
# Usando la herencia, me ahorro escribir de nuevo los atributos y métodos definidos en la clase padre.

    #Si vuelvo a definir un metodo existente en la clase padre, este se sobreescribe.
    def saludar(self):
        print(f"JAMAS!...")

alemito = Empleado("Ale",88,"Zaracatunga","Programador",15)
alemito.hablar() # Yo Ale estoy hablando...
print(alemito.trabajo) # Programador
alemito.saludar() # En lugar de "Hola querido!..." imprime "JAMAS!..." , ya que este metodo se sobreescribio en la clase Empleado.