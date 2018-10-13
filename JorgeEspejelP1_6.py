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

lista2 = []
lista.reverse() 

#copio una lista a otra
lista2 = lista.copy()	

print(lista2)