class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor" #El "_" indicara que es un atributo privado. Pero accesible
        self.__atributo_muy_privado = "Otro valor" #El "__" indicara que es un atributo privado. Pero accesible

    def __hablar(self):
        print("Hola")

objeto = MiClase()
print(objeto._atributo_privado) # Imprime "Valor", entiende que es privado pero puede acceder
#print(objeto.__atributo_muy_privado) # Da error, el atributo es privado y no lo puede acceder.
#objeto.__hablar() # Da error, el metodo es privado y no lo puede acceder.

"""
Sabiendo el nombre de la clase puedo invocar al atributo.
"""
print(objeto.__class__.__name__) # Obtengo el nombre de la clase
print(objeto._MiClase__atributo_muy_privado) # Especifico la clase y el nombre del atributo privado.
objeto._MiClase__hablar() # Imprime Hola