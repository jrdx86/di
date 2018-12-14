#! /usr/bin/python3
'''
This function compare the array with the parameter int
'''
def isVowel2(char):
	lista=["a","e","i","o","u","A","E","I","O","U"]

	if char in lista:
		return True
	else:
		return False
		

print(isVowel2(input("introduce una letra: ")))
