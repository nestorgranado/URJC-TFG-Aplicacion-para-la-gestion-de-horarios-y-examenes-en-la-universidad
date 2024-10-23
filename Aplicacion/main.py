import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from interfaces.MainWindow import Ui_MainWindow
from interfaces.Ui_import import Ui_importar

from estructuraDatos import *
from importar import *
from exportar import *

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

        self.importarBtn.clicked.connect(self.guardar) # Funcionalidad boton guardar
        self.examinarBtn.clicked.connect(self.seleccionarArchivo) # Funcionalidad boton selecionar archivo

    def guardar(self):
        # Comprobar si la rura existe
        if os.path.exists(self.rutaText.text()):
            # Obtener nombre del archivo y la extensión
            nombre_archivo_con_extension = os.path.basename(self.rutaText.text())
            nombre_archivo, extension = os.path.splitext(nombre_archivo_con_extension) 

            # Dividir funcionalida si el archivo es xml o no
            if extension in ['.xls', '.xlsx', '.csv']:
                # Depende del nombre del archivo se importaran las escuelas o los campus
                if nombre_archivo == 'uxxi':
                    escuela = importar_Escuelas(self.rutaText.text())
                    institucion.agregar_escuela(escuela)

                    self.close()
                elif nombre_archivo == 'mostoles2324.v1':
                    campusList = importar_Campus(self.rutaText.text())
                    institucion.setCampus(campusList)

                    self.close()
                else:
                    dialogoError = DialogoError(f"Error: el archivo '{self.rutaText.text()}' no contiene los datos necesarios para la aplicación")
                    dialogoError.exec()  
            elif extension == '.xml':
                campuses, escuelas = importarXML(self.rutaText.text())
                institucion.setCampus(campuses)
                institucion.setEscuelas(escuelas)

                self.close()
            else:
                dialogoError = DialogoError(f"Error: el formato '{extension}' no es soportado")
                dialogoError.exec()  
        else:
            dialogoError = DialogoError(f"Error: El archivo '{self.rutaText.text()}' no existe.")
            dialogoError.exec()

    def seleccionarArchivo(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            None, 
            "Seleccionar archivo", 
            "", 
            "Archivos Excel (*.xlsx *.xls);;Archivos CSV (*.csv);;Archivo XML (*.xml)"
        )

        self.rutaText.setText(ruta_archivo)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.importar.clicked.connect(self.mostrarImportUI)
        self.exportar.clicked.connect(self.exportarFunction)

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
            exportar(file_path, institucion)

    def mostrarImportUI(self):
        self.importUI = ImportarUI()
        self.importUI.show()

if __name__ == '__main__':
    institucion = Universidad("URJC")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())