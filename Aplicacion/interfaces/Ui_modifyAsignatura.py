# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyAsignaturarvEDHx.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpinBox, QSplitter,
    QWidget)

class Ui_ModificarAsignatura(object):
    def setupUi(self, ModificarAsignatura):
        if not ModificarAsignatura.objectName():
            ModificarAsignatura.setObjectName(u"ModificarAsignatura")
        ModificarAsignatura.resize(1009, 889)
        self.splitter = QSplitter(ModificarAsignatura)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 20, 331, 861))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.Title = QLabel(self.splitter)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.splitter.addWidget(self.Title)
        self.list = QListWidget(self.splitter)
        self.list.setObjectName(u"list")
        self.splitter.addWidget(self.list)
        self.save = QPushButton(self.splitter)
        self.save.setObjectName(u"save")
        self.splitter.addWidget(self.save)
        self.layoutWidget = QWidget(ModificarAsignatura)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(380, 350, 239, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add = QPushButton(self.layoutWidget)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.modify = QPushButton(self.layoutWidget)
        self.modify.setObjectName(u"modify")

        self.horizontalLayout.addWidget(self.modify)

        self.sup = QPushButton(self.layoutWidget)
        self.sup.setObjectName(u"sup")

        self.horizontalLayout.addWidget(self.sup)

        self.asignaturasHijas = QGroupBox(ModificarAsignatura)
        self.asignaturasHijas.setObjectName(u"asignaturasHijas")
        self.asignaturasHijas.setGeometry(QRect(369, 388, 631, 461))
        self.listHijas = QListWidget(self.asignaturasHijas)
        self.listHijas.setObjectName(u"listHijas")
        self.listHijas.setGeometry(QRect(20, 40, 271, 411))
        self.nombreHijaText = QLineEdit(self.asignaturasHijas)
        self.nombreHijaText.setObjectName(u"nombreHijaText")
        self.nombreHijaText.setGeometry(QRect(375, 68, 241, 21))
        self.codigoHija = QLabel(self.asignaturasHijas)
        self.codigoHija.setObjectName(u"codigoHija")
        self.codigoHija.setGeometry(QRect(301, 41, 63, 16))
        self.codigoHijaText = QLineEdit(self.asignaturasHijas)
        self.codigoHijaText.setObjectName(u"codigoHijaText")
        self.codigoHijaText.setGeometry(QRect(375, 41, 132, 21))
        self.nombreHija = QLabel(self.asignaturasHijas)
        self.nombreHija.setObjectName(u"nombreHija")
        self.nombreHija.setGeometry(QRect(301, 68, 68, 16))
        self.addHija = QPushButton(self.asignaturasHijas)
        self.addHija.setObjectName(u"addHija")
        self.addHija.setGeometry(QRect(300, 100, 121, 24))
        self.curso = QLabel(ModificarAsignatura)
        self.curso.setObjectName(u"curso")
        self.curso.setGeometry(QRect(380, 310, 31, 16))
        self.nombreText = QLineEdit(ModificarAsignatura)
        self.nombreText.setObjectName(u"nombreText")
        self.nombreText.setGeometry(QRect(476, 250, 132, 21))
        self.codigo = QLabel(ModificarAsignatura)
        self.codigo.setObjectName(u"codigo")
        self.codigo.setGeometry(QRect(380, 223, 39, 16))
        self.numAlumnos = QLabel(ModificarAsignatura)
        self.numAlumnos.setObjectName(u"numAlumnos")
        self.numAlumnos.setGeometry(QRect(380, 277, 101, 16))
        self.cursoText = QLineEdit(ModificarAsignatura)
        self.cursoText.setObjectName(u"cursoText")
        self.cursoText.setGeometry(QRect(476, 310, 132, 21))
        self.numAlumnosText = QSpinBox(ModificarAsignatura)
        self.numAlumnosText.setObjectName(u"numAlumnosText")
        self.numAlumnosText.setGeometry(QRect(476, 277, 88, 23))
        self.codigoText = QLineEdit(ModificarAsignatura)
        self.codigoText.setObjectName(u"codigoText")
        self.codigoText.setGeometry(QRect(476, 223, 132, 21))
        self.titulacion = QLabel(ModificarAsignatura)
        self.titulacion.setObjectName(u"titulacion")
        self.titulacion.setGeometry(QRect(380, 196, 52, 16))
        self.titulacionBox = QComboBox(ModificarAsignatura)
        self.titulacionBox.setObjectName(u"titulacionBox")
        self.titulacionBox.setGeometry(QRect(476, 196, 441, 21))
        self.nombre = QLabel(ModificarAsignatura)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(380, 250, 44, 16))

        self.retranslateUi(ModificarAsignatura)

        QMetaObject.connectSlotsByName(ModificarAsignatura)
    # setupUi

    def retranslateUi(self, ModificarAsignatura):
        ModificarAsignatura.setWindowTitle(QCoreApplication.translate("ModificarAsignatura", u"ModificarAsignatura", None))
        self.Title.setText(QCoreApplication.translate("ModificarAsignatura", u"Asignatura", None))
        self.save.setText(QCoreApplication.translate("ModificarAsignatura", u"Guardar", None))
        self.add.setText(QCoreApplication.translate("ModificarAsignatura", u"A\u00f1adir", None))
        self.modify.setText(QCoreApplication.translate("ModificarAsignatura", u"Modificar", None))
        self.sup.setText(QCoreApplication.translate("ModificarAsignatura", u"Borrar", None))
        self.asignaturasHijas.setTitle(QCoreApplication.translate("ModificarAsignatura", u"Asignaturas Hijas", None))
        self.codigoHija.setText(QCoreApplication.translate("ModificarAsignatura", u"C\u00f3digo Hija", None))
        self.nombreHija.setText(QCoreApplication.translate("ModificarAsignatura", u"Nombre Hija", None))
        self.addHija.setText(QCoreApplication.translate("ModificarAsignatura", u"A\u00f1adir", None))
        self.curso.setText(QCoreApplication.translate("ModificarAsignatura", u"Curso", None))
        self.codigo.setText(QCoreApplication.translate("ModificarAsignatura", u"C\u00f3digo", None))
        self.numAlumnos.setText(QCoreApplication.translate("ModificarAsignatura", u"N\u00famero alumnos", None))
        self.titulacion.setText(QCoreApplication.translate("ModificarAsignatura", u"Titulaci\u00f3n", None))
        self.nombre.setText(QCoreApplication.translate("ModificarAsignatura", u"Nombre", None))
    # retranslateUi

