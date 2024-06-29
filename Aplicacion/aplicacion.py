import xml.etree.ElementTree as ET
from xml.dom import minidom
import platform
import os

def limpiar_consola():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def CargaAsignatura(asignatura):
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

def CargaCurso(curso):
    año = input("----Introduzca el numero del curso: ")
    ET.SubElement(curso, "Año").text = año

    print("------Introduzca las Asignaturas")
    salir = False
    creditos = 0
    while salir == False:
        asignatura = ET.SubElement(curso, "Asignatura")
        creditos += CargaAsignatura(asignatura)
        parar = input("------Quiere añadir otra Asignatura (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("------Introduzca si ó no")
            parar = input("------Quiere añadir otra Asignatura (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    
    ET.SubElement(curso, "Creditos").text = str(creditos)          
    print("-------------------------------------------------")

def CargaTitulacion(titulacion, campusList):
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
        CargaCurso(curso)
        parar = input("----Quiere añadir otro Curso Académico (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("----Introduzca si ó no")
            parar = input("----Quiere añadir otro Curso Académico (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")
    
def CargaEscuelas(escuela, campusList):
    nombre = input("Introduzaca el nombre de la Escuela: ")
    ET.SubElement(escuela, "Nombre").text = nombre

    print("--Introduzca las titulaciones")
    salir = False
    while salir == False:
        titulacion = ET.SubElement(escuela, "Titulacion")
        CargaTitulacion(titulacion, campusList)
        parar = input("--Quiere añadir otra Titulación (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("--Introduzca si ó no")
            parar = input("--Quiere añadir otra Titulación (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")

def CargaAula(aula):
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
    ET.SubElement(aula, "Numero").text = tipo



def CargaEdificio(edificio):
    nombre = input("--Introduzaca el nombre del Edificio (EJ. Aulario1): ")
    ET.SubElement(edificio, "Nombre").text = nombre
    print("----Introduzca las Aulas")
    salir = False
    while salir == False:
        aula = ET.SubElement(edificio, "Aula")
        CargaAula(aula)
        parar = input("----Quiere añadir otra Aula (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("----Introduzca si ó no")
            parar = input("----Quiere añadir otra Aula (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")

def CargaCampus(Campus):
    nombre = input("Introduzaca el nombre del Campus: ").strip().lower()
    ET.SubElement(Campus, "Nombre").text = nombre

    print("--Introduzca los Edificios")
    salir = False
    while salir == False:
        edificio = ET.SubElement(Campus, "Edificio")
        CargaEdificio(edificio)
        parar = input("--Quiere añadir otro Edificio (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("--Introduzca si ó no")
            parar = input("--Quiere añadir otro Edificio (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
        print("-------------------------------------------------")
    return nombre

def PrevisualizarXML(root):
    # Convertir el árbol XML a una cadena y formatearla
    xml_str = ET.tostring(root, encoding='unicode')
    parsed_str = minidom.parseString(xml_str)
    formatted_xml = parsed_str.toprettyxml(indent="  ")
    print("\nPrevisualización del XML generado:\n")
    print(formatted_xml)
    return formatted_xml


def GuardarDatos(root):
    arbol = ET.ElementTree(root)
    # Obtener la ruta del archivo .py actual
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ruta completa del archivo XML
    xml_file_path = os.path.join(current_directory, "universidad.xml")
    
    # Guardar el árbol XML en el archivo
    arbol.write(xml_file_path, encoding="utf-8", xml_declaration=True)
    
    print(f"Archivo XML guardado en: {xml_file_path}")

def CargarDatos():
    root = ET.Element("Univerisdad")
    campusList = []

    print("-----Introduzca los Campus de su Universidad-----")
    salir = False
    while salir == False:
        Campus = ET.SubElement(root,"Campus")
        campusList.append(CargaCampus(Campus))
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
        CargaEscuelas(escuela, campusList)
        parar = input("Quiere añadir otra Escuela (si ó no): ").strip().lower()
        while parar not in ["si", "no"]:
            print("Introduzca si ó no")
            parar = input("Quiere añadir otra Escuela (si ó no): ").strip().lower()
        if parar == "no":
            salir = True
    print("-------------------------------------------------")

    # Previsualizar el xml generado
    PrevisualizarXML(root)
    # Guardar datos
    GuardarDatos(root)

"""
opcion = input("¿Quiere cargar datos o importarlos? (cargar ó importar)").strip().lower()
match opcion:
    case "cargar":
        CargarDatos()
    case "importar datos":
        ImportarDatos()
"""
CargarDatos()
