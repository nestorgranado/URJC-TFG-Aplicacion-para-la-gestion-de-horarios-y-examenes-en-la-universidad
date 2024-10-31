# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyTitulationbKpjAa.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSplitter, QWidget)

class Ui_ModificarTitulacion(object):
    def setupUi(self, ModificarTitulacion):
        if not ModificarTitulacion.objectName():
            ModificarTitulacion.setObjectName(u"ModificarTitulacion")
        ModificarTitulacion.resize(707, 569)
        self.splitter = QSplitter(ModificarTitulacion)
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
        self.layoutWidget = QWidget(ModificarTitulacion)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(370, 130, 321, 134))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nombre = QLabel(self.layoutWidget)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 3, 0, 1, 1)

        self.escuela = QLabel(self.layoutWidget)
        self.escuela.setObjectName(u"escuela")

        self.gridLayout.addWidget(self.escuela, 0, 0, 1, 1)

        self.codigo = QLabel(self.layoutWidget)
        self.codigo.setObjectName(u"codigo")

        self.gridLayout.addWidget(self.codigo, 2, 0, 1, 1)

        self.campus = QLabel(self.layoutWidget)
        self.campus.setObjectName(u"campus")

        self.gridLayout.addWidget(self.campus, 1, 0, 1, 1)

        self.nombreText = QLineEdit(self.layoutWidget)
        self.nombreText.setObjectName(u"nombreText")

        self.gridLayout.addWidget(self.nombreText, 3, 1, 1, 3)

        self.codigoText = QLineEdit(self.layoutWidget)
        self.codigoText.setObjectName(u"codigoText")

        self.gridLayout.addWidget(self.codigoText, 2, 1, 1, 2)

        self.campusText = QLineEdit(self.layoutWidget)
        self.campusText.setObjectName(u"campusText")

        self.gridLayout.addWidget(self.campusText, 1, 1, 1, 2)

        self.escuelaBox = QComboBox(self.layoutWidget)
        self.escuelaBox.setObjectName(u"escuelaBox")

        self.gridLayout.addWidget(self.escuelaBox, 0, 1, 1, 2)

        self.add = QPushButton(self.layoutWidget)
        self.add.setObjectName(u"add")

        self.gridLayout.addWidget(self.add, 4, 0, 1, 1)

        self.modify = QPushButton(self.layoutWidget)
        self.modify.setObjectName(u"modify")

        self.gridLayout.addWidget(self.modify, 4, 1, 1, 1)

        self.sup = QPushButton(self.layoutWidget)
        self.sup.setObjectName(u"sup")

        self.gridLayout.addWidget(self.sup, 4, 2, 1, 1)


        self.retranslateUi(ModificarTitulacion)

        QMetaObject.connectSlotsByName(ModificarTitulacion)
    # setupUi

    def retranslateUi(self, ModificarTitulacion):
        ModificarTitulacion.setWindowTitle(QCoreApplication.translate("ModificarTitulacion", u"ModificarTitulacion", None))
        self.Title.setText(QCoreApplication.translate("ModificarTitulacion", u"Titulaci\u00f3n", None))
        self.save.setText(QCoreApplication.translate("ModificarTitulacion", u"Guardar", None))
        self.nombre.setText(QCoreApplication.translate("ModificarTitulacion", u"Nombre", None))
        self.escuela.setText(QCoreApplication.translate("ModificarTitulacion", u"Escuela", None))
        self.codigo.setText(QCoreApplication.translate("ModificarTitulacion", u"C\u00f3digo", None))
        self.campus.setText(QCoreApplication.translate("ModificarTitulacion", u"Campus", None))
        self.add.setText(QCoreApplication.translate("ModificarTitulacion", u"A\u00f1adir", None))
        self.modify.setText(QCoreApplication.translate("ModificarTitulacion", u"Modificar", None))
        self.sup.setText(QCoreApplication.translate("ModificarTitulacion", u"Borrar", None))
    # retranslateUi

