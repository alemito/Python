# DECLARACION DE LISTAS

numeros = [1,2,3,4,5]
colores = ["rojo","verde","azul"]
lista_vacia =[]
matriz = [[1,2,3],[4,5,6],[7,8,9]]

# ACCEDEMOS POR SUBINDICES

print(numeros[0]) # 1
print(colores[1]) # Verde
print(matriz[1][2]) # 6


# Recorriendo subindices

i = 0
while i < len(numeros): # Len > tamaño de lista 
    print(f"El numero es: {numeros[i]}")
    i += 1 # i = i +1

for x in numeros:
    print(f"El numero es: {x}")


#Desempaquetado, permite asignarle una variable a cada posicion. Como ponerle nombre a las posiciones, pero no genera otros cambios.
c1,c2,c3 = colores 
# Es igual a hacer:
# c1 = colores[0]
# c2 = colores[1]
# c3 = colores[2]

print(c1)
print(c2)
print(c3)


# Funciones Listas

print(f"El numero maximo de la lista es: {max(numeros)}")
print(f"El numero minimo de la lista es: {min(numeros)}")
print(f"La suma de los numeros de la lista es: {sum(numeros)}")

# Agregar Elementos

# Nuevo elemento al final
numeros.append(10)
print(f"La lista ahora es: {numeros}")

# Insertar en una posicion especifica.
numeros.insert(0,0) # En 0 insertá 0
print(f"La lista ahora es: {numeros}")
numeros.insert(3,45) # En 3 insertá 45
print(f"La lista ahora es: {numeros}")

# Eliminar Elementos
#Pop sin especificar elemento, borra el ultimo

numeros.pop() # Elimina el ultimo
print(f"La lista ahora es: {numeros}")
numeros.pop(1) # Elimina la posicion 1
print(f"La lista ahora es: {numeros}")
