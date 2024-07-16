import xml.etree.ElementTree as ET
from xml.dom import minidom
import platform
import os

class Universidad:
    def __init__(self):
        self.campus = []
        self.escuelas = []
    def addCampus(self, campus):
        self.campus.append(campus)

    def addEscuela(self, escuela):
        self.escuelas.append(escuela)
    
    def show(self):
        print("-Universidad-")
        for campus in self.campus:
            campus.show()
        for escuela in self.escuelas:
            escuela.show()

class Campus:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificos = []

    def addEdificio(self, edificio):
        self.edificos.append(edificio)

    def show(self):
        print(" -Campus-")
        print(f"    nombre : {self.nombre}")
        for edificio in self.edificos:
            edificio.show()

class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aulas = []
    
    def addAula(self, aula):
        self.aulas.append(aula)

    def show(self):
        print("     -Edificio-")
        print(f"        nombre : {self.nombre}")
        for aula in self.aulas:
            aula.show()

class Aulas:
    def __init__(self, numero, capacidadClase, capacidadExamen, tipo):
        self.numero = numero
        self.capacidadClase = capacidadClase
        self.capacidadExamen = capacidadExamen
        self.tipo = tipo
    
    def show(self):
        print("         -Aula-")
        print(f"            nuemro : {self.numero}")
        print(f"            capacidadClase: {self.capacidadClase}")
        print(f"            capaciadExamen: {self.capacidadExamen}")
        print(f"            tipo: {self.tipo}")

class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.titulaciones = []

    def addTitulacion(self, titulacion):
        self.titulaciones.append(titulacion)

    def show(self):
        print(" -Escuela-")
        print(f"    nombre : {self.nombre}")
        for titulacion in self.titulaciones:
            titulacion.show()

class Titulacion:
    def __init__(self, nombre, campus):
        self.nombre = nombre
        self.campus = campus
        self.cursos = []
    
    def addCurso(self, curso):
        self.cursos.append(curso)

    def show(self):
        print("     -Titulacion-")
        print(f"        nombre : {self.nombre}")
        print(f"        campus : {self.campus}")
        for curso in self.cursos:
            curso.show()

class Curso:
    def __init__(self, año, creditos):
        self.año = año
        self.creditos = creditos
        self.asignaturas = []
    
    def addAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)
    
    def show(self):
        print("         -Curso-")
        print(f"            año : {self.año}")
        print(f"            creditos : {self.creditos}")
        for asignatura in self.asignaturas:
            asignatura.show()

class Asignatura:
    def __init__(self, nombre, creditos, alumnos, profesor):
        self.nombre = nombre
        self.creditos = creditos
        self.alumnos = alumnos
        self.profesor = profesor

    def show(self):
        print("             -Asignatura-")
        print(f"                nombre : {self.nombre}")
        print(f"                creditos: {self.creditos}")
        print(f"                alumnos: {self.alumnos}")
        print(f"                profesor: {self.profesor}")

def cargaAsignatura(asignatura):
    nombre = input("------Introduzca el nombre de la asignatura: ")
    ET.SubElement(asignatura, "Nombre").text = nombre

    while True:
        try:         
            creditos = int(input("------Introduzca el número de creditos: "))
            break
        except ValueError:
            print("------Introduzca un número entero")
    ET.SubElement(asignatura, "Creditos").text = str(creditos)

    while True:
        try:
            alumnos = input("------Introduzca el número de alumnos matriculados: ")
            break
        except ValueError:
            print("------Introduzca un número entero")
    ET.SubElement(asignatura, "nAlumnos").text = alumnos

    profesor = input("------Introduzca el nombre del profesor: ")
    ET.SubElement(asignatura, "Profesor").text = profesor

    return creditos

def cargaCurso(curso):
    año = input("----Introduzca el numero del curso: ")
    ET.SubElement(curso, "Año").text = año

    print("------Introduzca las Asignaturas")
    salir = False
    creditos = 0
    while salir == False:
        asignatura = ET.SubElement(curso, "Asignatura")
        creditos += cargaAsignatura(asignatura)
        parar = input("------Quiere añadir otra Asignatura (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("------Introduzca si ó no")
            parar = input("------Quiere añadir otra Asignatura (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    
    ET.SubElement(curso, "Creditos").text = str(creditos)          
    print("-------------------------------------------------")

def cargaTitulacion(titulacion, campusList):
    nombre = input("--Introduzca el nombre de la titulación: ")
    ET.SubElement(titulacion, "Nombre").text = nombre

    print("--Campus disponibles: ")
    print(*campusList)
    campus = input("--Introduzca el nombre del Campus en la que se cursa: ").strip().lower()
    while campus not in campusList:
        print("Introduzca uno de los campus disponibles: ")
        print(*campusList)
        campus = input("--Introduzca el nombre del Campus en la que se cursa: ").strip().lower()
    ET.SubElement(titulacion, "Campus").text = campus

    print("----Introduzca los Curso Académico")
    salir = False
    while salir == False:
        curso = ET.SubElement(titulacion, "Curso")
        cargaCurso(curso)
        parar = input("----Quiere añadir otro Curso Académico (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("----Introduzca si ó no")
            parar = input("----Quiere añadir otro Curso Académico (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")
    
def cargaEscuelas(escuela, campusList):
    nombre = input("Introduzaca el nombre de la Escuela: ")
    ET.SubElement(escuela, "Nombre").text = nombre

    print("--Introduzca las titulaciones")
    salir = False
    while salir == False:
        titulacion = ET.SubElement(escuela, "Titulacion")
        cargaTitulacion(titulacion, campusList)
        parar = input("--Quiere añadir otra Titulación (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("--Introduzca si ó no")
            parar = input("--Quiere añadir otra Titulación (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")

def cargaAula(aula):
    numero = input("----Introduzca el número del Aula: ")
    ET.SubElement(aula, "Numero").text = numero

    while True:
        try:         
            capacidadClase = int(input("----Introduzca la capacidad maxima para clase: "))
            break
        except ValueError:
            print("----Introduzca un número entero")
    ET.SubElement(aula, "CapacidadClase").text = str(capacidadClase)

    while True:
        try:         
            capacidadEx = int(input("----Introduzca la capacidad maxima para examenes: "))
            break
        except ValueError:
            print("----Introduzca un número entero")
    ET.SubElement(aula, "CapacidadExamen").text = str(capacidadEx)

    tipo = input("----Introduzca el tipo de aula (clase ó laboratorio): ").strip().lower()
    while tipo not in ["clase", "laboratorio"]:
        tipo = input("----Introduzca el tipo de aula (clase ó laboratorio): ").strip().lower()
    ET.SubElement(aula, "Tipo").text = tipo



def cargaEdificio(edificio):
    nombre = input("--Introduzaca el nombre del Edificio (EJ. Aulario1): ")
    ET.SubElement(edificio, "Nombre").text = nombre
    print("----Introduzca las Aulas")
    salir = False
    while salir == False:
        aula = ET.SubElement(edificio, "Aula")
        cargaAula(aula)
        parar = input("----Quiere añadir otra Aula (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("----Introduzca si ó no")
            parar = input("----Quiere añadir otra Aula (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")

def cargaCampus(Campus):
    nombre = input("Introduzaca el nombre del Campus: ").strip().lower()
    ET.SubElement(Campus, "Nombre").text = nombre

    print("--Introduzca los Edificios")
    salir = False
    while salir == False:
        edificio = ET.SubElement(Campus, "Edificio")
        cargaEdificio(edificio)
        parar = input("--Quiere añadir otro Edificio (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("--Introduzca si ó no")
            parar = input("--Quiere añadir otro Edificio (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
        print("-------------------------------------------------")
    return nombre

def previsualizarXML(root):
    # Convertir el árbol XML a una cadena y formatearla
    xml_str = ET.tostring(root, encoding='unicode')
    parsed_str = minidom.parseString(xml_str)
    formatted_xml = parsed_str.toprettyxml(indent="  ")
    print("\nPrevisualización del XML generado:\n")
    print(formatted_xml)
    return formatted_xml


def guardarDatos(root):
    arbol = ET.ElementTree(root)
    # Obtener la ruta del archivo .py actual
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ruta completa del archivo XML
    xml_file_path = os.path.join(current_directory, "universidad.xml")
    
    # Guardar el árbol XML en el archivo
    arbol.write(xml_file_path, encoding="utf-8", xml_declaration=True)
    
    print(f"Archivo XML guardado en: {xml_file_path}")

def cargarDatos():
    root = ET.Element("Univerisdad")
    campusList = []

    print("-----Introduzca los Campus de su Universidad-----")
    salir = False
    while salir == False:
        Campus = ET.SubElement(root,"Campus")
        campusList.append(cargaCampus(Campus))
        parar = input("Quiere añadir otro Campus (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("Introduzca si ó no")
            parar = input("Quiere añadir otro Campus (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")

    print("-----Introduzca las Escuelas de su Universidad-----")
    salir = False
    while salir == False:
        escuela = ET.SubElement(root,"Escuela")
        cargaEscuelas(escuela, campusList)
        parar = input("Quiere añadir otra Escuela (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("Introduzca si ó no")
            parar = input("Quiere añadir otra Escuela (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")

    # Previsualizar el xml generado
    previsualizarXML(root)
    # Guardar datos
    guardarDatos(root)

def importarDatos():
    ruta_archivo = input("introduzca la ruta del archivo que quiere importar: ")
    try:
        new_Universidad = Universidad()
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        for campus in root.findall("Campus"):
            new_campus = Campus(campus.find("Nombre").text)
            for edificio in campus.findall("Edificio"):
                new_edificio = Edificio(edificio.find("Nombre").text)
                for aula in edificio.findall("Aula"):
                    new_aula = Aulas(aula.find("Numero").text, aula.find("CapacidadClase").text, aula.find("CapacidadExamen").text, aula.find("Tipo").text)
                    new_edificio.addAula(new_aula)
                new_campus.addEdificio(new_edificio)
            new_Universidad.addCampus(new_campus)
        
        for escuela in root.findall("Escuela"):
            new_escuela = Escuela(escuela.find("Nombre").text)
            for titulacion in escuela.findall("Titulacion"):
                new_titulacion = Titulacion(titulacion.find("Nombre").text, titulacion.find("Campus").text)
                for curso in titulacion.findall("Curso"):
                    new_curso = Curso(curso.find("Año").text, curso.find("Creditos").text)
                    for asignatura in curso.findall("Asignatura"):
                        new_asignatura = Asignatura(asignatura.find("Nombre").text, asignatura.find("Creditos").text, asignatura.find("nAlumnos").text, asignatura.find("Profesor").text)
                        new_curso.addAsignatura(new_asignatura)
                    new_titulacion.addCurso(new_curso)
                new_escuela.addTitulacion(new_titulacion)
            new_Universidad.addEscuela(new_escuela)

        return new_Universidad

    except FileNotFoundError:
        print("El archivo no fue encontrado. Por favor, verifica la ruta e inténtalo de nuevo.")
    except ET.ParseError:
        print("El archivo no es un XML válido. Por favor, verifica el contenido del archivo.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

salir = False
while salir == False:
    opcion = input("¿Quiere cargar datos, importarlos o salir? (cargar, importar ó salir) ").strip().lower()
    match opcion:
        case "cargar":
            cargarDatos()
        case "importar":
            universidad = importarDatos()
            universidad.show()
        case "salir":
            salir = True