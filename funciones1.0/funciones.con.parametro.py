#funciones con parametros

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
def sumaLista(lista):
    i=0
    suma=0
    for i in range (0,len(lista)):
        suma+=lista[i]
    print("El resultado es:" + str(suma)


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



