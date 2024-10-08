# Una clase padre y muchas clases hijas

class Persona: # SUPERCLASE
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        return f"Yo {self.nombre} estoy hablando..."

class Artista: # SUPERCLASE
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad) # Ya no uso super(), sino el nombre de la clase super heredada. Ahora tengo que incluirles el "self,".
        Artista.__init__(self, habilidad) # Ya no uso super(), sino el nombre de la clase super heredada. Ahora tengo que incluirles el "self,"
        self.salario = salario
        self.empresa = empresa

    # Herencia de metodos

    def hablar(self):
        return "Yo soy hablar, pero dentro de la clase 'EmpleadoArtista' "

    def mostrar_habilidad(self):
        return "Yo soy mostrar_habilidad, pero dentro de la clase 'EmpleadoArtista' "

    def herencia_hablar(self):
        print("Propio: ")
        print(self.hablar()) #Llamo a la clase hija, imprime: Yo soy hablar, pero dentro de la clase 'EmpleadoArtista'
        print("Heredado: ")
        print(super().hablar()) #Llamo a la clase padre, imprime: Yo Alemito estoy hablando...

    def herencia_mostrar_habilidad(self):
        print("Propio: ")
        print(self.mostrar_habilidad()) # Yo soy mostrar_habilidad, pero dentro de la clase 'EmpleadoArtista'
        print("Heredado: ")
        print(super().mostrar_habilidad()) # Mi habilidad es: Procastinar



test = EmpleadoArtista("Alemito",38,"Zaracatunga","Procastinar",100,"Company")
test.herencia_hablar()
test.herencia_mostrar_habilidad()


#Verificar herencias
herencia1 = issubclass(EmpleadoArtista,Artista) # Pregunta si EmpleadoArtista es una subclase de Artista
print(herencia1) # True
herencia2 = issubclass(EmpleadoArtista,Persona)
print(herencia2) # True
herencia3 = issubclass(Persona,EmpleadoArtista)
print(herencia3) # False

#Verificar instancias
instancia1 = isinstance(test,Persona) # test es un objeto de la clase Persona
print(instancia1) # True
instancia2 = isinstance(test,EmpleadoArtista) # test es un objeto de la clase EmpleadoArtista
print(instancia2) # True

otra_variable = "PEPE"
instancia3 = isinstance(otra_variable,EmpleadoArtista) # otra_variable no es ningun objeto
print(instancia3) # False

test2 = Artista("Dormir")
print(test2.habilidad) # Dormir

instancia4 = isinstance(test2,EmpleadoArtista)
print(instancia4) # False
instancia5 = isinstance(test2,Persona)
print(instancia5) # False
instancia6 = isinstance(test2,Artista)
print(instancia6) # True
