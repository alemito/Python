#creando una funcion de 3 parametros

#def frase(nombre,apellido,adjetivo):
#    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keyword arguments . Con esto podemos poner las variables en cualquier orden y sabra armarlas
#frase_resultante = frase(adjetivo = "capo",nombre = "Lucas",apellido ="Dalto")


#creando la misma funcion con un parametro opcional y un valor por defecto. Si yo se lo paso en la llamada, lo sobreescribe.
def frase(nombre,apellido,adjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Lucas","Dalto","inteligente")
print(frase_resultante)
