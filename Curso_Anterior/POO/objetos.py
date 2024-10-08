# La clase es el molde/prototipo para crear objetos.

# El objeto, que tiene atributos y metodos. Para crear el objeto necesitamos la clase

# El objeto es una instancia de una clase

# Los metodos permiten a los objetos de una clase realizar acciones. Se declaran con "def" dentro de una clase.

### Clase
#Por convencion la clase siempre inicia con Mayuscula
class Persona:
    #atributos
    piernas = 2
    ### Metodo.
    def caminar(self): # definimos un metodo. (self) es obligatorio y lo usa para auto referenciarse.
        print("Esta caminando")
        #Usando la autoreferencia
        print(self.piernas) # Seria como hacer caminar.piernas

### Objeto
#instanciar la clase, creando el objeto.
persona1 = Persona()  # Creo mi primer persona, , con todos los atributos
persona2 = Persona()  # Creo mi segundo objeto, con todos los atributos

alemito = Persona()
alemito.edad = 37 # puedo definir atributos nuevos que solo afectaran al objeto en cuestion.     print(persona1.edad)  > AttributeError: 'Persona' object has no attribute 'edad'

### Atributos de clase
# Utilizo los objetos, se utiliza clase.atributo
print(persona1.piernas) # 2
print(persona2.piernas) # 2
print(alemito.edad) # 37

alemito.caminar() # Invocamos al metodo caminar() > ### Clase

# Otro ejemplo de self

class Prueba():
    def caminar(self): # Metodo caminar
        self.caminando = True # Atributo
        print("Estoy caminando...")

    def detener(self): # Metodo detener
        self.caminando = False # Atributo
        print("Estoy detenido...")

Alemito = Prueba() # Instancio
Alemito.caminar() # Estoy caminando...
print(Alemito.caminando) # True
Alemito.detener() # Estoy detenido...
print(Alemito.caminando) # False


class Persona2():
    piernas = 2
    nombre = "Alemito"

    def saludar(self):
        print("Hola " + self.nombre)

    def despedirse(self):
        print("Chau " + self.nombre)


personalizado = Persona2()
personalizado.saludar() # Hola Alemito
personalizado.despedirse() # Chau Alemito


### METODO CONSTRUCTOR

class Persona3():

    # Metodo constructor
    def constructor(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    # Metodo normal
    def identificarse(self):
        print(f"Hola. Soy {self.nombre} y tengo {self.edad} años.")


objeto3 = Persona3() # Instanciamos.
objeto3.constructor("Alemito",37) # Construyo con las variables.
objeto3.identificarse() # Hola. Soy Alemito y tengo 37 años.
objeto3.edad = 43 # Modifico la edad.
objeto3.identificarse() # Hola. Soy Alemito y tengo 43 años.