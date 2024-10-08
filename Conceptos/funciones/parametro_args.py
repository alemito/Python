# por lo que entiendo es solo para pasarle datos sin necesidad de agruparlos por tipo


#forma no optima de sumar valores
def suma(lista):
   numeros_sumados = 0
   for numero in lista:
       numeros_sumados = numeros_sumados + numero
   return numeros_sumados

resultado = suma([5,3,9,10,20,3])

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])


#lo mismo que arriba pero utilizando el operador * como parametro (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma(8,5,3,9,10,20,3)

def suma(nombre, *numeros):
    print(f"Nombre: {nombre}")
    print(f"Números: {numeros}")

# Llamada a la función
suma("Lucas", 5, 3, 9)


#Ejemplo de lista sin *args
def hacer_pizza(nombre, ingredientes):
    return f"{nombre}, tu pizza con {', '.join(ingredientes)} está lista!"

resultado = hacer_pizza("Alemito", ["queso", "pepperoni", "champiñones"])
print(resultado)

#Con *args
def hacer_pizza(nombre, *ingredientes):
    return f"{nombre}, tu pizza con {', '.join(ingredientes)} está lista!"

resultado = hacer_pizza("Alemito", "queso", "pepperoni", "champiñones")
print(resultado)
