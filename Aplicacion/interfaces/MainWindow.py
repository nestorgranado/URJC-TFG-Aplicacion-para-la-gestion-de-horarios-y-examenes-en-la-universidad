# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowIiyGfm.ui'
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
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 468)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(120, 100, 401, 261))
        self.datos = QWidget()
        self.datos.setObjectName(u"datos")
        self.addModify = QGroupBox(self.datos)
        self.addModify.setObjectName(u"addModify")
        self.addModify.setGeometry(QRect(20, 10, 356, 120))
        self.gridLayout_3 = QGridLayout(self.addModify)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.campus = QPushButton(self.addModify)
        self.campus.setObjectName(u"campus")

        self.gridLayout_3.addWidget(self.campus, 0, 1, 1, 1)

        self.escuela = QPushButton(self.addModify)
        self.escuela.setObjectName(u"escuela")

        self.gridLayout_3.addWidget(self.escuela, 0, 2, 1, 1)

        self.institucion = QPushButton(self.addModify)
        self.institucion.setObjectName(u"institucion")

        self.gridLayout_3.addWidget(self.institucion, 0, 0, 1, 1)

        self.asignatura = QPushButton(self.addModify)
        self.asignatura.setObjectName(u"asignatura")

        self.gridLayout_3.addWidget(self.asignatura, 2, 2, 1, 1)

        self.aula = QPushButton(self.addModify)
        self.aula.setObjectName(u"aula")

        self.gridLayout_3.addWidget(self.aula, 2, 1, 1, 1)

        self.titulacion = QPushButton(self.addModify)
        self.titulacion.setObjectName(u"titulacion")

        self.gridLayout_3.addWidget(self.titulacion, 1, 2, 1, 1)

        self.edificio = QPushButton(self.addModify)
        self.edificio.setObjectName(u"edificio")

        self.gridLayout_3.addWidget(self.edificio, 1, 1, 1, 1)

        self.importExport = QGroupBox(self.datos)
        self.importExport.setObjectName(u"importExport")
        self.importExport.setGeometry(QRect(20, 140, 361, 60))
        self.gridLayout_5 = QGridLayout(self.importExport)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.importar = QPushButton(self.importExport)
        self.importar.setObjectName(u"importar")

        self.gridLayout_5.addWidget(self.importar, 0, 0, 1, 1)

        self.exportar = QPushButton(self.importExport)
        self.exportar.setObjectName(u"exportar")

        self.gridLayout_5.addWidget(self.exportar, 0, 1, 1, 1)

        self.tabWidget.addTab(self.datos, "")
        self.restricciones = QWidget()
        self.restricciones.setObjectName(u"restricciones")
        self.tiempo = QGroupBox(self.restricciones)
        self.tiempo.setObjectName(u"tiempo")
        self.tiempo.setGeometry(QRect(20, 10, 356, 90))
        self.gridLayout = QGridLayout(self.tiempo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dias = QPushButton(self.tiempo)
        self.dias.setObjectName(u"dias")

        self.gridLayout.addWidget(self.dias, 0, 0, 1, 1)

        self.horas = QPushButton(self.tiempo)
        self.horas.setObjectName(u"horas")

        self.gridLayout.addWidget(self.horas, 0, 1, 1, 1)

        self.descansos = QPushButton(self.tiempo)
        self.descansos.setObjectName(u"descansos")

        self.gridLayout.addWidget(self.descansos, 0, 2, 1, 1)

        self.nuevaTiempo = QPushButton(self.tiempo)
        self.nuevaTiempo.setObjectName(u"nuevaTiempo")

        self.gridLayout.addWidget(self.nuevaTiempo, 1, 0, 1, 1)

        self.lugar = QGroupBox(self.restricciones)
        self.lugar.setObjectName(u"lugar")
        self.lugar.setGeometry(QRect(20, 110, 356, 90))
        self.gridLayout_2 = QGridLayout(self.lugar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.resEdififcio = QPushButton(self.lugar)
        self.resEdififcio.setObjectName(u"resEdififcio")

        self.gridLayout_2.addWidget(self.resEdififcio, 0, 0, 1, 1)

        self.resCampus = QPushButton(self.lugar)
        self.resCampus.setObjectName(u"resCampus")

        self.gridLayout_2.addWidget(self.resCampus, 0, 1, 1, 1)

        self.resAula = QPushButton(self.lugar)
        self.resAula.setObjectName(u"resAula")

        self.gridLayout_2.addWidget(self.resAula, 0, 2, 1, 1)

        self.nuevaLugar = QPushButton(self.lugar)
        self.nuevaLugar.setObjectName(u"nuevaLugar")

        self.gridLayout_2.addWidget(self.nuevaLugar, 1, 0, 1, 1)

        self.tabWidget.addTab(self.restricciones, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addModify.setTitle(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.campus.setText(QCoreApplication.translate("MainWindow", u"Campus", None))
        self.escuela.setText(QCoreApplication.translate("MainWindow", u"Escuela", None))
        self.institucion.setText(QCoreApplication.translate("MainWindow", u"Instituci\u00f3n", None))
        self.asignatura.setText(QCoreApplication.translate("MainWindow", u"Asignatura", None))
        self.aula.setText(QCoreApplication.translate("MainWindow", u"Aula", None))
        self.titulacion.setText(QCoreApplication.translate("MainWindow", u"Titulacion", None))
        self.edificio.setText(QCoreApplication.translate("MainWindow", u"Edificio", None))
        self.importExport.setTitle(QCoreApplication.translate("MainWindow", u"Importar/Exportar", None))
        self.importar.setText(QCoreApplication.translate("MainWindow", u"Importar Datos", None))
        self.exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar Datos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.datos), QCoreApplication.translate("MainWindow", u"Datos", None))
        self.tiempo.setTitle(QCoreApplication.translate("MainWindow", u"Restricicones de Tiempo", None))
        self.dias.setText(QCoreApplication.translate("MainWindow", u"D\u00edas", None))
        self.horas.setText(QCoreApplication.translate("MainWindow", u"Horas", None))
        self.descansos.setText(QCoreApplication.translate("MainWindow", u"Descansos", None))
        self.nuevaTiempo.setText(QCoreApplication.translate("MainWindow", u"Nueva Restricci\u00f3n", None))
        self.lugar.setTitle(QCoreApplication.translate("MainWindow", u"Restricciones de Lugar", None))
        self.resEdififcio.setText(QCoreApplication.translate("MainWindow", u"Edififcio", None))
        self.resCampus.setText(QCoreApplication.translate("MainWindow", u"Campus", None))
        self.resAula.setText(QCoreApplication.translate("MainWindow", u"Aula", None))
        self.nuevaLugar.setText(QCoreApplication.translate("MainWindow", u"Nueva Restricci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.restricciones), QCoreApplication.translate("MainWindow", u"Restricciones", None))
    # retranslateUi

