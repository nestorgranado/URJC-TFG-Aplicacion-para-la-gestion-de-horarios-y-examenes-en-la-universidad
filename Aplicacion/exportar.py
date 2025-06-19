from collections import defaultdict
import pandas as pd
import os
from estructuraDatos import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import platform

# Funcion que quita comas
def quitar_comas(texto):
    return texto.replace(',', '')

# Funcion para quitar comas de los nombres de las asignaturas de una lista
def quitar_comasLista(lista):
    # Eliminar comas de cada elemento
    lista_sin_comas = [elemento.replace(',', '') for elemento in lista]
    
    # Unir los elementos con comas
    return ', '.join(lista_sin_comas)

# Exportar las Titulaciones
def exportarTitulaciones(root, universidad):
    # Por cada escuela crear un elemnto "Escuela" y un atributo "Nombre" y recorrer la lista de Titulcaiones
    titulacionesListXML = ET.SubElement(root, "ListaTitulaciones")
    for titulacion in universidad.getTitulacion():
        titulacionXML = ET.SubElement(titulacionesListXML, "Titulación")
        ET.SubElement(titulacionXML, "Código").text = titulacion.getCodigo()
        ET.SubElement(titulacionXML, "Nombre").text = quitar_comas(titulacion.getNombre())
        ET.SubElement(titulacionXML, "Campus").text = titulacion.getCampus()
        for asignatura in titulacion.getAsignaturas():
            asignaturaXML = ET.SubElement(titulacionXML, "Asignatura")
            ET.SubElement(asignaturaXML, "Código").text = asignatura.getCodigo()
            ET.SubElement(asignaturaXML, "Nombre").text = quitar_comas(asignatura.getNombre())
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

# Exportar las Instituciones(Campus y Titulaciones)
def exportarInstitucion(root, universidad):
    # Nombre de la institucion
    ET.SubElement(root, "Nombre").text = universidad.getNombre()

    # Exportar Campus y Titulaciones
    exportarCampus(root, universidad)
    exportarTitulaciones(root, universidad)

# Exportar Cursos
def exportarCursos(root, alumnos):
    for alumnosTit in alumnos:
        alumnosTitXML = ET.SubElement(root, "AlumnosTitulacion")
        ET.SubElement(alumnosTitXML, "Nombre").text = quitar_comas(alumnosTit.getNombre())
        ET.SubElement(alumnosTitXML, "NúmeroAlumnos").text = str(alumnosTit.getNumAlumnos())
        for alumnosCurso in alumnosTit.getCursos():
            alumnosCursoXML = ET.SubElement(alumnosTitXML, "AlumnosCurso")
            ET.SubElement(alumnosCursoXML, "Nombre").text = quitar_comas(alumnosCurso.getNombre())
            ET.SubElement(alumnosCursoXML, "NúmeroAlumnos").text = str(alumnosCurso.getNumAlumnos())
            for alumnosAsig in alumnosCurso.getAsignaturas():
                alumnosAsigXML = ET.SubElement(alumnosCursoXML, "AlumnosAsignatura")
                ET.SubElement(alumnosAsigXML, "Nombre").text = quitar_comas(alumnosAsig.getNombre())
                ET.SubElement(alumnosAsigXML, "NúmeroAlumnos").text = str(alumnosAsig.getNumAlumnos())

# Exportar Días por Semana
def exportarDias(root, diasSemanaClases, diasSemanaExamenes):
    clasesXML = ET.SubElement(root, "Clases")
    ET.SubElement(clasesXML, "NumeroDias").text = str(diasSemanaClases.getNumDias())

    for dia in diasSemanaClases.getDias():
        diaXML = ET.SubElement(clasesXML, "Dia")
        ET.SubElement(diaXML, "Nombre").text = dia

    examenesXML = ET.SubElement(root, "Examenes")
    ET.SubElement(examenesXML, "NumeroDias").text = str(diasSemanaExamenes.getNumDias())

    for dia in diasSemanaExamenes.getDias():
        diaXML = ET.SubElement(examenesXML, "Dia")
        ET.SubElement(diaXML, "Nombre").text = dia

# Exportar Horas por Día
def exportarHoras(root, horasDiaClases, horasDiaExamenes):
    clasesXML = ET.SubElement(root, "Clases")
    ET.SubElement(clasesXML, "NumeroHoras").text = str(horasDiaClases.getNumHoras())

    for hora in horasDiaClases.getHoras():
        horaXML = ET.SubElement(clasesXML, "Hora")
        ET.SubElement(horaXML, "Nombre").text = hora

    examenesXML = ET.SubElement(root, "Examenes")
    ET.SubElement(examenesXML, "NumeroHoras").text = str(horasDiaExamenes.getNumHoras())

    for hora in horasDiaExamenes.getHoras():
        horaXML = ET.SubElement(examenesXML, "Hora")
        ET.SubElement(horaXML, "Nombre").text = hora

# Exportar Asignaturas
def exportarAsignaturas(root, asignaturas):
    for asignatura in asignaturas:
        asignaturaXML = ET.SubElement(root, "Asignatura")
        ET.SubElement(asignaturaXML, "Codigo").text = str(asignatura.getCodigo())
        ET.SubElement(asignaturaXML, "Nombre").text = quitar_comas(asignatura.getNombre())
        ET.SubElement(asignaturaXML, "Titulacion").text = quitar_comas(asignatura.getTitulacion())
        ET.SubElement(asignaturaXML, "NumAlumnos").text = str(asignatura.getNumAlumnos())
        ET.SubElement(asignaturaXML, "Curso").text = str(asignatura.getCurso())
        if asignatura.getAsignaturas_hijas():
            hijasXML = ET.SubElement(asignaturaXML, "AsignaturasHijas")
            for hija in asignatura.getAsignaturas_hijas():
                hijaXML = ET.SubElement(hijasXML, "AsignaturaHija")
                ET.SubElement(hijaXML, "PlanHija").text = quitar_comas(hija[0])
                ET.SubElement(hijaXML, "Asignatura").text = quitar_comas(hija[1])

# Exportar Actividades
def exportarActividades(root, actividadesCl, actividadesEx):
    i = 0
    for tipoHorario in [actividadesCl, actividadesEx]:
        actividadesXML = None
        if i == 0:
            actividadesXML = ET.SubElement(root, "Clases")
        elif i == 1:
             actividadesXML = ET.SubElement(root, "Examenes")

        for act in tipoHorario:
            activiadXML = ET.SubElement(actividadesXML, "Actividad")
            ET.SubElement(activiadXML, "Id").text = str(act.getIdActividad())
            ET.SubElement(activiadXML, "IdGrupo").text = str(act.getIdGrupo())
            ET.SubElement(activiadXML, "Asignatura").text = quitar_comas(act.getAsignatura())
            ET.SubElement(activiadXML, "Titulaciones").text = quitar_comasLista(act.getTitulacion())
            ET.SubElement(activiadXML, "Campus").text = act.getCampus()
            ET.SubElement(activiadXML, "Cursos").text = quitar_comasLista(act.getCurso())
            ET.SubElement(activiadXML, "Duracion").text = str(act.getDuracion())
            ET.SubElement(activiadXML, "DuracionTotal").text = str(act.getDuracionTotal())
            ET.SubElement(activiadXML, "TipoAula").text = act.getTipoAula()
            if act.getRestIndex() != None:
                ET.SubElement(activiadXML, "RestIndex").text = str(act.getRestIndex())
            if act.getActividadesHija():
                listaHijaXML = ET.SubElement(activiadXML, "ActividadesHijas")
                for actHija in act.getActividadesHija():
                    hijaXML = ET.SubElement(listaHijaXML, "ActividadHija")
                    ET.SubElement(hijaXML, "Id").text = str(actHija.getIdActividad())
                    ET.SubElement(hijaXML, "IdGrupo").text = str(actHija.getIdGrupo())
                    ET.SubElement(hijaXML, "Asignatura").text = quitar_comas(actHija.getAsignatura())
                    ET.SubElement(hijaXML, "Titulaciones").text = quitar_comasLista(actHija.getTitulacion())
                    ET.SubElement(hijaXML, "Campus").text = actHija.getCampus()
                    ET.SubElement(hijaXML, "Cursos").text = quitar_comasLista(actHija.getCurso())
                    ET.SubElement(hijaXML, "Duracion").text = str(actHija.getDuracion())
                    ET.SubElement(hijaXML, "DuracionTotal").text = str(actHija.getDuracionTotal())
                    ET.SubElement(hijaXML, "TipoAula").text = actHija.getTipoAula()
        i += 1    
# Exportar Restricciones
def exportarRestricciones(root, restriccionesC, restriccionesE):
    i = 0
    for restriccionesHorario in [restriccionesC, restriccionesE]:
        restXML = None
        if i == 0:
            restXML = ET.SubElement(root, "Clases")
        elif i == 1:
            restXML = ET.SubElement(root, "Examenes")
        
        rTiempoXML = ET.SubElement(restXML, "RestriccionesTiempo")

        for restriccion in restriccionesHorario["RestriccionesTiempo"]:
            restriccionXML = ET.SubElement(rTiempoXML, "Restriccion")
            ET.SubElement(restriccionXML, "Nombre").text = restriccion.getNombre()
            datosXML = ET.SubElement(restriccionXML, "Datos")
            for key, value in restriccion.getDatos().items():
                valorXML = ET.SubElement(datosXML, key)
                if isinstance(value, Actividad):
                    ET.SubElement(valorXML, "Id").text = str(value.getIdActividad())
                    ET.SubElement(valorXML, "IdGrupo").text = str(value.getIdGrupo())
                    ET.SubElement(valorXML, "Asignatura").text = quitar_comas(value.getAsignatura())
                    ET.SubElement(valorXML, "Titulaciones").text = quitar_comasLista(value.getTitulacion())
                    ET.SubElement(valorXML, "Campus").text = value.getCampus()
                    ET.SubElement(valorXML, "Cursos").text = quitar_comasLista(value.getCurso())
                    ET.SubElement(valorXML, "Duracion").text = str(value.getDuracion())
                    ET.SubElement(valorXML, "DuracionTotal").text = str(value.getDuracionTotal())
                    ET.SubElement(valorXML, "TipoAula").text = value.getTipoAula()
                    if value.getActividadesHija():
                        listaHijaXML = ET.SubElement(valorXML, "ActividadesHijas")
                        for actHija in value.getActividadesHija():
                            hijaXML = ET.SubElement(listaHijaXML, "ActividadHija")
                            ET.SubElement(hijaXML, "Id").text = str(actHija.getIdActividad())
                            ET.SubElement(hijaXML, "IdGrupo").text = str(actHija.getIdGrupo())
                            ET.SubElement(hijaXML, "Asignatura").text = quitar_comas(actHija.getAsignatura())
                            ET.SubElement(hijaXML, "Titulaciones").text = quitar_comasLista(actHija.getTitulacion())
                            ET.SubElement(hijaXML, "Campus").text = actHija.getCampus()
                            ET.SubElement(hijaXML, "Cursos").text = quitar_comasLista(actHija.getCurso())
                            ET.SubElement(hijaXML, "Duracion").text = str(actHija.getDuracion())
                            ET.SubElement(hijaXML, "DuracionTotal").text = str(actHija.getDuracionTotal())
                            ET.SubElement(hijaXML, "TipoAula").text = actHija.getTipoAula()
                elif isinstance(value, list):
                    for actividad in value:
                        actividadXML = ET.SubElement(valorXML, "Actividad")
                        ET.SubElement(actividadXML, "Id").text = str(actividad.getIdActividad())
                        ET.SubElement(actividadXML, "IdGrupo").text = str(actividad.getIdGrupo())
                        ET.SubElement(actividadXML, "Asignatura").text = quitar_comas(actividad.getAsignatura())
                        ET.SubElement(actividadXML, "Titulaciones").text = quitar_comasLista(actividad.getTitulacion())
                        ET.SubElement(actividadXML, "Campus").text = actividad.getCampus()
                        ET.SubElement(actividadXML, "Cursos").text = quitar_comasLista(actividad.getCurso())
                        ET.SubElement(actividadXML, "Duracion").text = str(actividad.getDuracion())
                        ET.SubElement(actividadXML, "DuracionTotal").text = str(actividad.getDuracionTotal())
                        ET.SubElement(actividadXML, "TipoAula").text = actividad.getTipoAula()
                        if actividad.getActividadesHija():
                            listaHijaXML = ET.SubElement(actividadXML, "ActividadesHijas")
                            for actHija in actividad.getActividadesHija():
                                hijaXML = ET.SubElement(listaHijaXML, "ActividadHija")
                                ET.SubElement(hijaXML, "Id").text = str(actHija.getIdActividad())
                                ET.SubElement(hijaXML, "IdGrupo").text = str(actHija.getIdGrupo())
                                ET.SubElement(hijaXML, "Asignatura").text = quitar_comas(actHija.getAsignatura())
                                ET.SubElement(hijaXML, "Titulaciones").text = quitar_comasLista(actHija.getTitulacion())
                                ET.SubElement(hijaXML, "Campus").text = actHija.getCampus()
                                ET.SubElement(hijaXML, "Cursos").text = quitar_comasLista(actHija.getCurso())
                                ET.SubElement(hijaXML, "Duracion").text = str(actHija.getDuracion())
                                ET.SubElement(hijaXML, "DuracionTotal").text = str(actHija.getDuracionTotal())
                                ET.SubElement(hijaXML, "TipoAula").text = actHija.getTipoAula()
                else:   
                    valorXML.text = str(value)
            
            ET.SubElement(restriccionXML, "Obligatoria").text = str(restriccion.isObligatoria())
            ET.SubElement(restriccionXML, "Activa").text = str(restriccion.getActividad())
        
        # Exportar restricciones de Lugar
        rLugarXML = ET.SubElement(restXML, "RestriccionesLugar")
        for restriccion in restriccionesHorario["RestriccionesLugar"]:
            restriccionXML = ET.SubElement(rLugarXML, "Restriccion")
            ET.SubElement(restriccionXML, "Nombre").text = restriccion.getNombre()
            datosXML = ET.SubElement(restriccionXML, "Datos")
            for key, value in restriccion.getDatos().items():
                valorXML = ET.SubElement(datosXML, key)
                if isinstance(value, Actividad):
                    ET.SubElement(valorXML, "Id").text = str(value.getIdActividad())
                    ET.SubElement(valorXML, "IdGrupo").text = str(value.getIdGrupo())
                    ET.SubElement(valorXML, "Asignatura").text = quitar_comas(value.getAsignatura())
                    ET.SubElement(valorXML, "Titulaciones").text = quitar_comasLista(value.getTitulacion())
                    ET.SubElement(valorXML, "Campus").text = value.getCampus()
                    ET.SubElement(valorXML, "Cursos").text = quitar_comasLista(value.getCurso())
                    ET.SubElement(valorXML, "Duracion").text = str(value.getDuracion())
                    ET.SubElement(valorXML, "DuracionTotal").text = str(value.getDuracionTotal())
                    ET.SubElement(valorXML, "TipoAula").text = value.getTipoAula()
                    if value.getActividadesHija():
                        listaHijaXML = ET.SubElement(valorXML, "ActividadesHijas")
                        for actHija in value.getActividadesHija():
                            hijaXML = ET.SubElement(listaHijaXML, "ActividadHija")
                            ET.SubElement(hijaXML, "Id").text = str(actHija.getIdActividad())
                            ET.SubElement(hijaXML, "IdGrupo").text = str(actHija.getIdGrupo())
                            ET.SubElement(hijaXML, "Asignatura").text = quitar_comas(actHija.getAsignatura())
                            ET.SubElement(hijaXML, "Titulaciones").text = quitar_comasLista(actHija.getTitulacion())
                            ET.SubElement(hijaXML, "Campus").text = actHija.getCampus()
                            ET.SubElement(hijaXML, "Cursos").text = quitar_comasLista(actHija.getCurso())
                            ET.SubElement(hijaXML, "Duracion").text = str(actHija.getDuracion())
                            ET.SubElement(hijaXML, "DuracionTotal").text = str(actHija.getDuracionTotal())
                            ET.SubElement(hijaXML, "TipoAula").text = actHija.getTipoAula()
                else:   
                    valorXML.text = str(value)

            ET.SubElement(restriccionXML, "Obligatoria").text = str(restriccion.isObligatoria())
            ET.SubElement(restriccionXML, "Activa").text = str(restriccion.getActividad())    
        
        i += 1

def exportar(path, universidad, alumnos, diasClases, diasExamenes, horasClases, horasExamenes, asignaturas, actividadesCl, actividadesEx, restriccionesC, restriccionesE):
    # Crear elementos raiz
    root = ET.Element("Datos")                              # Raiz archivo XML
    institucionXML = ET.SubElement(root, "Institucion")     # Crear Elemento raiz de la institución
    cursosXML = ET.SubElement(root, "Cursos")               # Crear Elemento raiz de los cursos
    diasXML = ET.SubElement(root, "DiasPorSemana")          # Crear Elemento raiz de los días
    horasXML = ET.SubElement(root, "HorasporDia")           # Crear Elemento raiz de las horas
    asignaturasXML = ET.SubElement(root, "Asignaturas")     # Crear Elemento raiz de las asignaturas
    actividadXML = ET.SubElement(root, "Actividades")       # Crear Elemento raiz de las actividades(Clases o Examenes)
    restriccionesXML = ET.SubElement(root, "Restricciones") # Crear Elemento raiz de las Restricciones(tiempo o lugar)

    # Exportar los datos de la institucion
    exportarInstitucion(institucionXML, universidad)

    # Exportar los alumnos y los cursos
    if alumnos:
        exportarCursos(cursosXML, alumnos)
    else:
        cursosXML.text = ""

    # Exportar los dias y las horas
    exportarDias(diasXML, diasClases, diasExamenes)
    exportarHoras(horasXML, horasClases, horasExamenes)

    # Exportar asignaturas
    if asignaturas:
        exportarAsignaturas(asignaturasXML, asignaturas)
    else:
        asignaturasXML.text = ""

    # Exportar Actividades
    if actividadesCl or actividadesEx:
        exportarActividades(actividadXML, actividadesCl, actividadesEx)
    else:
        actividadXML.text = ""

    # Exportar Restricciones
    if restriccionesC["RestriccionesTiempo"] or restriccionesC["RestriccionesLugar"] or restriccionesE["RestriccionesTiempo"] or restriccionesE["RestriccionesLugar"]:
        exportarRestricciones(restriccionesXML, restriccionesC, restriccionesE)
    else:
        restriccionesXML.text = ""

    # Convertir el árbol XML a una cadena y guardar en el archivo especificado
    tree = ET.ElementTree(root)
    try:
        tree.write(path, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error al guardar el archivo XML: {e}")