# Method Resolution Order / Metodo de Resolucion de Orden
# Define el orden de las herencias.

# Por jerarquia, los metodos de la clase hija ganan a los metodos heredados, por lo cual si se llaman igual se sobreescriben
# Demostrando esa definicion:
class A:
    def hablar(self):
        print("Hablo desde A")

class B(A):
    def hablar(self):
        print("Hablo desde B")

class C(A):
    def hablar(self):
        print("Hablo desde C")

class D(B,C):
    def hablar(self):
        print("Hablo desde D")


testA = A()
testA.hablar() # Hablo desde A

testB = B()
testB.hablar() # Hablo desde B

testC = C()
testC.hablar() # Hablo desde C

testD = D()
testD.hablar() # Hablo desde D

#############
# Cuando la primera clase no tiene el metodo buscado
class A:
    def hablar(self):
        print("Hablo desde A")

class B(A):
    def hablar(self):
        print("Hablo desde B")

class C(A):
    def hablar(self):
        print("Hablo desde C")

class D(B,C): # Cuando heredo dos clases, la primera en ser definida tiene prioridad. testD.hablar() imprime "Hablo desde B"
    pass


testA = A()
testA.hablar() # Hablo desde A

testB = B()
testB.hablar() # Hablo desde B

testC = C()
testC.hablar() # Hablo desde C

testD = D()
testD.hablar() # Hablo desde B


# Que pasa si ninguno de las 2 clases tiene el metodo, ahí consulta al padre de la primera clase definida.
# Siempre barre todo el camino de la primera clase, preguntando a padres y padres de padres. Si esa rama no trae el metodo, recien analiza el arbol de la segunda clase.

# B y C dependiendo del mismo padre
class A:
    def hablar(self):
        print("Hablo desde A")

class B(A):
    pass

class C(A):
    pass

class D(B,C): # Si ninguna clase de este nivel tiene el metodo, pregunta un nivel mas arriba,primero preguntando mas arriba de B. testD.hablar() imprime "Hablo desde A"
    pass


testA = A()
testA.hablar() # Hablo desde A

testB = B()
testB.hablar() # Hablo desde A

testC = C()
testC.hablar() # Hablo desde A

testD = D()
testD.hablar() # Hablo desde A

# B y C dependiendo de padres diferentes V1
class A:
    def hablar(self):
        print("Hablo desde A")

class Z:
    def hablar(self):
        print("Hablo desde Z")

class B(A):
    pass

class C(Z):
    def hablar(self):
        print("Hablo desde C")

class D(B,C): # Si ninguna clase de este nivel tiene el metodo, pregunta un nivel mas arriba,primero preguntando mas arriba de B. testD.hablar() imprime "Hablo desde A"
    pass


testA = A()
testA.hablar() # Hablo desde A

testB = B()
testB.hablar() # Hablo desde A

testC = C()
testC.hablar() # Hablo desde C

testD = D()
testD.hablar() # Hablo desde A, No imprime Z . Ya que primero analizo el arbol de B

# B y C dependiendo de padres diferentes V2
class A:
    pass

class Z:
    def hablar(self):
        print("Hablo desde Z")

class B(A):
    pass

class C(Z):
    pass

class D(B,C): # Si ninguna clase de este nivel tiene el metodo, pregunta un nivel mas arriba,primero preguntando mas arriba de B, como no obtiene lo que busca pasa al arbol de C. testD.hablar() imprime "Hablo desde Z"
    pass



testC = C()
testC.hablar() # Hablo desde Z

testD = D()
testD.hablar() # Hablo desde Z, Agoto el arbol de B y fue por el arbol de C

# Con la funcion "mro()" puedo ver el camino MRO de cada clase
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class '__main__.Z'>, <class 'object'>]