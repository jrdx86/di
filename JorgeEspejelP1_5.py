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

	print(lista2)

#Comparamos las listas y si coinciden se borran
for i in lista:
     if i in lista2:
         lista.remove(i)


respuesta ="La lista es ahora: "
#Concateno la respuesta y la lista
print(respuesta+' '.join(lista))