# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fetConnectRepSBy.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_conexionFET(object):
    def setupUi(self, conexionFET):
        if not conexionFET.objectName():
            conexionFET.setObjectName(u"conexionFET")
        conexionFET.resize(467, 128)
        self.formLayout = QFormLayout(conexionFET)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(conexionFET)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.examinarBtn = QPushButton(conexionFET)
        self.examinarBtn.setObjectName(u"examinarBtn")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.examinarBtn)

        self.rutaText = QLineEdit(conexionFET)
        self.rutaText.setObjectName(u"rutaText")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rutaText)

        self.importarBtn = QPushButton(conexionFET)
        self.importarBtn.setObjectName(u"importarBtn")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.importarBtn)


        self.retranslateUi(conexionFET)

        QMetaObject.connectSlotsByName(conexionFET)
    # setupUi

    def retranslateUi(self, conexionFET):
        conexionFET.setWindowTitle(QCoreApplication.translate("conexionFET", u"conexionFET", None))
        self.label.setText(QCoreApplication.translate("conexionFET", u"Buscar programa fet-cl.exe", None))
        self.examinarBtn.setText(QCoreApplication.translate("conexionFET", u"Examinar", None))
        self.importarBtn.setText(QCoreApplication.translate("conexionFET", u"importar", None))
    # retranslateUi

