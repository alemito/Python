def sumar(n1,n2):
    suma = n1 + n2
    return suma

print(sumar(1,2)) # Devuelve 3

#print(sumar(1,"2")) # unsupported operand type(s) for +: 'int' and 'str'


# finally
def sumar2(n1,n2):
    try:
        suma2 = n1 + n2
        return suma2
    except:
        return "Ocurrio un error"
    finally:
        print("finalizado, siempre me muestro haya pasado el try o el except")

print(sumar2(1,"2")) # Ocurrio un error

# TIPOS DE EXCEPCIONES:


#Exception
try:
    x = 10 / 0  # Esto lanza una excepción de tipo ZeroDivisionError
except Exception as e:
    print(f"Se produjo una excepción: {e}")

#ValueError
try:
    num = int("abc")  # Esto lanza una excepción de tipo ValueError
except ValueError as ve:
    print(f"Error de valor: {ve}") # Error de valor: invalid literal for int() with base 10: 'abc'

#TypeError
try:
    result = 5 + "2"  # Esto lanza una excepción de tipo TypeError
except TypeError as te:
    print(f"Error de tipo: {te}") # Error de tipo: unsupported operand type(s) for +: 'int' and 'str'

#FileNotFoundError
try:
    with open("archivo_inexistente.txt", "r") as f:  # Intenta abrir un archivo que no existe
        contenido = f.read()
except FileNotFoundError as fe:
    print(f"Archivo no encontrado: {fe}") # Archivo no encontrado: [Errno 2] No such file or directory: 'archivo_inexistente.txt'

#ZeroDivisionError
try:
    result = 5 / 0  # Esto lanza una excepción de tipo ZeroDivisionError
except ZeroDivisionError as zde:
    print(f"Error de división por cero: {zde}") # Error de división por cero: division by zero



def division():
    try:
        #resultado = 2/5 # 0.4
        #resultado = 2/"5" # No se puede dividir por una cadena de string
        resultado = 2/0 # No se puede dividir por cero
        print(f"El resultado es: {resultado}")
    except TypeError:
        print("No se puede dividir por una cadena de string")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e)) # si no defino "resultado" > Ha ocurrido un error no previsto <class 'NameError'>

division()