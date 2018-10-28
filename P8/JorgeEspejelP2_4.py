#! /usr/bin/python3

a = input("Introduce el valor de a: ")
b = input("Introduce el valor de b: ")
u = input("Introduce el valor de u: ")
termn = input("Introduce el valor de termino: ")


if a.isdigit() and b.isdigit() and u.isdigit() and termn.isdigit():
	#HERE MAKE A CAST STRING TO NUMBERS
	a = int(a)
	b = int(b)
	u = int(u)
	termn = int(termn)

	#HERE WE APPLIED THE FORMULA
	list = [u]
	for i in range(1,termn):
		r =(a*u)-1
		u = r
		list.append(r)

	print(list)

else:
	print("imposible")