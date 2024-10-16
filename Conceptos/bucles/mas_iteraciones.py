
#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Dalto"
numeros = [2,5,8,10]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue # El resto de instrucciones no se ejecuta y salta a la siguiente vuelta del FOR
    print(f'Me voy a comer una {fruta}')

#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break # Corta el for y no sigue con el resto de las vueltas
else:
    print("terminado") #Esto no se ejecuta por el break

#recorer una cadena de texto
for letra in cadena:
    print(letra)


#for en una sola linea de còdigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

#For en una linea reemplaza a :
# numeros_duplicados = list()
# for numero in numeros:
#     numeros_duplicados.append(numero*2)
# print(numeros_duplicados)