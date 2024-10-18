
from collections import defaultdict
import pandas as pd
import os
from estructuraDatos import *

# Función para cargar el archivo según su tipo (CSV o Excel)
def _cargar_archivo(path):
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

def importar_datos(path):
    # Cargar el archivo
    df = _cargar_archivo(path)

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
