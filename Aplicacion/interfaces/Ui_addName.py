# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addNameiPDODf.ui'
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

class Ui_AddNombre(object):
    def setupUi(self, AddNombre):
        if not AddNombre.objectName():
            AddNombre.setObjectName(u"AddNombre")
        AddNombre.resize(280, 127)
        self.formLayout = QFormLayout(AddNombre)
        self.formLayout.setObjectName(u"formLayout")
        self.Title = QLabel(AddNombre)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(29)
        self.Title.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.Title)

        self.nombre = QLabel(AddNombre)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nombre)

        self.nombreText = QLineEdit(AddNombre)
        self.nombreText.setObjectName(u"nombreText")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nombreText)

        self.save = QPushButton(AddNombre)
        self.save.setObjectName(u"save")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.save)


        self.retranslateUi(AddNombre)

        QMetaObject.connectSlotsByName(AddNombre)
    # setupUi

    def retranslateUi(self, AddNombre):
        AddNombre.setWindowTitle(QCoreApplication.translate("AddNombre", u"a\u00f1adirNombre", None))
        self.Title.setText(QCoreApplication.translate("AddNombre", u"Instituci\u00f3n", None))
        self.nombre.setText(QCoreApplication.translate("AddNombre", u"Nombre", None))
        self.save.setText(QCoreApplication.translate("AddNombre", u"Guardar", None))
    # retranslateUi

