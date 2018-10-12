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


#Buscamos las palabras a eliminar, si esta no coincide con la que buscamos ira a lista_nueva
buscar = input("Digame la palabra a sustituir : ")

lista_nueva = []



for i in lista:
     if i != buscar:
         lista_nueva.append(i)


respuesta ="La lista es ahora: "
#Concateno la respuesta y la lista
print(respuesta+' '.join(lista_nueva))