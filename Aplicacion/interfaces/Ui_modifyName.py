# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyNamePFCPEH.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSplitter, QWidget)

class Ui_ModificarName(object):
    def setupUi(self, ModificarName):
        if not ModificarName.objectName():
            ModificarName.setObjectName(u"ModificarName")
        ModificarName.resize(594, 501)
        self.splitter = QSplitter(ModificarName)
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
        self.layoutWidget = QWidget(ModificarName)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(300, 120, 265, 53))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nombre = QLabel(self.layoutWidget)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 0, 1, 1)

        self.add = QPushButton(self.layoutWidget)
        self.add.setObjectName(u"add")

        self.gridLayout.addWidget(self.add, 1, 0, 1, 1)

        self.modify = QPushButton(self.layoutWidget)
        self.modify.setObjectName(u"modify")

        self.gridLayout.addWidget(self.modify, 1, 1, 1, 1)

        self.sup = QPushButton(self.layoutWidget)
        self.sup.setObjectName(u"sup")

        self.gridLayout.addWidget(self.sup, 1, 2, 1, 1)

        self.nombreText = QLineEdit(self.layoutWidget)
        self.nombreText.setObjectName(u"nombreText")

        self.gridLayout.addWidget(self.nombreText, 0, 1, 1, 2)


        self.retranslateUi(ModificarName)

        QMetaObject.connectSlotsByName(ModificarName)
    # setupUi

    def retranslateUi(self, ModificarName):
        ModificarName.setWindowTitle(QCoreApplication.translate("ModificarName", u"ModificarName", None))
        self.Title.setText(QCoreApplication.translate("ModificarName", u"TextLabel", None))
        self.save.setText(QCoreApplication.translate("ModificarName", u"Guardar", None))
        self.nombre.setText(QCoreApplication.translate("ModificarName", u"Nombre", None))
        self.add.setText(QCoreApplication.translate("ModificarName", u"A\u00f1adir", None))
        self.modify.setText(QCoreApplication.translate("ModificarName", u"Modificar", None))
        self.sup.setText(QCoreApplication.translate("ModificarName", u"Borrar", None))
    # retranslateUi

