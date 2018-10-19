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


#I ask for a word 
buscar = input("Digame la palabra a buscar: ")
contador = 0

#I created a counter for count the coincidences
for i in lista:
	if i == buscar:
		contador+=  1
	
if contador > 0:
	npal = str(contador)		
	print("La palabra " + buscar + " aparece " + npal +" veces")
else:
	print("La palabra "+buscar+" no existe")
