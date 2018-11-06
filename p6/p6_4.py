#! /usr/bin/python3


def item_order(l):
	'''
	Busca varias coincidencias dentro de una cadena.
	
	Devuelve las veces que aparecen tres cadenas dentro de una cadena
		.count()
	Utiliza el metodo .count() para contar las coincidencias

	Parámetros:
	l -- string

	imprime: str + int
	'''
	H="hamburguesa"
	E="ensalada"
	A="agua"
	print("***********************")
	print(H,": ", l.count(str(H)))
	print(E,": ", l.count(str(E)))
	print(A,": ", l.count(str(A)))
	print("***********************")

l=input("Orden: ")
item_order(l)