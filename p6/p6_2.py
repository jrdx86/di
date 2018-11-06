#! /usr/bin/python3
import sys

'''
We make a loop for make the divisions and later add the results to the lists
for compare and add the matches for later show the biggest number
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