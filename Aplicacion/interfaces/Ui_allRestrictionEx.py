# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allRestrictionExZiyrry.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSplitter, QWidget)

class Ui_ListaRestriccionesEx(object):
    def setupUi(self, ListaRestriccionesEx):
        if not ListaRestriccionesEx.objectName():
            ListaRestriccionesEx.setObjectName(u"ListaRestriccionesEx")
        ListaRestriccionesEx.resize(646, 476)
        self.Title = QLabel(ListaRestriccionesEx)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(40, 40, 391, 41))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.listaRest = QListWidget(ListaRestriccionesEx)
        self.listaRest.setObjectName(u"listaRest")
        self.listaRest.setGeometry(QRect(30, 110, 491, 341))
        self.splitter = QSplitter(ListaRestriccionesEx)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(540, 110, 75, 82))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.activar = QPushButton(self.splitter)
        self.activar.setObjectName(u"activar")
        self.splitter.addWidget(self.activar)
        self.desactivar = QPushButton(self.splitter)
        self.desactivar.setObjectName(u"desactivar")
        self.splitter.addWidget(self.desactivar)
        self.modificar = QPushButton(self.splitter)
        self.modificar.setObjectName(u"modificar")
        self.splitter.addWidget(self.modificar)

        self.retranslateUi(ListaRestriccionesEx)

        QMetaObject.connectSlotsByName(ListaRestriccionesEx)
    # setupUi

    def retranslateUi(self, ListaRestriccionesEx):
        ListaRestriccionesEx.setWindowTitle(QCoreApplication.translate("ListaRestriccionesEx", u"ListaRestriccionesEx", None))
        self.Title.setText(QCoreApplication.translate("ListaRestriccionesEx", u"Todas las restricciones", None))
        self.activar.setText(QCoreApplication.translate("ListaRestriccionesEx", u"Activar", None))
        self.desactivar.setText(QCoreApplication.translate("ListaRestriccionesEx", u"Desactivar", None))
        self.modificar.setText(QCoreApplication.translate("ListaRestriccionesEx", u"Modificar", None))
    # retranslateUi

