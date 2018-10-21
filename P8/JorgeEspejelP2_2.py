 #! /usr/bin/python3
import sys

introduction = input("Digame un numero mayor que 0: ")

#WITH THE METHOD .isnumeric() IF ALL CHARACTERS IN A STRING ARE NUMERIC CHARACTERS 
if introduction.isnumeric():
 	index = int (introduction)

 	if index > 0:
 		list = []
 		cont = 0

 		for i in range(index):
 			i+=1
 			#WITH THIS OPERATION WE FIND THE DIVIDERS
 			if index % i == 0:
 				list.append(i)
 				cont+=1

 		print("El numero "+str(introduction)+" tiene "+str(cont)+" divisores:", list)
 	else:
 		print("----Necesito un numero mayor que cero----\n---------------Adios!-------------------")
 		sys.exit()

else:
	print("Imposible!")
	sys.exit()