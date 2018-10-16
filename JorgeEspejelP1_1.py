indice = input("Dime cuantas palabras tiene la lista: ")

if indice.isdigit():
	index = int (indice)
	if index > 0:
		lista = []

		for i in range(index):
			nombre=input("Digame la palabra "+ str(i+1) +": ")
			lista.append(nombre)
		print(lista)

else:
	print("Imposible")