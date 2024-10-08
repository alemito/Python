def sumar(numero1,numero2):
    suma = 0
    for elemento in range(numero1,numero2+1): #Sumo uno para que el stop no sea -1
        suma +=elemento
    print(f"La suma de todos los numeros es: {suma}")


sumar(1,10) #Del 1 al 10 sumame todos los numeros

def imprimir_mensaje_N_veces(n,m):
    for i in range(n):
        print(m)


mensaje = input("Mensaje: ")
veces = int(input("N° de veces que desea imprimir: "))
imprimir_mensaje_N_veces(veces, mensaje)


# #Parametros opcionales / valores por default

def otra_suma(a = 0, b = 0):  #ambas var tienen el valor 0 por default.
    return a + b

print(otra_suma()) # Puedo no pasarle valores y tomara los default
print(otra_suma(1,2)) # Puedo pasarle valores y funciona como siempre


# Parametros Posicionales
#los valores de la funcion se asigan en el orden en que se indican, esto se puede cambiar si llamamos a la funcion indicando el nombre de
#los parametros

def posicionales(nombre,apellido):
    print(f"La variable nombre contiene el valor {nombre} y la variable apellido contiene {apellido}")

posicionales("ale","mito") # La variable nombre contiene el valor ale y la variable apellido contiene mito
posicionales("mito","ale") # La variable nombre contiene el valor mito y la variable apellido contiene ale
posicionales(apellido="mito",nombre="ale") # La variable nombre contiene el valor ale y la variable apellido contiene mito


# Devolucion de valores: Return
# Return es opcional y puede o no devolver un valor.

#mostrar el cuadrado solo si es un numero par

def cuadrado_de_par(numero):
    if not numero % 2 == 0:
        return
    else:
        print(numero ** 2)

cuadrado_de_par(8) #64
cuadrado_de_par(3) #nada, por que return no dice nada y es impar.


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(2)) # True
print(es_par(5)) # False


# Devolver varios valores
# separando los valores con "," se puede enviar mas de un valor retornado.

def cuadrado_y_cubo(numero):
    return numero **2, numero **3

print(cuadrado_y_cubo(2)) # (4,8)
print(f"Cuadrado: {cuadrado_y_cubo(2)[0]}") # Cuadrado: 4
print(f"Cubo: {cuadrado_y_cubo(2)[1]}") # Cubo: 8

# Lo mismo, pero con desempaquetado:

cuadrado,cubo = cuadrado_y_cubo(2)
print(f"Cuadrado: {cuadrado}" ) # Cuadrado: 4
print(f"Cubo: {cubo}" ) # Cubo: 8


# Funciones que usan funciones

def funcion_principal():
    print("Inicio de la función principal.")
    otra_funcion()
    print("Fin de la función principal.")

def otra_funcion():
    print("Esta es otra función.")

funcion_principal()
# Inicio de la función principal.
# Esta es otra función.
# Fin de la función principal.


# Ciclo de vida de las variables

def funcion1():
    a = 3
    print(a)

funcion1() # 3
# # print(a) # Name 'a' is not defined

b = 8
def funcion2():
    b = 3
    print(b)

funcion2() # 3
print(b) # 8

c = 8
def funcion3():
    global c # hace que la variable se transforme en global, no es recomendado hacerlo.
    c = 3
    print(c)

funcion3() # 3
print(c) # 3