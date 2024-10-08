"""Los modulos son archivos que contienen definiciones que se pueden impoart en otros scripts para reutilizar sus funcionalidades.

Un modulo es un archivo py cuyos objetos (funciones, clases,excepciones,etc). pueden ser accedidos desde otro script.
Constituye una muy buena herramienta para organizar el codigo en proyectos grandes o complejos. """

#Para importar un modulo uso la palabra reservada IMPORT

# SIN IMPORT
#print(math.pi) #Name 'math' is not defined

import math

print(math.pi) # 3.141592653589793


#Importar a una funcion de otro py.
#Cuando es local debo aclarar de donde lo obtengo, para eso utilizo FROM

# FROM carpeta.subcarpeta.archivo(sin.py) IMPORT funcion
import os
import sys

# Obtén la ruta al directorio del script actual
current_dir = os.path.dirname(os.path.realpath(__file__))

# Agrega el directorio raíz de tu proyecto al sys.path
proyecto_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(proyecto_dir)

""" 
from funciones.funcion_01 import funcion1
funcion1() 

Cuando un módulo de Python es importado, todas las declaraciones en ese módulo se ejecutan. Esto incluye las llamadas a funciones.
como "funcion_01" tiene codigo que llama a las funciones, se termina ejecutando completo. """ 

from funciones.funcion_02 import funcion1 # por mas que cargue todo el archivo, solo puedo ejecutar las funciones que defini acá

funcion1() #3

""" En este caso, funcion_02 solo tiene las funciones, al no tener invocaciones obtengo el dato real."""