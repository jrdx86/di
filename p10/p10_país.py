class Pais:
	def __init__(self, nombre, poblacion,area):
		self.nombre=nombre
		self.poblacion=poblacion
		self.area=area

	def masGrandeque(self,Pais):
		return self.poblacion>Pais.poblacion

	def den_pobl(self):
		return self.poblacion/self.area

España = Pais("España", 46770000, 504645)
Francia = Pais ("Francia", 66030000, 640679)
print(Francia.masGrandeque(España))
print("Densidad poblacion de España",España.den_pobl())
print("Densidad poblacion de Francia",Francia.den_pobl())