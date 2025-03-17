from collections import defaultdict
import pandas as pd
import os
from estructuraDatos import *
import xml.etree.ElementTree as ET
from lxml import etree
from xml.dom import minidom
import platform
from datetime import datetime, timedelta

def exportarFET(path, institucion, dias, horas, asignaturas, alumnos, actividades, aulaPorCampus, aulaPorTipo, actividadesPorCuros, restriccionesTiempo, restriccionesLugar, tipo):
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
    for tipoAu in aulaPorTipo.keys():
        etiqueta = etree.SubElement(EtiquetasAsignaturas, "Activity_Tag")
        etree.SubElement(etiqueta, "Name").text = tipoAu
        etree.SubElement(etiqueta, "Printable").text = "true"
        etree.SubElement(etiqueta, "Comments").text = ""


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
                subGrupoXML = etree.SubElement(grupoXML, "Subgroup")
                etree.SubElement(subGrupoXML, "Name").text = alumnosAsig.getNombre()
                etree.SubElement(subGrupoXML, "Number_of_Students").text = str(alumnosAsig.getNumAlumnos())
                etree.SubElement(subGrupoXML, "Comments").text = ""

    # Lista Actividades
    listaActividades = etree.SubElement(root, "Activities_List")
    i = 1 
    for actividad in actividades:
        actividadXML = etree.SubElement(listaActividades, "Activity")
        if tipo == "Examen":
            etree.SubElement(actividadXML, "Subject").text = actividad.getAsignatura()
            etree.SubElement(actividadXML, "Activity_Tag").text = actividad.getTipoAula()
            for curso in actividad.getCurso():
                etree.SubElement(actividadXML, "Students").text = curso
            etree.SubElement(actividadXML, "Duration").text = str(actividad.getDuracion())
            etree.SubElement(actividadXML, "Total_Duration").text = str(actividad.getDuracion())
            etree.SubElement(actividadXML, "Id").text = str(i)
            etree.SubElement(actividadXML, "Activity_Group_Id").text = "0"
            etree.SubElement(actividadXML, "Active").text = "true"
            etree.SubElement(actividadXML, "Comments").text = ""
            i += 1
        else:
            etree.SubElement(actividadXML, "Subject").text = actividad.getAsignatura()
            etree.SubElement(actividadXML, "Activity_Tag").text = actividad.getTipoAula()
            for curso in actividad.getCurso():
                etree.SubElement(actividadXML, "Students").text = curso
            etree.SubElement(actividadXML, "Duration").text = str(actividad.getDuracion())
            etree.SubElement(actividadXML, "Total_Duration").text = str(actividad.getDuracionTotal())
            etree.SubElement(actividadXML, "Id").text = str(actividad.getIdActividad())
            etree.SubElement(actividadXML, "Activity_Group_Id").text = str(actividad.getIdGrupo())
            etree.SubElement(actividadXML, "Active").text = "true"
            etree.SubElement(actividadXML, "Comments").text = ""
            for hija in actividad.getActividadesHija():
                actividadHijaXML = etree.SubElement(listaActividades, "Activity")
                etree.SubElement(actividadHijaXML, "Subject").text = hija.getAsignatura()
                for curso in actividad.getCurso():
                    etree.SubElement(actividadHijaXML, "Students").text = curso
                etree.SubElement(actividadHijaXML, "Duration").text = str(hija.getDuracion())
                etree.SubElement(actividadHijaXML, "Total_Duration").text = str(hija.getDuracionTotal())
                etree.SubElement(actividadHijaXML, "Id").text = str(hija.getIdActividad())
                etree.SubElement(actividadHijaXML, "Activity_Group_Id").text = str(hija.getIdGrupo())
                etree.SubElement(actividadHijaXML, "Active").text = "true"
                etree.SubElement(actividadHijaXML, "Comments").text = ""
            
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
                                etree.SubElement(combinacionXML, "Real_Room").text = aulaComb.getNumero() + "-" + aulaComb.getEdificio()
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
    # Restriccion basica
    constraint_time = etree.SubElement(time_constraints, "ConstraintBasicCompulsoryTime")
    etree.SubElement(constraint_time, "Weight_Percentage").text = "100"
    etree.SubElement(constraint_time, "Active").text = "true"
    etree.SubElement(constraint_time, "Comments").text = ""

    if tipo == "Examen":
        for restriccion in restriccionesTiempo:
            if restriccion.getEstado():
                match restriccion.getNombre():
                    #Restriccion asignaturas cursos consecutivos separadas 48h
                    case "MismoCursoSeparado48h":
                        for curso in actividadesPorCuros:
                            # Dividir el curso en dos partes: el texto y el número final
                            grado, numcurso = curso.rsplit("-", 1)
                            # Crear el nuevo string con el número consecutivo
                            cursoConsecutivo = f"{grado}-{str(int(numcurso) + 1)}"

                            if cursoConsecutivo in actividadesPorCuros:
                                for actividadInicial in actividadesPorCuros[curso]:
                                    for actividadConsecutiva in actividadesPorCuros[cursoConsecutivo]:
                                        constraint_mismoCuros = etree.SubElement(time_constraints, "ConstraintMinDaysBetweenActivities")
                                        etree.SubElement(constraint_mismoCuros, "Weight_Percentage").text = str(restriccion.getObligatoria())
                                        etree.SubElement(constraint_mismoCuros, "Consecutive_If_Same_Day").text = "false"
                                        etree.SubElement(constraint_mismoCuros, "Number_of_Activities").text = "2"
                                        etree.SubElement(constraint_mismoCuros, "Activity_Id").text = str(actividadInicial.getIdActividad())
                                        etree.SubElement(constraint_mismoCuros, "Activity_Id").text = str(actividadConsecutiva.getIdActividad())
                                        etree.SubElement(constraint_mismoCuros, "MinDays").text = "1"
                                        etree.SubElement(constraint_mismoCuros, "Active").text = "true"
                                        etree.SubElement(constraint_mismoCuros, "Comments").text = ""

                    # Restriccion asignaturas mismo curso separadas 24h
                    case "CursosConsecutivosSeparado24h":
                        for curso in actividadesPorCuros:
                            constraint_mismoCuros = etree.SubElement(time_constraints, "ConstraintMinDaysBetweenActivities")
                            etree.SubElement(constraint_mismoCuros, "Weight_Percentage").text = str(restriccion.getObligatoria())
                            etree.SubElement(constraint_mismoCuros, "Consecutive_If_Same_Day").text = "false"
                            etree.SubElement(constraint_mismoCuros, "Number_of_Activities").text = str(len(actividadesPorCuros[curso]))

                            for actividad in actividadesPorCuros[curso]:
                                etree.SubElement(constraint_mismoCuros, "Activity_Id").text = str(actividad.getIdActividad())

                            etree.SubElement(constraint_mismoCuros, "MinDays").text = "2"
                            etree.SubElement(constraint_mismoCuros, "Active").text = "true"
                            etree.SubElement(constraint_mismoCuros, "Comments").text = ""

                    # Restriccion dos examenes son el mismo dia y hora
                    case "RestriccionExamenesMismoDia": 
                        constraint_mismoDia = etree.SubElement(time_constraints, "ConstraintActivitiesSameStartingTime")
                        etree.SubElement(constraint_mismoDia, "Weight_Percentage").text = str(restriccion.getObligatoria())
                        etree.SubElement(constraint_mismoDia, "Number_of_Activities").text = "2"
                        etree.SubElement(constraint_mismoDia, "Activity_Id").text = str(restriccion.getDatos()["Actividad"].getIdActividad())
                        etree.SubElement(constraint_mismoDia, "Activity_Id").text = str(restriccion.getDatos()["Actividad2"].getIdActividad())
                        etree.SubElement(constraint_mismoDia, "Active").text = "true"
                        etree.SubElement(constraint_mismoDia, "Comments").text = ""
                    
                    # Restriccion separacion entre dos asignaturas
                    case "RestriccionXDiasEntreActividades":
                        constraint_separacionclases = etree.SubElement(time_constraints, "ConstraintMinDaysBetweenActivities")
                        etree.SubElement(constraint_separacionclases, "Weight_Percentage").text = str(restriccion.getObligatoria())
                        etree.SubElement(constraint_separacionclases, "Consecutive_If_Same_Day").text = "false"
                        etree.SubElement(constraint_separacionclases, "Number_of_Activities").text = str(len(restriccion.getDatos()["Actividades"]))
                        for actividad in restriccion.getDatos()["Actividades"]:
                            etree.SubElement(constraint_separacionclases, "Activity_Id").text = str(actividad.getIdActividad())
                        etree.SubElement(constraint_separacionclases, "MinDays").text = str(restriccion.getDatos()["Separacion"])
                        etree.SubElement(constraint_separacionclases, "Active").text = "true"
                        etree.SubElement(constraint_separacionclases, "Comments").text = ""
    else:
        for restriccion in restriccionesTiempo:
            if restriccion.getEstado():
                match restriccion.getNombre():
                    # Restriccion separacion entre dos asignaturas
                    case "RestriccionXDiasEntreActividades" | "SeparacionClasesMismaAsignatura":
                        constraint_separacionclases = etree.SubElement(time_constraints, "ConstraintMinDaysBetweenActivities")
                        etree.SubElement(constraint_separacionclases, "Weight_Percentage").text = str(restriccion.getObligatoria())
                        etree.SubElement(constraint_separacionclases, "Consecutive_If_Same_Day").text = "false"
                        etree.SubElement(constraint_separacionclases, "Number_of_Activities").text = str(len(restriccion.getDatos()["Actividades"]))
                        for actividad in restriccion.getDatos()["Actividades"]:
                            etree.SubElement(constraint_separacionclases, "Activity_Id").text = str(actividad.getIdActividad())
                        etree.SubElement(constraint_separacionclases, "MinDays").text = str(restriccion.getDatos()["Separacion"])
                        etree.SubElement(constraint_separacionclases, "Active").text = "true"
                        etree.SubElement(constraint_separacionclases, "Comments").text = ""

                    # Turno de la asignatura
                    case "RestriccionTurno":
                        formato = "%H:%M"
                        horaini = datetime.strptime(restriccion.getDatos()["HoraIni"], formato)
                        horafin = datetime.strptime(restriccion.getDatos()["HoraFin"], formato)
                        turno = []

                        while horaini <= horafin:
                            turno.append(horaini.strftime(formato))
                            horaini += timedelta(hours=1)

                        for actividad in actividadesPorCuros[restriccion.getDatos()["Curso"]]:
                            constraint_turnoActividad= etree.SubElement(time_constraints, "ConstraintActivityPreferredTimeSlots")
                            etree.SubElement(constraint_turnoActividad, "Weight_Percentage").text = str(restriccion.getObligatoria())
                            etree.SubElement(constraint_turnoActividad, "Activity_Id").text = str(actividad.getIdActividad())
                            etree.SubElement(constraint_turnoActividad, "Number_of_Preferred_Time_Slots").text = str(dias.getNumDias() * len(turno))

                            for dia in dias.getDias():
                                for hora in turno:
                                    horaElegida = etree.SubElement(constraint_turnoActividad, "Preferred_Time_Slot")
                                    etree.SubElement(horaElegida, "Preferred_Day").text = str(dia)
                                    etree.SubElement(horaElegida, "Preferred_Hour").text = hora

                            etree.SubElement(constraint_turnoActividad, "Active").text = "true"
                            etree.SubElement(constraint_turnoActividad, "Comments").text = ""
                            for actividadHija in actividad.getActividadesHija():
                                constraint_turnoActividad= etree.SubElement(time_constraints, "ConstraintActivityPreferredTimeSlots")
                                etree.SubElement(constraint_turnoActividad, "Weight_Percentage").text = str(restriccion.getObligatoria())
                                etree.SubElement(constraint_turnoActividad, "Activity_Id").text = str(actividad.getIdActividad())
                                etree.SubElement(constraint_turnoActividad, "Number_of_Preferred_Time_Slots").text = str(dias.getNumDias() * len(turno))

                                for dia in dias.getDias():
                                    for hora in turno:
                                        horaElegida = etree.SubElement(constraint_turnoActividad, "Preferred_Time_Slot")
                                        etree.SubElement(horaElegida, "Preferred_Day").text = str(dia)
                                        etree.SubElement(horaElegida, "Preferred_Hour").text = hora

                                etree.SubElement(constraint_turnoActividad, "Active").text = "true"
                                etree.SubElement(constraint_turnoActividad, "Comments").text = ""

                    # Max Horas clase por día
                    case "MaxHorasPorDia":
                        constraint_maxHorasDia= etree.SubElement(time_constraints, "ConstraintStudentsSetMaxHoursDaily")
                        etree.SubElement(constraint_maxHorasDia, "Weight_Percentage").text = str(restriccion.getObligatoria())
                        etree.SubElement(constraint_maxHorasDia, "Maximum_Hours_Daily").text = str(restriccion.getDatos()["Horas"])
                        etree.SubElement(constraint_maxHorasDia, "Students").text = restriccion.getDatos()["Curso"]
                        etree.SubElement(constraint_maxHorasDia, "Active").text = "true"
                        etree.SubElement(constraint_maxHorasDia, "Comments").text = ""

                    # Max Huecos entre clases por semana
                    case "MaxHuecosPorSemana":
                        constraint_maxHorasDia= etree.SubElement(time_constraints, "ConstraintStudentsSetMaxGapsPerWeek")
                        etree.SubElement(constraint_maxHorasDia, "Weight_Percentage").text = str(restriccion.getObligatoria())
                        etree.SubElement(constraint_maxHorasDia, "Max_Gaps").text = str(restriccion.getDatos()["Horas"])
                        etree.SubElement(constraint_maxHorasDia, "Students").text = restriccion.getDatos()["Curso"]
                        etree.SubElement(constraint_maxHorasDia, "Active").text = "true"
                        etree.SubElement(constraint_maxHorasDia, "Comments").text = ""
                        
    # Restricciones de Lugar
    space_constraints = etree.SubElement(root, "Space_Constraints_List")
    # Restriccion Basica
    constraint_space = etree.SubElement(space_constraints, "ConstraintBasicCompulsorySpace")
    etree.SubElement(constraint_space, "Weight_Percentage").text = "100"
    etree.SubElement(constraint_space, "Active").text = "true"
    etree.SubElement(constraint_space, "Comments").text = ""

    for tipoAu, aulas in aulaPorTipo.items():
        constraint_tipoAulas = etree.SubElement(space_constraints, "ConstraintActivityTagPreferredRooms")
        etree.SubElement(constraint_tipoAulas, "Weight_Percentage").text = "100"
        etree.SubElement(constraint_tipoAulas, "Activity_Tag").text = tipoAu
        etree.SubElement(constraint_tipoAulas, "Number_of_Preferred_Rooms").text = str(len(aulas))
        for aula in aulas:
            etree.SubElement(constraint_tipoAulas, "Preferred_Room").text = str(aula.getNumero() + "-" + aula.getEdificio())

        etree.SubElement(constraint_tipoAulas, "Active").text = "true"
        etree.SubElement(constraint_tipoAulas, "Comments").text = ""

    for restriccion in restriccionesLugar:
        if restriccion.getEstado():
            match restriccion.getNombre():
                # Restriccion de Examens por Campus
                case "MismoCampusDondeSeImparte":
                    if len(aulaPorCampus) > 1:
                        i = 1
                        for actividad in actividades:
                            campus = actividad.getCampus()
                            aulas = aulaPorCampus[campus]

                            constraint_examenCampus = etree.SubElement(space_constraints, "ConstraintActivityPreferredRooms")
                            etree.SubElement(constraint_examenCampus, "Weight_Percentage").text = str(restriccion.getObligatoria())
                            etree.SubElement(constraint_examenCampus, "Activity_Id").text = str(i)
                            etree.SubElement(constraint_examenCampus, "Number_of_Preferred_Rooms").text = str(len(aulas))
                            for aula in aulas:
                                etree.SubElement(constraint_examenCampus, "Preferred_Room").text = str(aula.getNumero() + "-" + aula.getEdificio())

                            etree.SubElement(constraint_examenCampus, "Active").text = "true"
                            etree.SubElement(constraint_examenCampus, "Comments").text = ""
                            i += 1

    with open(path, "wb") as file:
        file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
