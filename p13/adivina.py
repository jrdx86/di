#! /usr/bin/python3
from random import randint

y = randint(1,10)#Generemos un numero entre 1 y 10

numero = int(input("Introduce un numero para adivinar entre 1 y 10: "))
pedir(numero)

def pedir(numero):
    
    try:
        if numero>10 or numero<1:
            print("Fuera de rango")
            return pedir(numero)
                           
    except:
            print("Warning: Necesito un numero entero!")#dara error cuando no sea un numero entero        
        


    print("Lo adivinaste era",y)#cuando salga el bucle nos avisara diciendo el numero

