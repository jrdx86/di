#! /usr/bin/python3
class Miembro():
# método constructor de objeto.
	def __init__(self, nombre, direccion,dni):
		#constructor con parametros
		self.nombre = nombre 
		self.direccion = direccion
		self.dni=dni

	def __str__(self):
		return str(self.nombre)+","+str(self.direccion)+","+str(self.dni)





class Profesor(Miembro):
	#Constructor que hereada de Miembro()
	def __init__(self, nombre, direccion,dni,n_reg):
		Miembro.__init__(self, nombre, direccion,dni)
		self.n_reg=n_reg

	def __str__(self):
		return str(self.nombre)+","+str(self.direccion)+","+str(self.dni)+","+str(self.n_reg)




class Estudiante(Miembro):
	#Constructor que hereada de Miembro()
	def __init__(self, nombre, direccion,dni,num_estudiante):
		Miembro.__init__(self, nombre, direccion,dni)
		self.num_estudiante=num_estudiante

	def __str__(self):
		return "Nombre: "+str(self.nombre)+" Dirección: "+str(self.direccion)+" DNI: "+str(self.dni)+" Num_estudiante: "+str(self.num_estudiante)



class asigngnatura():
	#Constructor asigngnatura
	def __init__(self,asign,codigo):
		self.asign=asign
		self.codigo=codigo
		#lista profesores
		self.profesores=[]

	def Añade_profesores(self,profesor):
		#Añadimos profesor a lista profesores
		self.profesores.append(profesor)
	
	def Mostrar_profesores(self):
		#Mostramos profesores
		print("Los profesores son: ")
		#Recorremos la lista profesores y vamos mostrando todas los objetos profesor
		for profesor in self.profesores:
			print("*Nombre: ",profesor.nombre," DNI: ",profesor.dni, " Dirección: ",profesor.direccion," n_reg: ",profesor.n_reg)
				
	
		
			


a1=Estudiante("Luisito","calle maravillas","445565699a",22)
p1=Profesor("Luis", "calle lepanto","4488995544j",34)
p2=Profesor("Juan", "calle lepanto","4488994564j",65)
matematicas=asigngnatura("matematicas",56)
print(a1)
matematicas.Añade_profesores(p1)
matematicas.Añade_profesores(p2)
matematicas.Mostrar_profesores()
