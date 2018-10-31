#! /usr/bin/python3

u = input("Introduce el valor de u: ")
termn = input("Introduce el valor de termino: ")

if u.isdigit() and termn.isdigit():
	u = int(u)
	termn = int(termn)
	list=[u]

	for i in range(1,termn):
		if u%2!=0:
			r=(3*u)+1
			u=r
			list.append(r)
		else:
			r=int(u/2)
			u=r
			list.append(r)
	print(list)
else:
	print("Solo acepto numeros: ")


		
