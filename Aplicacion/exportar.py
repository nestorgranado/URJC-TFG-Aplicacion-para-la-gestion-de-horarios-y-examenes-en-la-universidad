from collections import defaultdict
import pandas as pd
import os
from estructuraDatos import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import platform

# Exportar las Escuelas
def exportarEscuelas(root, universidad):
    # Por cada escuela crear un elemnto "Escuela" y un atributo "Nombre" y recorrer la lista de Titulcaiones
    for escuela in universidad.getEscuelas():
        escuelaXML = ET.SubElement(root, "Escuela")
        ET.SubElement(escuelaXML, "Nombre").text = escuela.getNombre()
        for titulacion in escuela.getTitulaciones():
            titulacionXML = ET.SubElement(escuelaXML, "Titulación")
            ET.SubElement(titulacionXML, "Código").text = titulacion.getCodigo()
            ET.SubElement(titulacionXML, "Nombre").text = titulacion.getNombre()
            ET.SubElement(titulacionXML, "Campus").text = titulacion.getCampus()
            for asignatura in titulacion.getAsignaturas():
                asignaturaXML = ET.SubElement(titulacionXML, "Asignatura")
                ET.SubElement(asignaturaXML, "Código").text = asignatura.getCodigo()
                ET.SubElement(asignaturaXML, "Nombre").text = asignatura.getNombre()
                ET.SubElement(asignaturaXML, "Titulación").text = asignatura.getTitulacion()
                ET.SubElement(asignaturaXML, "NumAlumnos").text = str(asignatura.getNumAlumnos())
                ET.SubElement(asignaturaXML, "Profesor").text = asignatura.getProfesor()
                ET.SubElement(asignaturaXML, "Curso").text = str(asignatura.getCurso())
                for hija in asignatura.getAsignaturas_hijas():
                    hijasXML = ET.SubElement(asignaturaXML, "AsignaturaHija")
                    ET.SubElement(hijasXML, "Código").text = hija[0]
                    ET.SubElement(hijasXML, "Nombre").text = hija[1]

# Exportar los Campus
def exportarCampus(root, universidad):
    # Por cada campus se crear un elemento "Campus" y un atributo "Nombre" y se recorre la lista de Edificios
    for campus in universidad.getCampus():
        campusXML = ET.SubElement(root, "Campus")
        ET.SubElement(campusXML, "Nombre").text = campus.getNombre()
        for edificio in campus.getEdificios():
            edificioXML = ET.SubElement(campusXML, "Edificio")
            ET.SubElement(edificioXML, "Nombre").text = edificio.getNombre()
            for aula in edificio.getAulas():
                aulaXML = ET.SubElement(edificioXML, "Aula")
                ET.SubElement(aulaXML, "Número").text = aula.getNumero()
                ET.SubElement(aulaXML, "CapacidadClase").text = str(aula.getCapacidadClase())
                ET.SubElement(aulaXML, "CapacidadExamen").text = str(aula.getCapacidadExamen())
                ET.SubElement(aulaXML, "Tipo").text = aula.getTipo()


# Exportar main
def exportar(path, universidad):
    # Crear el elemento raiz
    root = ET.Element("Institución")
    # Crear el atributo "Nombre"
    ET.SubElement(root, "Nombre").text = universidad.getNombre()
    # Exportar las escuelas y los campus
    exportarCampus(root, universidad)
    exportarEscuelas(root, universidad)

    # Crear el arbol XML
    arbol = ET.ElementTree(root)

    # Guardar el árbol XML en el archivo
    arbol.write(path, encoding="utf-8", xml_declaration=True)


