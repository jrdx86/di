#! /usr/bin/python3
import sys

'''
I make a condition if the exp is 0 the result is 0 but if the exp is more
I make a bucle what make a consecutive multiplications the loop will be substracting
1 to the variable exp
'''
def iterPower(base, exp):
	ans=1;
	if exp==0:
		ans=1;

	else:
		while exp>=1:
			ans*=base;
			exp-=1;

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