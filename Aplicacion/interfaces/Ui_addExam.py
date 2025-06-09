# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addExamzMihZU.ui'
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
    QSizePolicy, QSpinBox, QWidget)

class Ui_addExamen(object):
    def setupUi(self, addExamen):
        if not addExamen.objectName():
            addExamen.setObjectName(u"addExamen")
        addExamen.resize(402, 256)
        self.Title = QLabel(addExamen)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(9, 9, 162, 50))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.titulacion = QLabel(addExamen)
        self.titulacion.setObjectName(u"titulacion")
        self.titulacion.setGeometry(QRect(10, 90, 52, 16))
        self.titulacionText = QComboBox(addExamen)
        self.titulacionText.setObjectName(u"titulacionText")
        self.titulacionText.setGeometry(QRect(80, 90, 301, 21))
        self.duracion = QLabel(addExamen)
        self.duracion.setObjectName(u"duracion")
        self.duracion.setGeometry(QRect(10, 140, 48, 16))
        self.duarcionText = QSpinBox(addExamen)
        self.duarcionText.setObjectName(u"duarcionText")
        self.duarcionText.setGeometry(QRect(80, 140, 101, 23))
        self.save = QPushButton(addExamen)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(10, 220, 75, 24))
        self.infoDuarcion = QLabel(addExamen)
        self.infoDuarcion.setObjectName(u"infoDuarcion")
        self.infoDuarcion.setGeometry(QRect(10, 170, 371, 31))

        self.retranslateUi(addExamen)

        QMetaObject.connectSlotsByName(addExamen)
    # setupUi

    def retranslateUi(self, addExamen):
        addExamen.setWindowTitle(QCoreApplication.translate("addExamen", u"a\u00f1adirExamen", None))
        self.Title.setText(QCoreApplication.translate("addExamen", u"Ex\u00e1menes", None))
        self.titulacion.setText(QCoreApplication.translate("addExamen", u"Titluaci\u00f3n", None))
        self.duracion.setText(QCoreApplication.translate("addExamen", u"Duraci\u00f3n", None))
        self.save.setText(QCoreApplication.translate("addExamen", u"Guardar", None))
        self.infoDuarcion.setText(QCoreApplication.translate("addExamen", u"* En la opci\u00f3n modificar se puede cambiar la duraci\u00f3n por asignatura", None))
    # retranslateUi

