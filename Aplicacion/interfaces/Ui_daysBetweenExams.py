# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daysBetweenExamsNhtBvg.ui'
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

class Ui_res_separacionDias(object):
    def setupUi(self, res_separacionDias):
        if not res_separacionDias.objectName():
            res_separacionDias.setObjectName(u"res_separacionDias")
        res_separacionDias.resize(517, 281)
        self.Title = QLabel(res_separacionDias)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 20, 501, 61))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.actividad1 = QLabel(res_separacionDias)
        self.actividad1.setObjectName(u"actividad1")
        self.actividad1.setGeometry(QRect(30, 100, 71, 16))
        self.actividad2 = QLabel(res_separacionDias)
        self.actividad2.setObjectName(u"actividad2")
        self.actividad2.setGeometry(QRect(30, 130, 61, 16))
        self.separacion = QLabel(res_separacionDias)
        self.separacion.setObjectName(u"separacion")
        self.separacion.setGeometry(QRect(30, 160, 91, 16))
        self.actividad1Text = QComboBox(res_separacionDias)
        self.actividad1Text.setObjectName(u"actividad1Text")
        self.actividad1Text.setGeometry(QRect(130, 100, 311, 22))
        self.actividad2Text = QComboBox(res_separacionDias)
        self.actividad2Text.setObjectName(u"actividad2Text")
        self.actividad2Text.setGeometry(QRect(130, 130, 311, 22))
        self.separacionText = QSpinBox(res_separacionDias)
        self.separacionText.setObjectName(u"separacionText")
        self.separacionText.setGeometry(QRect(130, 160, 88, 23))
        self.save = QPushButton(res_separacionDias)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 230, 75, 24))
        self.obligatoria = QRadioButton(res_separacionDias)
        self.obligatoria.setObjectName(u"obligatoria")
        self.obligatoria.setGeometry(QRect(30, 190, 92, 20))

        self.retranslateUi(res_separacionDias)

        QMetaObject.connectSlotsByName(res_separacionDias)
    # setupUi

    def retranslateUi(self, res_separacionDias):
        res_separacionDias.setWindowTitle(QCoreApplication.translate("res_separacionDias", u"res_separacionDias", None))
        self.Title.setText(QCoreApplication.translate("res_separacionDias", u"Min. D\u00edas entre dos Actividades", None))
        self.actividad1.setText(QCoreApplication.translate("res_separacionDias", u"Actividad 1", None))
        self.actividad2.setText(QCoreApplication.translate("res_separacionDias", u"Actividad 2", None))
        self.separacion.setText(QCoreApplication.translate("res_separacionDias", u"D\u00edas separaci\u00f3n", None))
        self.save.setText(QCoreApplication.translate("res_separacionDias", u"Guardar", None))
        self.obligatoria.setText(QCoreApplication.translate("res_separacionDias", u"Obligatoria", None))
    # retranslateUi

