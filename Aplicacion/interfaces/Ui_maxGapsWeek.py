# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maxGapsWeekPmecNH.ui'
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
    QRadioButton, QSizePolicy, QSpinBox, QWidget)

class Ui_MaxHuecosSemana(object):
    def setupUi(self, MaxHuecosSemana):
        if not MaxHuecosSemana.objectName():
            MaxHuecosSemana.setObjectName(u"MaxHuecosSemana")
        MaxHuecosSemana.resize(624, 301)
        self.Title = QLabel(MaxHuecosSemana)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(0, 10, 611, 61))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.grupo = QLabel(MaxHuecosSemana)
        self.grupo.setObjectName(u"grupo")
        self.grupo.setGeometry(QRect(10, 130, 49, 16))
        self.grupoText = QComboBox(MaxHuecosSemana)
        self.grupoText.setObjectName(u"grupoText")
        self.grupoText.setGeometry(QRect(140, 130, 471, 22))
        self.huecos = QLabel(MaxHuecosSemana)
        self.huecos.setObjectName(u"huecos")
        self.huecos.setGeometry(QRect(10, 180, 121, 16))
        self.huecosText = QSpinBox(MaxHuecosSemana)
        self.huecosText.setObjectName(u"huecosText")
        self.huecosText.setGeometry(QRect(140, 180, 88, 23))
        self.save = QPushButton(MaxHuecosSemana)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(10, 250, 75, 24))
        self.titulacion = QLabel(MaxHuecosSemana)
        self.titulacion.setObjectName(u"titulacion")
        self.titulacion.setGeometry(QRect(10, 80, 51, 16))
        self.titulacionText = QComboBox(MaxHuecosSemana)
        self.titulacionText.setObjectName(u"titulacionText")
        self.titulacionText.setGeometry(QRect(140, 80, 471, 22))
        self.obligatoria = QRadioButton(MaxHuecosSemana)
        self.obligatoria.setObjectName(u"obligatoria")
        self.obligatoria.setGeometry(QRect(10, 210, 92, 20))

        self.retranslateUi(MaxHuecosSemana)

        QMetaObject.connectSlotsByName(MaxHuecosSemana)
    # setupUi

    def retranslateUi(self, MaxHuecosSemana):
        MaxHuecosSemana.setWindowTitle(QCoreApplication.translate("MaxHuecosSemana", u"maxHuecosSemana", None))
        self.Title.setText(QCoreApplication.translate("MaxHuecosSemana", u"Max. Huecos entre clases por semana", None))
        self.grupo.setText(QCoreApplication.translate("MaxHuecosSemana", u"Grupo", None))
        self.huecos.setText(QCoreApplication.translate("MaxHuecosSemana", u"Max. Huecos/Semana", None))
        self.save.setText(QCoreApplication.translate("MaxHuecosSemana", u"Guardar", None))
        self.titulacion.setText(QCoreApplication.translate("MaxHuecosSemana", u"Titulaci\u00f3n", None))
        self.obligatoria.setText(QCoreApplication.translate("MaxHuecosSemana", u"Obligatoria", None))
    # retranslateUi

