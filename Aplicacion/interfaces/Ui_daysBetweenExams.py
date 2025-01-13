# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daysBetweenExamserkMfI.ui'
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

class Ui_res_separacionDias(object):
    def setupUi(self, res_separacionDias):
        if not res_separacionDias.objectName():
            res_separacionDias.setObjectName(u"res_separacionDias")
        res_separacionDias.resize(517, 231)
        self.Title = QLabel(res_separacionDias)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 20, 501, 61))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.examen1 = QLabel(res_separacionDias)
        self.examen1.setObjectName(u"examen1")
        self.examen1.setGeometry(QRect(30, 100, 49, 16))
        self.examen2 = QLabel(res_separacionDias)
        self.examen2.setObjectName(u"examen2")
        self.examen2.setGeometry(QRect(30, 130, 61, 16))
        self.separacion = QLabel(res_separacionDias)
        self.separacion.setObjectName(u"separacion")
        self.separacion.setGeometry(QRect(30, 160, 91, 16))
        self.examen1Text = QComboBox(res_separacionDias)
        self.examen1Text.setObjectName(u"examen1Text")
        self.examen1Text.setGeometry(QRect(130, 100, 311, 22))
        self.examen2Text = QComboBox(res_separacionDias)
        self.examen2Text.setObjectName(u"examen2Text")
        self.examen2Text.setGeometry(QRect(130, 130, 311, 22))
        self.separacionText = QSpinBox(res_separacionDias)
        self.separacionText.setObjectName(u"separacionText")
        self.separacionText.setGeometry(QRect(130, 160, 88, 23))
        self.save = QPushButton(res_separacionDias)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 200, 75, 24))

        self.retranslateUi(res_separacionDias)

        QMetaObject.connectSlotsByName(res_separacionDias)
    # setupUi

    def retranslateUi(self, res_separacionDias):
        res_separacionDias.setWindowTitle(QCoreApplication.translate("res_separacionDias", u"res_separacionDias", None))
        self.Title.setText(QCoreApplication.translate("res_separacionDias", u"Min. D\u00edas entre dos examenes", None))
        self.examen1.setText(QCoreApplication.translate("res_separacionDias", u"Examen 1", None))
        self.examen2.setText(QCoreApplication.translate("res_separacionDias", u"Examen 2", None))
        self.separacion.setText(QCoreApplication.translate("res_separacionDias", u"D\u00edas separaci\u00f3n", None))
        self.save.setText(QCoreApplication.translate("res_separacionDias", u"Guardar", None))
    # retranslateUi

