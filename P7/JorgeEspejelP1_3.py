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


#Buscamos coincidencias
buscar = input("Digame la palabra que quiere sustituir: ")
nueva = input("Por la palabra nueva: ")




for i in range(len(lista)):
        if lista[i] == buscar:
           lista[i] = nueva


respuesta ="La lista es ahora: "
#Concateno la respuesta y la lista
print(respuesta+' '.join(lista))