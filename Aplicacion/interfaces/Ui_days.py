# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daysSLmaVu.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_dias(object):
    def setupUi(self, dias):
        if not dias.objectName():
            dias.setObjectName(u"dias")
        dias.resize(366, 501)
        self.title = QLabel(dias)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 10, 281, 71))
        font = QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.listaDias = QListWidget(dias)
        self.listaDias.setObjectName(u"listaDias")
        self.listaDias.setGeometry(QRect(30, 130, 256, 311))
        self.save = QPushButton(dias)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 450, 75, 24))
        self.widget = QWidget(dias)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 90, 164, 25))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.numDias = QLabel(self.widget)
        self.numDias.setObjectName(u"numDias")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.numDias)

        self.numDiasText = QSpinBox(self.widget)
        self.numDiasText.setObjectName(u"numDiasText")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numDiasText)


        self.retranslateUi(dias)

        QMetaObject.connectSlotsByName(dias)
    # setupUi

    def retranslateUi(self, dias):
        dias.setWindowTitle(QCoreApplication.translate("dias", u"dias", None))
        self.title.setText(QCoreApplication.translate("dias", u"D\u00edas por Semana", None))
        self.save.setText(QCoreApplication.translate("dias", u"Guardar", None))
        self.numDias.setText(QCoreApplication.translate("dias", u"N\u00famero de dias", None))
    # retranslateUi

