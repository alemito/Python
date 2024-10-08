#Atributos Estaticos
class NombreClase:
    """Estos son atributos estaticos, por que son iguales para todos los objetos"""
    propiedad1 = "Valor1"
    propiedad2 = "Valor2"
    propiedad3 = "Valor3"

#Crear objeto "prueba"
prueba = NombreClase() # A esto se llama instanciar objeto / crear un objeto . prueba (objeto) es una instancia de la clase NombreClase

#Imprimir datos del objeto
print(prueba) # <__main__.NombreClase object at 0x000001EA48B8EED0> , indica que es un objeto
print(prueba.propiedad2) # Invoco a la propiedad del objeto que quiero

#Creando mas objetos

otra_prueba = NombreClase()
otra_prueba_otra = NombreClase()
otra_prueba_mas = NombreClase()

print(otra_prueba.propiedad1)
print(otra_prueba_otra.propiedad2)
print(otra_prueba_mas.propiedad3)
print("*"*10 + "Fin de pruebas atributos estaticos" + "*"*10 + "\n\n")

#Atributos Dinamicos

class OtraClase:
    """Estos atributos son dinamicos, paso los valores cuando creo el objeto"""
    # Metodo constructor
    # __init__ es una funcion especial, siempre que se cree una instancia, la clase creara este metodo con los atributos definidos.
    def __init__(self, propiedad12, propiedad22, propiedad32): # self es una forma de referenciarse a si mismo . self.propiedad12 es igual a prueba1.propiedad12 o prueba2.propiedad12 , dependiendo de quien seas.
        # DEFINIR PROPIEDADES.
        self.propiedad12 = propiedad12 # aca le guardo el valor que le pase por la invocacion, podria pasarle propiedad12 * 2 y que eso lo guarde dentro del atributo propiedad12.
        self.propiedad22 = propiedad22
        self.propiedad32 = propiedad32
        self.unificado = "Mensaje " + propiedad12 + " " + propiedad22 + " " + propiedad32 # Esto es un atributo que creo en base a datos pasados. unificado seria una propiedad de self.


pruebas_2 = OtraClase("Valor12","Valor22","Valor32")
print(pruebas_2)
print(pruebas_2.propiedad12)
print(pruebas_2.propiedad22)
print(pruebas_2.propiedad32)
print(pruebas_2.unificado)

pruebas_3 = OtraClase("Valor44","Valor55","Valor66")
print(pruebas_3.unificado)