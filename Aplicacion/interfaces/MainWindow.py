# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowKEcSOM.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(494, 334)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.importExport = QGroupBox(self.centralwidget)
        self.importExport.setObjectName(u"importExport")
        self.importExport.setGeometry(QRect(70, 210, 361, 61))
        self.gridLayout_5 = QGridLayout(self.importExport)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.importar = QPushButton(self.importExport)
        self.importar.setObjectName(u"importar")

        self.gridLayout_5.addWidget(self.importar, 0, 0, 1, 1)

        self.exportar = QPushButton(self.importExport)
        self.exportar.setObjectName(u"exportar")

        self.gridLayout_5.addWidget(self.exportar, 0, 1, 1, 1)

        self.addModify = QGroupBox(self.centralwidget)
        self.addModify.setObjectName(u"addModify")
        self.addModify.setGeometry(QRect(72, 45, 356, 151))
        self.gridLayout_3 = QGridLayout(self.addModify)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.campus = QPushButton(self.addModify)
        self.campus.setObjectName(u"campus")

        self.gridLayout_3.addWidget(self.campus, 0, 1, 1, 1)

        self.institucion = QPushButton(self.addModify)
        self.institucion.setObjectName(u"institucion")

        self.gridLayout_3.addWidget(self.institucion, 0, 0, 1, 1)

        self.edificio = QPushButton(self.addModify)
        self.edificio.setObjectName(u"edificio")

        self.gridLayout_3.addWidget(self.edificio, 1, 1, 1, 1)

        self.aula = QPushButton(self.addModify)
        self.aula.setObjectName(u"aula")

        self.gridLayout_3.addWidget(self.aula, 2, 1, 1, 1)

        self.titulacion = QPushButton(self.addModify)
        self.titulacion.setObjectName(u"titulacion")

        self.gridLayout_3.addWidget(self.titulacion, 0, 2, 1, 1)

        self.asignatura = QPushButton(self.addModify)
        self.asignatura.setObjectName(u"asignatura")

        self.gridLayout_3.addWidget(self.asignatura, 1, 2, 1, 1)

        self.crearHorario = QPushButton(self.centralwidget)
        self.crearHorario.setObjectName(u"crearHorario")
        self.crearHorario.setGeometry(QRect(190, 280, 121, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.importExport.setTitle(QCoreApplication.translate("MainWindow", u"Importar/Exportar", None))
        self.importar.setText(QCoreApplication.translate("MainWindow", u"Importar Datos", None))
        self.exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar Datos", None))
        self.addModify.setTitle(QCoreApplication.translate("MainWindow", u"Instituci\u00f3n", None))
        self.campus.setText(QCoreApplication.translate("MainWindow", u"Campus", None))
        self.institucion.setText(QCoreApplication.translate("MainWindow", u"Instituci\u00f3n", None))
        self.edificio.setText(QCoreApplication.translate("MainWindow", u"Edificio", None))
        self.aula.setText(QCoreApplication.translate("MainWindow", u"Aula", None))
        self.titulacion.setText(QCoreApplication.translate("MainWindow", u"Titulacion", None))
        self.asignatura.setText(QCoreApplication.translate("MainWindow", u"Asignatura", None))
        self.crearHorario.setText(QCoreApplication.translate("MainWindow", u"Crear Horario", None))
    # retranslateUi

