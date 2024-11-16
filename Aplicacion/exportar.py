from collections import defaultdict
import pandas as pd
import os
from estructuraDatos import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import platform

# Función para convertir un elemento XML en una cadena
def xmlToString(raiz, incluir_declaracion=False):
    # Generar la cadena XML
    xml_string = ET.tostring(raiz, encoding="utf-8").decode("utf-8")
    if incluir_declaracion:
        # Agregar declaración XML solo si se especifica
        xml_string = f'<?xml version="1.0" encoding="utf-8"?>\n{xml_string}'
    return xml_string

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

# Exportar Cursos
def exportarCursos(cursos):
    # Crea un elemenro "Curso" y un atributo "Nombre" y "Número Alumnos" y se recorre los grupos
    cursoXML = ET.Element("Curso")
    ET.SubElement(cursoXML, "Nombre").text = str(cursos.getNombre())
    ET.SubElement(cursoXML, "NúmeroAlumnos").text = str(cursos.getNumAlumnos())
    for grupo in cursos.getGrupos():
        grupoXML = ET.SubElement(cursoXML, "Grupo")
        ET.SubElement(grupoXML, "Nombre").text = str(grupo.getNombre())
        ET.SubElement(grupoXML, "NúmeroAlumnos").text = str(grupo.getNumAlumnos())

    return cursoXML

# Exportar Institución
def exportarIntitucion(universidad):
    # Crear el elemento raiz
    institucion = ET.Element("Institución")
    # Crear el atributo "Nombre"
    ET.SubElement(institucion, "Nombre").text = universidad.getNombre()

    # Exportar datos de la institución
    exportarCampus(institucion, universidad)
    exportarEscuelas(institucion, universidad)

    return institucion

# Exportar Días por Semana
def exportarDias(diasSemana):
    # exportar datos del los dias
    dias = ET.Element("DiasPorSemana")
    ET.SubElement(dias, "NuemroDias").text = str(diasSemana.getNumDias())

    for dia in diasSemana.getDias():
        diaXML = ET.SubElement(dias, "Dia")
        ET.SubElement(diaXML, "Nombre").text = dia

    return dias

# Exportar Horas por Día
def exportarHoras(horasDia):
    # exportar datos del las horas
    horas = ET.Element("HorasporDia")
    ET.SubElement(horas, "NuemroHoras").text = str(horasDia.getNumHoras())

    for hora in horasDia.getHoras():
        horaXML = ET.SubElement(horas, "Hora")
        ET.SubElement(horaXML, "Nombre").text = hora

    return horas

# Exportar Actividades
def exportarActividades(actividades):
    actividad = ET.Element("Actividades")
    for act in actividades:
        activiadXML = ET.SubElement(actividad, "Actividad")
        ET.SubElement(activiadXML, "Asignatura").text = act.getAsignatura()
        ET.SubElement(activiadXML, "Profesor").text = act.getProfesor()
        ET.SubElement(activiadXML, "Curso").text = str(act.getCurso())
        ET.SubElement(activiadXML, "Duracion").text = str(act.getDuracion())

    return actividad

# Exportar main
def exportar(path, universidad, cursos, diasSemana, horasDia, actividades):
    # Exportar datos
    institucion = exportarIntitucion(universidad)
    curso = None
    if not cursos.isEmpty():
        curso = exportarCursos(cursos)
    dias = exportarDias(diasSemana)
    horas = exportarHoras(horasDia)
    actividad = exportarActividades(actividades)

    # Convertir los documentos XML a cadenas de texto
    xml_int = xmlToString(institucion, incluir_declaracion=True)
    xml_curso = ""
    if not cursos.isEmpty():
        xml_curso = xmlToString(curso)
    xml_dias = xmlToString(dias)
    xml_horas = xmlToString(horas)
    xml_actividades = xmlToString(actividad)

    # Guardar archivo
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(xml_int)
        archivo.write("\n")  # Agrega una línea en blanco entre documentos
        if not cursos.isEmpty():
            archivo.write(xml_curso)
            archivo.write("\n") 
        archivo.write(xml_dias)
        archivo.write("\n")
        archivo.write(xml_horas)
        archivo.write("\n")
        archivo.write(xml_actividades)