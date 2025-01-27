# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyClassmLOILn.ui'
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
    QSizePolicy, QSpinBox, QTabWidget, QWidget)

class Ui_ModificarClases(object):
    def setupUi(self, ModificarClases):
        if not ModificarClases.objectName():
            ModificarClases.setObjectName(u"ModificarClases")
        ModificarClases.resize(634, 418)
        self.Title = QLabel(ModificarClases)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(40, 40, 291, 51))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.asignatura = QLabel(ModificarClases)
        self.asignatura.setObjectName(u"asignatura")
        self.asignatura.setGeometry(QRect(40, 130, 61, 16))
        self.asignaturaText = QComboBox(ModificarClases)
        self.asignaturaText.setObjectName(u"asignaturaText")
        self.asignaturaText.setGeometry(QRect(160, 130, 451, 22))
        self.sesiones = QLabel(ModificarClases)
        self.sesiones.setObjectName(u"sesiones")
        self.sesiones.setGeometry(QRect(40, 170, 49, 16))
        self.sesionesText = QSpinBox(ModificarClases)
        self.sesionesText.setObjectName(u"sesionesText")
        self.sesionesText.setGeometry(QRect(160, 170, 88, 23))
        self.sesionesList = QTabWidget(ModificarClases)
        self.sesionesList.setObjectName(u"sesionesList")
        self.sesionesList.setGeometry(QRect(40, 210, 571, 131))
        self.save = QPushButton(ModificarClases)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(40, 360, 75, 24))

        self.retranslateUi(ModificarClases)

        self.sesionesList.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ModificarClases)
    # setupUi

    def retranslateUi(self, ModificarClases):
        ModificarClases.setWindowTitle(QCoreApplication.translate("ModificarClases", u"modificarClases", None))
        self.Title.setText(QCoreApplication.translate("ModificarClases", u"Modificar Clases", None))
        self.asignatura.setText(QCoreApplication.translate("ModificarClases", u"Asignatura", None))
        self.sesiones.setText(QCoreApplication.translate("ModificarClases", u"Sesiones", None))
        self.save.setText(QCoreApplication.translate("ModificarClases", u"Guardar", None))
    # retranslateUi

