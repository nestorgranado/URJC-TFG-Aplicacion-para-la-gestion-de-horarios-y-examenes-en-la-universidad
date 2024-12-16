
from collections import defaultdict
import pandas as pd
import xml.etree.ElementTree as ET
import os
from estructuraDatos import *
import re

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

        # Crear la titulación si no existe
        if codigo_plan not in titulaciones_dict:
            titulacion = Titulacion(codigo=codigo_plan, nombre=nombreTitulacion, campus=campus)
            titulaciones_dict[codigo_plan] = titulacion

        # Crear la asignatura si no existe
        if asignaturas_dict[codigo_asig] is None:
            asignatura = Asignatura(
                codigo=codigo_asig,
                nombre=row['ASIG_PADRE'],
                titulacion=nombreTitulacion,
                numAlumnos=row['TOTAL'],
                curso=row['CURSO_PADRE']
            )
            asignaturas_dict[codigo_asig] = asignatura

        # Agregar la asignatura hija si existe
        if pd.notna(cod_plan_hija):
            plan_hija = re.sub(r'\([^)]*\)', '', row['PLAN_HIJA']).strip() 
            tupla_hija = (plan_hija, row['ASIG_HIJA'])
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
            edificio = Edificio(edificio_nombre)
            campus_dict[campus_nombre].agregar_edificio(edificio)
            edificios_dict[(campus_nombre, edificio_nombre)] = edificio
        
        aula = Aula(row['ESPACIO'].split('(')[0].strip(), row['CAPACIDAD DOCENTE'], row['CAPACIDAD EXAMEN'], row['ESPACIO'].split()[0])
        edificios_dict[(campus_nombre, edificio_nombre)].agregar_aula(aula)

    campuses = list(campus_dict.values())

    return campuses

def importarXML(path):
    # cargar XML
    tree = ET.parse(path)
    # Obtener a raiz de XML
    root = tree.getroot()

    # Crear una universidad
    institucion = Universidad(root.find('Nombre').text)

    # Recorrer los campus
    campusListXML = root.find("ListaCampus")
    for campusXML in campusListXML.findall('Campus'):
        campus = Campus(campusXML.find('Nombre').text)
        for edificioXML in campusXML.findall('Edificio'):
            edificio = Edificio(edificioXML.find('Nombre').text)
            for aulaXML in edificioXML.findall('Aula'):
                if aulaXML.find("AulaCombinada").text == "False":
                    aula = Aula(
                        aulaXML.find('Número').text,
                        int(aulaXML.find('CapacidadClase').text),
                        int(aulaXML.find('CapacidadExamen').text),
                        aulaXML.find('Tipo').text
                    )

                    edificio.agregar_aula(aula)

                else:
                    combinaciones = []
                    for combinacionXML in aulaXML.findall("Combinación"):
                        aulasCombinadas = []
                        for aulaCombinadaXML in combinacionXML.findall("Aula"):
                            newAula = Aula(
                                aulaCombinadaXML.find('Número').text,
                                int(aulaCombinadaXML.find('CapacidadClase').text),
                                int(aulaCombinadaXML.find('CapacidadExamen').text),
                                aulaCombinadaXML.find('Tipo').text
                            )
                            aulasCombinadas.append(newAula)
                        combinaciones.append(aulasCombinadas)
                    
                    aula = AulaCombinada(
                        aulaXML.find('Número').text,
                        int(aulaXML.find('CapacidadClase').text),
                        int(aulaXML.find('CapacidadExamen').text),
                        combinaciones
                    )

                    edificio.agregar_aula(aula)

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
                asignatura.agregar_hija((hijaXML.find('Código'), hijaXML.find('Nombre')))
            titulacion.agregar_asignatura(asignatura)
        institucion.agregar_titulacion(titulacion)

    return institucion.getCampus(), institucion.getTitulacion()

def importarInstitucion(path):
    error = ""
    campuses = []
    titulaciones = []

    # Comprobar si la rura existe
    if os.path.exists(path):
        # Obtener nombre del archivo y la extensión
        nombre_archivo_con_extension = os.path.basename(path)
        nombre_archivo, extension = os.path.splitext(nombre_archivo_con_extension) 

        # Dividir funcionalida si el archivo es xml o no
        if extension in ['.xls', '.xlsx', '.csv']:
            # Depende del nombre del archivo se importaran las titulaciones o los campus
            if nombre_archivo == 'uxxi':
                titulaciones = importar_Titulaciones(path, "ETSII")

            elif nombre_archivo == 'mostoles2324.v1':
                campuses = importar_Campus(path)

            else:
                error = (f"Error: el archivo '{path}' no contiene los datos necesarios para la aplicación")

        elif extension == '.xml':
            campuses, titulaciones = importarXML(path)

        else:
            error = (f"Error: el formato '{extension}' no es soportado")

    else:
        error = (f"Error: El archivo '{path}' no existe.")
    
    return titulaciones, campuses, error
