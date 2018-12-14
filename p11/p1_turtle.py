#!/bin/python3

import turtle #importamos el modulo turtle
window = turtle.Screen()	#se crea el objeto canvas
cursor = turtle.Turtle()	#se crea el objeto turtle
cursor.left(90)#El cursor gira 90º
cursor.forward(90)#El cursor avanza 90px
cursor.right(90)#El cursor gira 90º
for x in range(1,25):    #Aquí empieza el dibujo
	cursor.left(5)
	cursor.forward(45)
	cursor.left(100)
	cursor.forward(45)
window.exitonclick()	#con un click en la ventana esta se cierra