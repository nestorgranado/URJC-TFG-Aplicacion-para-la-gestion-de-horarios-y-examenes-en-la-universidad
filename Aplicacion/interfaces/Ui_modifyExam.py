# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyExammOkVfH.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_ModificarExamenes(object):
    def setupUi(self, ModificarExamenes):
        if not ModificarExamenes.objectName():
            ModificarExamenes.setObjectName(u"ModificarExamenes")
        ModificarExamenes.resize(877, 667)
        self.Title = QLabel(ModificarExamenes)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(30, 30, 371, 71))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.actividadesList = QListWidget(ModificarExamenes)
        self.actividadesList.setObjectName(u"actividadesList")
        self.actividadesList.setGeometry(QRect(30, 120, 351, 481))
        self.asignatura = QLabel(ModificarExamenes)
        self.asignatura.setObjectName(u"asignatura")
        self.asignatura.setGeometry(QRect(400, 170, 61, 16))
        self.asignaturaText = QLineEdit(ModificarExamenes)
        self.asignaturaText.setObjectName(u"asignaturaText")
        self.asignaturaText.setGeometry(QRect(480, 170, 381, 21))
        self.alumnos = QLabel(ModificarExamenes)
        self.alumnos.setObjectName(u"alumnos")
        self.alumnos.setGeometry(QRect(400, 210, 49, 16))
        self.alumnosText = QLineEdit(ModificarExamenes)
        self.alumnosText.setObjectName(u"alumnosText")
        self.alumnosText.setGeometry(QRect(480, 210, 381, 21))
        self.duracion = QLabel(ModificarExamenes)
        self.duracion.setObjectName(u"duracion")
        self.duracion.setGeometry(QRect(400, 250, 49, 16))
        self.duracionText = QSpinBox(ModificarExamenes)
        self.duracionText.setObjectName(u"duracionText")
        self.duracionText.setGeometry(QRect(480, 250, 111, 23))
        self.save = QPushButton(ModificarExamenes)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 620, 75, 24))
        self.layoutWidget = QWidget(ModificarExamenes)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(390, 290, 239, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.modificar = QPushButton(self.layoutWidget)
        self.modificar.setObjectName(u"modificar")

        self.horizontalLayout.addWidget(self.modificar)

        self.sup = QPushButton(self.layoutWidget)
        self.sup.setObjectName(u"sup")

        self.horizontalLayout.addWidget(self.sup)

        self.titulacion = QLabel(ModificarExamenes)
        self.titulacion.setObjectName(u"titulacion")
        self.titulacion.setGeometry(QRect(400, 130, 61, 16))
        self.titulacionText = QComboBox(ModificarExamenes)
        self.titulacionText.setObjectName(u"titulacionText")
        self.titulacionText.setGeometry(QRect(480, 130, 381, 22))

        self.retranslateUi(ModificarExamenes)

        QMetaObject.connectSlotsByName(ModificarExamenes)
    # setupUi

    def retranslateUi(self, ModificarExamenes):
        ModificarExamenes.setWindowTitle(QCoreApplication.translate("ModificarExamenes", u"modificarExamenes", None))
        self.Title.setText(QCoreApplication.translate("ModificarExamenes", u"Modificar Ex\u00e1menes", None))
        self.asignatura.setText(QCoreApplication.translate("ModificarExamenes", u"Asignatura", None))
        self.alumnos.setText(QCoreApplication.translate("ModificarExamenes", u"Alumnos", None))
        self.duracion.setText(QCoreApplication.translate("ModificarExamenes", u"Duarci\u00f3n", None))
        self.save.setText(QCoreApplication.translate("ModificarExamenes", u"Guardar", None))
        self.modificar.setText(QCoreApplication.translate("ModificarExamenes", u"Modificar", None))
        self.sup.setText(QCoreApplication.translate("ModificarExamenes", u"Borrar", None))
        self.titulacion.setText(QCoreApplication.translate("ModificarExamenes", u"Titulaci\u00f3n", None))
    # retranslateUi

