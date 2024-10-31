# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyAulaDPgHwX.ui'
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
    QSizePolicy, QSpinBox, QSplitter, QWidget)

class Ui_ModificarAula(object):
    def setupUi(self, ModificarAula):
        if not ModificarAula.objectName():
            ModificarAula.setObjectName(u"ModificarAula")
        ModificarAula.resize(707, 569)
        self.splitter = QSplitter(ModificarAula)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 20, 331, 531))
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
        self.widget = QWidget(ModificarAula)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(370, 300, 239, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add = QPushButton(self.widget)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.modify = QPushButton(self.widget)
        self.modify.setObjectName(u"modify")

        self.horizontalLayout.addWidget(self.modify)

        self.sup = QPushButton(self.widget)
        self.sup.setObjectName(u"sup")

        self.horizontalLayout.addWidget(self.sup)

        self.edificioBox = QComboBox(ModificarAula)
        self.edificioBox.setObjectName(u"edificioBox")
        self.edificioBox.setGeometry(QRect(478, 159, 151, 21))
        self.numero = QLabel(ModificarAula)
        self.numero.setObjectName(u"numero")
        self.numero.setGeometry(QRect(372, 186, 44, 16))
        self.capExamenText = QSpinBox(ModificarAula)
        self.capExamenText.setObjectName(u"capExamenText")
        self.capExamenText.setGeometry(QRect(478, 242, 71, 23))
        self.tipoText = QLineEdit(ModificarAula)
        self.tipoText.setObjectName(u"tipoText")
        self.tipoText.setGeometry(QRect(478, 271, 151, 21))
        self.capClaseText = QSpinBox(ModificarAula)
        self.capClaseText.setObjectName(u"capClaseText")
        self.capClaseText.setGeometry(QRect(478, 213, 71, 23))
        self.tipo = QLabel(ModificarAula)
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(372, 271, 24, 16))
        self.edificio = QLabel(ModificarAula)
        self.edificio.setObjectName(u"edificio")
        self.edificio.setGeometry(QRect(372, 159, 39, 16))
        self.campus = QLabel(ModificarAula)
        self.campus.setObjectName(u"campus")
        self.campus.setGeometry(QRect(372, 132, 43, 16))
        self.numeroText = QLineEdit(ModificarAula)
        self.numeroText.setObjectName(u"numeroText")
        self.numeroText.setGeometry(QRect(478, 186, 151, 21))
        self.campusBox = QComboBox(ModificarAula)
        self.campusBox.setObjectName(u"campusBox")
        self.campusBox.setGeometry(QRect(478, 132, 151, 21))
        self.capExamen = QLabel(ModificarAula)
        self.capExamen.setObjectName(u"capExamen")
        self.capExamen.setGeometry(QRect(372, 242, 100, 16))
        self.capClase = QLabel(ModificarAula)
        self.capClase.setObjectName(u"capClase")
        self.capClase.setGeometry(QRect(372, 213, 87, 16))

        self.retranslateUi(ModificarAula)

        QMetaObject.connectSlotsByName(ModificarAula)
    # setupUi

    def retranslateUi(self, ModificarAula):
        ModificarAula.setWindowTitle(QCoreApplication.translate("ModificarAula", u"ModificarAula", None))
        self.Title.setText(QCoreApplication.translate("ModificarAula", u"Aula", None))
        self.save.setText(QCoreApplication.translate("ModificarAula", u"Guardar", None))
        self.add.setText(QCoreApplication.translate("ModificarAula", u"A\u00f1adir", None))
        self.modify.setText(QCoreApplication.translate("ModificarAula", u"Modificar", None))
        self.sup.setText(QCoreApplication.translate("ModificarAula", u"Borrar", None))
        self.numero.setText(QCoreApplication.translate("ModificarAula", u"N\u00famero", None))
        self.tipo.setText(QCoreApplication.translate("ModificarAula", u"Tipo", None))
        self.edificio.setText(QCoreApplication.translate("ModificarAula", u"Edificio", None))
        self.campus.setText(QCoreApplication.translate("ModificarAula", u"Campus", None))
        self.capExamen.setText(QCoreApplication.translate("ModificarAula", u"Capacidad Examen", None))
        self.capClase.setText(QCoreApplication.translate("ModificarAula", u"Capacidad Clase", None))
    # retranslateUi

