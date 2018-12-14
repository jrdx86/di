#! /usr/bin/python3
'''
We make two for's, the first for read "lista", and the second compare the 
string with the element where the first for is in, when we have a match
c is our counting, increases in 1
'''
def isVowel(char):
	c=0
	lista=["a","e","i","o","u","A","E","I","O","U"]

	for i in lista:
		for j in char:
			if (i == j):
				c=c+1

	print("Numero de vocales: ", c)


					

isVowel(input("introduce una letra: "))