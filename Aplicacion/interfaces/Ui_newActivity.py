# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newActivityEcXZJb.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Actividades(object):
    def setupUi(self, Actividades):
        if not Actividades.objectName():
            Actividades.setObjectName(u"Actividades")
        Actividades.resize(285, 128)
        self.verticalLayout = QVBoxLayout(Actividades)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(Actividades)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)

        self.verticalLayout.addWidget(self.Title)

        self.clases = QPushButton(Actividades)
        self.clases.setObjectName(u"clases")

        self.verticalLayout.addWidget(self.clases)

        self.examenes = QPushButton(Actividades)
        self.examenes.setObjectName(u"examenes")

        self.verticalLayout.addWidget(self.examenes)


        self.retranslateUi(Actividades)

        QMetaObject.connectSlotsByName(Actividades)
    # setupUi

    def retranslateUi(self, Actividades):
        Actividades.setWindowTitle(QCoreApplication.translate("Actividades", u"actividades", None))
        self.Title.setText(QCoreApplication.translate("Actividades", u"Nueva Actividad", None))
        self.clases.setText(QCoreApplication.translate("Actividades", u"Clases", None))
        self.examenes.setText(QCoreApplication.translate("Actividades", u"Examen", None))
    # retranslateUi

