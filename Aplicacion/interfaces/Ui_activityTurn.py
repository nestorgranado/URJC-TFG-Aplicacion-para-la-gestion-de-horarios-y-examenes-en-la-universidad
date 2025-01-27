# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activityTurnXSXoZp.ui'
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
    QRadioButton, QSizePolicy, QWidget)

class Ui_res_turno(object):
    def setupUi(self, res_turno):
        if not res_turno.objectName():
            res_turno.setObjectName(u"res_turno")
        res_turno.resize(402, 309)
        self.Title = QLabel(res_turno)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 10, 661, 71))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.am = QRadioButton(res_turno)
        self.am.setObjectName(u"am")
        self.am.setGeometry(QRect(20, 140, 92, 20))
        self.pm = QRadioButton(res_turno)
        self.pm.setObjectName(u"pm")
        self.pm.setGeometry(QRect(20, 170, 92, 20))
        self.save = QPushButton(res_turno)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(20, 210, 75, 24))
        self.actividad = QLabel(res_turno)
        self.actividad.setObjectName(u"actividad")
        self.actividad.setGeometry(QRect(20, 90, 49, 16))
        self.actividadText = QComboBox(res_turno)
        self.actividadText.setObjectName(u"actividadText")
        self.actividadText.setGeometry(QRect(80, 90, 301, 22))

        self.retranslateUi(res_turno)

        QMetaObject.connectSlotsByName(res_turno)
    # setupUi

    def retranslateUi(self, res_turno):
        res_turno.setWindowTitle(QCoreApplication.translate("res_turno", u"res_turno", None))
        self.Title.setText(QCoreApplication.translate("res_turno", u"Turno de una actividad", None))
        self.am.setText(QCoreApplication.translate("res_turno", u"Ma\u00f1ana", None))
        self.pm.setText(QCoreApplication.translate("res_turno", u"Tarde", None))
        self.save.setText(QCoreApplication.translate("res_turno", u"Guardar", None))
        self.actividad.setText(QCoreApplication.translate("res_turno", u"Actividad", None))
    # retranslateUi

