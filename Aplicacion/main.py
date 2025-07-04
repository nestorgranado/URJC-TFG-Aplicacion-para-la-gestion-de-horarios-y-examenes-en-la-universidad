# Librerías externas
import sys
import os
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QComboBox, QAbstractItemView, QTabWidget, QHBoxLayout, QSpinBox, QPushButton
from PySide6.QtCore import Qt
from collections import defaultdict
from itertools import combinations
import unicodedata

# Imports de las interfaces
from interfaces.MainWindow import Ui_MainWindow
from interfaces.Ui_import import Ui_importar
from interfaces.Ui_fetConnect import Ui_conexionFET

from interfaces.Ui_addName import Ui_AddNombre
from interfaces.Ui_modifyName import Ui_ModificarName
from interfaces.Ui_modifyBuilding import Ui_ModificarEdificio
from interfaces.Ui_modifyAula import Ui_ModificarAula
from interfaces.Ui_addVirtuaRooms import Ui_CrearAulaCombinada
from interfaces.Ui_modifyTitulation import Ui_ModificarTitulacion
from interfaces.Ui_modifyAsignatura import Ui_ModificarAsignatura

from interfaces.Ui_days import Ui_dias
from interfaces.Ui_hour import Ui_horas

from interfaces.Ui_newSchedule import Ui_crearHorario

from interfaces.Ui_exams import Ui_Examenes
from interfaces.Ui_addExam import Ui_addExamen
from interfaces.Ui_modifyExam import Ui_ModificarExamenes

from interfaces.Ui_classes import Ui_Clases
from interfaces.Ui_modifyClass import Ui_ModificarClases
from interfaces.Ui_others import Ui_otrosHorarios
from interfaces.Ui_restrictionsCl import Ui_RestriccionesCl
from interfaces.Ui_allRestrictionCl import Ui_ListaRestriccionesCl
from interfaces.Ui_activityTurn import Ui_res_turno
from interfaces.Ui_maxHoursDay import Ui_MaxHorasDia
from interfaces.Ui_maxGapsWeek import Ui_MaxHuecosSemana

from interfaces.Ui_restrictionsEx import Ui_RestriccionesEx
from interfaces.Ui_allRestrictionEx import Ui_ListaRestriccionesEx
from interfaces.Ui_daysBetweenExams import Ui_res_separacionDias
from interfaces.Ui_startSameDay import Ui_res_mismoDia
from interfaces.Ui_roomType import Ui_res_tipoAula

# Funcionalidades
from estructuraDatos import *
from importar import importarInstitucion
from importarXML import importarXML
from exportar import exportar
from exportarFET import exportarFET

def quitar_acentos(texto):
    # Normalizamos el texto para separar los caracteres base de sus acentos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Filtramos los caracteres que no sean marcas diacríticas
    texto_sin_acentos = ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')
    return texto_sin_acentos

# Clase para mostrar una ventana emergente con un mensaje de error que se le pase al constructor
class DialogoError(QDialog): 
    def __init__(self, mensaje):
        super().__init__()

        self.resize(240, 120) # Redimensionar ventana
        self.setWindowTitle("Error") # Titulo de la ventana

        # Crear un layout deonde colocar el mensaje 
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel(mensaje))
        self.adjustSize()

# Interfaz para importar datos al sistema
class ImportarUI(QWidget, Ui_importar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.importarBtn.clicked.connect(self.guardar) # Funcionalidad botón guardar
        self.examinarBtn.clicked.connect(self.seleccionarArchivo) # Funcionalidad botón selecionar archivo

    def guardar(self):
        global institucion, alumnos, diasSemanaClases, diasSemanaExamenes, horasDiaClases, horasDiaExamenes, actClases, actExamenes, asignaturasElegidas, aulasPorCampus, aulasPorTipo, clasesPorCuros, examenesPorCuros, restriccionesClases, restriccionesExamenes
        titulaciones = []
        campuses = []
        error = ""
        path = self.rutaText.text()

        # Comprobar si la rura existe
        if os.path.exists(path):
            # Obtener nombre del archivo y la extensión
            nombre_archivo_con_extension = os.path.basename(path)
            nombre_archivo, extension = os.path.splitext(nombre_archivo_con_extension) 

            # Dividir funcionalida si el archivo es xml o no
            if extension in ['.xls', '.xlsx', '.csv']:
                titulaciones, campuses, aulasPorCampusImp, aulasPorTipoImp = importarInstitucion(path) # Importación de datos
                if aulasPorCampusImp and aulasPorTipoImp:
                    if aulasPorCampus and aulasPorTipo:
                        aulasPorCampus = {clave: aulasPorCampus.get(clave, []) + aulasPorCampusImp.get(clave, []) for clave in set(aulasPorCampus) | set(aulasPorCampusImp)}
                        aulasPorTipo = {clave: aulasPorTipo.get(clave, []) + aulasPorTipoImp.get(clave, []) for clave in set(aulasPorTipo) | set(aulasPorTipoImp)}
                    else:
                        aulasPorCampus = aulasPorCampusImp
                        aulasPorTipo = aulasPorTipoImp
            elif extension == '.xml':
                institucion, alumnos, diasSemanaClases, diasSemanaExamenes, horasDiaClases, horasDiaExamenes, actClases, actExamenes, asignaturasElegidas, aulasPorCampus, aulasPorTipo, clasesPorCuros, examenesPorCuros, restriccionesClases, restriccionesExamenes = importarXML(path)
            else:
                error = (f"Error: el formato '{extension}' no es soportado")

        else:
            error = (f"Error: El archivo '{path}' no existe.")

        # Si no hay error comprobar que se ha importado y añadirlo a la Institución
        if error == "":
            if  campuses and titulaciones:
                institucion.sumar_campus(campuses)
                institucion.sumar_titulacion(titulaciones)
            elif campuses:
                institucion.sumar_campus(campuses)
            elif titulaciones:
                institucion.sumar_titulacion(titulaciones)
        else:
            dialogoError = DialogoError(error)
            dialogoError.exec()

        self.close()

    def seleccionarArchivo(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            None, 
            "Seleccionar archivo", 
            "", 
            "Archivos Excel (*.xlsx *.xls);;Archivos CSV (*.csv);;Archivo XML (*.xml)"
        )

        self.rutaText.setText(ruta_archivo)

# Conexion con fet-cl.exe
class FETConnectUI(QWidget, Ui_conexionFET):
    def __init__(self, mensaje):
        super().__init__()
        self.setupUi(self)

        self.label.setText(mensaje)
        self.adjustSize()

        if ruta_fet:
            self.rutaText.setText(ruta_fet)

        self.importarBtn.clicked.connect(self.guardar) # Funcionalidad botón guardar
        self.examinarBtn.clicked.connect(self.seleccionarArchivo) # Funcionalidad botón selecionar archivo

    def guardar(self):
        global ruta_fet
        ruta_fet = self.rutaText.text()

        if not ruta_fet.endswith("fet-cl.exe"):
            dialogoError = DialogoError("Se busca el archivo ejecutable fet-cl.exe")
            dialogoError.exec()
        else:
            self.close()

    def seleccionarArchivo(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            None, 
            "Buscar fet-cl.exe", 
            "", 
            "Ejecutables (*.exe)"
        )

        self.rutaText.setText(ruta_archivo)

# Clase para Modificar nombre de la institución
class ModificarInstitucion(QWidget, Ui_AddNombre):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nombreText.setText(institucion.getNombre())
        self.save.clicked.connect(self.guardar)

    def guardar(self):
        institucion.setNombre(self.nombreText.text())
        self.close()

# Clase para Modificar Datos Campuses
class ModificarName(QWidget, Ui_ModificarName):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Title.setText("Campus") # Titulo de la pantalla

        self.nameList = institucion.getCampus() # Lista de campus

        # Rellenar el QListWidget con los nombres de los campus
        self.list.clear()
        for campus in self.nameList:
            self.list.addItem(campus.getNombre())

        self.list.itemClicked.connect(self.updateLineEditText) # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.modify.clicked.connect(self.modificar_elemento) # Modificar valor del elemento seleccionado de la QListWidget
        self.add.clicked.connect(self.agregar_elemento) # Crear un nuevo elemento
        self.sup.clicked.connect(self.borrar_elemento) # Borrar elemento seleccionado

        self.save.clicked.connect(self.guardarCampus) # guardar
        
        self.selected_index = None  # Variable para guardar el índice del elemento seleccionado

    def updateLineEditText(self, item):
        self.selected_index = self.list.row(item)  # Guardar índice del elemento seleccionado
        self.nombreText.setText(self.nameList[self.selected_index].getNombre())  # Establecer el texto del QLineEdit al texto del item seleccionado
    
    def modificar_elemento(self):
        if self.selected_index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_texto = self.nombreText.text()
            
            # Actualizar el elemento en la lista de Campus
            self.nameList[self.selected_index].setNombre(nuevo_texto)

            # Actualizar el elemento de la lista de aulas por campus
            global aulasPorCampus
            antiguo = aulasPorCampus[quitar_acentos(self.list.item(self.selected_index).text())]
            aulasPorCampus[quitar_acentos(nuevo_texto)] = antiguo
            del antiguo
            
            # Actualizar el elemento visualmente en el QListWidget
            self.list.item(self.selected_index).setText(nuevo_texto)
    
    def agregar_elemento(self):
        # Obtener el texto del QLineEdit
        nuevo_texto = self.nombreText.text()
        
        # Agregar el nuevo texto a la lista de Campus
        nuevo_campus = Campus(nuevo_texto)
        self.nameList.append(nuevo_campus)
        
        # Añadir el campus a la lista de aulas por campus
        global aulasPorCampus
        aulasPorCampus[quitar_acentos(nuevo_texto)] = []
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        self.list.addItem(nuevo_texto)

    def borrar_elemento(self):
        if self.selected_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento de la lista de Campus
            del self.nameList[self.selected_index]

            # Eliminar campus de las aulas por campus
            del aulasPorCampus[quitar_acentos(self.nombreText.text())]
            
            # Eliminar el elemento del QListWidget
            self.list.takeItem(self.selected_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.nombreText.clear()
            self.selected_index = None

    def guardarCampus(self):
        institucion.setCampus(self.nameList)
        self.close()

# Clase para Modificar Datos de los Edififcios
class ModificarEdificio(QWidget, Ui_ModificarEdificio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.campuses = institucion.getCampus() # Lista de Campuses
        self.campusBox.addItem("Seleccione una opción...") # Inicializar el selector de campus

        # Rellenar el selector de campus con los nombres de los diferentes campus
        for campus in self.campuses:
            self.campusBox.addItem(campus.getNombre())
        
        self.campusBox.currentIndexChanged.connect(self.actualizar_edificio) # Si se seleciona un campus obtener sus edificios
        self.list.itemClicked.connect(self.updateLineEditText) # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.modify.clicked.connect(self.modificar_elemento) # Modificar valor del elemento seleccionado de la QListWidget
        self.add.clicked.connect(self.agregar_elemento) # Crear un nuevo elemento
        self.sup.clicked.connect(self.borrar_elemento) # Borrar elemento seleccionado
        self.save.clicked.connect(self.guardar) # guardar
        
        self.edificio_index = None  # Variable para guardar el índice del elemento seleccionado

    def actualizar_edificio(self):
        self.campus_index = self.campusBox.currentIndex() - 1 # Guardar Indice del campus seleccionado
        self.edificios = self.campuses[self.campus_index].getEdificios() # Obtener los edificios del campus seleccionado

        # Rellenar el QListWidget con los nombres de los edificios
        self.list.clear()
        for edificio in self.edificios:
            self.list.addItem(edificio.getNombre())

        # Limpiar Datos
        self.nombreText.clear()
    
    def updateLineEditText(self, item):
        self.edificio_index = self.list.row(item)  # Guardar índice del elemento seleccionado
        self.nombreText.setText(self.edificios[self.edificio_index].getNombre())  # Establecer el texto del QLineEdit al texto del item seleccionado
    
    def modificar_elemento(self):
        if self.edificio_index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_texto = self.nombreText.text()
            
            # Actualizar el elemento en la lista de Campus
            self.edificios[self.edificio_index].setNombre(nuevo_texto)
            
            # Actualizar el elemento visualmente en el QListWidget
            self.list.item(self.edificio_index).setText(nuevo_texto)

            # Actualizar campus
            self.campuses[self.campus_index].setEdificios(self.edificios)

    def agregar_elemento(self):
        # Obtener el texto del QLineEdit
        nuevo_texto = self.nombreText.text()
        
        # Agregar el nuevo texto a la lista de Campus
        nuevo_edificio = Edificio(nuevo_texto)
        self.edificios.append(nuevo_edificio)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        self.list.addItem(nuevo_texto)

        # Actualizar campus
        self.campuses[self.campus_index].setEdificios(self.edificios)

    def borrar_elemento(self):
        if self.edificio_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento de la lista de Campus
            del self.edificios[self.edificio_index]
            
            # Eliminar el elemento del QListWidget
            self.list.takeItem(self.edificio_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.nombreText.clear()
            self.edificio_index = None

            # Actualizar campus
            self.campuses[self.campus_index].setEdificios(self.edificios)

    def guardar(self):
        institucion.setCampus(self.campuses)
        self.close()
            
# Clase para Modificar Datos de las Titulaciones
class ModificarTitulacion(QWidget, Ui_ModificarTitulacion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.titulaciones = institucion.getTitulacion() # Obtenre la lista de titulaciones de la institución

        # Rellenar el QListWidget con los nombres de las titulaciones
        for titulacion in self.titulaciones:
            item = "(" + str(titulacion.getCodigo()) + ") " + str(titulacion.getNombre())
            self.list.addItem(item)

        self.list.itemClicked.connect(self.updateLineEditText) # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.modify.clicked.connect(self.modificar_elemento) # Modificar valor del elemento seleccionado de la QListWidget
        self.add.clicked.connect(self.agregar_elemento) # Crear un nuevo elemento
        self.sup.clicked.connect(self.borrar_elemento) # Borrar elemento seleccionado
        self.save.clicked.connect(self.guardar) # guardar
        
        self.titulaciones_index = None  # Variable para guardar el índice del elemento seleccionado

    def updateLineEditText(self, item):
        self.titulaciones_index = self.list.row(item)  # Guardar índice del elemento seleccionado
        # Rellenar los datos del elemneto selecionado
        self.nombreText.setText(self.titulaciones[self.titulaciones_index].getNombre())
        self.codigoText.setText(self.titulaciones[self.titulaciones_index].getCodigo())
        self.campusText.setText(self.titulaciones[self.titulaciones_index].getCampus())

    def modificar_elemento(self):
        if self.titulaciones_index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_nombre = self.nombreText.text()
            nuevo_codigo = self.codigoText.text()
            nuevo_campus = self.campusText.text()
            
            # Actualizar el elemento en la lista de titulaciones
            self.titulaciones[self.titulaciones_index].setNombre(nuevo_nombre)
            self.titulaciones[self.titulaciones_index].setCodigo(nuevo_codigo)
            self.titulaciones[self.titulaciones_index].setCampus(nuevo_campus)
            
            # Actualizar el elemento visualmente en el QListWidget
            nuevo_item = "(" + str(nuevo_codigo) + ") " + str(nuevo_nombre)
            self.list.item(self.titulaciones_index).setText(nuevo_item)
    
    def agregar_elemento(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_nombre = self.nombreText.text()
        nuevo_codigo = self.codigoText.text()
        nuevo_campus = self.campusText.text()
        
        # Agregar el nuevo texto a la lista de Campus
        nueva_titulacion = Titulacion(nuevo_codigo, nuevo_nombre, nuevo_campus)
        self.titulaciones.append(nueva_titulacion)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        nuevo_item = "(" + str(nuevo_codigo) + ") " + str(nuevo_nombre)
        self.list.addItem(nuevo_item)

    def borrar_elemento(self):
        if self.titulaciones_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento de la lista de Campus
            del self.titulaciones[self.titulaciones_index]
            
            # Eliminar el elemento del QListWidget
            self.list.takeItem(self.titulaciones_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.nombreText.clear()
            self.codigoText.clear()
            self.campusText.clear()
            self.titulaciones_index = None

    def guardar(self):
        institucion.setTitulacion(self.titulaciones)
        self.close()

# Clase para Modificar Datos de las Aulas
class ModificarAula(QWidget, Ui_ModificarAula):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.campuses = institucion.getCampus() # Lista de campuses

        # Inicializar
        self.campusBox.addItem("Seleccione una opción...")
        self.edificioBox.addItem("Seleccione una opción...")
        self.capClaseText.setMinimum(0)
        self.capClaseText.setMaximum(1000)
        self.capExamenText.setMinimum(0)
        self.capExamenText.setMaximum(1000)


        # Rellenar el selector de campus con los nombres de los diferentes campus
        for campus in self.campuses:
            self.campusBox.addItem(campus.getNombre())
        
        self.campusBox.currentIndexChanged.connect(self.actualizar_edificio) # Si se seleciona un campus obtener sus edificios
        self.edificioBox.currentIndexChanged.connect(self.actualizar_aula) # Si se seleciona un edificio obtener sus aulas
        self.list.itemClicked.connect(self.updateLineEditText) # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.modify.clicked.connect(self.modificar_elemento) # Modificar valor del elemento seleccionado de la QListWidget
        self.add.clicked.connect(self.agregar_elemento) # Crear un nuevo elemento
        self.sup.clicked.connect(self.borrar_elemento) # Borrar elemento seleccionado
        self.save.clicked.connect(self.guardar) # guardar
        
        self.aula_index = None  # Variable para guardar el índice del elemento seleccionado

    def actualizar_edificio(self):
        self.campus_index = self.campusBox.currentIndex() - 1 # Guardar Indice del campus seleccionado
        self.edificios = self.campuses[self.campus_index].getEdificios() # Obtener los edififcios del campus seleccionado

        # Rellenar el selector de edificio con los nombres de los diferentes edificios
        for edificio in self.edificios:
            self.edificioBox.addItem(edificio.getNombre())

        # Limpiar Datos
        self.numeroText.clear()
        self.capClaseText.clear()
        self.capExamenText.clear()
        self.tipoText.clear()
    
    def actualizar_aula(self):
        self.edificio_index = self.edificioBox.currentIndex() - 1 # Guardar Indice del edificio seleccionada
        self.aulas = self.edificios[self.edificio_index].getAulas() # Obtener las aulas del edificio seleccionado

        # Rellenar el QListWidget con los nombres de las aulas
        self.list.clear()
        for aula in self.aulas:
            self.list.addItem(aula.getNumero())

        # Limpiar Datos
        self.numeroText.clear()
        self.capClaseText.clear()
        self.capExamenText.clear()
        self.tipoText.clear()

    def updateLineEditText(self, item):
        self.aula_index = self.list.row(item)  # Guardar índice del elemento seleccionado
        # Rellenar los datos del elemneto selecionado
        self.numeroText.setText(self.aulas[self.aula_index].getNumero())
        self.capClaseText.setValue(self.aulas[self.aula_index].getCapacidadClase())
        self.capExamenText.setValue(self.aulas[self.aula_index].getCapacidadExamen())
        self.tipoText.setText(self.aulas[self.aula_index].getTipo())

    def calcularIndice(self, lista):
        aula = self.aulas[self.aula_index]
        indice = 0
        salir = False
        while indice < len(lista) and not salir:
            if lista[indice].getNumero() == aula.getNumero() and lista[indice].getEdificio() == aula.getEdificio():
                salir = True
            indice+=1
        return indice
    
    def modificar_elemento(self):
        global aulasPorTipo, aulasPorCampus
        if self.aula_index is not None:  # Verificar si hay un elemento seleccionado
            aula = self.aulas[self.aula_index]
            tipo = aula.getTipo()

            # Obtener el nuevo texto del QLineEdit
            nuevo_numero = self.numeroText.text()
            nuevo_capClase = self.capClaseText.value()
            nuevo_capExamen = self.capExamenText.value()
            nuevo_tipo = self.tipoText.text().upper()
            
            # Actualizar el elemento en la lista de titulaciones
            nueva_aula = Aula(nuevo_numero, self.edificios[self.edificio_index].getNombre(), nuevo_capClase, nuevo_capExamen, nuevo_tipo) 

            # Actualizar aulas por campus
            indiceAulaCampus = self.calcularIndice(aulasPorCampus[self.campuses[self.campus_index].getNombre()])
            aulasPorCampus[self.campuses[self.campus_index]][indiceAulaCampus] = nueva_aula

            # Actulizar aulas por tipo
            if tipo != nuevo_tipo:
                indiceAulaTipo = self.calcularIndice(aulasPorTipo["TODAS"])
                aulasPorTipo["TODAS"][indiceAulaTipo] = nueva_aula
                indiceAulaTipo = self.calcularIndice(aulasPorTipo[tipo])
                del aulasPorTipo[tipo][indiceAulaTipo]

                match nuevo_tipo:
                    case "AULA":
                        aulasPorTipo["AULA"].append(nueva_aula)
                    case "AULA MAGNA":
                        aulasPorTipo["AULA"].append(nueva_aula)
                        aulasPorTipo["AULA MAGNA"].append(nueva_aula)
                    case "SEMINARIO":
                        aulasPorTipo["SEMINARIO"].append(nueva_aula)
                    case "LABORATORIO":
                        aulasPorTipo["LABORATORIO"].append(nueva_aula)
         
            # Actualizar el elemento visualmente en el QListWidget
            self.list.item(self.aula_index).setText(nuevo_numero)

            # Actualizar datos
            self.aulas[self.aula_index] = nueva_aula
            self.edificios[self.edificio_index].setAulas(self.aulas)
            self.campuses[self.campus_index].setEdificios(self.edificios)
            institucion.setCampus(self.campuses)
    
    def agregar_elemento(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_numero = self.numeroText.text()
        nuevo_capClase = self.capClaseText.value()
        nuevo_capExamen = self.capExamenText.value()
        nuevo_tipo = self.tipoText.text()
        
        # Agregar el nuevo texto a la lista de Campus
        nueva_aula = Aula(nuevo_numero, self.edificios[self.edificio_index].getNombre(), nuevo_capClase, nuevo_capExamen, nuevo_tipo)
        self.edificios[self.edificio_index].agregar_aula(nueva_aula)

        global aulasPorCampus, aulasPorTipo
        aulasPorCampus[quitar_acentos(self.campuses[self.campus_index].getNombre())].append(nueva_aula)
        aulasPorTipo["TODAS"].append(nueva_aula)
        match nuevo_tipo:
            case "AULA":
                aulasPorTipo["AULA"].append(nueva_aula)
            case "AULA MAGNA":
                aulasPorTipo["AULA"].append(nueva_aula)
                aulasPorTipo["AULA MAGNA"].append(nueva_aula)
            case "SEMINARIO":
                aulasPorTipo["SEMINARIO"].append(nueva_aula)
            case "LABORATORIO":
                aulasPorTipo["LABORATORIO"].append(nueva_aula) 
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        self.list.addItem(nuevo_numero)

        # Actualizar datos
        self.campuses[self.campus_index].setEdificios(self.edificios)
        institucion.setCampus(self.campuses)

    def borrar_elemento(self):
        global aulasPorTipo, aulasPorCampus
        if self.aula_index is not None:  # Verificar si hay un elemento seleccionado
            aula = self.aulas[self.aula_index]
            # Eliminar el elemento de la lista de Campus
            del self.aulas[self.aula_index]

            # Eliminar de aulas por campus
            indiceAulaCampus = self.calcularIndice(aulasPorCampus[self.campuses[self.campus_index].getNombre()])
            del aulasPorCampus[self.campuses[self.campus_index]][indiceAulaCampus]
            # Eliminar de aulas por tipo
            indiceAulaTipo = self.calcularIndice(aulasPorTipo["TODAS"])
            del aulasPorTipo["TODAS"][indiceAulaTipo]
            indiceAulaTipo = self.calcularIndice(aulasPorTipo[aula.getTipo()])
            del aulasPorTipo[aula.getTipo()][indiceAulaTipo]
            
            # Eliminar el elemento del QListWidget
            self.list.takeItem(self.aula_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.numeroText.clear()
            self.capClaseText.clear()
            self.capExamenText.clear()
            self.tipoText.clear()
            self.aula_index = None

            # Actualizar datos
            self.edificios[self.edificio_index].setAulas(self.aulas)
            self.campuses[self.campus_index].setEdificios(self.edificios)

    def guardar(self):
        institucion.setCampus(self.campuses)
        self.close()
        
class AulaCombinadaUI(QWidget, Ui_CrearAulaCombinada):
    def __init__(self, tipoHorario):
        super().__init__()
        self.setupUi(self)

        self.campuses = institucion.getCampus() # Lista de campuses
        self.tipoHorario = tipoHorario

        # Inicializar
        self.campusText.addItem("Seleccione una opción...")
        self.edificioText.addItem("Seleccione una opción...")
        self.tipoAulaText.addItem("Seleccione una opción...")
        self.cantidadText.setMinimum(0)
        self.cantidadText.setMaximum(1000)
        self.capacidadText.setMinimum(0)
        self.capacidadText.setMaximum(1000)

        # Rellenar el selector de campus con los nombres de los diferentes campus
        for campus in self.campuses:
            self.campusText.addItem(campus.getNombre())

        self.tipoAulaText.addItem("AULA")
        self.tipoAulaText.addItem("AULA MAGNA")
        self.tipoAulaText.addItem("SEMINARIO")
        self.tipoAulaText.addItem("LABORATORIO")
        
        self.campusText.currentIndexChanged.connect(self.actualizar_edificio) # Si se seleciona un campus obtener sus edificios
        self.edificioText.currentIndexChanged.connect(self.actualizar_aula) # Si se seleciona un edificio obtener sus aulas

        self.add.clicked.connect(self.crearAulas)

    def esAulaMagna(self, aula):
        if " ".join(aula.getNumero().split()[:2]) == "AULA MAGNA":
            return True
        else:
            return False
    
    def actualizar_edificio(self):
        self.campus_index = self.campusText.currentIndex() - 1 # Guardar Indice del campus seleccionado
        self.edificios = self.campuses[self.campus_index].getEdificios() # Obtener los edififcios del campus seleccionado

        # Rellenar el selector de edificio con los nombres de los diferentes edificios
        for edificio in self.edificios:
            self.edificioText.addItem(edificio.getNombre())
    
    def actualizar_aula(self):
        self.edificio_index = self.edificioText.currentIndex() - 1 # Guardar Indice del edificio seleccionada
        self.aulas = self.edificios[self.edificio_index].getAulas() # Obtener las aulas del edificio seleccionado

    def crearAulas(self):
        global totalAulasCombinadas, aulasPorTipo
        cantidad = self.cantidadText.value()
        capacidad = self.capacidadText.value()
        tAula = self.tipoAulaText.currentText()

        listaCombinaciones = []

        for tam in range(2, 4):
            for comb in combinations(self.aulas, tam):
                suma_cap_clase = sum(aula.getCapacidadClase() for aula in comb)
                suma_cap_examen = sum(aula.getCapacidadExamen() for aula in comb)

            
                tipo = comb[0].getTipo()
                mismoTipo = all(aula.getTipo() == tipo for aula in comb)

                if self.esAulaMagna(comb[0]):
                    tipo = "AULA MAGNA"
                    mismoTipo = all(self.esAulaMagna(aula) for aula in comb)
               
                if mismoTipo and tipo == tAula:
                    if (self.tipoHorario == "Clase") and (suma_cap_clase >= capacidad):
                        listaCombinaciones.append(comb)
                    if (self.tipoHorario == "Examen") and (suma_cap_examen >= capacidad):
                        listaCombinaciones.append(comb)
        
        if listaCombinaciones:
            for i in range(cantidad):
                newAula = None
                if self.tipoHorario == "Clase":
                    newAula = AulaCombinada(f"AulaClaseCombinadaClase{totalAulasCombinadas + i}", self.edificios[self.edificio_index].getNombre(), capacidad, 0, tAula, listaCombinaciones)
                    self.edificios[self.edificio_index].agregar_aula(newAula)

                if self.tipoHorario == "Examen":
                    newAula = AulaCombinada(f"AulaClaseCombinadaExamen{totalAulasCombinadas + i}", self.edificios[self.edificio_index].getNombre(), 0, capacidad, tAula, listaCombinaciones)
                    self.edificios[self.edificio_index].agregar_aula(newAula)
                
                aulasPorTipo["TODAS"].append(newAula)
                aulasPorTipo[tAula].append(newAula)

            totalAulasCombinadas += cantidad
            self.close()
        else:
            self.error = DialogoError("No hay combinaciones de aulas que satisfagan esta restricción")
            self.error.exec()

# Clase para Modificar Datos de las Asignaturas
class ModificarAsignatura(QWidget, Ui_ModificarAsignatura):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.titulaciones = institucion.getTitulacion() # Lista de titulaciones

        # Inicializar el selectorer
        self.titulacionBox.addItem("Seleccione una opción...")

        # Rellenar el selector de titulaciones
        for titulacion in self.titulaciones:
            self.titulacionBox.addItem(titulacion.getNombre())

        self.titulacionBox.currentIndexChanged.connect(self.actualizar_asignatura) # Si se seleciona una titulación obtener sus asignaturas
        # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.list.itemClicked.connect(self.updateLineEditText) 
        self.listHijas.itemClicked.connect(self.updateLineEditHijas)

        # Botones
        self.modify.clicked.connect(self.modificar_elemento)
        self.add.clicked.connect(self.agregar_elemento)
        self.sup.clicked.connect(self.borrar_elemento)

        self.addHija.clicked.connect(self.agregar_hija)

        self.save.clicked.connect(self.guardar) # guardar
        
        self.asignatura_index = None  # Variable para guardar el índice del elemento seleccionado
        self.hija_index = None

    def actualizar_asignatura(self):
        self.titulacion_index = self.titulacionBox.currentIndex() - 1 # Guardar Indice
        self.asignaturas = self.titulaciones[self.titulacion_index].getAsignaturas() # Obtener las asignaturas

        # Rellenar el QListWidget
        self.list.clear()
        self.listHijas.clear()
        for asignatura in self.asignaturas:
            item = "(" + str(asignatura.codigo) + ") " + str(asignatura.getNombre())
            self.list.addItem(item)

        # Limpiar Datos
        self.codigoText.clear()
        self.nombreText.clear()
        self.numAlumnosText.clear()
        self.cursoText.clear()
        self.codigoHijaText.clear()
        self.nombreHijaText.clear()

    def updateLineEditText(self, item):
        self.asignatura_index = self.list.row(item)  # Guardar índice del elemento seleccionado

        # Rellenar los datos del elemneto selecionado
        self.codigoText.setText(self.asignaturas[self.asignatura_index].getCodigo())
        self.nombreText.setText(self.asignaturas[self.asignatura_index].getNombre())
        self.numAlumnosText.setValue(int(self.asignaturas[self.asignatura_index].getNumAlumnos()))
        self.cursoText.setText(str(self.asignaturas[self.asignatura_index].getCurso()))

        # Rellenar ListaHijas
        self.listHijas.clear()
        self.hijas = self.asignaturas[self.asignatura_index].getAsignaturas_hijas()
        for hija in self.hijas:
            item = "(" + str(hija[0]) + ") " + str(hija[1])
            self.listHijas.addItem(item)
        
        # Limpiar Datos
        self.codigoHijaText.clear()
        self.nombreHijaText.clear()

    def updateLineEditHijas(self, item):
        self.hija_index = self.list.row(item)  # Guardar índice del elemento seleccionado

        # Rellenar los datos del elemneto selecionado
        self.codigoHijaText.setText(self.hijas[self.hija_index][0])
        self.nombreHijaText.setText(self.hijas[self.hija_index][1])

    def modificar_elemento(self):
        if self.asignatura_index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_codigo = self.codigoText.text()
            nuevo_nombre = self.nombreText.text()
            nuevo_numAlumnos = int(self.numAlumnosText.value())
            nuevo_curso = int(self.cursoText.text())
            
            # Actualizar el elemento
            self.asignaturas[self.asignatura_index].setCodigo(nuevo_codigo)
            self.asignaturas[self.asignatura_index].setNombre(nuevo_nombre)
            self.asignaturas[self.asignatura_index].setCurso(nuevo_curso)

            if self.asignaturas[self.asignatura_index].getAsignaturas_hijas() and self.asignaturas[self.asignatura_index].getNumAlumnos() != nuevo_numAlumnos:
                self.asignaturas[self.asignatura_index].setNumAlumnos(nuevo_numAlumnos)

                for hija in self.asignaturas[self.asignatura_index].getAsignaturas_hijas():
                    salir = False
                    i = 0
                    titBuscada = hija[0]
                    asigBuscada = hija[1]
                    while not salir:
                        if titBuscada == self.titulaciones[i].getNombre():
                            listaAsignaturas = self.titulaciones[i].getAsignaturas()
                            j = 0
                            while not salir:
                                if asigBuscada == listaAsignaturas[j].getNombre():
                                    listaAsignaturas[j].setNumAlumnos(nuevo_numAlumnos)
                                    salir = True
                                j += 1
                        i += 1
            elif self.asignaturas[self.asignatura_index].getNumAlumnos() != nuevo_numAlumnos:
                tupla = (self.asignaturas[self.asignatura_index].getTitulacion(), self.asignaturas[self.asignatura_index].getNombre())
                for tit in self.titulaciones:
                    for asig in tit.getAsignaturas():
                        if tupla in asig.getAsignaturas_hijas():
                            asig.setNumAlumnos(nuevo_numAlumnos)
         
            # Actualizar el elemento visualmente en el QListWidget
            nuevo_item = "(" + str(nuevo_codigo) + ") " + str(nuevo_nombre)
            self.list.item(self.asignatura_index).setText(nuevo_item)

            # Actualizar datos
            self.titulaciones[self.titulacion_index].setAsignaturas(self.asignaturas)
    
    def agregar_elemento(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_codigo = self.codigoText.text()
        nuevo_nombre = self.nombreText.text()
        nuevo_numAlumnos = str(self.numAlumnosText.value())
        nuevo_curso = int(self.cursoText.text())
        
        # Agregar el nuevo texto a la lista de Campus
        nueva_asignatura = Asignatura(nuevo_codigo, nuevo_nombre, self.titulaciones[self.titulacion_index].getNombre(), nuevo_numAlumnos, nuevo_curso)
        self.titulaciones[self.titulacion_index].agregar_asignatura(nueva_asignatura)
        self.asignaturas = self.titulaciones[self.titulacion_index].getAsignaturas()
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        nuevo_item = "(" + str(nuevo_codigo) + ") " + str(nuevo_nombre)
        self.list.addItem(nuevo_item)

    def borrar_elemento(self):
        if self.asignatura_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar elemento de la asignatura padre si tiene
            if not self.asignaturas[self.asignatura_index].getAsignaturas_hijas():
                tupla = (self.asignaturas[self.asignatura_index].getTitulacion(), self.asignaturas[self.asignatura_index].getNombre())
                for tit in self.titulaciones:
                    for asig in tit.getAsignaturas():
                        listaHijas = asig.getAsignaturas_hijas()
                        if tupla in listaHijas:
                            asig.setAsignaturas_hijas(listaHijas.remove(tupla))
            # Eliminar el elemento
            del self.asignaturas[self.asignatura_index]
            
            # Eliminar el elemento del QListWidget
            self.list.takeItem(self.asignatura_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.codigoText.clear()
            self.nombreText.clear()
            self.numAlumnosText.clear()
            self.cursoText.clear()
            self.codigoHijaText.clear()
            self.nombreHijaText.clear()
            self.asignatura_index = None

            # Actualizar datos
            self.titulaciones[self.titulacion_index].setAsignaturas(self.asignaturas)

    def agregar_hija(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_hija = (self.codigoHijaText.text(), self.nombreHijaText.text())
        
        # Agregar el nuevo texto a la lista de Campus
        self.hijas.append(nuevo_hija)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        nuevo_item = "(" + str(self.codigoHijaText.text()) + ") " + str(self.nombreHijaText.text())
        self.listHijas.addItem(nuevo_item)

        # Actualizar datos
        self.asignaturas[self.asignatura_index].setAsignaturas_hijas(self.hijas)
        self.titulaciones[self.titulacion_index].setAsignaturas(self.asignaturas)
    
    def guardar(self):
        institucion.setTitulacion(self.titulaciones)
        self.close()

# Restricciones Examenes
class ListaRestricionesEx(QWidget, Ui_ListaRestriccionesEx):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.restriccionesT = list(restriccionesExamenes["RestriccionesTiempo"])
        self.restriccionesL = list(restriccionesExamenes["RestriccionesLugar"])

        for restriccion in self.restriccionesT:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            match restriccion.getNombre():
                case "RestriccionXDiasEntreActividades":
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividades"][0].getAsignatura() + "-" + estado)
                case _:
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)
        for restriccion in self.restriccionesL:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)
        self.listaRest.itemClicked.connect(self.irRestriccion)
        self.modificar.clicked.connect(self.modificarRestriccion)
        self.desactivar.clicked.connect(self.desactivarRestriccion)
        self.activar.clicked.connect(self.activarRestriccion)

        self.rest_index = None

    def recargarLista(self):
        self.listaRest.clear()
        for restriccion in self.restriccionesT:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            match restriccion.getNombre():
                case "RestriccionXDiasEntreActividades":
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividades"][0].getAsignatura() + "-" + estado)
                case _:
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)
        for restriccion in self.restriccionesL:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)

    def irRestriccion(self, item):
        self.rest_index = self.listaRest.row(item)
        self.tipo = ""
        
        if self.rest_index >= len(self.restriccionesT):
            self.rest_index -= len(self.restriccionesT)
            self.restricicon_selecionada = self.restriccionesL[self.rest_index]
            self.tipo = self.restricicon_selecionada.getNombre()
        else:
            self.restricicon_selecionada = self.restriccionesT[self.rest_index]
            self.tipo = self.restricicon_selecionada.getNombre()

    def modificarRestriccion(self):
        match self.tipo:
            case "RestriccionAulaPreferida": 
                self.restriccionUI = Res_TipoAula(self.restricicon_selecionada, self.rest_index)
                self.restriccionUI.show()
            case "RestriccionExamenesMismoDia":
                self.restriccionUI = Res_MismoDia(self.restricicon_selecionada, self.rest_index)
                self.restriccionUI.show()
            case "RestriccionXDiasEntreActividades":
                self.restriccionUI = Res_SeparacionDias(self.restricicon_selecionada, self.rest_index, "Asignaturas")
                self.restriccionUI.show()

    def activarRestriccion(self):
        if self.restricicon_selecionada in self.restriccionesL:
            self.restriccionesL[self.rest_index].activar()
        else:
            self.restriccionesT[self.rest_index].activar()

        self.recargarLista()

    def desactivarRestriccion(self):
        if self.restricicon_selecionada in self.restriccionesL:
            self.restriccionesL[self.rest_index].desactivar()
        else:
            self.restriccionesT[self.rest_index].desactivar()

        self.recargarLista()

class Res_TipoAula(QWidget, Ui_res_tipoAula):
    def __init__(self, restriccion, restIndex):
        super().__init__()
        self.setupUi(self) 

        global actClases, actExamenes
        self.actividades = None
        match tipoHorario:
            case "Clase": 
                self.actividades = list(actClases)
            case "Examen":
                self.actividades = list(actExamenes)
        self.campus = institucion.getCampus()
        self.restriccion = restriccion
        self.restIndex = restIndex

        # Inicializar Selectores
        self.actividadText.addItem("Seleccione una opción...")
        self.tipoAulaText.addItem("Seleccione una opción...")

        # Rellenar Selectores
        for actividad in self.actividades:
            self.actividadText.addItem(actividad.getAsignatura())

        self.tipoAulaText.addItem("TODAS")
        self.tipoAulaText.addItem("AULA")
        self.tipoAulaText.addItem("AULA MAGNA")
        self.tipoAulaText.addItem("SEMINARIO")
        self.tipoAulaText.addItem("LABORATORIO")

        if restriccion != None:
            self.actividadText.setCurrentText(restriccion.getDatos()["Actividad"].getAsignatura())
            self.tipoAulaText.setCurrentText(restriccion.getDatos()["Tipo"])
            self.actividadDato = restriccion.getDatos()["Actividad"]

        # Recoger dato del selector
        self.actividadText.currentIndexChanged.connect(self.recogerDatoExamen)

        # Guardar
        self.save.clicked.connect(self.guardar)

        self.actividad_index = None

    
    def recogerDatoExamen(self):
        self.actividad_index = self.actividadText.currentIndex() - 1 # Guardar Indice del elemento seleccionado
        self.actividadDato = self.actividades[self.actividad_index]
        self.currentCampus = self.actividadDato.getCampus()

    def guardar(self):
        datos = {}
        datos["Actividad"] = self.actividadDato
        datos["Tipo"] = self.tipoAulaText.currentText()

        nueva_restriccion = Restriccion("RestriccionAulaPreferida", datos, True, True)
        nueva_restriccion.getDatos()["Actividad"].setTipoAula(self.tipoAulaText.currentText())

        global restriccionesClases, restriccionesExamenes
        if self.restriccion != None:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesLugar"][self.restIndex] = nueva_restriccion
                case "Examen":
                    restriccionesExamenes["RestriccionesLugar"][self.restIndex] = nueva_restriccion
        else:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesLugar"].append(nueva_restriccion)
                case "Examen":
                    restriccionesExamenes["RestriccionesLugar"].append(nueva_restriccion)

        self.actividadDato.setTipoAula(self.tipoAulaText.currentText())

        self.close()

class Res_MismoDia(QWidget, Ui_res_mismoDia):
    def __init__(self, restriccion, restIndex):
        super().__init__()
        self.setupUi(self) 

        global actClases, actExamenes
        self.actividades = None
        match tipoHorario:
            case "Clase": 
                self.actividades = list(actClases)
            case "Examen":
                self.actividades = list(actExamenes)
        self.restriccion = restriccion
        self.restIndex = restIndex

        # Inicializar Selectores
        self.actividad1Text.addItem("Seleccione una opción...")
        self.actividad2Text.addItem("Seleccione una opción...")

        # Rellenar Selectores
        for actividad in self.actividades:
            self.actividad1Text.addItem(actividad.getAsignatura())
            self.actividad2Text.addItem(actividad.getAsignatura())

        if restriccion != None:
            self.actividad1Text.setCurrentText(restriccion.getDatos()["Actividad"].getAsignatura())
            self.actividad2Text.setCurrentText(restriccion.getDatos()["Actividad2"].getAsignatura())
            if restriccion.isObligatoria():
                self.obligatoria.setChecked(True)

        self.actividad1Text.currentIndexChanged.connect(self.actualizarSelector2)
        self.actividad2Text.currentIndexChanged.connect(self.actualizarSelector1)

        # Guardar
        self.save.clicked.connect(self.guardar)

        self.actividad1_index = None
        self.actividad2_index = None

    def actualizarSelector2(self):
        self.actividad1_index = self.actividad1Text.currentIndex() - 1 # Guardar Indice del elemento seleccionado
        self.actividad1Dato = self.actividades[self.actividad1_index]

    def actualizarSelector1(self):
        self.actividad2_index = self.actividad2Text.currentIndex() - 1 # Guardar Indice del elemento seleccionado
        self.actividad2Dato = self.actividades[self.actividad2_index]

    def guardar(self):
        datos = {}
        datos["Actividad"] = self.actividad1Dato
        datos["Actividad2"] = self.actividad2Dato

        nueva_restriccion = Restriccion("RestriccionExamenesMismoDia", datos, self.obligatoria.isChecked(), True)

        global tipoHorario
        if self.restriccion != None:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"][self.restIndex] = nueva_restriccion
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"][self.restIndex] = nueva_restriccion
        else:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"].append(nueva_restriccion)
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"].append(nueva_restriccion)

        self.close()

class Res_SeparacionDias(QWidget, Ui_res_separacionDias):
    def __init__(self, restriccion, restIndex, tipo):
        super().__init__()
        self.setupUi(self) 

        global actClases, actExamenes
        self.actividades = None
        match tipoHorario:
            case "Clase": 
                self.actividades = list(actClases)
            case "Examen":
                self.actividades = list(actExamenes)

        self.restriccion = restriccion
        self.restIndex = restIndex
        self.tipo = tipo

        # Inicializar Selectores
        self.actividad1Text.addItem("Seleccione una opción...")
        self.actividad2Text.addItem("Seleccione una opción...")

        # Rellenar Selectores
        for actividad in self.actividades:
            self.actividad1Text.addItem(actividad.getAsignatura())
            self.actividad2Text.addItem(actividad.getAsignatura())

        if restriccion != None:
            self.actividad1Text.setCurrentText(restriccion.getDatos()["Actividades"][0].getAsignatura())
            self.actividad2Text.setCurrentText(restriccion.getDatos()["Actividades"][1].getAsignatura())
            self.actividad1Dato = restriccion.getDatos()["Actividades"][0]
            self.actividad2Dato = restriccion.getDatos()["Actividades"][1]
            self.separacionText.setValue(restriccion.getDatos()["Separacion"])
            if restriccion.isObligatoria():
                self.obligatoria.setChecked(True)
            

        # Borrar del selector contrario el elemento seleccionado
        self.actividad1Text.currentIndexChanged.connect(self.actualizarSelector2)
        self.actividad2Text.currentIndexChanged.connect(self.actualizarSelector1)

        # Guardar
        self.save.clicked.connect(self.guardar)

        self.actividad1_index = None
        self.actividad2_index = None

    def actualizarSelector2(self):
        self.actividad1_index = self.actividad1Text.currentIndex() - 1 # Guardar Indice del elemento seleccionado
        self.actividad1Dato = self.actividades[self.actividad1_index]

    def actualizarSelector1(self):
        self.actividad2_index = self.actividad2Text.currentIndex() - 1 # Guardar Indice del elemento seleccionado
        self.actividad2Dato = self.actividades[self.actividad2_index]

    def guardar(self):
        datos = {}
        datos["Actividades"] = [self.actividad1Dato, self.actividad2Dato]
        datos["Separacion"] = self.separacionText.value()

        nueva_restriccion = None
        if self.tipo == "Asignaturas":
            nueva_restriccion = Restriccion("RestriccionXDiasEntreActividades", datos, self.obligatoria.isChecked(), True)
        elif self.tipo == "Clases":
            nueva_restriccion = Restriccion("SeparacionClasesMismaAsignatura", datos, self.obligatoria.isChecked(), True)

        global tipoHorario
        if self.restriccion != None:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"][self.restIndex] = nueva_restriccion
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"][self.restIndex] = nueva_restriccion
        else:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"].append(nueva_restriccion)
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"].append(nueva_restriccion)

        self.close()

class RestriccionesExamenes(QWidget, Ui_RestriccionesEx):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.separacion.clicked.connect(self.mostrarSeparacionUI)
        self.mismoDia.clicked.connect(self.mostrarMismoDiaUI)
        self.tipoAula.clicked.connect(self.mostrarTipoAulaUI)
        self.todas.clicked.connect(self.mostrarListaRestriccionesUI)

    def mostrarSeparacionUI(self):
        self.separacionUI = Res_SeparacionDias(None, 0, "Asignaturas")
        self.separacionUI.show()

    def mostrarMismoDiaUI(self):
        self.mismoDiaUI = Res_MismoDia(None, 0)
        self.mismoDiaUI.show()
    
    def mostrarTipoAulaUI(self):
        self.tipoAulaUI = Res_TipoAula(None, 0)
        self.tipoAulaUI.show()

    def mostrarListaRestriccionesUI(self):
        self.listaRestriccionesUI = ListaRestricionesEx()
        self.listaRestriccionesUI.show()

# Examenes
class ModificarExamen(QWidget, Ui_ModificarExamenes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.titulaciones = institucion.getTitulacion()

        # Inicializar el selectorer
        self.titulacionText.addItem("Seleccione una opción...")

        # Rellenar el selector de titulaciones
        for titulacion in self.titulaciones:
            self.titulacionText.addItem(titulacion.getNombre())
        
        self.actividades = list(actExamenes)

        self.titulacionText.currentIndexChanged.connect(self.actualizar_examenes)
        self.actividadesList.itemClicked.connect(self.updateLineEditText)
        self.modificar.clicked.connect(self.modificar_elemento)
        self.sup.clicked.connect(self.borrar_elemento)
        self.save.clicked.connect(self.guardar)

        self.index = None
        self.actividadesBorradas = []

    def actualizar_examenes(self):
        self.titulacion_index = self.titulacionText.currentIndex() - 1
        self.titName = self.titulaciones[self.titulacion_index].getNombre()

        self.actividadesTitulacion = []
        actividadesTitulacionNombre = []
        for actividad in self.actividades:
            if self.titName in actividad.getTitulacion():
                self.actividadesTitulacion.append(actividad)
                actividadesTitulacionNombre.append(actividad.getAsignatura())

        self.actividadesList.clear()
        self.actividadesList.addItems(actividadesTitulacionNombre)
    
    def updateLineEditText(self, item):
        self.index = self.actividadesList.row(item)  # Guardar índice del elemento seleccionado
        # Rellenar los datos del elemneto selecionado
        self.asignaturaText.setText(self.actividadesTitulacion[self.index].getAsignatura())
        self.alumnosText.setText(", ".join(self.actividadesTitulacion[self.index].getCurso()))
        self.duracionText.setValue(self.actividadesTitulacion[self.index].getDuracion())

    def modificar_elemento(self):
        if self.index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_duracion = self.duracionText.value()
            
            # Actualizar el elemento
            self.actividadesTitulacion[self.index].setDuracion(nuevo_duracion)

    def borrar_elemento(self):
        if self.index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento
            self.actividadesBorradas.append(self.actividadesTitulacion[self.index])
            del self.actividadesTitulacion[self.index]
            
            # Eliminar el elemento del QListWidget
            self.actividadesList.takeItem(self.index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.asignaturaText.clear()
            self.alumnosText.clear()
            self.duracionText.clear()
            self.index = None

    def guardar(self):
        global actExamenes
        if self.actividadesBorradas:
            for actBorrada in self.actividadesBorradas:
                self.actividades.remove(actBorrada)
            i = 1
            for actividad in self.actividades:
                actividad.setIdActividad(i)
                i += 1
        for i in range(len(self.actividades)):
            for actividadTit in self.actividadesTitulacion:
                if self.actividades[i].getIdActividad() == actividadTit.getIdActividad():
                    self.actividades[i] = actividadTit

        actExamenes = list(self.actividades)
        self.close()        

class ExamenesUI(QWidget, Ui_Examenes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.titulaciones = institucion.getTitulacion()

        self.crearCurso()

        self.modificar.clicked.connect(self.mostrarModificarExamenUI)
        
        self.periodoExamenesText.setValue(diasSemanaExamenes.getNumDias())
        self.periodoExamenesText.valueChanged.connect(self.crearDias)

        self.aulasCombinadas.clicked.connect(self.mostrarAulaCombinadaUI)

        self.exportar.clicked.connect(self.exportarDatos)

        self.restricciones.clicked.connect(self.mostrarRestriccionesUI)
        self.crearHorario.clicked.connect(self.nuevoHorario)

    def crearExamenes(self):
        global actExamenes, restriccionesExamenes, examenesPorCuros
        if not actExamenes:
            # Activar Restricciones automáticas
            restriccion48h = Restriccion("MismoCursoSeparado48h", {"Actividad": Actividad(0, 0, "Todas", [], "", [], 0, 0, "TODAS")}, True, True)
            restriccionesExamenes["RestriccionesTiempo"].append(restriccion48h)
            restricion24h = Restriccion("CursosConsecutivosSeparado24h", {"Actividad": Actividad(0, 0, "Todas", [], "", [], 0, 0, "TODAS")}, True, True)
            restriccionesExamenes["RestriccionesTiempo"].append(restricion24h)

            restriccionCampus = Restriccion("MismoCampusDondeSeImparte", {"Actividad": Actividad(0, 0, "Todas", [], "", [], 0, 0, "TODAS")}, True, True)
            restriccionesExamenes["RestriccionesLugar"].append(restriccionCampus)

            asignaturasUsadas = set()
            idActividad = 1
            cursos_dict = defaultdict(list)
            for tit in self.titulaciones:
                campus = tit.getCampus()
                for asignatura in tit.getAsignaturas():
                    if asignatura.getNombre() not in asignaturasUsadas:
                        asignaturasElegidas.append(asignatura)
                        asignaturasUsadas.add(asignatura.getNombre())
                        estudiantes = []
                        titulaciones = []
                        curso = tit.getNombre() + "-" + asignatura.getNombre()
                        if tit.getNombre() not in listaNegraAsignaturas:
                            estudiantes.append(curso)
                        titulaciones.append(asignatura.getTitulacion())
                        for hija in asignatura.getAsignaturas_hijas():
                            cursoHija = hija[0] + "-" + hija[1]
                            if hija[0] not in listaNegraAsignaturas:
                                estudiantes.append(cursoHija)
                            titulaciones.append(hija[0])
                            asignaturasUsadas.add(hija[1])

                        nuevaActividad = Actividad(idActividad, 0, asignatura.getNombre(), titulaciones, campus, estudiantes, 2, 2, "TODAS")
                        cursos_dict[str(tit.getNombre() + "-" + str(asignatura.getCurso()))].append(nuevaActividad)
                        idActividad += 1
                        actExamenes.append(nuevaActividad)
            
            examenesPorCuros = cursos_dict
    
    def crearCurso(self):
        if not alumnos:
            for tit in self.titulaciones:
                cursos_dict = {}
                alumnosTit = AlumnosTitulacion(tit.getNombre())
                for asignatura in tit.getAsignaturas():
                    numCurso = asignatura.getCurso()
                    nombreCurso = tit.getNombre() + "-" + str(numCurso)
                    cursos_dict.setdefault(numCurso, AlumnosCurso(nombreCurso))

                    nombreAsignatura = tit.getNombre() + "-" + asignatura.getNombre()
                    alumnosAsig = AlumnosAsignatura(nombreAsignatura, asignatura.getNumAlumnos())
                    cursos_dict[numCurso].agregar_asignatura(alumnosAsig)

                alumnosTit.setCursos(list(cursos_dict.values()))
                alumnos.append(alumnosTit)

        self.crearExamenes()
    
    def crearDias(self):
        numDias = self.periodoExamenesText.value()
        dia = 1
        semana = 1
        dias = []
        for i in range(numDias):
            match dia:
                case 1: 
                    dias.append(f"Lunes{semana}")
                    dia+=1
                case 2:
                    dias.append(f"Martes{semana}")
                    dia+=1
                case 3:
                    dias.append(f"Miercoles{semana}")
                    dia+=1
                case 4:
                    dias.append(f"Jueves{semana}")
                    dia+=1
                case 5:
                    dias.append(f"Viernes{semana}")
                    dia+=1
                case 6:
                    dias.append(f"Sabados{semana}")
                    dia = 1
                    semana+=1
            
        diasSemanaExamenes.setDias(dias)
    
    def mostrarRestriccionesUI(self):
        self.restriccionesUI = RestriccionesExamenes()
        self.restriccionesUI.show()
    
    def nuevoHorario(self):
        global ruta_fet

        ruta_carpeta = os.path.dirname(ruta_fet)

        if os.path.isdir(ruta_carpeta):
            if os.path.isfile(ruta_fet):
                # Nombre y extensión predeterminada del archivo
                default_filename = "data.fet"

                #  Abrir un diálogo para seleccionar la ubicación y nombre del archivo a guardar
                file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo FET", default_filename, "Archivos FET (*.fet)")

                if file_path:
                    # Asegurarse de que la extensión sea .fet (si el usuario la cambia accidentalmente)
                    if not file_path.endswith(".fet"):
                        file_path += ".fet"
                    
                    # Guardar el archivo en la ruta seleccionada
                    exportarFET(file_path, institucion, diasSemanaExamenes, horasDiaExamenes, asignaturasElegidas, alumnos, actExamenes, aulasPorCampus, aulasPorTipo, examenesPorCuros, restriccionesExamenes["RestriccionesTiempo"], restriccionesExamenes["RestriccionesLugar"], "Examen")
                
                # Obtener el directorio base del archivo .fet
                base_dir = os.path.dirname(file_path)

                # Crear el directorio "Resultado" en el mismo directorio que el archivo .fet
                resultado_dir = os.path.join(base_dir, "Resultado")
                os.makedirs(resultado_dir, exist_ok=True)

                # Verificar si el archivo existe
                if os.path.isfile(file_path):
                    try:
                        # Construir el comando para ejecutar FET
                        command = [ruta_fet, f"--inputfile={file_path}", f"--outputdir={resultado_dir}"]
                        print("Ejecutando comando:", " ".join(command))  # Para depuración
                        
                        # Ejecutar FET con el archivo .fet
                        subprocess.run(command, check=True)
                        print(f"FET se ejecutó correctamente. Los resultados están en: {resultado_dir}")
                        dialogoError = DialogoError(f"FET se ejecutó correctamente. Los resultados están en: {resultado_dir}")
                        dialogoError.exec()
                    except subprocess.CalledProcessError as e:
                        print(f"Hubo un error al ejecutar FET: {e}")
                        dialogoError = DialogoError(f"Error: Hubo un error al ejecutar FET: {e}")
                        dialogoError.exec()
                    except Exception as e:
                        print(f"Otro error ocurrió: {e}")
                        dialogoError = DialogoError(f"Error: Otro error ocurrió: {e}")
                        dialogoError.exec()
                else:
                    print(f"El archivo {file_path} no existe.")
                    dialogoError = DialogoError(f"Error: El archivo {file_path} no existe.")
                    dialogoError.exec()
            else:
                self.fetConnect = FETConnectUI(f"Error: No se encontró {ruta_fet}. Indique la ruta de fet-cl.exe:")
                self.fetConnect.show()
        else:
            self.fetConnect = FETConnectUI(f"Error: La carpeta {ruta_carpeta} no existe. Indique la ruta de fet-cl.exe:")
            self.fetConnect.show()

    def exportarDatos(self):
        # Nombre y extensión predeterminada del archivo
        default_filename = "archivo_guardado.xml"

        #  Abrir un diálogo para seleccionar la ubicación y nombre del archivo a guardar
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo XML", default_filename, "Archivos XML (*.xml)")

        if file_path:
            # Asegurarse de que la extensión sea .xml (si el usuario la cambia accidentalmente)
            if not file_path.endswith(".xml"):
                file_path += ".xml"
            
            # Guardar el archivo en la ruta seleccionada
            exportar(file_path, institucion, alumnos, diasSemanaClases, diasSemanaExamenes, horasDiaClases, horasDiaExamenes, asignaturasElegidas, actClases, actExamenes, restriccionesClases, restriccionesExamenes)

    def mostrarModificarExamenUI(self):
        self.modificarExamenUI = ModificarExamen()
        self.modificarExamenUI.show()

    def mostrarAulaCombinadaUI(self):
        self.aulaCombinadaUI = AulaCombinadaUI("Examen")
        self.aulaCombinadaUI.show()

# Restricciones Clases
class ListaRestricionesCl(QWidget, Ui_ListaRestriccionesCl):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.restriccionesT = list(restriccionesClases["RestriccionesTiempo"])
        self.restriccionesL = list(restriccionesClases["RestriccionesLugar"])

        for restriccion in self.restriccionesT:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            match restriccion.getNombre():
                case "RestriccionTurno" | "MaxHorasPorDia" | "MaxHuecosPorSemana":
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Curso"] + "-" + estado)
                case "RestriccionXDiasEntreActividades" | "SeparacionClasesMismaAsignatura":
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividades"][0].getAsignatura() + "-" + estado)
                case _:
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)
        for restriccion in self.restriccionesL:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)

        self.listaRest.itemClicked.connect(self.irRestriccion)
        self.modificar.clicked.connect(self.modificarRestriccion)
        self.desactivar.clicked.connect(self.desactivarRestriccion)
        self.activar.clicked.connect(self.activarRestriccion)

        self.rest_index = None

    def recargarLista(self):
        self.listaRest.clear()
        for restriccion in self.restriccionesT:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            match restriccion.getNombre():
                case "RestriccionTurno" | "MaxHorasPorDia" | "MaxHuecosPorSemana":
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Curso"] + "-" + estado)
                case "RestriccionXDiasEntreActividades" | "SeparacionClasesMismaAsignatura":
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividades"][0].getAsignatura() + "-" + estado)
                case _:
                    self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)
        for restriccion in self.restriccionesL:
            if restriccion.getEstado():
                estado = "Activa"
            else:
                estado = "Desactivada"
            self.listaRest.addItem(restriccion.getNombre() + "-" + restriccion.getDatos()["Actividad"].getAsignatura() + "-" + estado)

    def irRestriccion(self, item):
        self.rest_index = self.listaRest.row(item)
        self.tipo = ""
        
        if self.rest_index >= len(self.restriccionesT):
            self.rest_index -= len(self.restriccionesT)
            self.restricicon_selecionada = self.restriccionesL[self.rest_index]
            self.tipo = self.restricicon_selecionada.getNombre()
        else:
            self.restricicon_selecionada = self.restriccionesT[self.rest_index]
            self.tipo = self.restricicon_selecionada.getNombre()

    def modificarRestriccion(self):
        match self.tipo:
            case "RestriccionAulaPreferida": 
                self.restriccionUI = Res_TipoAula(self.restricicon_selecionada, self.rest_index)
                self.restriccionUI.show()

            case "RestriccionXDiasEntreActividades":
                self.restriccionUI = Res_SeparacionDias(self.restricicon_selecionada, self.rest_index, "Asignaturas")
                self.restriccionUI.show()

            case "SeparacionClasesMismaAsignatura":
                self.restriccionUI = Res_SeparacionDias(self.restricicon_selecionada, self.rest_index, "Clases")
                self.restriccionUI.show()

            case "MaxHorasPorDia":
                self.restriccionUI = Res_MaxHorasDia(self.restricicon_selecionada, self.rest_index, "")
                self.restriccionUI.show()

            case "MaxHuecosPorSemana":
                self.restriccionUI = Res_MaxHuecosSemana(self.restricicon_selecionada, self.rest_index, "")
                self.restriccionUI.show()

    def activarRestriccion(self):
        if self.restricicon_selecionada in self.restriccionesL:
            self.restriccionesL[self.rest_index].activar()
        else:
            self.restriccionesT[self.rest_index].activar()
        
        self.recargarLista()

    def desactivarRestriccion(self):
        if self.restricicon_selecionada in self.restriccionesL:
            self.restriccionesL[self.rest_index].desactivar()
        else:
            self.restriccionesT[self.rest_index].desactivar()

        self.recargarLista()

class Res_Turno(QWidget, Ui_res_turno):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tit = institucion.getTitulacion()

        # Inicializar Selectores
        self.titulacionText.addItem("Seleccione una opción...")
        self.cursoText.addItem("Seleccione una opción...")

        for titulacion in self.tit:
            self.titulacionText.addItem(titulacion.getNombre())

        self.titulacionText.currentIndexChanged.connect(self.actualizarAsignaturas)
        self.cursoText.currentIndexChanged.connect(self.getCurso)

        # Guardar
        self.save.clicked.connect(self.guardar)

        self.titulacion_index = None
    
    def actualizarAsignaturas(self):
        self.titulacion_index = self.titulacionText.currentIndex() - 1 # Guardar Indice
        self.asignaturas = self.tit[self.titulacion_index].getAsignaturas()

        for asignatura in self.asignaturas:
            cusoNum = str(asignatura.getCurso())
            if cusoNum not in [self.cursoText.itemText(i) for i in range(self.cursoText.count())]:
                self.cursoText.addItem(cusoNum)

    def getCurso(self):
        global actClases, actExamenes
        self.cursoName = self.titulacionText.currentText()  + "-" +  self.cursoText.currentText()
        match (tipoHorario):
            case "Clase":
                self.actividades  = clasesPorCuros[self.cursoName]
            case "Examen":
                self.actividades  = examenesPorCuros[self.cursoName]

    def guardar(self):
        dato = {"Curso": self.cursoName, "HoraIni": self.horaIniText.time().toString("HH:mm"), "HoraFin": self.horaFinText.time().toString("HH:mm")}
        nuevaRestriccion = Restriccion("RestriccionTurno", dato, True, True)
        match (tipoHorario):
            case "Clase":
                restriccionesClases["RestriccionesTiempo"].append(nuevaRestriccion)
            case "Examen":
                restriccionesExamenes["RestriccionesTiempo"].append(nuevaRestriccion)

        self.close()

class Res_MaxHorasDia(QWidget, Ui_MaxHorasDia):
    def __init__(self, restriccion, restIndex, tipo):
        super().__init__()
        self.setupUi(self) 

        self.tit = institucion.getTitulacion()
        self.cursos = list(alumnos)
        self.restIndex = restIndex
        self.restriccion = restriccion

        self.titulacionText.addItem("Seleccione una opción...")
        self.grupoText.addItem("Seleccione una opción...")

        for titulacion in self.tit:
            self.titulacionText.addItem(titulacion.getNombre())

        self.titulacionText.currentIndexChanged.connect(self.actualizarGrupos)

        if self.restriccion != None:
            self.titulacionText.setCurrentText(restriccion.getDatos()["Curso"].split('-')[0])
            self.grupoText.setCurrentText(restriccion.getDatos()["Curso"])
            self.horasText.setValue(restriccion.getDatos()["Horas"])

        # Guardar
        self.save.clicked.connect(self.guardar)

        self.titulacion_index = None

    def actualizarGrupos(self):
        self.titulacion_index = self.titulacionText.currentIndex() - 1 # Guardar Indice
        self.currentTit = self.tit[self.titulacion_index].getNombre()

        for curso in self.cursos:
            if curso.getNombre() == self.currentTit:
                self.grupos = curso.getCursos()
                for grupo in self.grupos:
                    self.grupoText.addItem(grupo.getNombre())

    def guardar(self):
        global tipoHorario

        currentGrupo = self.grupoText.currentText()
        dato = {"Curso": currentGrupo, "Horas": self.horasText.value()}
        nuevaRestriccion = Restriccion("MaxHorasPorDia", dato, True, True)

        if self.restriccion != None:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"][self.restIndex] = nuevaRestriccion
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"][self.restIndex] = nuevaRestriccion
        else:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"].append(nuevaRestriccion)
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"].append(nuevaRestriccion)
        
        self.close()

class Res_MaxHuecosSemana(QWidget, Ui_MaxHuecosSemana):
    def __init__(self, restriccion, restIndex, tipo):
        super().__init__()
        self.setupUi(self) 

        self.tit = institucion.getTitulacion()
        self.cursos = list(alumnos)
        self.restIndex = restIndex
        self.restriccion = restriccion

        self.titulacionText.addItem("Seleccione una opción...")
        self.grupoText.addItem("Seleccione una opción...")

        for titulacion in self.tit:
            self.titulacionText.addItem(titulacion.getNombre())

        self.titulacionText.currentIndexChanged.connect(self.actualizarGrupos)

        if self.restriccion != None:
            self.titulacionText.setCurrentText(self.restriccion.getDatos()["Curso"].split('-')[0])
            self.grupoText.setCurrentText(self.restriccion.getDatos()["Curso"])
            self.huecosText.setValue(self.restriccion.getDatos()["Horas"])

        # Guardar
        self.save.clicked.connect(self.guardar)

        self.titulacion_index = None

    def actualizarGrupos(self):
        self.titulacion_index = self.titulacionText.currentIndex() - 1 # Guardar Indice
        self.currentTit = self.tit[self.titulacion_index].getNombre()

        for curso in self.cursos:
            if curso.getNombre() == self.currentTit:
                self.grupos = curso.getCursos()
                for grupo in self.grupos:
                    self.grupoText.addItem(grupo.getNombre())

    def guardar(self):
        global tipoHorario

        currentGrupo = self.grupoText.currentText()
        dato = {"Curso": currentGrupo, "Horas": self.huecosText.value()}
        nuevaRestriccion = Restriccion("MaxHuecosPorSemana", dato, True, True)

        if self.restriccion != None:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"][self.restIndex] = nuevaRestriccion
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"][self.restIndex] = nuevaRestriccion
        else:
            match (tipoHorario):
                case "Clase":
                    restriccionesClases["RestriccionesTiempo"].append(nuevaRestriccion)
                case "Examen":
                    restriccionesExamenes["RestriccionesTiempo"].append(nuevaRestriccion)
        
        self.close()

class RestriccionesClases(QWidget, Ui_RestriccionesCl):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.separacion.clicked.connect(self.mostrarSeparacionUI)
        self.turno.clicked.connect(self.mostrarTurnoUI)
        self.horasDia.clicked.connect(self.mostrarMaxHorasUI)
        self.huecosSemana.clicked.connect(self.mostrarMaxHuecosUI)
        self.tipoAula.clicked.connect(self.mostrarTipoAulaUI)
        self.todas.clicked.connect(self.mostrarListaRestriccionesUI)

    def mostrarSeparacionUI(self):
        self.separacionUI = Res_SeparacionDias(None, 0, "Asignaturas")
        self.separacionUI.show()

    def mostrarTurnoUI(self):
        self.turnoUI = Res_Turno()
        self.turnoUI.show()

    def mostrarMaxHorasUI(self):
        self.maxDiaUI = Res_MaxHorasDia(None, 0 , "")
        self.maxDiaUI.show()

    def mostrarMaxHuecosUI(self):
        self.maxHuecosUI = Res_MaxHuecosSemana(None, 0 , "")
        self.maxHuecosUI.show()
        
    def mostrarTipoAulaUI(self):
        self.tipoAulaUI = Res_TipoAula(None, 0)
        self.tipoAulaUI.show()

    def mostrarListaRestriccionesUI(self):
        self.listaRestriccionesUI = ListaRestricionesCl()
        self.listaRestriccionesUI.show()

# Clases
class ModificarClase(QWidget, Ui_ModificarClases):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.clases = list(actClases)
        self.duraciones = []
        self.duracionTotal = 0

        # Crear un QWidget para la pestaña
        tab = QWidget()
        
        # Crear los elementos
        label_duracion = QLabel("Duración")
        spin_box = QSpinBox()
        spin_box.setSuffix("h")  # Añadir "h" como sufijo opcional en el QSpinBox
        spin_box.setRange(0, 24)  # Rango de valores: 0 a 24 horas
        
        # Crear un layout horizontal y agregar los elementos
        layout = QHBoxLayout()
        layout.addWidget(label_duracion)
        layout.addWidget(spin_box)
        
        # Establecer el layout al QWidget de la pestaña
        tab.setLayout(layout)
        
        # Agregar la pestaña al QTabWidget
        nombre = "Clase" + str(1)
        self.sesionesList.addTab(tab, nombre)

        # Inicializar el selectorer
        self.asignaturaText.addItem("Seleccione una opción...")

        for clase in self.clases:
            self.asignaturaText.addItem(clase.getAsignatura())

        self.sesionesText.setValue(1)
        self.asignaturaText.currentIndexChanged.connect(self.actualizarClases)
        self.sesionesText.valueChanged.connect(self.actualizarSesiones)
        self.save.clicked.connect(self.guardar)

        self.index = None

    def actualizarClases(self):
        self.index = self.asignaturaText.currentIndex() - 1
        self.clase = self.clases[self.index]

        self.sesionesIniciales = len(self.clase.getActividadesHija()) + 1
        self.sesionesText.setValue(self.sesionesIniciales)

    def borrarPestañas(self):
        while self.sesionesList.count() > 0:
            self.sesionesList.removeTab(0)

    def actualizarSesiones(self):
        self.borrarPestañas()
        self.sesionesAñadidas = self.sesionesText.value() - self.sesionesIniciales
        for i in range(0, self.sesionesText.value()):
            # Crear un QWidget para la pestaña
            tab = QWidget()
            
            # Crear los elementos
            label_duracion = QLabel("Duración")
            spin_box = QSpinBox()
            spin_box.setSuffix("h")  # Añadir "h" como sufijo opcional en el QSpinBox
            spin_box.setRange(0, 24)  # Rango de valores: 0 a 24 horas

            if i == 0:
                spin_box.setValue(self.clase.getDuracion())
            elif i <= len(self.clase.getActividadesHija()):
                spin_box.setValue(self.clase.getActividadesHija()[i-1].getDuracion())
            else:
                spin_box.setValue(0)
            
            # Crear un layout horizontal y agregar los elementos
            layout = QHBoxLayout()
            layout.addWidget(label_duracion)
            layout.addWidget(spin_box)
            
            # Establecer el layout al QWidget de la pestaña
            tab.setLayout(layout)
            
            # Agregar la pestaña al QTabWidget
            nombre = "Clase" + str(i+1)
            self.sesionesList.addTab(tab, nombre)

    def calcularDuraciones(self):
        # Recorrer cada pestaña
        for i in range(self.sesionesList.count()):
            # Obtener el widget de la pestaña
            tab = self.sesionesList.widget(i)
            
            # Acceder al layout de la pestaña
            layout = tab.layout()
            
            # Buscar el QSpinBox en el layout y obtener su valor
            for j in range(layout.count()):
                widget = layout.itemAt(j).widget()
                if isinstance(widget, QSpinBox):
                    self.duraciones.append(widget.value())
                    self.duracionTotal += widget.value()

    def actualizarIdActividad(self):
        elementoSiguiente = self.index+1
        for actividad in self.clases[elementoSiguiente:]:
            idAntiguo = actividad.getIdActividad()
            idNuevo = idAntiguo + self.sesionesAñadidas
            actividad.setIdActividad(idNuevo)
            for hija in actividad.getActividadesHija():
                idAntiguoH = hija.getIdActividad()
                idNuevoH = idAntiguoH + self.sesionesAñadidas
                hija.setIdActividad(idNuevoH)
   
    def guardar(self):
        self.calcularDuraciones()

        self.clase.setDuracion(self.duraciones[0])
        self.clase.setDuracionTotal(self.duracionTotal)
        self.hijas = self.clase.getActividadesHija()
        self.nuevasHijas = []
        for i in range(1, len(self.duraciones)):
            try: 
                self.hijas[i-1].setDuracion(self.duraciones[i])
                self.hijas[i-1].setDuracionTotal(self.duracionTotal)
                self.nuevasHijas.append(self.hijas[i-1])
            except IndexError:
                nuevaID = self.clase.getIdActividad() + len(self.hijas) + 1
                nuevaSesion = Actividad(nuevaID, self.clase.getIdGrupo(), self.clase.getAsignatura(), self.clase.getTitulacion(), self.clase.getCampus(), self.clase.getCurso(), self.duraciones[i], self.duracionTotal, self.clase.getTipoAula())
                self.nuevasHijas.append(nuevaSesion)
            
        self.clase.setActividadesHija(self.nuevasHijas)
        self.clases[self.index] = self.clase
        self.actualizarIdActividad()
        global actClases, restriccionesClases
        actClases = self.clases

        restriccionesClases["RestriccionesTiempo"][self.clase.getRestIndex()].setDatos({"Actividades": [self.clase] + self.nuevasHijas, "Separacion": 1})

        self.close()

class OtrosHorariosUI(QWidget, Ui_otrosHorarios):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.totalDias = diasSemanaClases.getDias()
        self.totalHoras = horasDiaClases.getHoras()

        self.numDiasText.setValue(5)
        self.numHorasText.setValue(13)

        for dia in self.totalDias:
            item = QListWidgetItem(dia)
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # Hacer el elemento editable
            self.listaDias.addItem(item)
        
        for hora in self.totalHoras:
            item = QListWidgetItem(hora)
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # Hacer el elemento editable
            self.listaHoras.addItem(item)

        
        self.numDiasText.valueChanged.connect(self.modificarDias)
        self.numHorasText.valueChanged.connect(self.modificarHoras)
        self.save.clicked.connect(self.guardar)
            
    
    def modificarDias(self):
        numTotalDias = self.numDiasText.value()
        diferencia = self.listaDias.count() - numTotalDias

        if diferencia > 0:
            while numTotalDias != self.listaDias.count():
                self.listaDias.takeItem(self.listaDias.count() - 1)
        elif diferencia < 0:
            i = 0
            while numTotalDias != self.listaDias.count():
                item = QListWidgetItem("NuevoDia" + str(i))
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.listaDias.addItem(item)
                i+=1

    def modificarHoras(self):
        numTotalHoras = self.numHorasText.value()
        diferencia = self.listaHoras.count() - numTotalHoras

        if diferencia > 0:
            while numTotalHoras != self.listaHoras.count():
                self.listaHoras.takeItem(self.listaHoras.count() - 1)
        elif diferencia < 0:
            i = 0
            while numTotalHoras != self.listaHoras.count():
                item = QListWidgetItem("NuevaHora" + str(i))
                item.setFlags(item.flags() | Qt.ItemIsEditable)  # Hacer el elemento editable
                self.listaHoras.addItem(item)
                i+=1

    def guardar(self):
        global diasSemanaClases, horasDiaClases
        diasSemanaClases.setDias([self.listaDias.item(i).text() for i in range(self.listaDias.count())])
        horasDiaClases.setHoras([self.listaHoras.item(i).text() for i in range(self.listaHoras.count())])
        self.close()

class ClasesUI(QWidget, Ui_Clases):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.semanal.setChecked(True)
        self.titulaciones = institucion.getTitulacion()
        self.crearCurso()

        self.modificar.clicked.connect(self.mostrarModificarClasesUI)
        self.otros.clicked.connect(self.mostrarOtrosHorariosUI)
        self.aulasCombinadas.clicked.connect(self.mostrarAulaCombinadaUI)
        self.exportar.clicked.connect(self.exportarDatos)
        self.crearHorario.clicked.connect(self.nuevoHorario)
        self.restricciones.clicked.connect(self.mostrarRestriccionesUI)

    def crearClases(self):
        global actClases, restriccionesClases, clasesPorCuros
        if not actClases:
            restriccionCampus = Restriccion("MismoCampusDondeSeImparte", {"Actividad": Actividad(0, 0, "Todas", [], "", [], 0, 0, "TODAS")}, True, True)
            restriccionesClases["RestriccionesLugar"].append(restriccionCampus)

            asignaturasUsadas = set()
            idActividad = 1
            cursos_dict = defaultdict(list)
            for tit in self.titulaciones:
                campus = tit.getCampus()
                for asignatura in tit.getAsignaturas():
                    if asignatura.getNombre() not in asignaturasUsadas:
                        asignaturasElegidas.append(asignatura)
                        asignaturasUsadas.add(asignatura.getNombre())
                        estudiantes = []
                        titulaciones = []
                        curso = tit.getNombre() + "-" + asignatura.getNombre()
                        if tit.getNombre() not in listaNegraAsignaturas:
                            estudiantes.append(curso)
                        titulaciones.append(asignatura.getTitulacion())
                        for hija in asignatura.getAsignaturas_hijas():
                            cursoHija = hija[0] + "-" + hija[1]
                            if hija[0] not in listaNegraAsignaturas:
                                estudiantes.append(cursoHija)
                            titulaciones.append(hija[0])
                            asignaturasUsadas.add(hija[1])

                        nuevaActividad1 = Actividad(idActividad, idActividad, asignatura.getNombre(), titulaciones, campus, estudiantes, 2, 4, "TODAS")
                        nuevaActividad2 = Actividad(idActividad + 1, idActividad, asignatura.getNombre(), titulaciones, campus, estudiantes, 2, 4, "TODAS")
                        nuevaActividad1.addActividadesHija(nuevaActividad2)

                        separacionClases = Restriccion("SeparacionClasesMismaAsignatura", {"Actividades": [nuevaActividad1, nuevaActividad2], "Separacion": 1}, True, True)

                        restriccionesClases["RestriccionesTiempo"].append(separacionClases)
                        nuevaActividad1.addRestIndex(len(restriccionesClases["RestriccionesTiempo"]) - 1)

                        cursos_dict[str(tit.getNombre() + "-" + str(asignatura.getCurso()))].append(nuevaActividad1)
                        idActividad += 2
                        actClases.append(nuevaActividad1)
        
            clasesPorCuros = cursos_dict

    def crearCurso(self):
        if not alumnos:
            for tit in self.titulaciones:
                cursos_dict = {}
                alumnosTit = AlumnosTitulacion(tit.getNombre())
                for asignatura in tit.getAsignaturas():
                    numCurso = asignatura.getCurso()
                    nombreCurso = tit.getNombre() + "-" + str(numCurso)
                    cursos_dict.setdefault(numCurso, AlumnosCurso(nombreCurso))

                    nombreAsignatura = tit.getNombre() + "-" + asignatura.getNombre()
                    alumnosAsig = AlumnosAsignatura(nombreAsignatura, asignatura.getNumAlumnos())
                    cursos_dict[numCurso].agregar_asignatura(alumnosAsig)

                alumnosTit.setCursos(list(cursos_dict.values()))
                alumnos.append(alumnosTit)

        self.crearClases()

    def exportarDatos(self):
        # Nombre y extensión predeterminada del archivo
        default_filename = "archivo_guardado.xml"

        #  Abrir un diálogo para seleccionar la ubicación y nombre del archivo a guardar
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo XML", default_filename, "Archivos XML (*.xml)")

        if file_path:
            # Asegurarse de que la extensión sea .xml (si el usuario la cambia accidentalmente)
            if not file_path.endswith(".xml"):
                file_path += ".xml"
            
            # Guardar el archivo en la ruta seleccionada
            exportar(file_path, institucion, alumnos, diasSemanaClases, diasSemanaExamenes, horasDiaClases, horasDiaExamenes, asignaturasElegidas, actClases, actExamenes, restriccionesClases, restriccionesExamenes)

    def nuevoHorario(self):
        if self.semanal.isChecked():
                global diasSemanaClases, horasDiaClases
                diasSemanaClases = Dias()
                horasDiaClases = Horas()

        global ruta_fet
        ruta_carpeta = os.path.dirname(ruta_fet)

        if os.path.isdir(ruta_carpeta):
            if os.path.isfile(ruta_fet):
                # Nombre y extensión predeterminada del archivo
                default_filename = "data.fet"

                #  Abrir un diálogo para seleccionar la ubicación y nombre del archivo a guardar
                file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo FET", default_filename, "Archivos FET (*.fet)")

                if file_path:
                    # Asegurarse de que la extensión sea .fet (si el usuario la cambia accidentalmente)
                    if not file_path.endswith(".fet"):
                        file_path += ".fet"
                    
                    # Guardar el archivo en la ruta seleccionada
                    exportarFET(file_path, institucion, diasSemanaClases, horasDiaClases, asignaturasElegidas, alumnos, actClases, aulasPorCampus, aulasPorTipo, clasesPorCuros, restriccionesClases["RestriccionesTiempo"], restriccionesClases["RestriccionesLugar"], "Clase")
                
                # Obtener el directorio base del archivo .fet
                base_dir = os.path.dirname(file_path)

                # Crear el directorio "Resultado" en el mismo directorio que el archivo .fet
                resultado_dir = os.path.join(base_dir, "Resultado")
                os.makedirs(resultado_dir, exist_ok=True)

                # Verificar si el archivo existe
                if os.path.isfile(file_path):
                    try:
                        # Construir el comando para ejecutar FET
                        command = [ruta_fet, f"--inputfile={file_path}", f"--outputdir={resultado_dir}"]
                        print("Ejecutando comando:", " ".join(command))  # Para depuración
                        
                        # Ejecutar FET con el archivo .fet
                        subprocess.run(command, check=True)
                        print(f"FET se ejecutó correctamente. Los resultados están en: {resultado_dir}")
                        dialogoError = DialogoError(f"FET se ejecutó correctamente. Los resultados están en: {resultado_dir}")
                        dialogoError.exec()
                    except subprocess.CalledProcessError as e:
                        print(f"Hubo un error al ejecutar FET: {e}")
                        dialogoError = DialogoError(f"Error: Hubo un error al ejecutar FET: {e}")
                        dialogoError.exec()
                    except Exception as e:
                        print(f"Otro error ocurrió: {e}")
                        dialogoError = DialogoError(f"Error: Otro error ocurrió: {e}")
                        dialogoError.exec()
                else:
                    print(f"El archivo {file_path} no existe.")
                    dialogoError = DialogoError(f"Error: El archivo {file_path} no existe.")
                    dialogoError.exec()
            else:
                self.fetConnect = FETConnectUI(f"Error: No se encontró {ruta_fet}. Indique la ruta de fet-cl.exe:")
                self.fetConnect.show()
        else:
            self.fetConnect = FETConnectUI(f"Error: La carpeta {ruta_carpeta} no existe. Indique la ruta de fet-cl.exe:")
            self.fetConnect.show()

    def mostrarAulaCombinadaUI(self):
        self.aulaCombinadaUI = AulaCombinadaUI("Clase")
        self.aulaCombinadaUI.show()

    def mostrarOtrosHorariosUI(self):
        self.semanal.setChecked(False)
        self.otrosHorariosUI = OtrosHorariosUI()
        self.otrosHorariosUI.show()
    
    def mostrarRestriccionesUI(self):
        self.restriccionesUI = RestriccionesClases()
        self.restriccionesUI.show()
    
    def mostrarModificarClasesUI(self):
        self.modificarClaseUI = ModificarClase()
        self.modificarClaseUI.show()

# Horarios
class HorariosUI(QWidget, Ui_crearHorario):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.examenes.clicked.connect(self.mostrarExamenesUI)
        self.clases.clicked.connect(self.mostrarClasesUI)

    def mostrarExamenesUI(self):
        global tipoHorario
        tipoHorario = "Examen"
        self.examenesUI = ExamenesUI()
        self.examenesUI.show()

    def mostrarClasesUI(self):
        global tipoHorario
        tipoHorario = "Clase"
        self.clasesUI = ClasesUI()
        self.clasesUI.show()

    def error(self):
        self.dialogoError = DialogoError("Error: El tipo de horario importado no coincide con el tipo de horaio seleccionado")
        self.dialogoError.exec()

# Main Window
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Datos institución
        self.institucion.clicked.connect(self.mostrarModificarInstitucionUI)

        self.campus.clicked.connect(self.mostrarModificarCampusUI)
        self.edificio.clicked.connect(self.mostrarModificarEdificioUI)
        self.aula.clicked.connect(self.mostrarModificarAulaUI)

        self.titulacion.clicked.connect(self.mostrarModificarTitulacionUI)
        self.asignatura.clicked.connect(self.mostrarModificarAsignaturaUI)

        # Exportar/Importar
        self.importar.clicked.connect(self.mostrarImportUI)
        self.exportar.clicked.connect(self.exportarFunction)

        # Crear Horario
        self.crearHorario.clicked.connect(self.mostrarCrearHorarioUI)

    def mostrarCrearHorarioUI(self):
        self.horariosUI = HorariosUI()
        self.horariosUI.show()
        
    def exportarFunction(self):
        # Nombre y extensión predeterminada del archivo
        default_filename = "archivo_guardado.xml"

        #  Abrir un diálogo para seleccionar la ubicación y nombre del archivo a guardar
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo XML", default_filename, "Archivos XML (*.xml)")

        if file_path:
            # Asegurarse de que la extensión sea .xml (si el usuario la cambia accidentalmente)
            if not file_path.endswith(".xml"):
                file_path += ".xml"
            
            # Guardar el archivo en la ruta seleccionada
            exportar(file_path, institucion, alumnos, diasSemanaClases, diasSemanaExamenes, horasDiaClases, horasDiaExamenes, asignaturasElegidas, actClases, actExamenes, restriccionesClases, restriccionesExamenes)

    def mostrarImportUI(self):
        self.importUI = ImportarUI()
        self.importUI.show()

    def mostrarModificarInstitucionUI(self):
        self.modificarInstitucionUI = ModificarInstitucion()
        self.modificarInstitucionUI.show()

    def mostrarModificarCampusUI(self):
        self.modificarUI = ModificarName()
        self.modificarUI.show()

    def mostrarModificarEdificioUI(self):
        self.modificarEdificioUI = ModificarEdificio()
        self.modificarEdificioUI.show()

    def mostrarModificarAulaUI(self):
        self.modificarAulaUI = ModificarAula()
        self.modificarAulaUI.show()

    def mostrarModificarTitulacionUI(self):
        self.modificarTitulacionUI = ModificarTitulacion()
        self.modificarTitulacionUI.show()
    
    def mostrarModificarAsignaturaUI(self):
        self.modificarAsignaturaUI = ModificarAsignatura()
        self.modificarAsignaturaUI.show()

if __name__ == '__main__':
    # Ruta FET
    ruta_fet = "./fet-6.18.1/fet-cl.exe"

    # Variables auxiliares
    totalAulasCombinadas = 0

    # Datos Aplicación
    tipoHorario = ""                                                                                      # Tipo de horaio que se va ha realizar
    institucion = Universidad("URJC")                                                                     # ED Universidad
    alumnos = []                                                                                          # Titulaciones-Cursos-Asignaturas
    asignaturasElegidas = []                                                                              # Asignaturas que se han usado para las Actividades
    aulasPorCampus = {}                                                                                   # Aulas separadas por campus
    aulasPorTipo = {"TODAS": [], "AULA": [], "AULA MAGNA": [], "SEMINARIO": [], "LABORATORIO": []}        # Aulas separadas por Tipo de aula
        # Dias y horas
    diasSemanaClases = Dias()                 
    horasDiaClases = Horas()  
    diasSemanaExamenes = Dias()                 
    horasDiaExamenes = Horas()   
                
        # Actividades             
    actClases = []
    actExamenes = []
        # Actividades separados por Curso
    examenesPorCuros = {}           
    clasesPorCuros = {}             

        # Restricciones
    restriccionesClases = {"RestriccionesTiempo": [], "RestriccionesLugar": []}
    restriccionesExamenes = {"RestriccionesTiempo": [], "RestriccionesLugar": []}

    # Asignaturas de las que no se pueden hacer examenes
    listaNegraAsignaturas = ["DOBLE GRADO EN ECONOMIA Y MATEMATICAS (MOSTOLES)", "DOBLE GRADO EN EDUCACION PRIMARIA Y MATEMATICAS (MOSTOLES)"]

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())