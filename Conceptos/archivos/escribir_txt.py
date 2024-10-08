# Usamos el parametro W para escribrir, siempre sobreescribe el archivo.

with open("archivos\\texto_de_Alemito.txt","w",encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo

    #linea unica
    # archivo.write("Jajajajaa te la recontra teclee")

    #agregando 2 lineas con writelines, se debe escribir como lista
    archivo.writelines([" - Hola maestro como andas\n"," - misericordia\n"])

    #agregando otras 2 lineas
    archivo.writelines([" - no se porque dijiste eso\n"," - yo tampoco"])