diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continùa). La usamos mas cuando queremos definirle un valor por defecto si la clave no existe. diccionario.get("nombre", "Valor por defecto")
valor_de_kasdks = diccionario.get("kasdks")
print("hola papa, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)