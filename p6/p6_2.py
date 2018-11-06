#! /usr/bin/python3
import sys


def gcdIter(a,b):
	'''
	Máximo común divisor.
	Nos dice cual es el máximo común divisor de dos numeros
		a%x == 0
		b%x == 0
	Parámetros:
	a -- numero entero
	b -- número entero

	'''
	
	if (a<b):
		c=a
	else:
		c=b

	for x in range(c,0,-1):
		if a%x == 0 and b%x == 0:
			print("mayor divisor: ", x)
			break
			
	


try:
	a = int (input("Introduce un numero: "))

except:
	print("Ops! necesito un numero entero")
	sys.exit()
try:
	b = int (input("Introduce un numero: "))

except:
	print("Ops! necesito un numero entero")
	sys.exit()

gcdIter(a,b)







'''
def gcdIter(a,b):
	lista=[]
	lista2=[]
	listaFinal=[]
	c=0
	c=a
	while a>=1:
		if (c%a==0):
			lista.append(a)
		a-=1

	d=0
	d=b
	while b>=1:
		if (d%b==0):
			lista2.append(b)
		b-=1

	for i in lista:
		for j in lista2:
			if i==j:
				listaFinal.append(i)

	print(listaFinal[:1])
try:
	a = int (input("Introduce un numero: "))

except:
	print("Ops! necesito un numero entero")
	sys.exit()
try:
	b = int (input("Introduce un numero: "))

except:
	print("Ops! necesito un numero entero")
	sys.exit()

gcdIter(a,b)
'''