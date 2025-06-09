# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'othersZhseUm.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QWidget)

class Ui_otrosHorarios(object):
    def setupUi(self, otrosHorarios):
        if not otrosHorarios.objectName():
            otrosHorarios.setObjectName(u"otrosHorarios")
        otrosHorarios.resize(437, 670)
        self.tabWidget = QTabWidget(otrosHorarios)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(60, 90, 311, 521))
        self.dias = QWidget()
        self.dias.setObjectName(u"dias")
        self.listaDias = QListWidget(self.dias)
        self.listaDias.setObjectName(u"listaDias")
        self.listaDias.setGeometry(QRect(10, 120, 256, 361))
        self.layoutWidget = QWidget(self.dias)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 164, 25))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.numDias = QLabel(self.layoutWidget)
        self.numDias.setObjectName(u"numDias")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.numDias)

        self.numDiasText = QSpinBox(self.layoutWidget)
        self.numDiasText.setObjectName(u"numDiasText")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numDiasText)

        self.title = QLabel(self.dias)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 0, 281, 71))
        font = QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.tabWidget.addTab(self.dias, "")
        self.horas = QWidget()
        self.horas.setObjectName(u"horas")
        self.listaHoras = QListWidget(self.horas)
        self.listaHoras.setObjectName(u"listaHoras")
        self.listaHoras.setGeometry(QRect(10, 120, 256, 361))
        self.title_2 = QLabel(self.horas)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(10, 0, 281, 71))
        self.title_2.setFont(font)
        self.layoutWidget_2 = QWidget(self.horas)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 80, 172, 25))
        self.formLayout_2 = QFormLayout(self.layoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.numHoras = QLabel(self.layoutWidget_2)
        self.numHoras.setObjectName(u"numHoras")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.numHoras)

        self.numHorasText = QSpinBox(self.layoutWidget_2)
        self.numHorasText.setObjectName(u"numHorasText")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.numHorasText)

        self.tabWidget.addTab(self.horas, "")
        self.Title = QLabel(otrosHorarios)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(60, 30, 311, 61))
        self.Title.setFont(font)
        self.save = QPushButton(otrosHorarios)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(60, 620, 75, 24))

        self.retranslateUi(otrosHorarios)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(otrosHorarios)
    # setupUi

    def retranslateUi(self, otrosHorarios):
        otrosHorarios.setWindowTitle(QCoreApplication.translate("otrosHorarios", u"otrosHorarios", None))
        self.numDias.setText(QCoreApplication.translate("otrosHorarios", u"N\u00famero de d\u00edas", None))
        self.title.setText(QCoreApplication.translate("otrosHorarios", u"D\u00edas por Semana", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dias), QCoreApplication.translate("otrosHorarios", u"D\u00edas por semana", None))
        self.title_2.setText(QCoreApplication.translate("otrosHorarios", u"Horas por D\u00eda", None))
        self.numHoras.setText(QCoreApplication.translate("otrosHorarios", u"N\u00famero de horas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.horas), QCoreApplication.translate("otrosHorarios", u"Horas por d\u00eda", None))
        self.Title.setText(QCoreApplication.translate("otrosHorarios", u"Otros Horarios", None))
        self.save.setText(QCoreApplication.translate("otrosHorarios", u"Guardar", None))
    # retranslateUi

