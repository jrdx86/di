#! /usr/bin/python3
import sys

indice = input("Dime cuantas palabras tiene la lista: ")

if indice.isdigit():
	index = int (indice)
	cont=0
	if index > 0:
		lista = []

		for i in range(index):
			nombre=input("Digame la palabra "+ str(i+1) +": ")
			lista.append(nombre)
			cont=cont+1
		print(lista)

else:
	print("Imposible!")
	sys.exit()

#Buscamos las palabras a eliminar
buscar = input("Digame la palabra a eliminar : ")


for i in lista:
	if i == buscar:
		lista.remove(i)
	continue
			
print (lista)
