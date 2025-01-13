# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allRestrictionExhtGCYG.ui'
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
    QSizePolicy, QWidget)

class Ui_ListaRestriccionesEx(object):
    def setupUi(self, ListaRestriccionesEx):
        if not ListaRestriccionesEx.objectName():
            ListaRestriccionesEx.setObjectName(u"ListaRestriccionesEx")
        ListaRestriccionesEx.resize(551, 476)
        self.Title = QLabel(ListaRestriccionesEx)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(40, 40, 391, 41))
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.listaRest = QListWidget(ListaRestriccionesEx)
        self.listaRest.setObjectName(u"listaRest")
        self.listaRest.setGeometry(QRect(30, 110, 491, 341))

        self.retranslateUi(ListaRestriccionesEx)

        QMetaObject.connectSlotsByName(ListaRestriccionesEx)
    # setupUi

    def retranslateUi(self, ListaRestriccionesEx):
        ListaRestriccionesEx.setWindowTitle(QCoreApplication.translate("ListaRestriccionesEx", u"ListaRestriccionesEx", None))
        self.Title.setText(QCoreApplication.translate("ListaRestriccionesEx", u"Todas las restricciones", None))
    # retranslateUi

