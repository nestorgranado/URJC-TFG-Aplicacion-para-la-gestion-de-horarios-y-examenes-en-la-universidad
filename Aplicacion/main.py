# Librerías externas
import sys
import os
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QListWidget, QComboBox, QAbstractItemView
from PySide6.QtCore import Qt
from collections import defaultdict

# Imports de las interfaces
from interfaces.MainWindow import Ui_MainWindow
from interfaces.Ui_import import Ui_importar
from interfaces.Ui_addName import Ui_AddNombre
from interfaces.Ui_modifyName import Ui_ModificarName
from interfaces.Ui_modifyBuilding import Ui_ModificarEdificio
from interfaces.Ui_modifyAula import Ui_ModificarAula
from interfaces.Ui_modifyTitulation import Ui_ModificarTitulacion
from interfaces.Ui_modifyAsignatura import Ui_ModificarAsignatura
from interfaces.Ui_days import Ui_dias
from interfaces.Ui_hour import Ui_horas
from interfaces.Ui_newActivity import Ui_Actividades
from interfaces.Ui_schedule import Ui_Horario
from interfaces.Ui_addExam import Ui_Examenes
from interfaces.Ui_modifyExam import Ui_ModificarExamenes

# Funcionalidades
from estructuraDatos import *
from importar import importarInstitucion
from exportar import exportar
from exportarFET import exportarFET

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

# Interfaz para importar datos al sistema
class ImportarUI(QWidget, Ui_importar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.importarBtn.clicked.connect(self.guardar) # Funcionalidad botón guardar
        self.examinarBtn.clicked.connect(self.seleccionarArchivo) # Funcionalidad botón selecionar archivo

    def guardar(self):
        escuelas, campuses, error = importarInstitucion(self.rutaText.text()) # Importación de datos

        # Si no hay error comprobar que se ha importado y añadirlo a la Institución
        if error == "": 
            if not campuses:
                institucion.sumar_escuelas(escuelas)
            elif not escuelas:
                institucion.sumar_campus(campuses)   
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

# Clase para Modificar Datos de Escuelas y Campuses
class ModificarName(QWidget, Ui_ModificarName):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)

        self.Title.setText(name) # Titulo de la pantalla

        # Diferentes funcionalidades si se trata de una Escuela o un Campus
        if name == "Campus":
            self.nameList = institucion.getCampus() # Lista de campus

            # Rellenar el QListWidget con los nombres de los campus
            self.list.clear()
            for campus in self.nameList:
                self.list.addItem(campus.getNombre())

            self.save.clicked.connect(self.guardarCampus) # guardar
        elif name == "Escuela":
            self.nameList = institucion.getEscuelas() # Lista de escuelas

            # Rellenar el QListWidget con los nombres de las escuelas
            self.list.clear()
            for escuela in self.nameList:
                self.list.addItem(escuela.getNombre())

            self.save.clicked.connect(self.guardarEscuela) # guardar

        self.list.itemClicked.connect(self.updateLineEditText) # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.modify.clicked.connect(self.modificar_elemento) # Modificar valor del elemento seleccionado de la QListWidget
        self.add.clicked.connect(self.agregar_elemento) # Crear un nuevo elemento
        self.sup.clicked.connect(self.borrar_elemento) # Borrar elemento seleccionado
        
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
            
            # Actualizar el elemento visualmente en el QListWidget
            self.list.item(self.selected_index).setText(nuevo_texto)
    
    def agregar_elemento(self):
        # Obtener el texto del QLineEdit
        nuevo_texto = self.nombreText.text()
        
        # Agregar el nuevo texto a la lista de Campus
        nuevo_campus = Campus(nuevo_texto)
        self.nameList.append(nuevo_campus)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        self.list.addItem(nuevo_texto)

    def borrar_elemento(self):
        if self.selected_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento de la lista de Campus
            del self.nameList[self.selected_index]
            
            # Eliminar el elemento del QListWidget
            self.list.takeItem(self.selected_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.nombreText.clear()
            self.selected_index = None

    def guardarCampus(self):
        institucion.sumar_campus(self.nameList)
        self.close()

    def guardarEscuela(self):
        institucion.sumar_escuelas(self.nameList)
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

        self.escuelas = institucion.getEscuelas() # Obtenre la lista de escuelas de la institución

        self.escuelaBox.addItem("Seleccione una opción...") # Inicializar el selector de escuela

        # Rellenar el selector de escuelas con los nombres de las diferentes escuelas
        for escuela in self.escuelas:
            self.escuelaBox.addItem(escuela.getNombre())

        self.escuelaBox.currentIndexChanged.connect(self.actualizar_titulacion) # Si se seleciona una escuela obtener sus titulaciones
        self.list.itemClicked.connect(self.updateLineEditText) # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.modify.clicked.connect(self.modificar_elemento) # Modificar valor del elemento seleccionado de la QListWidget
        self.add.clicked.connect(self.agregar_elemento) # Crear un nuevo elemento
        self.sup.clicked.connect(self.borrar_elemento) # Borrar elemento seleccionado
        self.save.clicked.connect(self.guardar) # guardar
        
        self.titulaciones_index = None  # Variable para guardar el índice del elemento seleccionado

    def actualizar_titulacion(self):
        self.escuela_index = self.escuelaBox.currentIndex() - 1 # Guardar Indice de la escuela seleccionada
        self.titulaciones = self.escuelas[self.escuela_index].getTitulaciones() # Obtener las titulaciones de la escuela seleccionada

        # Rellenar el QListWidget con los nombres de las titulaciones
        self.list.clear()
        for titulacion in self.titulaciones:
            item = "(" + str(titulacion.getCodigo()) + ") " + str(titulacion.getNombre())
            self.list.addItem(item)

        # Limpiar Datos
        self.nombreText.clear()
        self.codigoText.clear()
        self.campusText.clear()

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

            # Actualizar campus
            self.escuelas[self.escuela_index].setTitulaciones(self.titulaciones)
    
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

        # Actualizar campus
        self.escuelas[self.escuela_index].setTitulaciones(self.titulaciones)

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

            # Actualizar campus
            self.escuelas[self.escuela_index].setTitulaciones(self.titulaciones)

    def guardar(self):
        institucion.setEscuelas(self.escuelas)
        self.close()

# Clase para Modificar Datos de las Aulas
class ModificarAula(QWidget, Ui_ModificarAula):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.campuses = institucion.getCampus() # Lista de campuses

        # Inicializar el selectorer
        self.campusBox.addItem("Seleccione una opción...")
        self.edificioBox.addItem("Seleccione una opción...")

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

    def modificar_elemento(self):
        if self.aula_index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_numero = self.numeroText.text()
            nuevo_capClase = self.capClaseText.value()
            nuevo_capExamen = self.capExamenText.value()
            nuevo_tipo = self.tipoText.text()
            
            # Actualizar el elemento en la lista de titulaciones
            self.aulas[self.aulas].setNumero(nuevo_numero)
            self.aulas[self.aulas].setCapacidadClase(nuevo_capClase)
            self.aulas[self.aulas].setCapacidadExamen(nuevo_capExamen)
            self.aulas[self.aulas].setTipo(nuevo_tipo)
         
            # Actualizar el elemento visualmente en el QListWidget
            self.list.item(self.aula_index).setText(nuevo_numero)

            # Actualizar datos
            self.edificios[self.edificio_index].setAulas(self.aulas)
            self.campuses[self.campus_index].setEdificios(self.edificios)
    
    def agregar_elemento(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_numero = self.numeroText.text()
        nuevo_capClase = self.capClaseText.value()
        nuevo_capExamen = self.capExamenText.value()
        nuevo_tipo = self.tipoText.text()
        
        # Agregar el nuevo texto a la lista de Campus
        nueva_aula = Aula(nuevo_numero, nuevo_capClase, nuevo_capExamen, nuevo_tipo)
        self.edificios[self.edificio_index].agregar_aula(nueva_aula)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        self.list.addItem(nuevo_numero)

        # Actualizar datos
        self.campuses[self.campus_index].setEdificios(self.edificios)

    def borrar_elemento(self):
        if self.aula_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento de la lista de Campus
            del self.aulas[self.aula_index]
            
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
        
# Clase para Modificar Datos de las Asignaturas
class ModificarAsignatura(QWidget, Ui_ModificarAsignatura):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.escuelas = institucion.getEscuelas() # Lista de escuelas

        # Inicializar el selectorer
        self.escuelaBox.addItem("Seleccione una opción...")
        self.titulacionBox.addItem("Seleccione una opción...")

        # Rellenar selector escuelas
        for escuela in self.escuelas:
            self.escuelaBox.addItem(escuela.getNombre())

        self.escuelaBox.currentIndexChanged.connect(self.actualizar_titulacion) # Si se seleciona una escuela obtener sus titulaciones
        self.titulacionBox.currentIndexChanged.connect(self.actualizar_asignatura) # Si se seleciona una titulación obtener sus asignaturas
        # Actualizar el lineEdit con el nombre del elemento selecionado del QListWidget
        self.list.itemClicked.connect(self.updateLineEditText) 
        self.listHijas.itemClicked.connect(self.updateLineEditHijas)

        # Botones
        self.modify.clicked.connect(self.modificar_elemento)
        self.add.clicked.connect(self.agregar_elemento)
        self.sup.clicked.connect(self.borrar_elemento)

        self.modifyHija.clicked.connect(self.modificar_hija)
        self.addHija.clicked.connect(self.agregar_hija)
        self.supHija.clicked.connect(self.borrar_hija)

        self.save.clicked.connect(self.guardar) # guardar
        
        self.asignatura_index = None  # Variable para guardar el índice del elemento seleccionado
        self.hija_index = None

    def actualizar_titulacion(self):
        self.escuela_index = self.escuelaBox.currentIndex() - 1 # Guardar Indice
        self.titulaciones = self.escuelas[self.escuela_index].getTitulaciones() # Obtener las titulaciones del elemento seleccionado

        # Rellenar el selector de titulaciones
        for titulacion in self.titulaciones:
            self.titulacionBox.addItem(titulacion.getNombre())

        # Limpiar Datos
        self.codigoText.clear()
        self.nombreText.clear()
        self.numAlumnosText.clear()
        self.profesorText.clear()
        self.cursoText.clear()
        self.codigoHijaText.clear()
        self.nombreHijaText.clear()

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
        self.profesorText.clear()
        self.cursoText.clear()
        self.codigoHijaText.clear()
        self.nombreHijaText.clear()

    def updateLineEditText(self, item):
        self.asignatura_index = self.list.row(item)  # Guardar índice del elemento seleccionado

        # Rellenar los datos del elemneto selecionado
        self.codigoText.setText(self.asignaturas[self.asignatura_index].getCodigo())
        self.nombreText.setText(self.asignaturas[self.asignatura_index].getNombre())
        self.numAlumnosText.setValue(int(self.asignaturas[self.asignatura_index].getNumAlumnos()))
        self.profesorText.setText(self.asignaturas[self.asignatura_index].getProfesor())
        self.cursoText.setText(str(self.asignaturas[self.asignatura_index].getCurso()))

        # Rellenar ListaHijas
        self.listHijas.clear()
        self.hijas = self.asignaturas[self.asignatura_index].getAsignaturas_hijas()
        for hija in self.hijas:
            item = "(" + str(hija[0]) + ") " + str(hija[1])
            self.listHijas.addItem(item)

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
            nuevo_numAlumnos = str(self.numAlumnosText.value())
            nuevo_profesor = self.profesorText.text()
            nuevo_curso = int(self.cursoText.text())
            
            # Actualizar el elemento
            self.asignaturas[self.asignatura_index].setCodigo(nuevo_codigo)
            self.asignaturas[self.asignatura_index].setNombre(nuevo_nombre)
            self.asignaturas[self.asignatura_index].setNumAlumnos(nuevo_numAlumnos)
            self.asignaturas[self.asignatura_index].setProfesor(nuevo_profesor)
            self.asignaturas[self.asignatura_index].setCurso(nuevo_curso)

         
            # Actualizar el elemento visualmente en el QListWidget
            nuevo_item = "(" + str(nuevo_codigo) + ") " + str(nuevo_nombre)
            self.list.item(self.asignatura_index).setText(nuevo_item)

            # Actualizar datos
            self.titulaciones[self.titulacion_index].setAsignaturas(self.asignaturas)
            self.escuelas[self.escuela_index].setTitulaciones(self.titulaciones)
    
    def agregar_elemento(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_codigo = self.codigoText.text()
        nuevo_nombre = self.nombreText.text()
        nuevo_numAlumnos = str(self.numAlumnosText.value())
        nuevo_profesor = self.profesorText.text()
        nuevo_curso = int(self.cursoText.text())
        
        # Agregar el nuevo texto a la lista de Campus
        nueva_asignatura = Asignatura(nuevo_codigo, nuevo_nombre, nuevo_numAlumnos, self.titulaciones[self.titulacion_index].getNombre(), nuevo_profesor, nuevo_curso)
        self.titulaciones[self.titulacion_index].agregar_asignatura(nueva_asignatura)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        nuevo_item = "(" + str(nuevo_codigo) + ") " + str(nuevo_nombre)
        self.list.addItem(nuevo_item)

        # Actualizar datos
        self.escuelas[self.escuela_index].setTitulaciones(self.titulaciones)

    def borrar_elemento(self):
        if self.asignatura_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento
            del self.asignaturas[self.asignatura_index]
            
            # Eliminar el elemento del QListWidget
            self.list.takeItem(self.asignatura_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.codigoText.clear()
            self.nombreText.clear()
            self.numAlumnosText.clear()
            self.profesorText.clear()
            self.cursoText.clear()
            self.codigoHijaText.clear()
            self.nombreHijaText.clear()
            self.asignatura_index = None

            # Actualizar datos
            self.titulaciones[self.titulacion_index].setAsignaturas(self.asignaturas)
            self.escuelas[self.escuela_index].setTitulaciones(self.titulaciones)

    def modificar_hija(self):
        if self.hija_index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_hija = (self.codigoHijaText.text(), self.nombreHijaText.text())
            
            # Actualizar el elemento
            self.hijas[self.hija_index].setAsignaturas_hijas(nuevo_hija)
         
            # Actualizar el elemento visualmente en el QListWidget
            nuevo_item = "(" + str(self.codigoHijaText.text()) + ") " + str(self.nombreHijaText.text())
            self.listHijas.item(self.hija_index).setText(nuevo_item)

            # Actualizar datos
            self.asignaturas[self.asignatura_index].setAsignaturas_hijas(self.hijas)

    def agregar_hija(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_hija = (self.codigoHijaText.text(), self.nombreHijaText.text())
        
        # Agregar el nuevo texto a la lista de Campus
        self.hijas[self.hija_index].agregar_hija(nuevo_hija)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        nuevo_item = "(" + str(self.codigoHijaText.text()) + ") " + str(self.nombreHijaText.text())
        self.listHijas.addItem(nuevo_item)

        # Actualizar datos
        self.asignaturas[self.asignatura_index].setAsignaturas_hijas(self.hijas)

    def borrar_hija(self):
        if self.hija_index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento
            del self.hijas[self.hija_index]
            
            # Eliminar el elemento del QListWidget
            self.listHijas.takeItem(self.hija_index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.codigoHijaText.clear()
            self.nombreHijaText.clear()
            self.hija_index = None

            # Actualizar datos
            self.asignaturas[self.asignatura_index].setAsignaturas_hijas(self.hijas)
    
    def guardar(self):
        institucion.setEscuelas(self.escuelas)
        self.close()

# Añadir Días por Semana
class DiasUI(QWidget, Ui_dias):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.numero = diasSemana.getNumDias()
        self.dias = diasSemana.getDias()

        self.numDiasText.setValue(self.numero)
        self.previousValue = self.numDiasText.value()
        self.listaDias.addItems(self.dias)

        # Hacer los elementos editables
        for index in range(self.listaDias.count()):
            item = self.listaDias.item(index)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            
        self.listaDias.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.numDiasText.valueChanged.connect(self.actualizarDias)
        self.listaDias.itemChanged.connect(self.actualizarDatos)
        self.save.clicked.connect(self.guardar)

    def actualizarDias(self, value):
        if value > self.previousValue:
            for i in range(self.previousValue, value):
                self.dias.append(f"Nuevo dia {i+1}")
        elif value < self.previousValue:
            for i in range(self.previousValue, value, -1):
                self.dias.pop()
            
        self.previousValue = value

        self.listaDias.clear()
        self.listaDias.addItems(self.dias)

        # Hacer los elementos editables
        for index in range(self.listaDias.count()):
            item = self.listaDias.item(index)
            item.setFlags(item.flags() | Qt.ItemIsEditable)

    def actualizarDatos(self):
        self.dias = [self.listaDias.item(i).text() for i in range(self.listaDias.count())]

    def guardar(self):
        diasSemana.setDias(self.dias)
        self.close()

# Añadir Horas por día
class HorasUI(QWidget, Ui_horas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.numero = horasDia.getNumHoras()
        self.horas = horasDia.getHoras()

        self.numHorasText.setValue(self.numero)
        self.previousValue = self.numHorasText.value()
        self.listaHoras.addItems(self.horas)

        # Hacer los elementos editables
        for index in range(self.listaHoras.count()):
            item = self.listaHoras.item(index)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            
        self.listaHoras.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.numHorasText.valueChanged.connect(self.actualizarHoras)
        self.listaHoras.itemChanged.connect(self.actualizarDatos)
        self.save.clicked.connect(self.guardar)

    def actualizarHoras(self, value):
        if value > self.previousValue:
            for i in range(self.previousValue, value):
                self.horas.append(f"Nueva hora {i+1}")
        elif value < self.previousValue:
            for i in range(self.previousValue, value, -1):
                self.horas.pop()
            
        self.previousValue = value

        self.listaHoras.clear()
        self.listaHoras.addItems(self.horas)

        # Hacer los elementos editables
        for index in range(self.listaHoras.count()):
            item = self.listaHoras.item(index)
            item.setFlags(item.flags() | Qt.ItemIsEditable)

    def actualizarDatos(self):
        self.horas = [self.listaHoras.item(i).text() for i in range(self.listaHoras.count())]

    def guardar(self):
        horasDia.setHoras(self.horas)
        self.close()

# Añadir actividades
class NuevoExamen(QWidget, Ui_Examenes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.escuelas = institucion.getEscuelas()

        self.listaTitulaciones = {}
        for escuela in self.escuelas:
            for titulaciones in escuela.getTitulaciones():
                self.listaTitulaciones[titulaciones.getNombre()] = titulaciones

        self.titulacionText.addItem("Seleccione una opción...")
        self.titulacionText.addItems(list(self.listaTitulaciones.keys()))

        self.save.clicked.connect(self.guardar)

    def guardar(self):
        tit = self.listaTitulaciones[self.titulacionText.currentText()]
        for asignatura in tit.getAsignaturas():
            nuevaActividad = Actividad(asignatura.getNombre(), asignatura.getProfesor(), asignatura.getCurso(), self.duarcionText.value())
            actividades.append(nuevaActividad)
            asignaturasElegidas.append(asignatura)
        self.close()

class ModificarExamen(QWidget, Ui_ModificarExamenes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actividades = list(actividades)
        for actividad in self.actividades:
            self.actividadesList.addItem(actividad.getAsignatura())

        self.actividadesList.itemClicked.connect(self.updateLineEditText)
        self.modificar.clicked.connect(self.modificar_elemento)
        self.add.clicked.connect(self.agregar_elemento)
        self.sup.clicked.connect(self.borrar_elemento)
        self.save.clicked.connect(self.guardar)

        self.index = None

    def updateLineEditText(self, item):
        self.index = self.actividadesList.row(item)  # Guardar índice del elemento seleccionado
        # Rellenar los datos del elemneto selecionado
        self.asignaturaText.setText(self.actividades[self.index].getAsignatura())
        self.profesorText.setText(self.actividades[self.index].getProfesor())
        self.alumnosText.setText(str(self.actividades[self.index].getCurso()))
        self.duracionText.setValue(self.actividades[self.index].getDuracion())

    def modificar_elemento(self):
        if self.index is not None:  # Verificar si hay un elemento seleccionado
            # Obtener el nuevo texto del QLineEdit
            nuevo_asignatura = self.asignaturaText.text()
            nuevo_profesor = self.profesorText.text()
            nuevo_alumnos = int(self.alumnosText.text())
            nuevo_duracion = self.duracionText.value()
            
            # Actualizar el elemento
            self.actividades[self.index].setAsignatura(nuevo_asignatura)
            self.actividades[self.index].setProfesor(nuevo_profesor)
            self.actividades[self.index].setCurso(nuevo_alumnos)
            self.actividades[self.index].setDuracion(nuevo_duracion)
         
            # Actualizar el elemento visualmente en el QListWidget
            self.actividadesList.item(self.index).setText(nuevo_asignatura)
    
    def agregar_elemento(self):
        # Obtener el nuevo texto del QLineEdit
        nuevo_asignatura = self.asignaturaText.text()
        nuevo_profesor = self.profesorText.text()
        nuevo_alumnos = self.alumnosText.text()
        nuevo_duracion = self.duracionText.value()
        
        # Agregar el nuevo texto a la lista de Campus
        nuevaActividad = Actividad(nuevo_asignatura, nuevo_profesor, nuevo_alumnos, nuevo_duracion)
        self.actividades[self.index].append(nuevaActividad)
        
        # Agregar el nuevo texto como un nuevo item en el QListWidget
        self.actividadesList.addItem(nuevo_asignatura)

    def borrar_elemento(self):
        if self.index is not None:  # Verificar si hay un elemento seleccionado
            # Eliminar el elemento
            del self.actividades[self.index]
            
            # Eliminar el elemento del QListWidget
            self.actividadesList.takeItem(self.index)
            
            # Limpiar el QLineEdit y reiniciar el índice seleccionado
            self.asignaturaText.clear()
            self.profesorText.clear()
            self.alumnosText.clear()
            self.duracionText.clear()
            self.index = None

    def guardar(self):
        actividades = list(self.actividades)
        self.close()        

class ExamenesUI(QWidget, Ui_Horario):
    def __init__(self, titulo):
        super().__init__()
        self.setupUi(self)

        self.Title.setText(titulo)
        self.tipo = titulo

        if titulo == "Nuevo Examen":
            self.add.clicked.connect(self.mostrarNuevoExamenUI)
            self.modificar.clicked.connect(self.mostrarModificarExamenUI)

        self.crearHorario.clicked.connect(self.nuevoHorario)
        self.exportar.clicked.connect(self.exportarXML)

    def nuevoHorario(self):
        # Nombre y extensión predeterminada del archivo
        default_filename = "archivo_guardado.fet"

        #  Abrir un diálogo para seleccionar la ubicación y nombre del archivo a guardar
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo FET", default_filename, "Archivos FET (*.fet)")

        if file_path:
            # Asegurarse de que la extensión sea .fet (si el usuario la cambia accidentalmente)
            if not file_path.endswith(".fet"):
                file_path += ".fet"
            
            # Guardar el archivo en la ruta seleccionada
            if self.tipo == "Nuevo Examen":
                exportarFET(file_path, institucion, diasSemana, horasDia, asignaturasElegidas, curso, actividades, "Examen")
            else:
                exportarFET(file_path, institucion, diasSemana, horasDia, asignaturasElegidas, curso, actividades, "Clase")

        ruta_fet = "C:/Users/nesto/Desktop/TFG/FET/fet-6.18.1/fet.exe"

        # Verificar si el archivo existe
        if os.path.isfile(file_path):
            try:
                # Ejecutar FET con el archivo .fet
                subprocess.run([ruta_fet, file_path], check=True)
                print("FET se ejecutó correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"Hubo un error al ejecutar FET: {e}")
        else:
            print(f"El archivo {file_path} no existe.")

    def exportarXML(self):
        # Nombre y extensión predeterminada del archivo
        default_filename = "archivo_guardado.xml"

        #  Abrir un diálogo para seleccionar la ubicación y nombre del archivo a guardar
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo XML", default_filename, "Archivos XML (*.xml)")

        if file_path:
            # Asegurarse de que la extensión sea .xml (si el usuario la cambia accidentalmente)
            if not file_path.endswith(".xml"):
                file_path += ".xml"
            
            # Guardar el archivo en la ruta seleccionada
            exportar(file_path, institucion, curso, diasSemana, horasDia, actividades)
    
    def mostrarNuevoExamenUI(self):
        self.nuevoExamenUI = NuevoExamen()
        self.nuevoExamenUI.show()

    def mostrarModificarExamenUI(self):
        self.modificarExamenUI = ModificarExamen()
        self.modificarExamenUI.show()

class ActividadesUI(QWidget, Ui_Actividades):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.examenes.clicked.connect(self.mostrarExamenesUI)

    def mostrarExamenesUI(self):
        self.examenesUI = ExamenesUI("Nuevo Examen")
        self.examenesUI.show()

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

        self.escuela.clicked.connect(self.mostrarModificarEscuelaUI)
        self.titulacion.clicked.connect(self.mostrarModificarTitulacionUI)
        self.asignatura.clicked.connect(self.mostrarModificarAsignaturaUI)

        # Dias/Horas/Descansos
        self.dias.clicked.connect(self.mostrarDiasUI)
        self.horas.clicked.connect(self.mostrarHorasUI)

        # Exportar/Importar
        self.importar.clicked.connect(self.mostrarImportUI)
        self.exportar.clicked.connect(self.exportarFunction)

        # Crear Horario
        self.crearHorario.clicked.connect(self.mostrarActividadesUI)

    def crearCurso(self):
        # Variables
        alumnosTotales = 0
        grupos_dict = {}

        # Obtener escuelas
        escuelas = institucion.getEscuelas()

        for escuela in escuelas:
            for titulacion in escuela.getTitulaciones():
                for asignatura in titulacion.getAsignaturas():
                    numero_grupo = asignatura.getCurso()
                    grupos_dict.setdefault(numero_grupo, Grupo(numero_grupo))
                    grupos_dict[numero_grupo].sumarAlumnos(asignatura.getNumAlumnos())
        
        curso.setGrupos(list(grupos_dict.values()))
        curso.calcularAulumnos()

    def mostrarActividadesUI(self):
        self.crearCurso()
        self.actividadesUI = ActividadesUI()
        self.actividadesUI.show()

    def mostrarDiasUI(self):
        self.diasUI = DiasUI()
        self.diasUI.show()

    def mostrarHorasUI(self):
        self.horasUI = HorasUI()
        self.horasUI.show()
        
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
            exportar(file_path, institucion, curso, diasSemana, horasDia, actividades)

    def mostrarImportUI(self):
        self.importUI = ImportarUI()
        self.importUI.show()

    def mostrarModificarInstitucionUI(self):
        self.modificarInstitucionUI = ModificarInstitucion()
        self.modificarInstitucionUI.show()

    def mostrarModificarCampusUI(self):
        self.modificarUI = ModificarName("Campus")
        self.modificarUI.show()

    def mostrarModificarEdificioUI(self):
        self.modificarEdificioUI = ModificarEdificio()
        self.modificarEdificioUI.show()

    def mostrarModificarAulaUI(self):
        self.modificarAulaUI = ModificarAula()
        self.modificarAulaUI.show()

    def mostrarModificarEscuelaUI(self):
        self.modificarUI = ModificarName("Escuela")
        self.modificarUI.show()

    def mostrarModificarTitulacionUI(self):
        self.modificarTitulacionUI = ModificarTitulacion()
        self.modificarTitulacionUI.show()
    
    def mostrarModificarAsignaturaUI(self):
        self.modificarAsignaturaUI = ModificarAsignatura()
        self.modificarAsignaturaUI.show()

if __name__ == '__main__':
    institucion = Universidad("URJC")
    curso = Curso()
    diasSemana = Dias()
    horasDia = Horas()
    actividades = []
    asignaturasElegidas = []

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())