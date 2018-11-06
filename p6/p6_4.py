#! /usr/bin/python3
'''
I create diferents strings for search in the pedido string
and i count the matches with .count()
'''

def item_order(l):
	H="hamburguesa"
	E="ensalada"
	A="agua"

	print("Pedido realizado:")
	print("Hamburguesa: ", l.count(str(H)))
	print("Ensalada: ", l.count(str(E)))
	print("Agua: ", l.count(str(A)))

l=input("Pedido: ")
item_order(l)