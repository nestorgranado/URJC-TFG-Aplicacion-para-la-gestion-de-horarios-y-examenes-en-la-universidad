# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roomTypeBNetTz.ui'
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
    QSizePolicy, QWidget)

class Ui_res_tipoAula(object):
    def setupUi(self, res_tipoAula):
        if not res_tipoAula.objectName():
            res_tipoAula.setObjectName(u"res_tipoAula")
        res_tipoAula.resize(560, 230)
        self.Title = QLabel(res_tipoAula)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 20, 521, 41))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.save = QPushButton(res_tipoAula)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 180, 75, 24))
        self.actividad = QLabel(res_tipoAula)
        self.actividad.setObjectName(u"actividad")
        self.actividad.setGeometry(QRect(30, 100, 49, 16))
        self.actividadText = QComboBox(res_tipoAula)
        self.actividadText.setObjectName(u"actividadText")
        self.actividadText.setGeometry(QRect(130, 100, 401, 22))
        self.tipoAula = QLabel(res_tipoAula)
        self.tipoAula.setObjectName(u"tipoAula")
        self.tipoAula.setGeometry(QRect(30, 140, 49, 16))
        self.tipoAulaText = QComboBox(res_tipoAula)
        self.tipoAulaText.setObjectName(u"tipoAulaText")
        self.tipoAulaText.setGeometry(QRect(130, 140, 171, 22))

        self.retranslateUi(res_tipoAula)

        QMetaObject.connectSlotsByName(res_tipoAula)
    # setupUi

    def retranslateUi(self, res_tipoAula):
        res_tipoAula.setWindowTitle(QCoreApplication.translate("res_tipoAula", u"res_tipoAula", None))
        self.Title.setText(QCoreApplication.translate("res_tipoAula", u"Tipo de aula para una Actividad", None))
        self.save.setText(QCoreApplication.translate("res_tipoAula", u"Guardar", None))
        self.actividad.setText(QCoreApplication.translate("res_tipoAula", u"Actividad", None))
        self.tipoAula.setText(QCoreApplication.translate("res_tipoAula", u"Tipo Aula", None))
    # retranslateUi

