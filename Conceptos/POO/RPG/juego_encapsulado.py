"""
Vamos a impedir que los atributos sean accesibles por fuera de la clase
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
        print(f"nombre: {self.__nombre}")
        print(f"fuerza: {self.__fuerza}")
        print(f"inteligencia: {self.__inteligencia}")
        print(f"defensa: {self.__defensa}")
        print(f"vida: {self.__vida}")
        print(f"aguante: {self.__aguante}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self): # Morir solo va a poder accederse desde atacar, el usuario no puede invocarlo directamente.
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

# Permitir acceder / editar ciertos atributos:

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, nueva_fuerza):
        if nueva_fuerza < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.__fuerza = nueva_fuerza

#Creo personajes
mi_personaje = Personaje("Alemito", 30, 50 , 30, 200)
mi_enemigo = Personaje("Enemigo 1", 30, 10, 15, 10)

#intento modificar fuerza, pero no puedo
mi_enemigo.__fuerza = 0
mi_personaje.atributos()
mi_enemigo.atacar(mi_enemigo)

print("#"*15)
mi_personaje.set_fuerza(5)
print(mi_personaje.get_fuerza())
mi_personaje.atributos()