# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maxHoursDayRxsZDR.ui'
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

class Ui_MaxHorasDia(object):
    def setupUi(self, MaxHorasDia):
        if not MaxHorasDia.objectName():
            MaxHorasDia.setObjectName(u"MaxHorasDia")
        MaxHorasDia.resize(520, 301)
        self.Title = QLabel(MaxHorasDia)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(0, 10, 551, 61))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.grupo = QLabel(MaxHorasDia)
        self.grupo.setObjectName(u"grupo")
        self.grupo.setGeometry(QRect(10, 130, 49, 16))
        self.grupoText = QComboBox(MaxHorasDia)
        self.grupoText.setObjectName(u"grupoText")
        self.grupoText.setGeometry(QRect(90, 130, 421, 22))
        self.horas = QLabel(MaxHorasDia)
        self.horas.setObjectName(u"horas")
        self.horas.setGeometry(QRect(10, 180, 61, 16))
        self.horasText = QSpinBox(MaxHorasDia)
        self.horasText.setObjectName(u"horasText")
        self.horasText.setGeometry(QRect(90, 180, 88, 23))
        self.save = QPushButton(MaxHorasDia)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(10, 260, 75, 24))
        self.titulacion = QLabel(MaxHorasDia)
        self.titulacion.setObjectName(u"titulacion")
        self.titulacion.setGeometry(QRect(10, 80, 51, 16))
        self.titulacionText = QComboBox(MaxHorasDia)
        self.titulacionText.setObjectName(u"titulacionText")
        self.titulacionText.setGeometry(QRect(90, 80, 421, 22))
        self.obligatoria = QRadioButton(MaxHorasDia)
        self.obligatoria.setObjectName(u"obligatoria")
        self.obligatoria.setGeometry(QRect(10, 220, 92, 20))

        self.retranslateUi(MaxHorasDia)

        QMetaObject.connectSlotsByName(MaxHorasDia)
    # setupUi

    def retranslateUi(self, MaxHorasDia):
        MaxHorasDia.setWindowTitle(QCoreApplication.translate("MaxHorasDia", u"maxHorasDia", None))
        self.Title.setText(QCoreApplication.translate("MaxHorasDia", u"Max. Horas de clase en un d\u00eda", None))
        self.grupo.setText(QCoreApplication.translate("MaxHorasDia", u"Grupo", None))
        self.horas.setText(QCoreApplication.translate("MaxHorasDia", u"Max. Horas", None))
        self.save.setText(QCoreApplication.translate("MaxHorasDia", u"Guardar", None))
        self.titulacion.setText(QCoreApplication.translate("MaxHorasDia", u"Titulaci\u00f3n", None))
        self.obligatoria.setText(QCoreApplication.translate("MaxHorasDia", u"Obligatoria", None))
    # retranslateUi

