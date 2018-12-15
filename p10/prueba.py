#! /usr/bin/python3

class Miembro():
# método constructor de objeto.
	def __init__(self, nombre, direccion,dni):
		#constructor con parametros
		self.nombre = nombre 
		self.direccion = direccion
		self.dni=dni
    
    def devuelve(self,object):
        
        return self.dni

   

P=Miembro("juan",["lepanto","luis"],2222)

print(P.nombre)
print(P.direccion)
Miembro.devuelve(P)