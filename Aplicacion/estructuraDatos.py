from datetime import datetime

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.campus = []
        self.escuelas = []

    def agregar_campus(self, campus):
        self.campus.append(campus)

    def sumar_campus(self, campusList):
        if self.campus == []:
            self.setCampus(campusList)
        else:
            self.campus += campusList

    def setCampus(self, campusList):
        self.campus = campusList
    
    def getCampus(self):
        return list(self.campus)

    def agregar_escuela(self, escuela):
        self.escuelas.append(escuela)

    def sumar_escuelas(self, escuelaList):
        if self.escuelas == []:
            self.setEscuelas(escuelaList)
        else:
            self.escuelas += escuelaList
    
    def setEscuelas(self, escuelasList):
        self.escuelas = escuelasList
    
    def getEscuelas(self):
        return list(self.escuelas)
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def isEmpty(self):
        if not self.campus and not self.escuelas:
            return True
        else:
            return False

class Campus:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificos = []

    def agregar_edificio(self, edificio):
        self.edificos.append(edificio)

    def setEdificios(self, edificioList):
        self.edificos = edificioList
    
    def getEdificios(self):
        return list(self.edificos)

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aulas = []

    def agregar_aula(self, aula):
        self.aulas.append(aula)

    def setAulas(self, aulaList):
        self.aula = aulaList

    def getAulas(self):
        return list(self.aulas)

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

class Aula:
    def __init__(self, numero, capacidadClase, capacidadExamen, tipo):
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
    def __init__(self, nombre):
        self.nombre = nombre            # Nombre de la Escuela
        self.titulaciones = []          # Lista de titulaciones que pertenecen a la escuela (Inicialmente vacia)
    
    def agregar_titulacion(self, titulacion):
        self.titulaciones.append(titulacion)
    
    def setTitulaciones(self, titulacionesList):
        self.titulaciones = titulacionesList
    
    def getTitulaciones(self):
        return list(self.titulaciones)

    def getNombre(self):
        return self.nombre

    def mostrarEscuela(self):
        print(f"Escuela: {self.nombre}")
        titulaciones = self.titulaciones
        for titulacion in titulaciones:
            print(f"{titulacion.getCodigo()}, {titulacion.getNombre()}")
            asignaturas = titulacion.getAsignaturas()
            for asignatura in asignaturas:
                print(f"    {asignatura.getCodigo()},  {asignatura.getNombre()}")

class Titulacion:
    def __init__(self, codigo, nombre, campus=None):
        self.codigo = codigo            # Código Titulación
        self.nombre = nombre            # Nombre Titulación
        self.campus = campus            # Campus (opcional)
        self.asignaturas = []           # Lista de asignaturas de la titulacion (Inicialmente vacia)

    # Getters y Setters para 'codigo'
    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    # Getters y Setters para 'nombre'
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    # Getters y Setters para 'campus'
    def getCampus(self):
        return self.campus

    def setCampus(self, campus):
        self.campus = campus

    # Métodos para asignaturas
    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
    
    def setAsignaturas(self, asignaturaList):
        self.asignaturas = asignaturaList

    def getAsignaturas(self):
        return list(self.asignaturas)
    
class Asignatura:
    def __init__(self, codigo, nombre, titulacion, numAlumnos, profesor=None, curso=None):
        self.codigo = codigo                # Código de la asignatura
        self.nombre = nombre                # Nombre de la asignatura
        self.titulacion = titulacion        # Titulación a la que pertenece
        self.numAlumnos = numAlumnos        # Número de alumnos
        self.profesor = profesor            # Profesor responsable de la asignatura (opcional)
        self.curso = curso                  # Curso de la asignatura (opcional)
        self.asignaturas_hijas = []         # Lista de asignaturas hijas (inicialmente vacía)

    # Getters y Setters para 'codigo'
    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    # Getters y Setters para 'nombre'
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    # Getters y Setters para 'titulacion'
    def getTitulacion(self):
        return self.titulacion

    def setTitulacion(self, titulacion):
        self.titulacion = titulacion

    # Getters y Setters para 'numAlumnos'
    def getNumAlumnos(self):
        return self.numAlumnos

    def setNumAlumnos(self, numAlumnos):
        self.numAlumnos = numAlumnos

    # Getters y Setters para 'profesor'
    def getProfesor(self):
        return self.profesor

    def setProfesor(self, profesor):
        self.profesor = profesor

    # Getters y Setters para 'curso'
    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso

    # Métodos para asignaturas hijas
    def agregar_hija(self, asignatura_hija):
        self.asignaturas_hijas.append(asignatura_hija)

    def setAsignaturas_hijas(self, asignaturasHijasList):
        self.asignaturas_hijas = asignaturasHijasList
    
    def getAsignaturas_hijas(self):
        return list(self.asignaturas_hijas)

class Curso:
    def __init__(self):
        self.nombre = f"{datetime.now().year}-{datetime.now().year + 1}"
        self.gurpos = []
        self.numAlumnos = 0

    def isEmpty(self):
        empty = False
        if not self.gurpos:
            return True
        return empty

    def calcularAulumnos(self):
        self.numAlumnos = 0
        for grupo in self.gurpos:
            self.numAlumnos += grupo.getNumAlumnos()

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNumAlumnos(self):
        return self.numAlumnos
    
    def setNumAlumnos(self, numAlumnos):
        self.numAlumnos = numAlumnos
    
    def agregar_gurpo(grupo):
        self.gurpos.append(grupo)

    def getGrupos(self):
        return self.gurpos
    
    def setGrupos(self, gruposList):
        self.gurpos = gruposList
        self.calcularAulumnos()

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numAlumnos = 0

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNumAlumnos(self):
        return self.numAlumnos
    
    def setNumAlumnos(self, numAlumnos):
        self.numAlumnos = numAlumnos
    
    def sumarAlumnos(self, numero):
        self.numAlumnos += numero

class Dias:
    def __init__(self):
        self.numDias = "7"
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    def añadirDia(self, dia):
        self.dias.append(dia)
        self.numDias = str(len(self.dias))
    
    def quitarUltimoDia(self):
        self.dias.pop()
        self.numDias -= 1

    def getNumDias(self):
        return int(self.numDias)
    
    def setDias(self, daisList):
        self.dias = daisList
        self.numDias = str(len(self.dias))
    
    def getDias(self):
        return list(self.dias)

class Horas:
    def __init__(self):
        self.numHoras = "7"
        self.horas = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]

    def añadirHoras(self, hora):
        self.horas.append(hora)
        self.numHoras = str(len(self.horas))
    
    def quitarUltimaHora(self):
        self.horas.pop()
        self.numHoras -= 1

    def getNumHoras(self):
        return int(self.numHoras)
    
    def setHoras(self, horasList):
        self.horas = horasList
        self.numHoras = str(len(self.horas))
    
    def getHoras(self):
        return list(self.horas)
