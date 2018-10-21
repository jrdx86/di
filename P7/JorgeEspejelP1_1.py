#! /usr/bin/python3
import sys

indice = input("Dime cuantas palabras tiene la lista: ")

#With the method isdigit() we can filter if is a char, a number or both
if indice.isdigit():
	print("Imposible!")
	sys.exit()

else:

	introduction = input("Digame cuantas palabras tiene la lista")
	
	if introduction.isdigit():
		print("Imposible!")
		sys.exit()
 	
	else:
		number = int (introduction)

	 	if number > 0:
	 		list = []
	 		for i in range(index):
	 			if n%i = 0 and i<=n:
	 				list.append(i)
	 	print("lala",list)
