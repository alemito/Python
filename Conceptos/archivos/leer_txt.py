# IMPORTANTE: No puedo abrir 2 veces un mismo archivo, siempre tengo que cerrarlo antes de volver a abrirlo para algo. La solucion a eso es with open

#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo_sin_leer= open("archivos\\texto_de_Alemito.txt",encoding="UTF-8")
# archivo= open("archivos\\texto_de_Alemito.txt")

# archivo = archivo_sin_leer.read()

# print(archivo)


#leer archivo completo
#archivo = archivo.read()

#leer una sola linea
linea = archivo_sin_leer.readline() # Lee la primera linea, readline(5) lee los primeros 5 caracteres de la 1° linea

#leer linea por linea
# lineas = archivo_sin_leer.readlines()

# #cerrar el archivo
archivo_sin_leer.close()


print(linea)