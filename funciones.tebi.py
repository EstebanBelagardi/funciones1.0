#funciones sin parametro
#1
def advertencia():
    print("No dejar los dispositivos conectados a la red electrica, Gracias")

advertencia()
#2
def edades():
    print("Prohibida su venta a menores de 18 años")

edades()
#3
def lunes():
    print("Curricula del dia Lunes: 8.30hs a 11.25hs Sistema Operativo \n 11:25hs a 13.25hs Programacion 2")

lunes()
#4
def martes():
    print("Curricula del dia Martes: 8.30hs a 12.05hs Modelado de Sistema \n 12.05hs a 13.25hs Practico Profecionalizantes 1")

martes()
#5
def miercoles():
    print("Curricula del dia Miercoles: 8.30hs a 11.25hs Programacion 2 \n 11:25hs a 13.25hs Practico Profecionalizantes 1")

miercoles()
#6
def jueves():
    print("Curricula del dia Jueves: 8.30hs a 10:30hs Matematicas Aplicadas \n 10:45hs a 12:45hs Base de Datos")

jueves()
#7
def viernes():
    print("Curricula del dia Viernes: 8.30hs a 10:30hs Practico Profecionalizantes 1")

viernes()

#funciones con 1 parametros

#1
def saludo (nombre):
    print('¡Hola ' + nombre +'!')
    return

saludo('Mario')

#2
def impuesto(neto, vat=21):
       return neto + neto*vat/100

print(impuesto(1000))

#3
def esPrimo(numero):
    for n in range(2, numero):
        if (numero % n == 0):
            return False

    return True

print(esPrimo(29))

#4



#funciones con parametros

#1
def notas(lista):
    return sum(lista)/len(lista)

print(notas([8, 9, 7, 10, 5]))

#2
def entre(num1, num2):
    if (num1 > num2):
 
        aux = num1
        num1 = num2
        num2 = aux
 
    for i in range(num1+1, num2):
        print(i)
 
entre(5,10)

#3
def cuadrado(x):
    return x ** 2

def raiz_cuadrada(x):
    return x ** 0.5

def operar(func, *args):
    for n in args:
        print(func(n))

operar(cuadrado, 3, 4, 5)

operar(raiz_cuadrada, 5, 6, 7)

#4
def triangulo_superf(base,altura):
    return (base*altura)/2

triangulo_superf(20,7)

#5 

frase=""
def contar_palabras(frase):
    cont = 0
    vocales = ['a','e','i','o','u']
    if len(frase)<20:
        for i in range(len(frase)):
            if frase[i] in vocales:
                cont = cont +1
    else:
        return 'frase demasiado larga'
    return cont
contar_palabras(frase)



