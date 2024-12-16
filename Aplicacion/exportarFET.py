from collections import defaultdict
import pandas as pd
import os
from estructuraDatos import *
import xml.etree.ElementTree as ET
from lxml import etree
from xml.dom import minidom
import platform

def exportarFET(path, institucion, dias, horas, asignaturas, alumnos, actividades, tipo):
    # Elemento Raiz
    root = etree.Element("fet")
    root.set("version", "6.18.1")

    # Modo FET (A lo mejor luego hay que cambiar de modo pero por ahora solo el oficial)
    etree.SubElement(root, "Mode").text = "Official"

    # Nombre de la institución
    etree.SubElement(root, "Institution_Name").text = institucion.getNombre()

    # Comentarios default
    etree.SubElement(root, "Comments").text = "Comentario predefinido"

    # Lista de Días por Semana
    listaDias = etree.SubElement(root, "Days_List")
    etree.SubElement(listaDias, "Number_of_Days").text = str(dias.getNumDias())
    for dia in dias.getDias():
        diaXML = etree.SubElement(listaDias, "Day")
        etree.SubElement(diaXML, "Name").text = dia

    # Lista de Horas por Día
    listaHoras = etree.SubElement(root, "Hours_List")
    etree.SubElement(listaHoras, "Number_of_Hours").text = str(horas.getNumHoras())
    for hora in horas.getHoras():
        horaXML = etree.SubElement(listaHoras, "Hour")
        etree.SubElement(horaXML, "Name").text = hora

    # Lista de asignaturas
    """profesores = {}"""
    listaAsignaturas = etree.SubElement(root, "Subjects_List")
    for asignatura in asignaturas:
        asignaturaXML = etree.SubElement(listaAsignaturas, "Subject")
        etree.SubElement(asignaturaXML, "Name").text = asignatura.getNombre()
        etree.SubElement(asignaturaXML, "Comments").text = asignatura.getNombre()

        """if asignatura.getProfesor() != None:
            profesores.setdefault(asignatura.getProfesor(), []).append(asignatura.getNombre())
        """
    
    """if not profesores:
        for asignatura in asignaturas:
            # Crear un porfesor por asignatura solucion primera
            nombreProfesor = "Profesor- " + asignatura.getNombre()
            profesores.setdefault(nombreProfesor, []).append(asignatura.getNombre())
    """

    # Etiquetas de asignaturas(por ahora sin usar)
    EtiquetasAsignaturas = etree.SubElement(root, "Activity_Tags_List")
    EtiquetasAsignaturas.text = ""

    # Lista Profesores
    listaProfesores = etree.SubElement(root, "Teachers_List")
    listaProfesores.text = ""
    """if profesores:
        for profesor in profesores:
            profesorXML = etree.SubElement(listaProfesores, "Teacher")
            etree.SubElement(profesorXML, "Name").text = profesor
            etree.SubElement(profesorXML, "Target_Number_of_Hours").text = "0"
            asignaturasImpartidas = etree.SubElement(profesorXML, "Qualified_Subjects")
            if profesor:
                for asignatura in profesores[profesor]:
                    etree.SubElement(asignaturasImpartidas,"Qualified_Subject").text = asignatura
            else:
                asignaturasImpartidas.text = ""

            etree.SubElement(profesorXML, "Comments").text = profesor
    else:
        listaProfesores.text = ""
    """
    
    # Estudiantes
    listaEstudiantes = etree.SubElement(root, "Students_List")
    for alumnosTit in alumnos:
        cursoXML = etree.SubElement(listaEstudiantes, "Year")
        etree.SubElement(cursoXML, "Name").text = alumnosTit.getNombre()
        etree.SubElement(cursoXML, "Number_of_Students").text = str(alumnosTit.getNumAlumnos())
        etree.SubElement(cursoXML, "Comments").text = ""
        comentario = etree.Comment(
        "The information regarding categories, divisions of each category, "
        "and separator is only used in the divide year automatically by categories dialog."
        )
        cursoXML.append(comentario)
        etree.SubElement(cursoXML, "Number_of_Categories").text = "0"
        etree.SubElement(cursoXML, "Separator").text = ""
        for alumnosCurso in alumnosTit.getCursos():
            grupoXML = etree.SubElement(cursoXML, "Group")
            etree.SubElement(grupoXML, "Name").text = alumnosCurso.getNombre()
            etree.SubElement(grupoXML, "Number_of_Students").text = str(alumnosCurso.getNumAlumnos())
            etree.SubElement(grupoXML, "Comments").text = ""
            for alumnosAsig in alumnosCurso.getAsignaturas():
                subGrupoXML = etree.SubElement(cursoXML, "Subgroup")
                etree.SubElement(subGrupoXML, "Name").text = alumnosAsig.getNombre()
                etree.SubElement(subGrupoXML, "Number_of_Students").text = str(alumnosAsig.getNumAlumnos())
                etree.SubElement(subGrupoXML, "Comments").text = ""

    # Lista Actividades
    listaActividades = etree.SubElement(root, "Activities_List")
    i = 1 
    for actividad in actividades:
        actividadXML = etree.SubElement(listaActividades, "Activity")
        
        """if actividad.getProfesor() == None:
            etree.SubElement(actividadXML, "Teacher").text = "Profesor- " + actividad.getAsignatura()
        else:
            etree.SubElement(actividadXML, "Teacher").text = actividad.getProfesor()
        """

        etree.SubElement(actividadXML, "Subject").text = actividad.getAsignatura()
        for curso in actividad.getCurso():
            etree.SubElement(actividadXML, "Students").text = curso
        etree.SubElement(actividadXML, "Duration").text = str(actividad.getDuracion())
        etree.SubElement(actividadXML, "Total_Duration").text = str(actividad.getDuracion())
        etree.SubElement(actividadXML, "Id").text = str(i)
        etree.SubElement(actividadXML, "Activity_Group_Id").text = "0"
        etree.SubElement(actividadXML, "Active").text = "true"
        etree.SubElement(actividadXML, "Comments").text = ""
        i += 1

    # Lista Edificios
    listaEdificios = etree.SubElement(root, "Buildings_List")
    for campus in institucion.getCampus():
        for edificio in campus.getEdificios():
            edificioXML = etree.SubElement(listaEdificios, "Building")
            etree.SubElement(edificioXML, "Name").text = edificio.getNombre()
            etree.SubElement(edificioXML, "Comments").text = ""

    # Lista Aulas
    listaAulas = etree.SubElement(root, "Rooms_List")
    if tipo == "Clase": # Aula para clases
        for campus in institucion.getCampus():
            for edificio in campus.getEdificios():
                for aula in edificio.getAulas():
                    aulaClaseXML = etree.SubElement(listaAulas, "Room")
                    etree.SubElement(aulaClaseXML, "Name").text = str(aula.getNumero()) + "-" + edificio.getNombre()
                    etree.SubElement(aulaClaseXML, "Building").text = edificio.getNombre()
                    etree.SubElement(aulaClaseXML, "Capacity").text = str(aula.getCapacidadClase())
                    if aula.getCombinacion():
                        etree.SubElement(aulaClaseXML, "Virtual").text = "true"
                        etree.SubElement(aulaClaseXML, "Number_of_Sets_of_Real_Rooms").text = str(aula.getNumCombinaciones())
                        for combinacion in aula.getAulasCombinadas():
                            combinacionXML = etree.SubElement(aulaClaseXML, "Set_of_Real_Rooms")
                            etree.SubElement(combinacionXML, "Number_of_Real_Rooms").text = str(len(combinacion))
                            for aulaComb in combinacion:
                                etree.SubElement(combinacionXML, "Real_Room").text = aulaComb.getNumero()
                    else:
                        etree.SubElement(aulaClaseXML, "Virtual").text = "false"

                    etree.SubElement(aulaClaseXML, "Comments").text = ""
    else: # Aula para Examen
        for campus in institucion.getCampus():
            for edificio in campus.getEdificios():
                for aula in edificio.getAulas():
                    aulaExamenXML = etree.SubElement(listaAulas, "Room")
                    etree.SubElement(aulaExamenXML, "Name").text = str(aula.getNumero()) + "-" + edificio.getNombre()
                    etree.SubElement(aulaExamenXML, "Building").text = edificio.getNombre()
                    etree.SubElement(aulaExamenXML, "Capacity").text = str(aula.getCapacidadExamen())
                    if aula.getCombinacion():
                        etree.SubElement(aulaExamenXML, "Virtual").text = "true"
                        etree.SubElement(aulaExamenXML, "Number_of_Sets_of_Real_Rooms").text = str(aula.getNumCombinaciones())
                        for combinacion in aula.getAulasCombinadas():
                            combinacionXML = etree.SubElement(aulaExamenXML, "Set_of_Real_Rooms")
                            etree.SubElement(combinacionXML, "Number_of_Real_Rooms").text = str(len(combinacion))
                            for aulaComb in combinacion:
                                etree.SubElement(combinacionXML, "Real_Room").text = aulaComb.getNumero() + "-" + edificio.getNombre()
                    else:
                        etree.SubElement(aulaExamenXML, "Virtual").text = "false"

                    etree.SubElement(aulaExamenXML, "Comments").text = ""

    # Resticciones de Tiempo
    time_constraints = etree.SubElement(root, "Time_Constraints_List")
    constraint_time = etree.SubElement(time_constraints, "ConstraintBasicCompulsoryTime")
    etree.SubElement(constraint_time, "Weight_Percentage").text = "100"
    etree.SubElement(constraint_time, "Active").text = "true"
    etree.SubElement(constraint_time, "Comments").text = ""

    # Restricciones de Lugar
    space_constraints = etree.SubElement(root, "Space_Constraints_List")
    constraint_space = etree.SubElement(space_constraints, "ConstraintBasicCompulsorySpace")
    etree.SubElement(constraint_space, "Weight_Percentage").text = "100"
    etree.SubElement(constraint_space, "Active").text = "true"
    etree.SubElement(constraint_space, "Comments").text = ""

    with open(path, "wb") as file:
        file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
