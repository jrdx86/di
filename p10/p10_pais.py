#! /usr/bin/python3
class Pais:
	
	def __init__(self, nombre, poblacion,area):
		#Constructor con parametros
		self.nombre=nombre
		self.poblacion=poblacion
		self.area=area

	def MasGrandeque(self,Pais):
		#Comparamos dos objetos
		return self.poblacion>Pais.poblacion

	def Den_pobl(self):
		#Calculamos la densidad poblacion/area
		return self.poblacion/self.area

España = Pais("España", 46770000, 504645)
Francia = Pais ("Francia", 66030000, 640679)
print(Francia.MasGrandeque(España))
print("Densidad poblacion de España",España.Den_pobl())
print("Densidad poblacion de Francia",Francia.Den_pobl())