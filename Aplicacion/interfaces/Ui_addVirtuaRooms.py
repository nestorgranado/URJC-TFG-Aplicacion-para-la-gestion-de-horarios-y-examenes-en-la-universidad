# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addVirtuaRoomsdoGsNn.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_CrearAulaCombinada(object):
    def setupUi(self, CrearAulaCombinada):
        if not CrearAulaCombinada.objectName():
            CrearAulaCombinada.setObjectName(u"CrearAulaCombinada")
        CrearAulaCombinada.resize(484, 424)
        self.Title = QLabel(CrearAulaCombinada)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(40, 40, 421, 51))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.campus = QLabel(CrearAulaCombinada)
        self.campus.setObjectName(u"campus")
        self.campus.setGeometry(QRect(50, 140, 51, 16))
        self.campusText = QComboBox(CrearAulaCombinada)
        self.campusText.setObjectName(u"campusText")
        self.campusText.setGeometry(QRect(120, 140, 201, 22))
        self.edificio = QLabel(CrearAulaCombinada)
        self.edificio.setObjectName(u"edificio")
        self.edificio.setGeometry(QRect(50, 180, 49, 16))
        self.edificioText = QComboBox(CrearAulaCombinada)
        self.edificioText.setObjectName(u"edificioText")
        self.edificioText.setGeometry(QRect(120, 180, 201, 22))
        self.cantidad = QLabel(CrearAulaCombinada)
        self.cantidad.setObjectName(u"cantidad")
        self.cantidad.setGeometry(QRect(50, 280, 171, 16))
        self.cantidadText = QSpinBox(CrearAulaCombinada)
        self.cantidadText.setObjectName(u"cantidadText")
        self.cantidadText.setGeometry(QRect(230, 280, 101, 23))
        self.capacidad = QLabel(CrearAulaCombinada)
        self.capacidad.setObjectName(u"capacidad")
        self.capacidad.setGeometry(QRect(50, 310, 101, 16))
        self.capacidadText = QSpinBox(CrearAulaCombinada)
        self.capacidadText.setObjectName(u"capacidadText")
        self.capacidadText.setGeometry(QRect(230, 310, 101, 23))
        self.add = QPushButton(CrearAulaCombinada)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(50, 360, 75, 24))
        self.tipoAula = QLabel(CrearAulaCombinada)
        self.tipoAula.setObjectName(u"tipoAula")
        self.tipoAula.setGeometry(QRect(50, 220, 61, 16))
        self.tipoAulaText = QComboBox(CrearAulaCombinada)
        self.tipoAulaText.setObjectName(u"tipoAulaText")
        self.tipoAulaText.setGeometry(QRect(120, 220, 201, 22))

        self.retranslateUi(CrearAulaCombinada)

        QMetaObject.connectSlotsByName(CrearAulaCombinada)
    # setupUi

    def retranslateUi(self, CrearAulaCombinada):
        CrearAulaCombinada.setWindowTitle(QCoreApplication.translate("CrearAulaCombinada", u"crearAulasCombinadas", None))
        self.Title.setText(QCoreApplication.translate("CrearAulaCombinada", u"Crear Aulas Combinadas", None))
        self.campus.setText(QCoreApplication.translate("CrearAulaCombinada", u"Campus", None))
        self.edificio.setText(QCoreApplication.translate("CrearAulaCombinada", u"Edificio", None))
        self.cantidad.setText(QCoreApplication.translate("CrearAulaCombinada", u"Cantidad de Aulas Combinadas", None))
        self.capacidad.setText(QCoreApplication.translate("CrearAulaCombinada", u"Capacidad Minima", None))
        self.add.setText(QCoreApplication.translate("CrearAulaCombinada", u"Crear", None))
        self.tipoAula.setText(QCoreApplication.translate("CrearAulaCombinada", u"Tipo Aula", None))
    # retranslateUi

