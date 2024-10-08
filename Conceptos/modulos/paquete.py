#Un paquete es una carpeta con muchos modulos python
#Sabe que es un paquete si existe un archivo llamado __init__.py (debe estar creado y vacio)

#Por lo que entiendo, en lugar de tener un modulo con muchas funciones y hacer un import de eso o tener muchos archivos .py y hacer un import de cada uno
#los meto todo en un directorio, creo __init__.py y ese directorio se me transforma en un paquete donde solo haciendole un import a el puedo traerme todas las funciones
#de ese directorio.


import paquete.saludar

print(paquete.saludar.saludar("dalto"))