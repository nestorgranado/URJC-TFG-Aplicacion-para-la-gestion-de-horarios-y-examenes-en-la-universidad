# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'examsCIPjPc.ui'
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
        Examenes.resize(391, 458)
        self.Title = QLabel(Examenes)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(50, 10, 181, 50))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.Datos = QGroupBox(Examenes)
        self.Datos.setObjectName(u"Datos")
        self.Datos.setGeometry(QRect(90, 80, 221, 321))
        self.layoutWidget = QWidget(self.Datos)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 30, 201, 271))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.modificar = QPushButton(self.layoutWidget)
        self.modificar.setObjectName(u"modificar")

        self.verticalLayout_2.addWidget(self.modificar)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.periodoExamenesText = QSpinBox(self.layoutWidget)
        self.periodoExamenesText.setObjectName(u"periodoExamenesText")

        self.horizontalLayout.addWidget(self.periodoExamenesText)

        self.dias = QLabel(self.layoutWidget)
        self.dias.setObjectName(u"dias")

        self.horizontalLayout.addWidget(self.dias)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.aulasCombinadas = QPushButton(self.layoutWidget)
        self.aulasCombinadas.setObjectName(u"aulasCombinadas")

        self.verticalLayout_2.addWidget(self.aulasCombinadas)

        self.exportar = QPushButton(self.layoutWidget)
        self.exportar.setObjectName(u"exportar")

        self.verticalLayout_2.addWidget(self.exportar)

        self.layoutWidget1 = QWidget(Examenes)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 410, 301, 26))
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
        self.Title.setText(QCoreApplication.translate("Examenes", u"Ex\u00e1menes", None))
        self.Datos.setTitle(QCoreApplication.translate("Examenes", u"Datos", None))
        self.modificar.setText(QCoreApplication.translate("Examenes", u"Modificar Ex\u00e1menes", None))
        self.label.setText(QCoreApplication.translate("Examenes", u"Periodo de ex\u00e1menes", None))
        self.dias.setText(QCoreApplication.translate("Examenes", u"D\u00edas", None))
        self.aulasCombinadas.setText(QCoreApplication.translate("Examenes", u"Aulas Combinadas", None))
        self.exportar.setText(QCoreApplication.translate("Examenes", u"Exportar Datos", None))
        self.restricciones.setText(QCoreApplication.translate("Examenes", u"Ver Restricciones", None))
        self.crearHorario.setText(QCoreApplication.translate("Examenes", u"Crear Horario", None))
    # retranslateUi

