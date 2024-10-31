# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyBuildingFbkNMU.ui'
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

class Ui_ModificarEdificio(object):
    def setupUi(self, ModificarEdificio):
        if not ModificarEdificio.objectName():
            ModificarEdificio.setObjectName(u"ModificarEdificio")
        ModificarEdificio.resize(594, 501)
        self.splitter = QSplitter(ModificarEdificio)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 20, 256, 461))
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
        self.widget = QWidget(ModificarEdificio)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(300, 110, 239, 80))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.campus = QLabel(self.widget)
        self.campus.setObjectName(u"campus")

        self.gridLayout.addWidget(self.campus, 0, 0, 1, 1)

        self.nombre = QLabel(self.widget)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 1, 0, 1, 1)

        self.add = QPushButton(self.widget)
        self.add.setObjectName(u"add")

        self.gridLayout.addWidget(self.add, 2, 0, 1, 2)

        self.modify = QPushButton(self.widget)
        self.modify.setObjectName(u"modify")

        self.gridLayout.addWidget(self.modify, 2, 2, 1, 1)

        self.sup = QPushButton(self.widget)
        self.sup.setObjectName(u"sup")

        self.gridLayout.addWidget(self.sup, 2, 3, 1, 1)

        self.nombreText = QLineEdit(self.widget)
        self.nombreText.setObjectName(u"nombreText")

        self.gridLayout.addWidget(self.nombreText, 1, 2, 1, 2)

        self.campusBox = QComboBox(self.widget)
        self.campusBox.setObjectName(u"campusBox")

        self.gridLayout.addWidget(self.campusBox, 0, 2, 1, 2)


        self.retranslateUi(ModificarEdificio)

        QMetaObject.connectSlotsByName(ModificarEdificio)
    # setupUi

    def retranslateUi(self, ModificarEdificio):
        ModificarEdificio.setWindowTitle(QCoreApplication.translate("ModificarEdificio", u"ModificarName", None))
        self.Title.setText(QCoreApplication.translate("ModificarEdificio", u"Edificios", None))
        self.save.setText(QCoreApplication.translate("ModificarEdificio", u"Guardar", None))
        self.campus.setText(QCoreApplication.translate("ModificarEdificio", u"Campus", None))
        self.nombre.setText(QCoreApplication.translate("ModificarEdificio", u"Nombre", None))
        self.add.setText(QCoreApplication.translate("ModificarEdificio", u"A\u00f1adir", None))
        self.modify.setText(QCoreApplication.translate("ModificarEdificio", u"Modificar", None))
        self.sup.setText(QCoreApplication.translate("ModificarEdificio", u"Borrar", None))
    # retranslateUi

