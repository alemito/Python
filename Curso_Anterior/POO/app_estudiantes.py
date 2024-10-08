
# 1 - CARGAR ESTUDIANTE
# 2 - LISTAR ESTUDIANTE
# 3 - MOSTRAR ESTUDIANTES CON NOTAS MAYORES A 7
# 4 - SALIR DEL PROGRAMA

class Estudiante:

    #Constructor
    def __init__(self):
        self.nombres = []
        self.notas = []

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1 - Cargar Estudiante")
            print("2 - Listar")
            print("3 - Mostrar aprobados")
            print("4 - Finalizar el programa" + "\n")
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.mostrar_aprobados()
            else:
                self.finalizar()

    def cargar(self):
        nombre = input("Nombre del estudiante: ")
        self.nombres.append(nombre)
        nota = int(input("Nota del estudiante: "))
        self.notas.append(nota)
    
    def listar(self):
        print("Listado de estudiantes")

        for x,y in zip(self.nombres, self.notas) :
            print(f"Estudiante: {x}, Nota: {y}")
        print("\n")
        print("\n")

    def mostrar_aprobados(self):
        print("Listado de estudiantes Aprobados")

        for x,y in zip(self.nombres, self.notas) :
            if y >= 7:
                print(f"Estudiante: {x}, Nota: {y} - Aprobado")
        print("\n")
        print("\n")
    
    def finalizar(self):
        print("Programa finalizado")
    

#PROGRAMA PRINCIPAL

lista_de_alumnos = Estudiante() # Instancio mi lista de alumnos
lista_de_alumnos.menu() # Acceder al menu, despues de ahi se maneja todo
