### METODO CONSTRUCTOR me permite pasarle variables a la clase

class Persona1():

    # Metodo constructor
    def constructor(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    # Metodo normal
    def identificarse(self):
        print(f"Hola. Soy {self.nombre} y tengo {self.edad} años.")


objeto1 = Persona1() # Instanciamos.
objeto1.constructor("Alemito",37) # Construyo con las variables.
objeto1.identificarse() # Hola. Soy Alemito y tengo 37 años.
objeto1.edad = 43 # Modifico la edad.
objeto1.identificarse() # Hola. Soy Alemito y tengo 43 años.


### Metodo __init__()

class Persona2():

    # Metodo constructor
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    # Metodo normal
    def identificarse(self):
        print(f"Hola. Soy {self.nombre} y tengo {self.edad} años.")


objeto2 = Persona2("Alemitosis",28) # Instancio y construyo las variables.
objeto2.identificarse()
objeto3 = Persona2("Pepe",44)
objeto3.identificarse()



### __STR__

class Jugador:
    def __init__(self,nombre,apellido,goles):
        self.nombre = nombre
        self.apellido = apellido
        self.goles = goles

    def __str__(self):
        return f"El jugador {self.nombre} {self.apellido} hizo {self.goles} goles"

    def __del__(self):
        print("El objeto fue eliminado") # Este mensaje aparece tambien cuando termina el programa y se limpia todo
 
    def saludar(self):
        return f"Hola {self.nombre} {self.apellido}"
    
    def despedirse(self):
        return f"Chau {self.nombre} {self.apellido}"    
    

jugador1 = Jugador("Leo","Messo",45)
jugador2 = Jugador("Pepe","Sand",124546)
jugador3 = Jugador("Cosme","Fulanito",4)

print(jugador1.saludar())
print(jugador3.despedirse())
print(jugador2)

# del jugador2 # Borrar directamente. Sin haber tenido __del__() definido
# print(jugador2) # print(jugador2) NameError: name 'jugador2' is not defined
del jugador2


# Ejemplo mas avanzado.

class Alumno: # Creo la clase.
    nro_alumnos = 0 # Cantidad de legajos existentes.

    #Constructor
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        Alumno.nro_alumnos += 1 # Agrego un legajo.

    #Mostrar datos del objeto.
    def __str__(self):
        return f"Nombre: {self.nombre} (nota: {self.nota})"
    
    #Dar de baja al alumno.
    def __del__(self):
        Alumno.nro_alumnos -= 1 # Resto un legajo.
        print("Alumno dado de baja.")
        print(f"{Alumno.nro_alumnos} legajos restantes.")

    def mostrar_estado(self): # Esta aprobado?
        print(f"El estado de {self.nombre} es ",end="")
        if self.nota <= 4:
            print("Regular")
        elif self.nota < 9:
            print("Bueno")
        else:
            print("Excelente")

# Programa principal

alumno1 = Alumno("Cosme Fulanito",8)
alumno2 = Alumno("Peter Pan",3)
print(alumno1) # Nombre: Cosme Fulanito (nota: 8)
print(alumno2) # Nombre: Peter Pan (nota: 3)
alumno1.mostrar_estado() # El estado de Cosme Fulanito es Bueno
alumno2.mostrar_estado() # El estado de Peter Pan es Regular
input("Pulse Enter para salir")
# Despues de apretar Enter se imprime:
# El objeto fue eliminado
# El objeto fue eliminado
# Alumno dado de baja.
# 1 legajos restantes.
# Alumno dado de baja.
# 0 legajos restantes.