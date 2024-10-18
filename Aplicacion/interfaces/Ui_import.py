# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importNxESUn.ui'
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

class Ui_importar(object):
    def setupUi(self, importar):
        if not importar.objectName():
            importar.setObjectName(u"importar")
        importar.resize(359, 128)
        self.formLayout = QFormLayout(importar)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(importar)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.examinarBtn = QPushButton(importar)
        self.examinarBtn.setObjectName(u"examinarBtn")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.examinarBtn)

        self.rutaText = QLineEdit(importar)
        self.rutaText.setObjectName(u"rutaText")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rutaText)

        self.importarBtn = QPushButton(importar)
        self.importarBtn.setObjectName(u"importarBtn")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.importarBtn)


        self.retranslateUi(importar)

        QMetaObject.connectSlotsByName(importar)
    # setupUi

    def retranslateUi(self, importar):
        importar.setWindowTitle(QCoreApplication.translate("importar", u"importarDatos", None))
        self.label.setText(QCoreApplication.translate("importar", u"Importar Datos", None))
        self.examinarBtn.setText(QCoreApplication.translate("importar", u"Examinar", None))
        self.importarBtn.setText(QCoreApplication.translate("importar", u"importar", None))
    # retranslateUi

