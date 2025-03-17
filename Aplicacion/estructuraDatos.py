from datetime import datetime

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.campus = []
        self.titulaciones = []

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

    def agregar_titulacion(self, titulacion):
        self.titulaciones.append(titulacion)

    def sumar_titulacion(self, titulacionList):
        if self.titulaciones == []:
            self.setTitulacion(titulacionList)
        else:
            self.titulaciones += titulacionList
    
    def setTitulacion(self, titulacionList):
        self.titulaciones = titulacionList
    
    def getTitulacion(self):
        return list(self.titulaciones)
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def isEmpty(self):
        if not self.campus and not self.titulaciones:
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
    def __init__(self, nombre, edififcio, capacidadClase, capacidadExamen, tipo):
        self.nombre = nombre
        self.edificio = edififcio
        self.capacidadClase = capacidadClase
        self.capacidadExamen = capacidadExamen
        self.tipo = tipo
        self.combinacion = False

    def setNumero(self, nombre):
        self.nombre = nombre

    def getNumero(self):
        return self.nombre

    def setEdificio(self, edificio):
        self.edificio = edificio

    def getEdificio(self):
        return self.edificio
    
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
    
    def getCombinacion(self):
        return self.combinacion

class AulaCombinada(Aula):
    def __init__(self, nombre, edificio, capacidadClase, capacidadExamen, tipo, listaCombinaciones):
        super().__init__(nombre, edificio, capacidadClase, capacidadExamen, tipo)
        self.numCombinaciones = len(listaCombinaciones)
        self.listaAulas = listaCombinaciones
        self.combinacion = True

    def getAulasCombinadas(self):
        return list(self.listaAulas)

    def getCombinacion(self):
        return self.combinacion

    def getNumCombinaciones(self):
        return self.numCombinaciones

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
    def __init__(self, codigo, nombre, titulacion, numAlumnos, curso=None):
        self.codigo = codigo                # Código de la asignatura
        self.nombre = nombre                # Nombre de la asignatura
        self.titulacion = titulacion        # Titulación a la que pertenece
        self.numAlumnos = numAlumnos        # Número de alumnos
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

class Dias:
    def __init__(self):
        self.numDias = "5"
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

    def getNumDias(self):
        return int(self.numDias)
    
    def setDias(self, daisList):
        self.dias = daisList
        self.numDias = str(len(self.dias))
    
    def getDias(self):
        return list(self.dias)

class Horas:
    def __init__(self):
        self.numHoras = "13"
        self.horas = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]

    def getNumHoras(self):
        return int(self.numHoras)
    
    def setHoras(self, horasList):
        self.horas = horasList
        self.numHoras = str(len(self.horas))
    
    def getHoras(self):
        return list(self.horas)

class Actividad:
    def __init__(self, idActividad, idGrupo, asignatura, titulacion, campus, curso, duracion, duracionTotal, tipoAula):
        self.idActividad = idActividad
        self.idGrupo = idGrupo
        self.asignatura = asignatura
        self.titulacion = titulacion
        self.campus = campus
        self.curso = curso
        self.duracion = duracion
        self.duracionTotal = duracionTotal
        self.actividadesHija = []
        self.tipoAula = tipoAula

    def getIdActividad(self):
        return self.idActividad
    
    def setIdActividad(self, idActividad):
        self.idActividad = idActividad

    def getIdGrupo(self):
        return self.idGrupo
    
    def setIdGrupo(self, idGrupo):
        self.idGrupo = idGrupo

    def getAsignatura(self):
        return self.asignatura

    def setAsignatura(self, asignatura):
        self.asignatura = asignatura

    def getTitulacion(self):
        return list(self.titulacion)

    def setTitulacion(self, titulacion):
        self.titulacion = titulacion

    def getCampus(self):
        return self.campus
    
    def setCampus(self, campus):
        self.campus = campus

    def getCurso(self):
        return list(self.curso)

    def setCurso(self, curso):
        self.curso = curso

    def getDuracion(self):
        return self.duracion

    def setDuracion(self, duracion):
        self.duracion = duracion

    def getDuracionTotal(self):
        return self.duracionTotal

    def setDuracionTotal(self, duracionTotal):
        self.duracionTotal = duracionTotal

    def getActividadesHija(self):
        return self.actividadesHija
    
    def setActividadesHija(self, actividadesHija):
        self.actividadesHija = list(actividadesHija)

    def addActividadesHija(self, actividad):
        self.actividadesHija.append(actividad)

    def getTipoAula(self):
        return self.tipoAula

    def setTipoAula(self, tipo):
        self.tipoAula = tipo

    def addRestIndex(self, index):
        self.restIndex = index
    
    def getRestIndex(self):
        return self.restIndex

class AlumnosTitulacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numAlumnos = 0
        self.cursos = []
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def getNumAlumnos(self):
        return self.numAlumnos

    def getCursos(self):
        return list(self.cursos)
    
    def setCursos(self, cursosList):
        self.cursos = cursosList
        self.calcularAulumnos()
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
        self.calcularAulumnos()

    def calcularAulumnos(self):
        for i in self.cursos:
            self.numAlumnos += i.getNumAlumnos()

class AlumnosCurso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numAlumnos = 0
        self.asignaturas = []
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def getNumAlumnos(self):
        return self.numAlumnos

    def getAsignaturas(self):
        return list(self.asignaturas)
    
    def setAsignaturas(self, asignaturaList):
        self.asignaturas = asignaturaList
        self.calcularAulumnos()
    
    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        self.calcularAulumnos()

    def calcularAulumnos(self):
        for i in self.asignaturas:
            self.numAlumnos += i.getNumAlumnos()

class AlumnosAsignatura:
    def __init__(self, nombre, numAlumnos):
        self.nombre = nombre
        self.numAlumnos = numAlumnos
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def getNumAlumnos(self):
        return self.numAlumnos
        
    def setNumAlumnos(self, num):
        self.numAlumnos = num

class Restriccion:
    def __init__(self, nombre, datos, obligatoria, activo):
        self.nombre = nombre
        self.datos = datos
        if obligatoria:
            self.obligatoria = 100
        else:
            self.obligatoria = 60
        self.activo = activo

    def getNombre(self):
        return self.nombre

    def getDatos(self):
        return dict(self.datos)
    
    def setDatos(self, datos):
        self.datos = datos

    def getEstado(self):
        return self.activo

    def getObligatoria(self):
        return self.obligatoria
    
    def isObligatoria(self):
        if self.obligatoria == 100:
            return True
        else:
            return False

    def setObligatoria(self, obligatoria):
        if obligatoria:
            self.obligatoria = 100
        else:
            self.obligatoria = 60

    def activar(self):
        self.activo = True
    
    def desactivar(self):
        self.activo = False
    
    def getActividad(self):
        return self.activo