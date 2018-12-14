#! /usr/bin/python3
'''
This function compare the array with the parameter introduced
with the for iterates the list and compare the values with the parameter
'''
def isVowel(char):
	c=0
	lista=["a","e","i","o","u","A","E","I","O","U"]

	for i in range(0,len(lista)):
		if (lista[i] == char):
			c=1
			return True
	if (c == 0):
		return False		

print(isVowel(input("introduce una letra: ")))