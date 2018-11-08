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
	def __init__(self,asi,codigo):
		self.asi=asi
		self.codigo=codigo
		self.profesores=[]

	def añade_profesores(self,profesor):
		self.profesores.append(profesor)
	
	def mostrar_profesores(self):
		print("Los profesores son: ")
		for profesor in self.profesores:
			print("*Nombre: ",profesor.nombre," DNI: ",profesor.dni, " Edad: ",profesor.direccion," n_reg: ",profesor.n_reg)
				
	def __str__(self):
		return "Nombre: "+str(self.asi)+" CódAsignat.:"+str(self.codigo)
		
			



p1=profesor("Luis", "calle lepanto",4488995544j,34)
p2=profesor("Juan", "calle lepanto",4488994564j,65)
matematicas=asignatura("matematicas",56)
print(matematicas)
matematicas.añade_profesores(p1)
matematicas.añade_profesores(p2)
matematicas.mostrar_profesores()
