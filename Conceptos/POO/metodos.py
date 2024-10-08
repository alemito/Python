# Un metodo es una funcion.
#Definir los metodos es definir las acciones que puede hacer nuestro objeto

class Celular():
    def __init__(self, marca, modelo, camaraT, camaraF):
        self.marca = marca
        self.modelo = modelo
        self.camaraT = camaraT
        self.camaraF = camaraF

    def llamar(self): #Hay que pasarle el parametro self que hace referencia al objeto.
        return "Llamando"

    def cortar(self):
        print(f"Cortaste la llamada que hiciste desde el telefono {self.marca}") #Como le pase self a la funcion, ahora puedo invocar los datos del objeto creado.

celular1 = Celular("samsung","S23","48MP","24MP")
celular2 = Celular("apple","Iphone 15 pro","48MP","24MP")
celular3 = Celular("huawei","P20 Pro","12MP","8MP")


print(celular1.llamar()) # Lo invoco como a las funciones, con ()
celular2.cortar() # Como cortar es un print y no un return, puedo invocarlo y directamente imprimir el resultado. Si hago print con el que tiene print, imprime y agrega un "none"
celular3.cortar()
