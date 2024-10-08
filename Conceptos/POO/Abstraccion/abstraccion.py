"""
Concepto de abstraccion
"""
class Auto:
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
            print("encendiendo...")
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.encender()
mi_auto.conducir() # Acá hay abstraccion, quien lo invoca no sabe que hay un if chequeando algo, solo sabe que tiene que invocar al metodo conducir() para ejecutarlo.