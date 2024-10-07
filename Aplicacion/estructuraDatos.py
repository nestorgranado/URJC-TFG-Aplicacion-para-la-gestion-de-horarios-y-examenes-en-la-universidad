class Universidad:
    def __init__(self):
        self.campus = []
        self.escuelas = []
    def addCampus(self, campus):
        self.campus.append(campus)

    def addEscuela(self, escuela):
        self.escuelas.append(escuela)
    
    def getCampus(self):
        return self.campus
    
    def getEscuelas(self):
        return self.escuelas

class Campus:
    def __init__(self):
        self.nombre = ""
        self.edificos = []

    def addEdificio(self, edificio):
        self.edificos.append(edificio)

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def getEdificios(self):
        return self.edificos

class Edificio:
    def __init__(self):
        self.nombre = ""
        self.aulas = []

    def addAula(self, aula):
        self.aulas.append(aula)

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def getAulas(self):
        return self.aulas

class Aula:
    def __init__(self):
        self.numero = ""
        self.capacidadClase = ""
        self.capacidadExamen = ""
        self.tipo = ""
    
    def fill(self, numero, capacidadClase, capacidadExamen, tipo):
        self.numero = numero
        self.capacidadClase = capacidadClase
        self.capacidadExamen = capacidadExamen
        self.tipo = tipo

    def setNumero(self, numero):
        self.numero = numero

    def getNumero(self):
        return self.numero
    
    def setCapacidadClase(self, capacidadClase):
        self.capacidadClase = capacidadClase
    
    def getCapacidadClase(self):
        return self.capacidadClase
    
    def setCapacidadExamen(self, capacidadExamen):
        self.capacidadExamen = capacidadExamen
    
    def getCapacidadExamen(self):
        return self.capacidadExamen
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getTipo(self):
        return self.tipo

class Escuela:
    def __init__(self):
        self.nombre = ""
        self.titulaciones = []

    def addTitulacion(self, titulacion):
        self.titulaciones.append(titulacion)

    def getTitulaciones(self):
        return self.titulaciones
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre

class Titulacion:
    def __init__(self):
        self.nombre = ""
        self.campus = ""
        self.cursos = []
    
    def addCurso(self, curso):
        self.cursos.append(curso)
    
    def getCurso(self):
        return self.cursos
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setCampus(self, campus):
        self.campus = campus
    
    def getCampus(self):
        return self.campus
    
class Curso:
    def __init__(self):
        self.año = ""
        self.creditos = ""
        self.asignaturas = []
    
    def addAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def getAsignaturas(self):
        return self.asignaturas
    
    def setAño(self, año):
        self.año = año

    def getAño(self):
        return self.año
    
    def setCreditos(self, creditos):
        self.creditos = creditos

    def getCreditos(self):
        return self.creditos
    
class Asignatura:
    def __init__(self):
        self.nombre = ""
        self.creditos = ""
        self.alumnos = ""
        self.profesor = ""

    def fill(self, nombre, creditos, alumnos, profesor):
        self.nombre = nombre
        self.creditos = creditos
        self.alumnos = alumnos
        self.profesor = profesor
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setCreditos(self, creditos):
        self.creditos = creditos
    
    def getCreditos(self):
        return self.creditos
    
    def setAlumnos(self, alumnos):
        self.alumnos = alumnos
    
    def getAlumnos(self):
        return self.alumnos
    
    def setProfesor(self, profesor):
        self.profesor = profesor
    
    def getProfesor(self):
        return self.profesor