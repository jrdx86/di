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
		print("La primera lista es: ", lista)

else:
	print("Imposible!")
	sys.exit()


#We create the second list
indice2 = input("Dígame cuantas palabras tiene la lista: ")
index2 = int(indice)
lista2 = []

if indice2.isdigit():
	index2= int (indice2)
	if index2 > 0:
		lista2 = []

		for i in range(index2):
			nombre2=input("Digame la palabra "+ str(i+1) +": ")
			lista2.append(nombre2)
		print("La segunda lista es: ",lista2)

else:
	print("Imposible!")
	sys.exit()


#We compare for coincidences
comun = []
for i in lista:
    if i in lista2:
        comun.append(i)
    continue
print("Palabras que aparecen en las dos listas:", comun)

#We compare and the values has only in the first list, we added to primera list 
primeraSolo = []
for i in lista:
    if i not in lista2:
        primeraSolo.append(i)
    continue
print("Palabras que sólo aparecen en la primera lista:", primeraSolo)

#We compare and the values has only in the second list, we added to segunda list 
segundaSolo= []
for i in lista2:
    if i not in lista:
        segundaSolo.append(i)
    continue
print("Palabras que sólo aparecen en la segunda lista:", segundaSolo)


todo = comun + primeraSolo + segundaSolo

print("Todas las palabras", todo)