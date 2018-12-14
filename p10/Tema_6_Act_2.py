'''
Asumo que una asignatura solo puede ser impartida por un profesor.
La asociación de asignaturas a alumnos determina los profesores de
cada alumno.

En un planteamiento más ámplio establecería una relación M:M entre
profesores y asignaturas. Agregaría esta relación y establecería una
relacion M:M entre Alumnos y dicha agregación. No creo que sea un
planteamiento de esta complejidad lo que se persigue con el ejercicio
por lo que opto por el plantemiento inicial.
'''
class Asignatura():
    # método constructor de objeto.
    def __init__(self, nombre, codigo):
        self.nombre = nombre # inicializa el nombre
        self.codigo = codigo # inicializa el código
class Miembro():
    # método constructor de objeto.
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre # inicializa el nombre
        self.edad = edad # inicializa la edad
        self.dni = dni # inicializa el dni

class Profesor(Miembro):
    # método constructor de objeto.
    def __init__(self, nombre, edad, dni, nreg):
        Miembro.__init__(self, nombre, edad, dni)
        self.nreg = nreg # inicializa el número de registro
        self.docencia = set()
    def agrega_docencia(self, asignatura):
        self.docencia.add(asignatura)
    def imprime_docencia(self):
        for a in self.docencia:
            print(a.nombre)
        
class Estudiante(Miembro):
    # método constructor de objeto.
    def __init__(self, nombre, edad, dni, nest):
        Miembro.__init__(self, nombre, edad, dni)
        self.nest = nest # inicializa el número de estudiante
        self.asignaturas = set()
    def agrega_asignatura (self, asignatura):
        self.asignaturas.add(asignatura)
    def imprime_asignaturas(self):
        for a in self.asignaturas:
            print(a.nombre)

asig1 = Asignatura("Matetemáticas",5)
asig2 = Asignatura("Álgebra",7)
prof1 = Profesor("Luis",50,34567,5001)
prof1.agrega_docencia(asig1)
prof1.agrega_docencia(asig2)
est1 = Estudiante("Luisito", 20, 56678, 1001)
est1.agrega_asignatura(asig1)
est1.agrega_asignatura(asig2)
print("Docencia del profesor ",prof1.nombre)
prof1.imprime_docencia()
print("Asignaturas del alumno",est1.nombre)
est1.imprime_asignaturas()
