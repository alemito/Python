import modulo_saludar as m_saludar # Haciendo import me traigo todo lo del archivo modulo_saludar, si quiero traer una funcion especifica tengo que usar "from"

#Ahora la funciones de modulo saludar se comportan como objetos
# saludo = modulo_saludar.saludar_raro("Alemio") #Al haber puesto el as m_saludar ya no tengo que invocar al metodo completo
saludo = m_saludar.saludar_raro("Alemio")
print(saludo)

#Ver todas las funciones y variables que me puedo traer del modulo.
print(dir(m_saludar))

#Trayendo funciones especificas con FROM, esto integra la funcion al codigo y ya no hay que llamarla como antes

from modulo_saludar import saludar as sa, saludar_raro as sar

sal = sa("pepe")
print(sal)

sal2 = sar("pipo")
print(sal2)

#Si quiero traer mas de una funcion de ese modulo, separo por comas los immport from modulo_saludar import saludar as sa, saludar_raro as sar
#Si quiero importar todo, hago from modulo_saludar import * , pero es una mala practica.

#importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde ese modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu

#creamos las variables con los saludos
saludo = saludar_normal("Lucas")
saludo_raro = saludar_como_coscu("Fran")

#mostramos los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)

