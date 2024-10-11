"""
Permitir crear diferentes clases de personajes y acciones con encapsulado y herencias.
"""

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        self.__aguante = fuerza * vida

# Atributos accesibles
    @property
    def nombre(self):
        return self.__nombre
    @property
    def fuerza(self):
        return self.__fuerza
    @property
    def inteligencia(self):
        return self.__inteligencia
    @property
    def defensa(self):
        return self.__defensa
    @property
    def vida(self):
        return self.__vida
    @property
    def aguante(self):
        return self.__aguante

# Atributos editables
    @vida.setter
    def vida(self,nueva_vida):
        self.__vida = nueva_vida
    @fuerza.setter
    def fuerza(self,nueva_fuerza):
        self.__fuerza = nueva_fuerza
    @inteligencia.setter
    def inteligencia(self,nueva_inteligencia):
        self.__inteligencia = nueva_inteligencia
    @defensa.setter
    def defensa(self,nueva_defensa):
        self.__defensa = nueva_defensa

    def atributos(self):
        print(f"-Nombre: {self.__nombre}")
        print(f"-Fuerza: {self.__fuerza}")
        print(f"-Inteligencia: {self.__inteligencia}")
        print(f"-Defensa: {self.__defensa}")
        print(f"-Vida: {self.__vida}")
        print(f"-Aguante: {self.__aguante}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def __morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def damage(self, enemigo):
        #return self.fuerza - enemigo.defensa
        return max(self.fuerza - enemigo.defensa, 0) # Si el calculo da negativo, que el daño sea 0

    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(f"{self.nombre} ha realizado {damage} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} ahora es {enemigo.vida}")
        else:
            enemigo.__morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada=0):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, damage +8. (2) Matadragones, damage +10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("-Espada: ", self.espada)

    def damage(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, objeto_magico=0):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.objeto_magico = objeto_magico

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Vara, damage +15. (2) Libro, damage +11 "))
        if opcion == 1:
            self.objeto_magico = 15
        elif opcion == 2:
            self.objeto_magico = 11
        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("-Objeto Magico: ", self.objeto_magico)

    def damage(self, enemigo):
        return self.inteligencia * self.objeto_magico - enemigo.defensa

# Polimormismo ya que dependiendo de los argumentos que le pase variaran los valores del combate, pero el combate es el mismo.
def equipar(personaje):
    personaje.cambiar_arma() #tiene muchas formas de usarse, dependiendo de los argumentos

""" Combate, la secuencia se repetira hasta que uno de los 2 muera"""
def combate(personaje_atacante, personaje_defensor):
    turno = 0
    while personaje_atacante.esta_vivo() and personaje_defensor.esta_vivo(): # Cuando alguno sea False se corta
        print("\nTurno", turno)
        print("\n>>> Accion de", personaje_atacante.nombre, ":")
        personaje_atacante.atacar(personaje_defensor)
        print("\n>>> Accion de", personaje_defensor.nombre, ":")
        personaje_defensor.atacar(personaje_atacante)
        turno = turno + 1
    if personaje_atacante.esta_vivo():
        print(f"\n Ganó el jugador {personaje_atacante.nombre}, quedó con {personaje_atacante.vida} de vida.")
    elif personaje_defensor.esta_vivo():
        print(f"\n Ganó el jugador {personaje_defensor.nombre}, quedó con {personaje_defensor.vida} de vida.")
    else:
        print(f"Empate! , {personaje_atacante.nombre} y {personaje_defensor.nombre} se mataron mutuamente.")


#Creo personajes
mi_guerrero = Guerrero("Alemito", 30, 50 , 30, 1300)
mi_enemigo = Personaje("Enemigo 1", 50, 60, 15, 300)
mi_mago = Mago("Brujo",10, 80, 5, 1000)

equipar(mi_guerrero)
equipar(mi_mago)
combate(mi_guerrero, mi_mago)