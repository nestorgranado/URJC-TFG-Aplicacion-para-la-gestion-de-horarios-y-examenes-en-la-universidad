# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restrictionsExfiRKSv.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_RestriccionesEx(object):
    def setupUi(self, RestriccionesEx):
        if not RestriccionesEx.objectName():
            RestriccionesEx.setObjectName(u"RestriccionesEx")
        RestriccionesEx.resize(236, 188)
        self.formLayout = QFormLayout(RestriccionesEx)
        self.formLayout.setObjectName(u"formLayout")
        self.Title = QLabel(RestriccionesEx)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Title)

        self.mismoDia = QPushButton(RestriccionesEx)
        self.mismoDia.setObjectName(u"mismoDia")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.mismoDia)

        self.separacion = QPushButton(RestriccionesEx)
        self.separacion.setObjectName(u"separacion")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.separacion)

        self.tipoAula = QPushButton(RestriccionesEx)
        self.tipoAula.setObjectName(u"tipoAula")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.tipoAula)

        self.todas = QPushButton(RestriccionesEx)
        self.todas.setObjectName(u"todas")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.todas)


        self.retranslateUi(RestriccionesEx)

        QMetaObject.connectSlotsByName(RestriccionesEx)
    # setupUi

    def retranslateUi(self, RestriccionesEx):
        RestriccionesEx.setWindowTitle(QCoreApplication.translate("RestriccionesEx", u"RestriccionesEx", None))
        self.Title.setText(QCoreApplication.translate("RestriccionesEx", u"Restricciones", None))
        self.mismoDia.setText(QCoreApplication.translate("RestriccionesEx", u"Ex\u00e1menes mimmo d\u00eda y hora", None))
        self.separacion.setText(QCoreApplication.translate("RestriccionesEx", u"Separaci\u00f3n entre asignaturas", None))
        self.tipoAula.setText(QCoreApplication.translate("RestriccionesEx", u"Tipo aula para un examen", None))
        self.todas.setText(QCoreApplication.translate("RestriccionesEx", u"Todas las restricciones", None))
    # retranslateUi

