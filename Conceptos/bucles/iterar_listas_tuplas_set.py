animales =  ["gato","perro","loro","cocorilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)


#iterando dos listas del MISMO tamaño al mismo tiempo . Se debe usar zip, funciona con mas de 2 listas
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")


#forma no optima de recorer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el ìndice es: {indice} y el valor es: {valor}')


#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino" )


#todo lo anterior funciona exactamente igual para tuplas y conjuntos