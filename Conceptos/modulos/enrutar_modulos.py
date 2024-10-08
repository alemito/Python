#MODULOS DENTRO DE LA MISMA CARPETA
# import paquete.saludar

# saludo = paquete.saludar.saludar("jose") # El ultimo saludar es el nombre de la funcion dentro del archivo
# print(saludo)

import paquete.saludar as saludador

saludo = saludador.saludar("jose") # El ultimo saludar es el nombre de la funcion dentro del archivo
print(saludo)

#MODULOS EN CARPETA EXTERIOR, en este caso "funciones_externas"

# import sys

# sys.path.append("C:\\Users\\nowyo\\OneDrive\\Escritorio\\Programacion\\Conceptos\\funciones_externas")

# import saludo_externo

# print(saludo_externo.saludar("Lolo"))