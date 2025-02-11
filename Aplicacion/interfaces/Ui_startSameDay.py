# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startSameDaydZlhct.ui'
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
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_res_mismoDia(object):
    def setupUi(self, res_mismoDia):
        if not res_mismoDia.objectName():
            res_mismoDia.setObjectName(u"res_mismoDia")
        res_mismoDia.resize(491, 284)
        self.actividad1 = QLabel(res_mismoDia)
        self.actividad1.setObjectName(u"actividad1")
        self.actividad1.setGeometry(QRect(30, 150, 71, 16))
        self.actividad2 = QLabel(res_mismoDia)
        self.actividad2.setObjectName(u"actividad2")
        self.actividad2.setGeometry(QRect(30, 180, 61, 16))
        self.actividad1Text = QComboBox(res_mismoDia)
        self.actividad1Text.setObjectName(u"actividad1Text")
        self.actividad1Text.setGeometry(QRect(130, 150, 311, 22))
        self.actividad2Text = QComboBox(res_mismoDia)
        self.actividad2Text.setObjectName(u"actividad2Text")
        self.actividad2Text.setGeometry(QRect(130, 180, 311, 22))
        self.save = QPushButton(res_mismoDia)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 240, 75, 24))
        self.layoutWidget = QWidget(res_mismoDia)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 464, 108))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title = QLabel(self.layoutWidget)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)

        self.verticalLayout.addWidget(self.Title)

        self.Title2 = QLabel(self.layoutWidget)
        self.Title2.setObjectName(u"Title2")
        self.Title2.setFont(font)

        self.verticalLayout.addWidget(self.Title2)

        self.obligatoria = QRadioButton(res_mismoDia)
        self.obligatoria.setObjectName(u"obligatoria")
        self.obligatoria.setGeometry(QRect(30, 210, 92, 20))

        self.retranslateUi(res_mismoDia)

        QMetaObject.connectSlotsByName(res_mismoDia)
    # setupUi

    def retranslateUi(self, res_mismoDia):
        res_mismoDia.setWindowTitle(QCoreApplication.translate("res_mismoDia", u"res_mismoDia", None))
        self.actividad1.setText(QCoreApplication.translate("res_mismoDia", u"Actividad 1", None))
        self.actividad2.setText(QCoreApplication.translate("res_mismoDia", u"Actividad 2", None))
        self.save.setText(QCoreApplication.translate("res_mismoDia", u"Guardar", None))
        self.Title.setText(QCoreApplication.translate("res_mismoDia", u"Dos Actividades ", None))
        self.Title2.setText(QCoreApplication.translate("res_mismoDia", u"se realizan simultaneamente", None))
        self.obligatoria.setText(QCoreApplication.translate("res_mismoDia", u"Obligatoria", None))
    # retranslateUi

