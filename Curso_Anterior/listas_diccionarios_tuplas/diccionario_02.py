# Diccionarios
# almacenan datos, CLAVE - VALOR

# Creacion de un diccionario.

estudiantes = {"Juan": 10, "Ana": 10, "Maria": 9}

print(f"El diccionario contiene: {estudiantes}")

print(estudiantes.keys()) #Lo imprime en modo lista


# Recorrer elementos

# Recorriendo las claves
for elemento in estudiantes.keys(): #Si el elemento está en estudiantes.key va a imprimir los registros.
    print(elemento)

# o se puede hacer asi
mis_llaves = estudiantes.keys()
for x in mis_llaves:
    print(x)

# Recorrer por clave y valor.

for clave,valor in estudiantes.items(): # Los items del diccionario.
    print(f"El estudiante {clave} obtuvo {valor}")


for clave,valor in estudiantes.items(): # Los items del diccionario.
    print(f"El estudiante {clave} obtuvo {valor}", end="; \n")   # En agrega algo al final de cada elemento

