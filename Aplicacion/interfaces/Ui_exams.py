# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'examshHNovS.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Examenes(object):
    def setupUi(self, Examenes):
        if not Examenes.objectName():
            Examenes.setObjectName(u"Examenes")
        Examenes.resize(575, 442)
        self.Title = QLabel(Examenes)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(50, 10, 181, 50))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.Datos = QGroupBox(Examenes)
        self.Datos.setObjectName(u"Datos")
        self.Datos.setGeometry(QRect(50, 90, 471, 271))
        self.Titulaciones = QGroupBox(self.Datos)
        self.Titulaciones.setObjectName(u"Titulaciones")
        self.Titulaciones.setGeometry(QRect(20, 20, 427, 79))
        self.horizontalLayout_2 = QHBoxLayout(self.Titulaciones)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add = QPushButton(self.Titulaciones)
        self.add.setObjectName(u"add")

        self.horizontalLayout_2.addWidget(self.add)

        self.modificar = QPushButton(self.Titulaciones)
        self.modificar.setObjectName(u"modificar")

        self.horizontalLayout_2.addWidget(self.modificar)

        self.layoutWidget = QWidget(self.Datos)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 110, 249, 49))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.periodoExamenesText = QSpinBox(self.layoutWidget)
        self.periodoExamenesText.setObjectName(u"periodoExamenesText")

        self.horizontalLayout.addWidget(self.periodoExamenesText)

        self.semanas = QLabel(self.layoutWidget)
        self.semanas.setObjectName(u"semanas")

        self.horizontalLayout.addWidget(self.semanas)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.exportar = QPushButton(self.Datos)
        self.exportar.setObjectName(u"exportar")
        self.exportar.setGeometry(QRect(20, 220, 202, 24))
        self.aulasCombinadas = QPushButton(self.Datos)
        self.aulasCombinadas.setObjectName(u"aulasCombinadas")
        self.aulasCombinadas.setGeometry(QRect(20, 180, 201, 24))
        self.layoutWidget1 = QWidget(Examenes)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(130, 380, 301, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.restricciones = QPushButton(self.layoutWidget1)
        self.restricciones.setObjectName(u"restricciones")

        self.horizontalLayout_3.addWidget(self.restricciones)

        self.crearHorario = QPushButton(self.layoutWidget1)
        self.crearHorario.setObjectName(u"crearHorario")

        self.horizontalLayout_3.addWidget(self.crearHorario)


        self.retranslateUi(Examenes)

        QMetaObject.connectSlotsByName(Examenes)
    # setupUi

    def retranslateUi(self, Examenes):
        Examenes.setWindowTitle(QCoreApplication.translate("Examenes", u"horarioEx", None))
        self.Title.setText(QCoreApplication.translate("Examenes", u"Examenes", None))
        self.Datos.setTitle(QCoreApplication.translate("Examenes", u"Datos", None))
        self.Titulaciones.setTitle(QCoreApplication.translate("Examenes", u"Titulaciones", None))
        self.add.setText(QCoreApplication.translate("Examenes", u"A\u00f1adir", None))
        self.modificar.setText(QCoreApplication.translate("Examenes", u"Modificar", None))
        self.label.setText(QCoreApplication.translate("Examenes", u"Periodo de examenes", None))
        self.semanas.setText(QCoreApplication.translate("Examenes", u"Semanas", None))
        self.exportar.setText(QCoreApplication.translate("Examenes", u"Exportar Datos", None))
        self.aulasCombinadas.setText(QCoreApplication.translate("Examenes", u"Aulas Combinadas", None))
        self.restricciones.setText(QCoreApplication.translate("Examenes", u"Ver Restricciones", None))
        self.crearHorario.setText(QCoreApplication.translate("Examenes", u"Crear Horario", None))
    # retranslateUi

