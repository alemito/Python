"""
Vamos a permitir crear diferentes clases de personajes
"""

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        self.__aguante = fuerza * vida

    def atributos(self):
        print(f"-Nombre: {self.__nombre}")
        print(f"-Fuerza: {self.__fuerza}")
        print(f"-Inteligencia: {self.__inteligencia}")
        print(f"-Defensa: {self.__defensa}")
        print(f"-Vida: {self.__vida}")
        print(f"-Aguante: {self.__aguante}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def damage(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.__vida = enemigo.__vida - damage
        print(f"{self.__nombre} ha realizado {damage} puntos de daño a {enemigo.__nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.__nombre} ahora es {enemigo.__vida}")
        else:
            enemigo.__morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, damage +8. (2) Matadragones, damage +10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion ==2:
            self.espada = 10
        else:
            print("Numero de arma incorrecto")

    # Hacer que al invocar atributos tambien incluya el daño de la espada.
    def atributos(self):
        super().atributos() # Carga todos los atributos de Personaje
        print("-Espada: ", self.espada)

    def damage(self, enemigo):
        return self.fuerza * self.espada - enemigo.__defensa

#Creo personajes
mi_guerrero = Guerrero("Alemito", 30, 50 , 30, 200,0)
mi_enemigo = Personaje("Enemigo 1", 30, 10, 15, 10)

#
print(mi_guerrero.espada)
mi_guerrero.cambiar_arma()
mi_guerrero.atributos()
mi_guerrero.atacar(mi_enemigo)