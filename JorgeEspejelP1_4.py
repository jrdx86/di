#! /usr/bin/python3
import sys

indice = input("Dígame cuantas palabras tiene la lista: ")
index = int(indice)
lista = []

#Compruebo que el numero de palabras sea mayor a 0
if index == 0: 
	print("¡Imposible!")
	sys.exit()

if index > 0:
	for i in range(index):
		nombre=input("Digame la palabra "+ str(i+1) +": ")
		lista.append(nombre)

	print(lista)


#Buscamos coincidencias
buscar = input("Digame la palabra que quiere sustituir: ")
nueva = input("Por la palabra nueva: ")

lista_nueva = []


for i in lista:
     if i != buscar:
         lista_nueva.append(i)
     else:
     	lista_nueva.append(nueva)


respuesta ="La lista es ahora: "
#Concateno la respuesta y la lista
print(respuesta+' '.join(lista_nueva))