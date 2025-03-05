
from collections import defaultdict
import pandas as pd
import xml.etree.ElementTree as ET
import os
from estructuraDatos import *
import re
import unicodedata

# Funcion para quitar acentos a los nombres
def quitar_acentos(texto):
    # Normalizamos el texto para separar los caracteres base de sus acentos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Filtramos los caracteres que no sean marcas diacríticas
    texto_sin_acentos = ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')
    return texto_sin_acentos

# Funciones para cargar el archivo según su tipo (CSV o Excel)
def cargar_archivo_Titulaciones(path):
    # Detectar la extensión del archivo
    _, extension = os.path.splitext(path)
    
    # Cargar el archivo según la extensión
    if extension == '.csv':
        df = pd.read_csv(path, delimiter=';', dtype={
            'COD_PLAN_PADRE': str,
            'PLAN_PADRE': str,
            'COD_ASIG_PADRE': str,
            'ASIG_PADRE': str,
            'COD_PLAN_HIJA': str,
            'PLAN_HIJA': str,
            'TOTAL': int,
            'CURSO_PADRE': int,
            "ASIG_HIJA": str
        })
    elif extension in ['.xls', '.xlsx']:
        df = pd.read_excel(path, sheet_name="CompartenDetalleLimpio(leeme)", dtype={
            'COD_PLAN_PADRE': str,
            'PLAN_PADRE': str,
            'COD_ASIG_PADRE': str,
            'ASIG_PADRE': str,
            'COD_PLAN_HIJA': str,
            'PLAN_HIJA': str,
            'TOTAL': int,
            'CURSO_PADRE': int
        })
    else:
        raise ValueError("Formato de archivo no compatible. Solo se permiten archivos CSV o Excel.")
    
    return df

def cargar_archivo_Campus(path):
    _, extension = os.path.splitext(path)

    if extension == '.csv':
        df = pd.read_csv(path, delimiter=';', dtype={
            'CAMPUS': str,
            'EDIFICIO': str,
            'ESPACIO': str,
            'CAPACIDAD DOCENTE': int,
            'CAPACIDAD EXAMEN': int
        })
    elif extension in ['.xls', '.xlsx']:
        df = pd.read_excel(path, sheet_name="ESPACIOS", dtype={
            'CAMPUS': str,
            'EDIFICIO': str,
            'ESPACIO': str,
            'CAPACIDAD DOCENTE': int,
            'CAPACIDAD EXAMEN': int
        })
    else:
        raise ValueError("Formato de archivo no compatible. Solo se permiten archivos CSV o Excel.")
    
    return df

# Funciones para importar los datos
def importar_Titulaciones(path, nombre):
    # Cargar el archivo
    df = cargar_archivo_Titulaciones(path)

    # Diccionarios para titulaciones y asignaturas
    titulaciones_dict = {}
    asignaturas_dict = defaultdict(lambda: None)  # Usar defaultdict para evitar comprobaciones explícitas
    codsAsignaturas = set()  # Usar un set en lugar de lista para evitar duplicados automáticamente

    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        codigo_plan = row['COD_PLAN_PADRE']
        nombre_plan = row['PLAN_PADRE']
        codigo_asig = row['COD_ASIG_PADRE']
        cod_plan_hija = row['COD_PLAN_HIJA']

        # Extraer todo el contenido que no este entre parentesis
        nombreTitulacion =  re.sub(r'\([^)]*\)', '', nombre_plan).strip() 

        # Extraer todo el contenido que este entre parentesis
        campus_matches = re.findall(r'\((.*?)\)', nombre_plan)
        campus = campus_matches[-1].strip() if campus_matches else None

        nombreTitulacionFinal = nombreTitulacion + " (" + campus + ")"

        # Crear la titulación si no existe
        if codigo_plan not in titulaciones_dict:
            titulacion = Titulacion(codigo=codigo_plan, nombre=nombreTitulacionFinal, campus=campus)
            titulaciones_dict[codigo_plan] = titulacion

        # Crear la asignatura si no existe
        if asignaturas_dict[codigo_asig] is None:
            asignatura = Asignatura(
                codigo=codigo_asig,
                nombre=row['ASIG_PADRE'],
                titulacion=nombreTitulacionFinal,
                numAlumnos=row['TOTAL'],
                curso=row['CURSO_PADRE']
            )
            asignaturas_dict[codigo_asig] = asignatura

        # Agregar la asignatura hija si existe
        if pd.notna(cod_plan_hija):
            plan_hija = re.sub(r'\([^)]*\)', '', row['PLAN_HIJA']).strip() 
            campus_hijasMatches = re.findall(r'\((.*?)\)', nombre_plan)
            campusHija = campus_hijasMatches[-1].strip() if campus_hijasMatches else None
            nombreHija = plan_hija + " (" + campusHija + ")"
            tupla_hija = (nombreHija, row['ASIG_HIJA'])
            asignaturas_dict[codigo_asig].agregar_hija(tupla_hija)

        # Agregar la asignatura a la titulación si no está ya añadida
        if codigo_asig not in codsAsignaturas:
            titulaciones_dict[codigo_plan].agregar_asignatura(asignaturas_dict[codigo_asig])
            codsAsignaturas.add(codigo_asig)  # Añadir a set

    # Convertir diccionario a lista de titulaciones
    titulaciones = list(titulaciones_dict.values())

    return titulaciones

def importar_Campus(path):
    # Cargar el archivo
    df = cargar_archivo_Campus(path)

    # Crear diccionarios para campus y edificios
    campus_dict = {}
    edificios_dict = {}
    aulasCampus_dict = defaultdict(list)
    aulasTipo_dict = defaultdict(list)

    # Iterar sobre cada fila del archivo
    for _, row in df.iterrows():
        campus_nombre = row['CAMPUS']
        edificio_nombre = row['EDIFICIO']

        # Crear campus si no existe
        if campus_nombre not in campus_dict:
            campus = Campus(campus_nombre)
            campus_dict[campus_nombre] = campus

        # Crear edificios
        if (campus_nombre, edificio_nombre) not in edificios_dict:
            nombre_edififcio_final = edificio_nombre + "("+ campus_nombre + ")"
            edificio = Edificio(nombre_edififcio_final)
            campus_dict[campus_nombre].agregar_edificio(edificio)
            edificios_dict[(campus_nombre, edificio_nombre)] = edificio
        
        nombre_aula = row['ESPACIO'].split('(')[0].strip()
        tipo_aula = row['ESPACIO'].split()[0]
        aula = Aula(quitar_acentos(nombre_aula), edificio.getNombre(), row['CAPACIDAD DOCENTE'], row['CAPACIDAD EXAMEN'], tipo_aula)

        aulasTipo_dict["TODAS"].append(aula)
        match tipo_aula:
            case "AULA":
                if " ".join(row['ESPACIO'].split()[:2]) == "AULA MAGNA":
                    aulasTipo_dict["AULA MAGNA"].append(aula)
                aulasTipo_dict["AULA"].append(aula)
            case "SEMINARIO":
                aulasTipo_dict["SEMINARIO"].append(aula)
            case "LABORATORIO":
                aulasTipo_dict["LABORATORIO"].append(aula)

        edificios_dict[(campus_nombre, edificio_nombre)].agregar_aula(aula)
        aulasCampus_dict[quitar_acentos(campus_nombre)].append(aula)

    campuses = list(campus_dict.values())

    return campuses, aulasCampus_dict, aulasTipo_dict

def importarXML(path):
    # cargar XML
    tree = ET.parse(path)
    # Obtener a raiz de XML
    root = tree.getroot()

    # Crear una universidad
    institucion = Universidad(root.find('Nombre').text)

    aulasCampus_dict = defaultdict(list)
    aulasTipo_dict = defaultdict(list)

    # Recorrer los campus
    campusListXML = root.find("ListaCampus")
    for campusXML in campusListXML.findall('Campus'):
        nombreCampus = campusXML.find('Nombre').text
        campus = Campus(nombreCampus)
        for edificioXML in campusXML.findall('Edificio'):
            edificio = Edificio(edificioXML.find('Nombre').text)
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

    # Recorrer las titulaciones
    titulacionesListXML =  root.find("ListaTitulaciones")
    for titulacionesXML in titulacionesListXML.findall('Titulación'):
        titulacion = Titulacion(
            titulacionesXML.find('Código').text,
            titulacionesXML.find('Nombre').text,
            titulacionesXML.find('Campus').text
        )
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

    return institucion.getCampus(), institucion.getTitulacion(), aulasCampus_dict, aulasTipo_dict

def importarInstitucion(path):
    error = ""
    campuses = []
    titulaciones = []
    aulasCampus = defaultdict(list)
    aulasTipo = defaultdict(list)

    # Obtener nombre del archivo y la extensión
    nombre_archivo_con_extension = os.path.basename(path)
    nombre_archivo, extension = os.path.splitext(nombre_archivo_con_extension) 

    # Depende del nombre del archivo se importaran las titulaciones o los campus
    if nombre_archivo == 'uxxi':
        titulaciones = importar_Titulaciones(path, "ETSII")

    elif nombre_archivo == 'mostoles2324.v1':
        campuses, aulasCampus, aulasTipo = importar_Campus(path)
    
    return titulaciones, campuses, aulasCampus, aulasTipo
