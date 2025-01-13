# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startSameDayozqpYT.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_res_mismoDia(object):
    def setupUi(self, res_mismoDia):
        if not res_mismoDia.objectName():
            res_mismoDia.setObjectName(u"res_mismoDia")
        res_mismoDia.resize(491, 258)
        self.examen1 = QLabel(res_mismoDia)
        self.examen1.setObjectName(u"examen1")
        self.examen1.setGeometry(QRect(30, 150, 49, 16))
        self.examen2 = QLabel(res_mismoDia)
        self.examen2.setObjectName(u"examen2")
        self.examen2.setGeometry(QRect(30, 180, 61, 16))
        self.examen1Text = QComboBox(res_mismoDia)
        self.examen1Text.setObjectName(u"examen1Text")
        self.examen1Text.setGeometry(QRect(130, 150, 311, 22))
        self.examen2Text = QComboBox(res_mismoDia)
        self.examen2Text.setObjectName(u"examen2Text")
        self.examen2Text.setGeometry(QRect(130, 180, 311, 22))
        self.save = QPushButton(res_mismoDia)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 220, 75, 24))
        self.widget = QWidget(res_mismoDia)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 464, 108))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title = QLabel(self.widget)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)

        self.verticalLayout.addWidget(self.Title)

        self.Title2 = QLabel(self.widget)
        self.Title2.setObjectName(u"Title2")
        self.Title2.setFont(font)

        self.verticalLayout.addWidget(self.Title2)


        self.retranslateUi(res_mismoDia)

        QMetaObject.connectSlotsByName(res_mismoDia)
    # setupUi

    def retranslateUi(self, res_mismoDia):
        res_mismoDia.setWindowTitle(QCoreApplication.translate("res_mismoDia", u"res_mismoDia", None))
        self.examen1.setText(QCoreApplication.translate("res_mismoDia", u"Examen 1", None))
        self.examen2.setText(QCoreApplication.translate("res_mismoDia", u"Examen 2", None))
        self.save.setText(QCoreApplication.translate("res_mismoDia", u"Guardar", None))
        self.Title.setText(QCoreApplication.translate("res_mismoDia", u"Dos Examenes ", None))
        self.Title2.setText(QCoreApplication.translate("res_mismoDia", u"se realizan simultaneamente", None))
    # retranslateUi

