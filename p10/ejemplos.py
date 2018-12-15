#! /usr/bin/python3
class autores:	
	def __init__(self, nombre, poblacion,area):
		#Constructor con parametros
		self.nombre=nombre
		self.poblacion=poblacion
		self.area=area
	
	def __str__(self):
		return "soy {nombre} y estoy en {poblacion} en {area}". format(nombre = self.nombre, area = self.area, poblacion=self.poblacion)

	def MasGrandeque(self):
		return len(self.poblacion)
	

P = autores("Juan", ["Patato", "juanolo"],100)
print(P.__dict__)
print("Numero de autores: ",P.MasGrandeque())
print(P.area)
print(P)