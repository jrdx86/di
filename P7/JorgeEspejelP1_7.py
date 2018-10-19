#! /usr/bin/python3
import sys

indice = input("Dime cuantas palabras tiene la lista: ")

#With the method isdigit() we can filter if is a char, a number or both
if indice.isdigit():
	index = int (indice)
	if index > 0:
		lista = []

		for i in range(index):
			nombre=input("Digame la palabra "+ str(i+1) +": ")
			lista.append(nombre)
		print("La lista creada es",lista)

else:
	print("Imposible!")
	sys.exit()

#We start to read through the array in the reverse way,and we dont delete the last
for i in range(len(lista)-1, -1, -1):
     if lista[i] in lista[:i]:
        del(lista[i])

print("La lista sin repeticiones: ",lista)