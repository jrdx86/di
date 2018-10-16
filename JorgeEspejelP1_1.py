#! /usr/bin/python3

indice = input("Dime cuantas palabras tiene la lista: ")
index = int(indice)a
lista = []

if index > 0:
	for i in range(index):
		nombre=input("Digame la palabra "+ str(i+1) +": ")
		lista.append(nombre)
	

	print(lista)
else:
	print("¡Imposible!")

