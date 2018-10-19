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
		print(lista)

else:
	print("Imposible!")
	sys.exit()



indice2 = input("Dígame cuantas palabras tiene la lista: ")
index2 = int(indice)
lista2 = []

if index2 == 0: 
	print("¡Imposible!")
	sys.exit()

if index2 > 0:
	for i in range(index):
		nombre2=input("Digame la palabra "+ str(i+1) +": ")
		lista2.append(nombre2)

	print("La lista de palabras a eliminar es: ",lista2)

#We compare both lists and remove the coincidences of both
for i in lista:
     if i in lista2:
         lista.remove(i)




print("La lista primera lista es ahora: ",lista)