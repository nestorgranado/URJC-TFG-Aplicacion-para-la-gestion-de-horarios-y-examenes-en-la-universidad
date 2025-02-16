# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activityTurnfPIepG.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTimeEdit, QWidget)

class Ui_res_turno(object):
    def setupUi(self, res_turno):
        if not res_turno.objectName():
            res_turno.setObjectName(u"res_turno")
        res_turno.resize(469, 264)
        self.Title = QLabel(res_turno)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 10, 661, 71))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.save = QPushButton(res_turno)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(20, 230, 75, 24))
        self.layoutWidget = QWidget(res_turno)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 160, 361, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horaIni = QLabel(self.layoutWidget)
        self.horaIni.setObjectName(u"horaIni")

        self.horizontalLayout.addWidget(self.horaIni)

        self.horaIniText = QTimeEdit(self.layoutWidget)
        self.horaIniText.setObjectName(u"horaIniText")

        self.horizontalLayout.addWidget(self.horaIniText)

        self.horaFin = QLabel(self.layoutWidget)
        self.horaFin.setObjectName(u"horaFin")

        self.horizontalLayout.addWidget(self.horaFin)

        self.horaFinText = QTimeEdit(self.layoutWidget)
        self.horaFinText.setObjectName(u"horaFinText")

        self.horizontalLayout.addWidget(self.horaFinText)

        self.layoutWidget1 = QWidget(res_turno)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 100, 431, 61))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.titulacion = QLabel(self.layoutWidget1)
        self.titulacion.setObjectName(u"titulacion")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titulacion)

        self.titulacionText = QComboBox(self.layoutWidget1)
        self.titulacionText.setObjectName(u"titulacionText")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titulacionText)

        self.curso = QLabel(self.layoutWidget1)
        self.curso.setObjectName(u"curso")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.curso)

        self.cursoText = QComboBox(self.layoutWidget1)
        self.cursoText.setObjectName(u"cursoText")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cursoText)

        self.obligatoria = QRadioButton(res_turno)
        self.obligatoria.setObjectName(u"obligatoria")
        self.obligatoria.setGeometry(QRect(20, 200, 92, 20))

        self.retranslateUi(res_turno)

        QMetaObject.connectSlotsByName(res_turno)
    # setupUi

    def retranslateUi(self, res_turno):
        res_turno.setWindowTitle(QCoreApplication.translate("res_turno", u"res_turno", None))
        self.Title.setText(QCoreApplication.translate("res_turno", u"Turno de un Curso", None))
        self.save.setText(QCoreApplication.translate("res_turno", u"Guardar", None))
        self.horaIni.setText(QCoreApplication.translate("res_turno", u"Hora Inicio", None))
        self.horaFin.setText(QCoreApplication.translate("res_turno", u"Hora Fin", None))
        self.titulacion.setText(QCoreApplication.translate("res_turno", u"Titulacion", None))
        self.curso.setText(QCoreApplication.translate("res_turno", u"Curso", None))
        self.obligatoria.setText(QCoreApplication.translate("res_turno", u"Obligatoria", None))
    # retranslateUi

