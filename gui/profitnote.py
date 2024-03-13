# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profitnote.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import gui.res

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 50)
        Frame.setMinimumSize(QSize(0, 40))
        Frame.setMaximumSize(QSize(16777215, 50))
        Frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius:15px;\n"
"	border: 1px solid rgb(180,0,63);\n"
"}\n"
"QLabel{	\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 12px;\n"
"	border:none;\n"
"	font-family: Impact;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(50, 0))
        self.frame.setMaximumSize(QSize(50, 16777215))
        self.frame.setStyleSheet(u"border:none;\n"
"border-radius:0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.time = QLabel(self.frame)
        self.time.setObjectName(u"time")
        self.time.setMinimumSize(QSize(50, 0))
        self.time.setStyleSheet(u"font-size: 14px;\n"
"color: rgb(229, 229, 229)\n"
"")

        self.verticalLayout.addWidget(self.time)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QLabel{\n"
"	padding-right:60px;\n"
"	font-size: 16px;\n"
"\n"
"}\n"
"QFrame{\n"
"	border:none;\n"
"	border-radius:0px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 2, 9, 4)
        self.profit = QLabel(self.frame_2)
        self.profit.setObjectName(u"profit")
        self.profit.setMinimumSize(QSize(0, 20))
        self.profit.setStyleSheet(u"")
        self.profit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.profit)

        self.profit_name = QLabel(self.frame_2)
        self.profit_name.setObjectName(u"profit_name")
        self.profit_name.setStyleSheet(u"")
        self.profit_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.profit_name)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.time.setText(QCoreApplication.translate("Frame", u"33:33:33", None))
        self.profit.setText(QCoreApplication.translate("Frame", u"\u0445\u0443\u0440\u0438\u043a\u0438", None))
        self.profit_name.setText(QCoreApplication.translate("Frame", u"130.000$", None))
    # retranslateUi

