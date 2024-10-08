#Se usa "a" para hacer un append de la informacion y no sobreescribir el archivo.

with open("archivos\\texto_de_Alemito.txt","a",encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        #agregando lineas
        archivo.write(f"Linea {i+1} agregada\n")