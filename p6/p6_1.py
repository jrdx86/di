#! /usr/bin/python3
import sys

def iterPower(b, e):
	'''
	Calcula el exponencial.
	Devuelve la multiplicacion de la b por un numero e de veces

		ans = ans * b

		Parametros:
		b -- int o float
		e -- int >=0

		returns: int or float >= 0
	'''
	ans=1;
	if e==0:
		ans=1;

	else:
		while e>=1:
			ans*=b;
			e-=1;

	return ans
    
try:
	b = float (input("Introduce la base: "))
except:
	print("Ops! necesito un numero almenos float")
	sys.exit()

try:
	e = int (input("Introduce el exponente: "))
except:
	print("Ops! necesito un numero entero")
	sys.exit()


print(iterPower(b,e))