#! /usr/bin/python3
import sys

indice = input("Dime cuantas palabras tiene la lista: ")

#With the method isdigit() we can filter if is a char, a number or both
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


buscar = input("Digame la palabra a eliminar : ")

'''
a=0
while a<cont:
	a=a+1
	for i in lista:
		if i == buscar:
			lista.remove(i)
		'''
# I read the array for remove the letter what i need to remove of the array
for i in lista:
	if i == buscar:
		lista.remove(i)
	continue
				
print (lista)
