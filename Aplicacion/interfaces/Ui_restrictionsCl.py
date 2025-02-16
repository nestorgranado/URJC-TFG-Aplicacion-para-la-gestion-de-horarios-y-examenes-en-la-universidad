# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restrictionsClIqdEUE.ui'
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

class Ui_RestriccionesCl(object):
    def setupUi(self, RestriccionesCl):
        if not RestriccionesCl.objectName():
            RestriccionesCl.setObjectName(u"RestriccionesCl")
        RestriccionesCl.resize(236, 278)
        self.formLayout = QFormLayout(RestriccionesCl)
        self.formLayout.setObjectName(u"formLayout")
        self.Title = QLabel(RestriccionesCl)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Title)

        self.todas = QPushButton(RestriccionesCl)
        self.todas.setObjectName(u"todas")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.todas)

        self.turno = QPushButton(RestriccionesCl)
        self.turno.setObjectName(u"turno")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.turno)

        self.horasDia = QPushButton(RestriccionesCl)
        self.horasDia.setObjectName(u"horasDia")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.horasDia)

        self.huecosSemana = QPushButton(RestriccionesCl)
        self.huecosSemana.setObjectName(u"huecosSemana")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.huecosSemana)

        self.separacion = QPushButton(RestriccionesCl)
        self.separacion.setObjectName(u"separacion")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.separacion)

        self.tipoAula = QPushButton(RestriccionesCl)
        self.tipoAula.setObjectName(u"tipoAula")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.tipoAula)


        self.retranslateUi(RestriccionesCl)

        QMetaObject.connectSlotsByName(RestriccionesCl)
    # setupUi

    def retranslateUi(self, RestriccionesCl):
        RestriccionesCl.setWindowTitle(QCoreApplication.translate("RestriccionesCl", u"RestriccionesCl", None))
        self.Title.setText(QCoreApplication.translate("RestriccionesCl", u"Restricciones", None))
        self.todas.setText(QCoreApplication.translate("RestriccionesCl", u"Todas las restricciones", None))
        self.turno.setText(QCoreApplication.translate("RestriccionesCl", u"Elegir turno", None))
        self.horasDia.setText(QCoreApplication.translate("RestriccionesCl", u"Max. Horas por d\u00eda", None))
        self.huecosSemana.setText(QCoreApplication.translate("RestriccionesCl", u"Max. Huecos por semana", None))
        self.separacion.setText(QCoreApplication.translate("RestriccionesCl", u"Separaci\u00f3n entre clases", None))
        self.tipoAula.setText(QCoreApplication.translate("RestriccionesCl", u"Tipo aula para clase", None))
    # retranslateUi

