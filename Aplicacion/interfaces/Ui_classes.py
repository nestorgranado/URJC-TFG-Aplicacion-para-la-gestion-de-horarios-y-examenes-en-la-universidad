# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classesJAgSLi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Clases(object):
    def setupUi(self, Clases):
        if not Clases.objectName():
            Clases.setObjectName(u"Clases")
        Clases.resize(349, 432)
        self.Title = QLabel(Clases)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(50, 10, 181, 50))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.Datos = QGroupBox(Clases)
        self.Datos.setObjectName(u"Datos")
        self.Datos.setGeometry(QRect(80, 70, 191, 261))
        self.layoutWidget = QWidget(self.Datos)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 161, 221))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.modificar = QPushButton(self.layoutWidget)
        self.modificar.setObjectName(u"modificar")

        self.verticalLayout_2.addWidget(self.modificar)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(13, 12, 131, 101))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tipo = QLabel(self.layoutWidget1)
        self.tipo.setObjectName(u"tipo")

        self.verticalLayout.addWidget(self.tipo)

        self.semanal = QRadioButton(self.layoutWidget1)
        self.semanal.setObjectName(u"semanal")

        self.verticalLayout.addWidget(self.semanal)

        self.otros = QPushButton(self.layoutWidget1)
        self.otros.setObjectName(u"otros")

        self.verticalLayout.addWidget(self.otros)


        self.verticalLayout_2.addWidget(self.frame)

        self.aulasCombinadas = QPushButton(self.layoutWidget)
        self.aulasCombinadas.setObjectName(u"aulasCombinadas")

        self.verticalLayout_2.addWidget(self.aulasCombinadas)

        self.exportar = QPushButton(self.layoutWidget)
        self.exportar.setObjectName(u"exportar")

        self.verticalLayout_2.addWidget(self.exportar)

        self.layoutWidget2 = QWidget(Clases)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 350, 301, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.restricciones = QPushButton(self.layoutWidget2)
        self.restricciones.setObjectName(u"restricciones")

        self.horizontalLayout_3.addWidget(self.restricciones)

        self.crearHorario = QPushButton(self.layoutWidget2)
        self.crearHorario.setObjectName(u"crearHorario")

        self.horizontalLayout_3.addWidget(self.crearHorario)


        self.retranslateUi(Clases)

        QMetaObject.connectSlotsByName(Clases)
    # setupUi

    def retranslateUi(self, Clases):
        Clases.setWindowTitle(QCoreApplication.translate("Clases", u"horarioClas", None))
        self.Title.setText(QCoreApplication.translate("Clases", u"Clases", None))
        self.Datos.setTitle(QCoreApplication.translate("Clases", u"Datos", None))
        self.modificar.setText(QCoreApplication.translate("Clases", u"Modificar Clases", None))
        self.tipo.setText(QCoreApplication.translate("Clases", u"Tipo Hoario", None))
        self.semanal.setText(QCoreApplication.translate("Clases", u"Semanal", None))
        self.otros.setText(QCoreApplication.translate("Clases", u"Otros", None))
        self.aulasCombinadas.setText(QCoreApplication.translate("Clases", u"Aulas Combinadas", None))
        self.exportar.setText(QCoreApplication.translate("Clases", u"Exportar Datos", None))
        self.restricciones.setText(QCoreApplication.translate("Clases", u"Ver Restricciones", None))
        self.crearHorario.setText(QCoreApplication.translate("Clases", u"Crear Horario", None))
    # retranslateUi

