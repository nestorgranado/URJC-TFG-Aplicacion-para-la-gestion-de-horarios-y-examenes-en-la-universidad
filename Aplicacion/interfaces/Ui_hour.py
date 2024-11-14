# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hourApfkNq.ui'
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
    QWidget)

class Ui_horas(object):
    def setupUi(self, horas):
        if not horas.objectName():
            horas.setObjectName(u"horas")
        horas.resize(366, 501)
        self.title = QLabel(horas)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 10, 281, 71))
        font = QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.listaHoras = QListWidget(horas)
        self.listaHoras.setObjectName(u"listaHoras")
        self.listaHoras.setGeometry(QRect(30, 130, 256, 311))
        self.save = QPushButton(horas)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 450, 75, 24))
        self.layoutWidget = QWidget(horas)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 90, 172, 25))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.numHoras = QLabel(self.layoutWidget)
        self.numHoras.setObjectName(u"numHoras")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.numHoras)

        self.numHorasText = QSpinBox(self.layoutWidget)
        self.numHorasText.setObjectName(u"numHorasText")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numHorasText)


        self.retranslateUi(horas)

        QMetaObject.connectSlotsByName(horas)
    # setupUi

    def retranslateUi(self, horas):
        horas.setWindowTitle(QCoreApplication.translate("horas", u"horas", None))
        self.title.setText(QCoreApplication.translate("horas", u"Horas por D\u00eda", None))
        self.save.setText(QCoreApplication.translate("horas", u"Guardar", None))
        self.numHoras.setText(QCoreApplication.translate("horas", u"N\u00famero de horas", None))
    # retranslateUi

