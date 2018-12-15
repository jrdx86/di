#! /usr/bin/python3

try:
    x = int(input("Introduce un numero entero para obtener sus divisores: "))
except :
    print("Warning: Necesito un numero entero!")#dara error cuando no sea un numero entero

lista = []

for i in range(1,x+1):#recorremos los numeros entre 1 y el numero introducido comparandolos y introduciendo en la lista los divisores
    if x % i == 0:
        lista.append(i)

print(lista)
