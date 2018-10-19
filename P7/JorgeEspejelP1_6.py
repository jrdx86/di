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
		

else:
	print("Imposible!")
	sys.exit()

#We reverse the list with this method
lista.reverse() 

#We copy the two list adding the method copy for create a new array 
lista2 = lista.copy()	

print("La lista creada es: ",lista)
print("La lista inversa es: ",lista2)