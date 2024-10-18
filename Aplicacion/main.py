import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PySide6.QtCore import Qt

from interfaces.MainWindow import Ui_MainWindow
from interfaces.Ui_import import Ui_importar

from estructuraDatos import *
from importar import *

class ImportarUI(QWidget, Ui_importar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.importarBtn.clicked.connect(self.guardar)
        self.examinarBtn.clicked.connect(self.seleccionarArchivo)

    def guardar(self):
        if self.rutaText.text().strip():
            escuela = importar_datos(self.rutaText.text())
            
            institucion.agregar_escuela(escuela)

            escuela.mostrarEscuela() # Borrar esta linea despues
            self.close()
        else:
            print("no se ha selecionado ningun archivo") #Cambiar el error por un mensaje de la interfaz

    def seleccionarArchivo(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            None, 
            "Seleccionar archivo", 
            "", 
            "Archivos Excel (*.xlsx *.xls);;Archivos CSV (*.csv)"
        )

        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe.") #Cambiar el error por un mensaje de la interfaz
        else:
            self.rutaText.setText(ruta_archivo)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.importar.clicked.connect(self.mostrarImportUI)

    def mostrarImportUI(self):
        self.importUI = ImportarUI()
        self.importUI.show()

if __name__ == '__main__':
    institucion = Universidad("URJC")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())