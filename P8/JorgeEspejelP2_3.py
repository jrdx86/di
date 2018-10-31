 #! /usr/bin/python3
import sys

introduction = input("Digame un numero mayor que 0: ")

#WITH THE METHOD .isnumeric() IF ALL CHARACTERS IN A STRING ARE NUMERIC CHARACTERS 
if introduction.isnumeric():
 	index = int (introduction)

 	if index > 0:
 		list = []
 		i=1
 		
 		for i in range(2,index+1):
 			if (i%2!=0 or i==2) and (i%3!=0 or i==3) and (i%5!=0 or i==5) and (i%7!=0 or i==7):
 				list.append(i)
 				

 		print("Los numeros primos son: ", list)
 	else:
 		print("----No es primo----\n---------------Adios!-------------------")
 		sys.exit()

else:
	print("Imposible!")
	sys.exit()
