"""
Es una funcion especial que añade codigo extra a funciones ya existentes.
Se manejan mucho para la excepcion de errores, mediciones de tiempos.
"""

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada


def saludo():
    print("Holis")


# saludo() # Holis

# decorador(saludo) # No imprime nada

# Version no OPTIMA
# saludo_modificado = decorador(saludo)
# saludo_modificado() # Antes de llamar a la funcion - Holis - Despues de llamar a la funcion


""" Version con decorador optimo.
Se define la funcion decoradora y se la invoca con "@" justo arriba de la funcion que queremos decorar.
"""

@decorador
def saludo2():
    print("Te saludo de nuevo")

saludo2() # Antes de llamar a la funcion - Te saludo de nuevo - Despues de llamar a la funcion
