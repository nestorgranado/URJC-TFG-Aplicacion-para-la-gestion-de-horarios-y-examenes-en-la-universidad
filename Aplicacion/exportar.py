from collections import defaultdict
import pandas as pd
import os
from estructuraDatos import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import platform

# Exportar las Escuelas
def exportarTitulaciones(root, universidad):
    # Por cada escuela crear un elemnto "Escuela" y un atributo "Nombre" y recorrer la lista de Titulcaiones
    titulacionesListXML = ET.SubElement(root, "ListaTitulaciones")
    for titulacion in universidad.getTitulacion():
        titulacionXML = ET.SubElement(titulacionesListXML, "Titulación")
        ET.SubElement(titulacionXML, "Código").text = titulacion.getCodigo()
        ET.SubElement(titulacionXML, "Nombre").text = titulacion.getNombre()
        ET.SubElement(titulacionXML, "Campus").text = titulacion.getCampus()
        for asignatura in titulacion.getAsignaturas():
            asignaturaXML = ET.SubElement(titulacionXML, "Asignatura")
            ET.SubElement(asignaturaXML, "Código").text = asignatura.getCodigo()
            ET.SubElement(asignaturaXML, "Nombre").text = asignatura.getNombre()
            ET.SubElement(asignaturaXML, "Titulación").text = asignatura.getTitulacion()
            ET.SubElement(asignaturaXML, "NumAlumnos").text = str(asignatura.getNumAlumnos())
            ET.SubElement(asignaturaXML, "Curso").text = str(asignatura.getCurso())
            for hija in asignatura.getAsignaturas_hijas():
                hijasXML = ET.SubElement(asignaturaXML, "AsignaturaHija")
                ET.SubElement(hijasXML, "Código").text = hija[0]
                ET.SubElement(hijasXML, "Nombre").text = hija[1]

# Exportar los Campus
def exportarCampus(root, universidad):
    # Por cada campus se crear un elemento "Campus" y un atributo "Nombre" y se recorre la lista de Edificios
    campusListXML = ET.SubElement(root, "ListaCampus")
    for campus in universidad.getCampus():
        campusXML = ET.SubElement(campusListXML, "Campus")
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
                ET.SubElement(aulaXML, "AulaCombinada").text = str(aula.getCombinacion())
                if aula.getCombinacion():
                    ET.SubElement(aulaXML, "NúmeroCombinaciones").text = str(aula.getNumCombinaciones())
                    for combinacion in aula.getAulasCombinadas():
                        combinacionXML = ET.SubElement(aulaXML, "Combinación")
                        ET.SubElement(combinacionXML, "NúmeroAulas").text = str(len(combinacion))
                        for aulaCombinada in combinacion:
                            aulasCombinadasXML = ET.SubElement(combinacionXML, "Aula")
                            ET.SubElement(aulasCombinadasXML, "Número").text = aulaCombinada.getNumero()
                            ET.SubElement(aulasCombinadasXML, "CapacidadClase").text = str(aulaCombinada.getCapacidadClase())
                            ET.SubElement(aulasCombinadasXML, "CapacidadExamen").text = str(aulaCombinada.getCapacidadExamen())
                            ET.SubElement(aulasCombinadasXML, "Tipo").text = aulaCombinada.getTipo()

# Exportar Cursos
def exportarCursos(root, alumnos):
    # Crea un elemenro "Curso" y un atributo "Nombre" y "Número Alumnos" y se recorre los grupos
    cursoXML = ET.SubElement(root, "Alumnos")
    for alumnosTit in alumnos:
        alumnosTitXML = ET.SubElement(cursoXML, "AlumnosTitulacion")
        ET.SubElement(alumnosTitXML, "Nombre").text = alumnosTit.getNombre()
        ET.SubElement(alumnosTitXML, "NúmeroAlumnos").text = str(alumnosTit.getNumAlumnos())
        for alumnosCurso in alumnosTit.getCursos():
            alumnosCursoXML = ET.SubElement(alumnosTitXML, "AlumnosCurso")
            ET.SubElement(alumnosCursoXML, "Nombre").text = alumnosCurso.getNombre()
            ET.SubElement(alumnosCursoXML, "NúmeroAlumnos").text = str(alumnosCurso.getNumAlumnos())
            for alumnosAsig in alumnosCurso.getAsignaturas():
                alumnosAsigXML = ET.SubElement(alumnosCursoXML, "AlumnosAsignatura")
                ET.SubElement(alumnosAsigXML, "Nombre").text = alumnosAsig.getNombre()
                ET.SubElement(alumnosAsigXML, "NúmeroAlumnos").text = str(alumnosAsig.getNumAlumnos())

# Exportar Días por Semana
def exportarDias(root, diasSemana):
    # exportar datos del los dias
    dias = ET.SubElement(root, "DiasPorSemana")
    ET.SubElement(dias, "NuemroDias").text = str(diasSemana.getNumDias())

    for dia in diasSemana.getDias():
        diaXML = ET.SubElement(dias, "Dia")
        ET.SubElement(diaXML, "Nombre").text = dia

# Exportar Horas por Día
def exportarHoras(root, horasDia):
    # exportar datos del las horas
    horas = ET.SubElement(root, "HorasporDia")
    ET.SubElement(horas, "NuemroHoras").text = str(horasDia.getNumHoras())

    for hora in horasDia.getHoras():
        horaXML = ET.SubElement(horas, "Hora")
        ET.SubElement(horaXML, "Nombre").text = hora

    return horas

# Exportar Actividades
def exportarActividades(root, actividades):
    actividad = ET.SubElement(root, "Actividades")
    for act in actividades:
        activiadXML = ET.SubElement(actividad, "Actividad")
        ET.SubElement(activiadXML, "Asignatura").text = act.getAsignatura()
        ET.SubElement(activiadXML, "Titulaciones").text = ", ".join(act.getTitulacion())
        ET.SubElement(activiadXML, "Cursos").text = ", ".join(act.getCurso())
        ET.SubElement(activiadXML, "Duracion").text = str(act.getDuracion())

# Exportar main
def exportar(path, universidad, alumnos, diasSemana, horasDia, actividades):
     # Crear el elemento raiz
    root = ET.Element("Institución")
    # Crear el atributo "Nombre"
    ET.SubElement(root, "Nombre").text = universidad.getNombre()

    # Exportar datos de la institución
    exportarCampus(root, universidad)
    exportarTitulaciones(root, universidad)

    curso = None
    if alumnos:
        curso = exportarCursos(root, alumnos)

    dias = exportarDias(root, diasSemana)
    horas = exportarHoras(root, horasDia)
    
    actividad = None
    if actividades:
        actividad = exportarActividades(root, actividades)

    # Convertir el árbol XML a una cadena y guardar en el archivo especificado
    tree = ET.ElementTree(root)
    try:
        tree.write(path, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error al guardar el archivo XML: {e}")