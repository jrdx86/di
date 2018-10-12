import sys

indice = input("Dime cuantas palabras tiene la lista: ")
index = int(indice)
lista = []

#Compruebo que el numero de palabras sea mayor a 0
if index == 0: 
	print("Imposible!")
	sys.exit()

if index > 0:
	for i in range(index):
		nombre=input("Digame la palabra "+ str(i+1) +": ")
		lista.append(nombre)
	

	print(lista)

#Pido la palabra a buscar y recorro la lista con un contador sumo las coincidencias
buscar = input("Digame la palabra a buscar: ")
contador = 0

for i in lista:
	if i == buscar:
		contador+=  1
	
if contador > 0:
	npal = str(contador)		
	print("La palabra " + buscar + " aparece " + npal +" veces")
else:
	print("La palabra "+buscar+" no existe")
