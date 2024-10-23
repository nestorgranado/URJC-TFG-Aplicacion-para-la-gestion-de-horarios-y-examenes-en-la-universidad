
from collections import defaultdict
import pandas as pd
import xml.etree.ElementTree as ET
import os
from estructuraDatos import *

# Función para cargar el archivo según su tipo (CSV o Excel)
def _cargar_archivo_Escuelas(path):
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
            'CURSO_PADRE': int
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

def _cargar_archivo_Campus(path):
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

def importar_Escuelas(path):
    # Cargar el archivo
    df = _cargar_archivo_Escuelas(path)

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

        # Crear la titulación si no existe
        if codigo_plan not in titulaciones_dict:
            titulacion = Titulacion(codigo=codigo_plan, nombre=nombre_plan)
            titulaciones_dict[codigo_plan] = titulacion

        # Crear la asignatura si no existe
        if asignaturas_dict[codigo_asig] is None:
            asignatura = Asignatura(
                codigo=codigo_asig,
                nombre=row['ASIG_PADRE'],
                titulacion=nombre_plan,
                numAlumnos=row['TOTAL'],
                curso=row['CURSO_PADRE']
            )
            asignaturas_dict[codigo_asig] = asignatura

        # Agregar la asignatura hija si existe
        if pd.notna(cod_plan_hija):
            tupla_hija = (cod_plan_hija, row['PLAN_HIJA'])
            asignaturas_dict[codigo_asig].agregar_hija(tupla_hija)

        # Agregar la asignatura a la titulación si no está ya añadida
        if codigo_asig not in codsAsignaturas:
            titulaciones_dict[codigo_plan].agregar_asignatura(asignaturas_dict[codigo_asig])
            codsAsignaturas.add(codigo_asig)  # Añadir a set

    # Convertir diccionario a lista de titulaciones
    titulaciones = list(titulaciones_dict.values())

    # Crear escuela con las titulaciones leidas
    escuela = Escuela("ETSII")
    escuela.setTitulaciones(titulaciones)

    return escuela

def importar_Campus(path):
    df = _cargar_archivo_Campus(path)

    campus_dict = {}
    edificios_dict = {}

    for _, row in df.iterrows():
        campus_nombre = row['CAMPUS']
        edificio_nombre = row['EDIFICIO']

        if campus_nombre not in campus_dict:
            campus = Campus(campus_nombre)
            campus_dict[campus_nombre] = campus

        if edificio_nombre not in edificios_dict:
            edificio = Edificio(edificio_nombre)
            campus_dict[campus_nombre].agregar_edificio(edificio)
            edificios_dict[edificio_nombre] = edificio
        
        aula = Aula(row['ESPACIO'].split('(')[0].strip(), row['CAPACIDAD DOCENTE'], row['CAPACIDAD EXAMEN'], row['ESPACIO'].split()[0])
        edificios_dict[edificio_nombre].agregar_aula(aula)

    campuses = list(campus_dict.values())

    return campuses

def importarXML(path):
    tree = ET.parse(path)
    root = tree.getroot()

    institucion = Universidad(root.find('Nombre').text)

    for campusXML in root.findall('Campus'):
        campus = Campus(campusXML.find('Nombre').text)
        for edificioXML in campusXML.findall('Edificio'):
            edificio = Edificio(edificioXML.find('Nombre').text)
            for aulaXML in edificioXML.findall('Aula'):
                aula = Aula(
                    aulaXML.find('Número').text,
                    int(aulaXML.find('CapacidadClase').text),
                    int(aulaXML.find('CapacidadExamen').text),
                    aulaXML.find('Tipo').text
                )
                edificio.agregar_aula(aula)
            campus.agregar_edificio(edificio)
        institucion.agregar_campus(campus)

    for escuelaXML in root.findall('Escuela'):
        escuela = Escuela(escuelaXML.find('Nombre').text)
        for titulacionesXML in escuelaXML.findall('Titulación'):
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
                    asignaturaXML.find('Profesor').text,
                    int(asignaturaXML.find('Curso').text)
                )
                for hijaXML in asignaturaXML.findall('AsignaturaHija'):
                    asignatura.agregar_hija((hijaXML.find('Código'), hijaXML.find('Nombre')))
                titulacion.agregar_asignatura(asignatura)
            escuela.agregar_titulacion(titulacion)
        institucion.agregar_escuela(escuela)

    return institucion.getCampus(), institucion.getEscuelas()