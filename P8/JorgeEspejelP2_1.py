 #! /usr/bin/python3
import sys

introduction = input("Digame cuantas palabras tiene la lista")

if introduction.isdigit():
 	index = int (introduction)

 	if index > 0:
 		list = []

 		for i in range(index):
 			word = input ("Digame la palabra "+ str(i+1) +": ")
 			list.append(word)

 		print("La lista creada es:", list)
 		#WITH THIS METHOD .sort() SORTS THE LIST ASCENDING BY DEFAULT
 		list.sort()
 		print("La lista ordenada es:", list)

