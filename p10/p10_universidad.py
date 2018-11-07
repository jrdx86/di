class miembro():
# método constructor de objeto.
	def __init__(self, nombre, direccion,dni):
		self.nombre = nombre 
		self.direccion = direccion
		self.dni=dni
	def __str__(self):
		return str(self.nombre)+","+str(self.direccion)+","+str(self.dni)



class profesor(miembro):
	def __init__(self, nombre, direccion,dni,n_reg):
		miembro.__init__(self, nombre, direccion,dni)
		self.n_reg=n_reg

	def __str__(self):
		return str(self.nombre)+","+str(self.direccion)+","+str(self.dni)+","+str(self.n_reg)
	

class estudiante(miembro):
	def __init__(self, nombre, direccion,dni,num_estudiante):
		miembro.__init__(self, nombre, direccion,dni)
		self.num_estudiante=num_estudiante

	def __str__(self):
		return str(self.nombre)+","+str(self.direccion)+","+str(self.dni)+","+str(self.num_estudiante)

class asignatura():
	nombre=""
	codAsignatura=""