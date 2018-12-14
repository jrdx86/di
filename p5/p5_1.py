#! /usr/bin/python3
'''
Here compare the variables and print a diferent results
'''
varA="Mañana"
varB="Hoy"

if (type(varA) == str ):
	print("Cadena involucrada") 
elif (type(varB) == str):
	print("Cadena involucrada")

if (varA>varB):
	print("Grande")

if (varA==varB):
	print("Igual")

if (varA<varB):
	print("Pequeño")