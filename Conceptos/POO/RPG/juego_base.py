class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.aguante = fuerza * vida

    def atributos(self):
        print(f"nombre: {self.nombre}")
        print(f"fuerza: {self.fuerza}")
        print(f"inteligencia: {self.inteligencia}")
        print(f"defensa: {self.defensa}")
        print(f"vida: {self.vida}")
        print(f"aguante: {self.aguante}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0 #Devuelve True si la vida es mayor a 0

    def morir(self):
        self.vida = 0 # Setea la vida en cero
        print(self.nombre, "ha muerto")

    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa # Entonces puedo acceder a todos los atributos de enemigo ??

    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(f"{self.nombre} ha realizado {damage} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} ahora es {enemigo.vida}")
        else:
            enemigo.morir() # Lo mato si la vida baja de 0

#Creo mi personaje
mi_personaje = Personaje("Alemito", 30, 50 , 30, 200)
mi_personaje.atributos()

#Subir de nivel
mi_personaje.subir_nivel(0,2,1)
mi_personaje.atributos() # Stats subidos

#Ver estado
print(mi_personaje.esta_vivo())

#Matar
mi_personaje.morir()
mi_personaje.atributos()

#Creo a mi enemigo
mi_enemigo = Personaje("Enemigo 1", 30, 10, 15, 10)
print(mi_personaje.damage(mi_enemigo))
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()