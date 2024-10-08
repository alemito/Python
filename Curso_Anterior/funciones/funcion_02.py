# Mismo codigo de funciones_01 , pero sin invocar a las funciones

def sumar(numero1,numero2):
    suma = 0
    for elemento in range(numero1,numero2+1): 
        suma +=elemento
    print(f"La suma de todos los numeros es: {suma}")


def imprimir_mensaje_N_veces(n,m):
    for i in range(n):
        print(m)

def otra_suma(a = 0, b = 0):     return a + b


def posicionales(nombre,apellido):
    print(f"La variable nombre contiene el valor {nombre} y la variable apellido contiene {apellido}")


def cuadrado_de_par(numero):
    if not numero % 2 == 0:
        return
    else:
        print(numero ** 2)


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def cuadrado_y_cubo(numero):
    return numero **2, numero **3


def funcion_principal():
    print("Inicio de la función principal.")
    otra_funcion()
    print("Fin de la función principal.")

def otra_funcion():
    print("Esta es otra función.")

def funcion1():
    a = 3
    print(a)


b = 8
def funcion2():
    b = 3
    print(b)


c = 8
def funcion3():
    global c 
    c = 3
    print(c)
