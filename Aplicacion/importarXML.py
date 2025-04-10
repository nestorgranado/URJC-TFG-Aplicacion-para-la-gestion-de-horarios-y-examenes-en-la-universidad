from collections import defaultdict
import pandas as pd
import xml.etree.ElementTree as ET
import os
from estructuraDatos import *
import re
import unicodedata

# Función para quitar acentos a los nombres
def quitar_acentos(texto):
    # Normalizamos el texto para separar los caracteres base de sus acentos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Filtramos los caracteres que no sean marcas diacríticas
    texto_sin_acentos = ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')
    return texto_sin_acentos

# Función para buscar la asignatura por su nombre
def buscarAsignatura(asig, lista):
    for asignatura in lista:
        if asignatura.getNombre() == asig:
            return asignatura
    return None  

def importarXML(path):
    # cargar XML
    tree = ET.parse(path)
    # Obtener a raiz de XML
    root = tree.getroot()

    # Tipo Horario
    tipo = root.find('Horario').text
    
    # Crear la institución
    instituciónXML = root.find('Institucion')
    institucion = Universidad(instituciónXML.find('Nombre').text)

    # Diccionarios para guardar las aulas por campus y tipo
    aulasCampus_dict = defaultdict(list)
    aulasTipo_dict = defaultdict(list)

    # Importar Campus
    campusListXML = instituciónXML.find("ListaCampus")
    for campusXML in campusListXML.findall('Campus'):
        nombreCampus = campusXML.find('Nombre').text
        campus = Campus(nombreCampus)
        # Importar los edificios del campus
        for edificioXML in campusXML.findall('Edificio'):
            edificio = Edificio(edificioXML.find('Nombre').text)
            # Importar las aulas del edificio
            for aulaXML in edificioXML.findall('Aula'):
                if aulaXML.find("AulaCombinada").text == "False":
                    aula = Aula(
                        aulaXML.find('Número').text,
                        edificioXML.find('Nombre').text,
                        int(aulaXML.find('CapacidadClase').text),
                        int(aulaXML.find('CapacidadExamen').text),
                        aulaXML.find('Tipo').text
                    )

                    aulasTipo_dict["TODAS"].append(aula)
                    match aulaXML.find('Tipo').text:
                        case "AULA":
                            if " ".join(aulaXML.find('Número').text.split()[:2]) == "AULA MAGNA":
                                aulasTipo_dict["AULA MAGNA"].append(aula)
                            aulasTipo_dict["AULA"].append(aula)
                        case "SEMINARIO":
                            aulasTipo_dict["SEMINARIO"].append(aula)
                        case "LABORATORIO":
                            aulasTipo_dict["LABORATORIO"].append(aula)

                    edificio.agregar_aula(aula)
                    aulasCampus_dict[quitar_acentos(nombreCampus)].append((edificio.getNombre(), aula))

                else:
                    combinaciones = []
                    for combinacionXML in aulaXML.findall("Combinación"):
                        aulasCombinadas = []
                        for aulaCombinadaXML in combinacionXML.findall("Aula"):
                            newAula = Aula(
                                aulaCombinadaXML.find('Número').text,
                                edificioXML.find('Nombre').text,
                                int(aulaCombinadaXML.find('CapacidadClase').text),
                                int(aulaCombinadaXML.find('CapacidadExamen').text),
                                aulaCombinadaXML.find('Tipo').text
                            )
                            aulasCombinadas.append(newAula)
                        combinaciones.append(aulasCombinadas)
                    
                    aula = AulaCombinada(
                        aulaXML.find('Número').text,
                        edificioXML.find('Nombre').text,
                        int(aulaXML.find('CapacidadClase').text),
                        int(aulaXML.find('CapacidadExamen').text),
                        aulaXML.find('Tipo').text,
                        combinaciones
                    )

                    aulasTipo_dict["TODAS"].append(aula)
                    match aulaXML.find('Tipo').text:
                        case "AULA":
                            if " ".join(aulaCombinadaXML.find('Número').text.split()[:2]) == "AULA MAGNA":
                                aulasTipo_dict["AULA MAGNA"].append(aula)
                            aulasTipo_dict["AULA"].append(aula)
                        case "SEMINARIO":
                            aulasTipo_dict["SEMINARIO"].append(aula)
                        case "LABORATORIO":
                            aulasTipo_dict["LABORATORIO"].append(aula)

                    edificio.agregar_aula(aula)
                    aulasCampus_dict[quitar_acentos(nombreCampus)].append((edificio.getNombre(), aula))

            campus.agregar_edificio(edificio)
        institucion.agregar_campus(campus)

    # Importar Titulaciones
    titulacionesListXML =  instituciónXML.find("ListaTitulaciones")
    for titulacionesXML in titulacionesListXML.findall('Titulación'):
        titulacion = Titulacion(
            titulacionesXML.find('Código').text,
            titulacionesXML.find('Nombre').text,
            titulacionesXML.find('Campus').text
        )
        # Importar asignaturas de la titulación
        for asignaturaXML in titulacionesXML.findall('Asignatura'):
            asignatura = Asignatura(
                asignaturaXML.find('Código').text,
                asignaturaXML.find('Nombre').text,
                asignaturaXML.find('Titulación').text,
                int(asignaturaXML.find('NumAlumnos').text),
                int(asignaturaXML.find('Curso').text)
            )
            for hijaXML in asignaturaXML.findall('AsignaturaHija'):
                asignatura.agregar_hija((hijaXML.find('Código').text, hijaXML.find('Nombre').text))

            titulacion.agregar_asignatura(asignatura)
        institucion.agregar_titulacion(titulacion)
    
    # Importar alumnos
    listaCursosXML = root.find('Cursos')
    alumnos = []

    for cursoTitXML in listaCursosXML.findall('AlumnosTitulacion'):
        alumnosTit = AlumnosTitulacion(cursoTitXML.find('Nombre').text)
        for cursoAlXML in cursoTitXML.findall('AlumnosCurso'):
            alumnosCur = AlumnosCurso(cursoAlXML.find('Nombre').text)
            for cursoAsig in cursoAlXML.findall('AlumnosAsignatura'):
                nombre = cursoAsig.find('Nombre').text
                numAlum = int(cursoAsig.find('NúmeroAlumnos').text)
                alumnosAsig = AlumnosAsignatura(nombre, numAlum)

                alumnosCur.agregar_asignatura(alumnosAsig)
            alumnosTit.agregar_curso(alumnosCur)
        alumnos.append(alumnosTit)
    
    # Importar Días
    diasListXML =  root.find("DiasPorSemana")

    diasClaseXML = diasListXML.find("Clases")
    diasSemanaClase = Dias()
    dias = []
    for diaXML in diasClaseXML.findall('Dia'):
        dias.append(diaXML.find('Nombre').text)
    diasSemanaClase.setDias(dias)

    diasExamenesXML = diasListXML.find("Examenes")
    diasSemanaExamen = Dias()
    dias = []
    for diaXML in diasExamenesXML.findall('Dia'):
        dias.append(diaXML.find('Nombre').text)
    diasSemanaExamen.setDias(dias)

    # Importar Horas
    horasListXML =  root.find("HorasporDia")

    horasClaseXML = horasListXML.find("Clases")
    horasDiaClase = Horas()
    horas = []
    for horaXML in horasClaseXML.findall('Hora'):
        horas.append(horaXML.find('Nombre').text)
    horasDiaClase.setHoras(horas)

    horasExamenesXML = horasListXML.find("Examenes")
    horasDiaExamen = Horas()
    horas = []
    for horaXML in horasExamenesXML.findall('Hora'):
        horas.append(horaXML.find('Nombre').text)
    horasDiaExamen.setHoras(horas)

    # Importar Asignaturas
    asignaturasListXML = root.find("Asignaturas")
    asignaturas = []

    for asignaturaXML in asignaturasListXML.findall('Asignatura'):
        cod = asignaturaXML.find('Codigo').text
        nombre = asignaturaXML.find('Nombre').text
        tit = asignaturaXML.find('Titulacion').text
        numAlum = int(asignaturaXML.find('NumAlumnos').text)
        curso = int(asignaturaXML.find('Curso').text)

        asignatura = Asignatura(cod, nombre, tit, numAlum, curso)

        hijasListXML = asignaturaXML.find('AsignaturasHijas')
        if hijasListXML is not None:
            asigHijas = []
            for hijaXML in hijasListXML.findall('AsignaturaHija'):
                plan = hijaXML.find('PlanHija').text
                hija = hijaXML.find('Asignatura').text
                asigHijas.append((plan, hija))
            
            asignatura.setAsignaturas_hijas(asigHijas)
        asignaturas.append(asignatura)
    
    # Importar Actividades
    actividadesListXML = root.find('Actividades')
    actividades = []
    actividadesCuros = defaultdict(list)

    for actividadXML in actividadesListXML.findall('Actividad'):
        idAct = int(actividadXML.find('Id').text)
        idGrupo = int(actividadXML.find('IdGrupo').text)
        asig = actividadXML.find('Asignatura').text
        titList = actividadXML.find('Titulaciones').text.split(", ")
        campus = actividadXML.find('Campus').text
        cursos = actividadXML.find('Cursos').text.split(", ")
        duracion = int(actividadXML.find('Duracion').text)
        duracionTot = int(actividadXML.find('DuracionTotal').text)
        tipoAula = actividadXML.find('TipoAula').text

        nuevaActividad = Actividad(idAct, idGrupo, asig, titList, campus, cursos, duracion, duracionTot, tipoAula)
        actividades.append(nuevaActividad)
        asignatura = buscarAsignatura(asig, asignaturas)
        actividadesCuros[str(titList[0] + "-" + str(asignatura.getCurso()))].append(nuevaActividad)

    # Importar Restricciones
    restriccionesListXML = root.find('Restricciones')
    # Restricciones de Tiempo
    restriccionesTListXML = restriccionesListXML.find('RestriccionesTiempo')
    restriccionesTiempo = []
    for restriccionXML in restriccionesTListXML.findall('Restriccion'):
        nombreRest = restriccionXML.find('Nombre').text
        obligatoria = restriccionXML.find('Obligatoria').text
        activa = restriccionXML.find('Activa').text
        datos = {}
        datosXML = restriccionXML.find('Datos')
        # Importat actividad si existe
        actividadXML = datosXML.find('Actividad')
        if actividadXML is not None:
            idAct = int(actividadXML.find('Id').text)
            idGrupo = int(actividadXML.find('IdGrupo').text)
            asig = actividadXML.find('Asignatura').text
            if idAct == 0:
                titList = []
                campus = ""
                cursos = []
            else:
                titList = actividadXML.find('Titulaciones').text.split(", ")
                campus = actividadXML.find('Campus').text
                cursos = actividadXML.find('Cursos').text.split(", ")

            duracion = int(actividadXML.find('Duracion').text)
            duracionTot = int(actividadXML.find('DuracionTotal').text)
            tipoAula = actividadXML.find('TipoAula').text

            datos["Actividad"] = Actividad(idAct, idGrupo, asig, titList, campus, cursos, duracion, duracionTot, tipoAula)

        # Importar actividad2 si existe
        actividad2XML = datosXML.find('Actividad2')
        if actividad2XML is not None:
            idAct2 = int(actividad2XML.find('Id').text)
            idGrupo2 = int(actividad2XML.find('IdGrupo').text)
            asig2 = actividad2XML.find('Asignatura').text
            titList2 = actividad2XML.find('Titulaciones').text.split(", ")
            campus2 = actividad2XML.find('Campus').text
            cursos2 = actividad2XML.find('Cursos').text.split(", ")
            duracion2 = int(actividad2XML.find('Duracion').text)
            duracionTot2 = int(actividad2XML.find('DuracionTotal').text)
            tipoAula2 = actividad2XML.find('TipoAula').text

            datos["Actividad2"] = Actividad(idAct2, idGrupo2, asig2, titList2, campus2, cursos2, duracion2, duracionTot2, tipoAula2)

        # Importar lista de actividades si existe
        actividadesXML = datosXML.find('Actividades')
        if actividadesXML is not None:
            for actividadXML in actividadesXML.findall("Actividad"):
                idAct = int(actividadXML.find('Id').text)
                idGrupo = int(actividadXML.find('IdGrupo').text)
                asig = actividadXML.find('Asignatura').text
                titList = actividadXML.find('Titulaciones').text.split(", ")
                campus = actividadXML.find('Campus').text
                cursos = actividadXML.find('Cursos').text.split(", ")
                duracion = int(actividadXML.find('Duracion').text)
                duracionTot = int(actividadXML.find('DuracionTotal').text)
                tipoAula = actividadXML.find('TipoAula').text

                datos["Actividades"].append(Actividad(idAct, idGrupo, asig, titList, campus, cursos, duracion, duracionTot, tipoAula))

        # Importar separacion si existe
        separacionXML = datosXML.find('Separacion')
        if separacionXML is not None:
            datos["Separacion"] = int(separacionXML.text)

        # Importar tipoAula si existe
        tipoXML = datosXML.find('Tipo')
        if tipoXML is not None:
            datos["Tipo"] = tipoXML.text

        # Importar Curso si existe
        cursoXML = datosXML.find('Curso')
        if cursoXML is not None:
            datos["Curso"] = cursoXML.text
        
        # Importar HoraInicio y HoraFin si existe
        iniXML = datosXML.find('HoraIni')
        finXML = datosXML.find('HoraFin')
        if None not in (iniXML, finXML):
            datos["HoraIni"] = iniXML.text
            datos["HoraFin"] = finXML.text

        # Importar Horas si existe
        horasXML = datosXML.find('Horas')
        if horasXML is not None:
            datos["Horas"] = horasXML.text 

        restriccionesTiempo.append(Restriccion(nombreRest, datos, obligatoria, activa))

    # Restricciones de Lugar
    restriccionesLListXML = restriccionesListXML.find('RestriccionesLugar')
    restriccionesLugar = []
    for restriccionXML in restriccionesLListXML.findall('Restriccion'):
        nombreRest = restriccionXML.find('Nombre').text
        obligatoria = restriccionXML.find('Obligatoria').text
        activa = restriccionXML.find('Activa').text
        datos = {}
        datosXML = restriccionXML.find('Datos')
        # Importat actividad si existe
        actividadXML = datosXML.find('Actividad')
        if actividadXML is not None:
            idAct = int(actividadXML.find('Id').text)
            idGrupo = int(actividadXML.find('IdGrupo').text)
            asig = actividadXML.find('Asignatura').text
            if idAct == 0:
                titList = []
                campus = ""
                cursos = []
            else:
                titList = actividadXML.find('Titulaciones').text.split(", ")
                campus = actividadXML.find('Campus').text
                cursos = actividadXML.find('Cursos').text.split(", ")

            duracion = int(actividadXML.find('Duracion').text)
            duracionTot = int(actividadXML.find('DuracionTotal').text)
            tipoAula = actividadXML.find('TipoAula').text

            datos["Actividad"] = Actividad(idAct, idGrupo, asig, titList, campus, cursos, duracion, duracionTot, tipoAula)

        # Importar actividad2 si existe
        actividad2XML = datosXML.find('Actividad2')
        if actividad2XML is not None:
            idAct2 = int(actividad2XML.find('Id').text)
            idGrupo2 = int(actividad2XML.find('IdGrupo').text)
            asig2 = actividad2XML.find('Asignatura').text
            titList2 = actividad2XML.find('Titulaciones').text.split(", ")
            campus2 = actividad2XML.find('Campus').text
            cursos2 = actividad2XML.find('Cursos').text.split(", ")
            duracion2 = int(actividad2XML.find('Duracion').text)
            duracionTot2 = int(actividad2XML.find('DuracionTotal').text)
            tipoAula2 = actividad2XML.find('TipoAula').text

            datos["Actividad2"] = Actividad(idAct2, idGrupo2, asig2, titList2, campus2, cursos2, duracion2, duracionTot2, tipoAula2)

        # Importar separacion si existe
        separacionXML = datosXML.find('Separacion')
        if separacionXML is not None:
            datos["Separacion"] = int(separacionXML.text)

        # Importar tipoAula si existe
        tipoXML = datosXML.find('Tipo')
        if tipoXML is not None:
            datos["Tipo"] = tipoXML.text

        # Importar Curso si existe
        cursoXML = datosXML.find('Curso')
        if cursoXML is not None:
            datos["Curso"] = cursoXML.text
        
        # Importar HoraInicio y HoraFin si existe
        iniXML = datosXML.find('HoraIni')
        finXML = datosXML.find('HoraFin')
        if None not in (iniXML, finXML):
            datos["HoraIni"] = iniXML.text
            datos["HoraFin"] = finXML.text

        # Importar Horas si existe
        horasXML = datosXML.find('Horas')
        if horasXML is not None:
            datos["Horas"] = horasXML.text 

        restriccionesLugar.append(Restriccion(nombreRest, datos, obligatoria, activa))

    return institucion, alumnos, diasSemanaClase, diasSemanaExamen, horasDiaClase, horasDiaExamen, actividades, asignaturas, aulasCampus_dict, aulasTipo_dict, actividadesCuros, restriccionesTiempo, restriccionesLugar, tipo

