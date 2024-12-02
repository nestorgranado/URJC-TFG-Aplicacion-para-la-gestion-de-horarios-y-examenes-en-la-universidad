# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newSchedulebioiZQ.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_crearHorario(object):
    def setupUi(self, crearHorario):
        if not crearHorario.objectName():
            crearHorario.setObjectName(u"crearHorario")
        crearHorario.resize(285, 128)
        self.verticalLayout = QVBoxLayout(crearHorario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(crearHorario)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)

        self.verticalLayout.addWidget(self.Title)

        self.clases = QPushButton(crearHorario)
        self.clases.setObjectName(u"clases")

        self.verticalLayout.addWidget(self.clases)

        self.examenes = QPushButton(crearHorario)
        self.examenes.setObjectName(u"examenes")

        self.verticalLayout.addWidget(self.examenes)


        self.retranslateUi(crearHorario)

        QMetaObject.connectSlotsByName(crearHorario)
    # setupUi

    def retranslateUi(self, crearHorario):
        crearHorario.setWindowTitle(QCoreApplication.translate("crearHorario", u"CrearHorario", None))
        self.Title.setText(QCoreApplication.translate("crearHorario", u"Crear Horarios", None))
        self.clases.setText(QCoreApplication.translate("crearHorario", u"Clases", None))
        self.examenes.setText(QCoreApplication.translate("crearHorario", u"Examen", None))
    # retranslateUi

