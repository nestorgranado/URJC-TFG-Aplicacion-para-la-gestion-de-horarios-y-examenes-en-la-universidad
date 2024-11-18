# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedulecrzWuV.ui'
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

class Ui_Horario(object):
    def setupUi(self, Horario):
        if not Horario.objectName():
            Horario.setObjectName(u"Horario")
        Horario.resize(298, 197)
        self.verticalLayout = QVBoxLayout(Horario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(Horario)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)

        self.verticalLayout.addWidget(self.Title)

        self.add = QPushButton(Horario)
        self.add.setObjectName(u"add")

        self.verticalLayout.addWidget(self.add)

        self.modificar = QPushButton(Horario)
        self.modificar.setObjectName(u"modificar")

        self.verticalLayout.addWidget(self.modificar)

        self.exportar = QPushButton(Horario)
        self.exportar.setObjectName(u"exportar")

        self.verticalLayout.addWidget(self.exportar)

        self.crearHorario = QPushButton(Horario)
        self.crearHorario.setObjectName(u"crearHorario")

        self.verticalLayout.addWidget(self.crearHorario)


        self.retranslateUi(Horario)

        QMetaObject.connectSlotsByName(Horario)
    # setupUi

    def retranslateUi(self, Horario):
        Horario.setWindowTitle(QCoreApplication.translate("Horario", u"horario", None))
        self.Title.setText(QCoreApplication.translate("Horario", u"TextLabel", None))
        self.add.setText(QCoreApplication.translate("Horario", u"Nuevo", None))
        self.modificar.setText(QCoreApplication.translate("Horario", u"Modificar", None))
        self.exportar.setText(QCoreApplication.translate("Horario", u"Exportar Datos", None))
        self.crearHorario.setText(QCoreApplication.translate("Horario", u"Crear Horario", None))
    # retranslateUi

