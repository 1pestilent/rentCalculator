# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addincome.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import gui.res

class Ui_AddIncome(object):
    def setupUi(self, AddIncome):
        if not AddIncome.objectName():
            AddIncome.setObjectName(u"AddIncome")
        AddIncome.resize(400, 220)
        AddIncome.setMinimumSize(QSize(400, 220))
        AddIncome.setMaximumSize(QSize(400, 220))
        self.centralwidget = QWidget(AddIncome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u".QFrame{\n"
"	background-color: rgb(255, 255, 255);}\n"
".QLineEdit{\n"
"font-size: 26px; \n"
"font-family: Bahnschrift;\n"
"height: 35px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"margin-bottom:10px;\n"
"}\n"
".QPushButton { background-color: rgba(0, 205, 165, 255); color: white; font-size: 22px; font-family: Bahnschrift;font-weight:bold; border-radius:20px}\n"
".QPushButton:hover { background-color:  rgba(0, 205, 165, 205);}\n"
".QPushButton:pressed {background-color: rgba(0, 205, 165, 105);}\n"
".QLabel{\n"
"	font-size: 26px; \n"
"	font-family: Bahnschrift;\n"
"    text-align: center;\n"
"}\n"
"QComboBox{\n"
"	font-size: 26px; \n"
"	font-family: Bahnschrift;\n"
"	height: 35px;\n"
"	border: 1px solid black;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border:none;\n"
"	background-color:none;\n"
"    }\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"	image: url(:/black-icons/icons/menu.svg);\n"
"	paddin"
                        "g-top:5px;\n"
"	padding-right:10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cars_combobox = QComboBox(self.frame)
        self.cars_combobox.setObjectName(u"cars_combobox")

        self.verticalLayout_4.addWidget(self.cars_combobox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.income_income_label = QLabel(self.frame)
        self.income_income_label.setObjectName(u"income_income_label")

        self.verticalLayout_3.addWidget(self.income_income_label)

        self.income_income_edit = QLineEdit(self.frame)
        self.income_income_edit.setObjectName(u"income_income_edit")
        self.income_income_edit.setMinimumSize(QSize(260, 0))

        self.verticalLayout_3.addWidget(self.income_income_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.time_income_label = QLabel(self.frame)
        self.time_income_label.setObjectName(u"time_income_label")

        self.verticalLayout_2.addWidget(self.time_income_label)

        self.time_income_edit = QLineEdit(self.frame)
        self.time_income_edit.setObjectName(u"time_income_edit")
        self.time_income_edit.setMaximumSize(QSize(100, 16777215))
        self.time_income_edit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.time_income_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.add_income_button = QPushButton(self.frame)
        self.add_income_button.setObjectName(u"add_income_button")
        self.add_income_button.setMinimumSize(QSize(0, 50))
        self.add_income_button.setStyleSheet(u"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;")

        self.horizontalLayout.addWidget(self.add_income_button)

        self.cancel_income_button = QPushButton(self.frame)
        self.cancel_income_button.setObjectName(u"cancel_income_button")
        self.cancel_income_button.setMinimumSize(QSize(0, 50))
        self.cancel_income_button.setStyleSheet(u"border-bottom-left-radius: 0px;\n"
"border-top-left-radius: 0px;")

        self.horizontalLayout.addWidget(self.cancel_income_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        AddIncome.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddIncome)

        self.cars_combobox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(AddIncome)
    # setupUi

    def retranslateUi(self, AddIncome):
        AddIncome.setWindowTitle(QCoreApplication.translate("AddIncome", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u0431\u044b\u043b\u0438", None))
        self.income_income_label.setText(QCoreApplication.translate("AddIncome", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c:", None))
        self.time_income_label.setText(QCoreApplication.translate("AddIncome", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.add_income_button.setText(QCoreApplication.translate("AddIncome", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancel_income_button.setText(QCoreApplication.translate("AddIncome", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

