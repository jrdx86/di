#! /usr/bin/python3
import calendar
'''
Con calendar.weekday te devuelve un numero entero del día que es la fecha introducida
que lo usare para sacar el día de la lista semana
Lista:
	semana 
Variable:
	día
'''


semana = ["lunes",
			"martes",
			"miércoles",
			"jueves",
			"viernes",
			"sábado",
			"domingo"]

dia = calendar.weekday(2020,2,19)

print("El 19 de febrero de 2020 es ",semana[dia])