# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcar.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import gui.res

class Ui_AddCar(object):
    def setupUi(self, AddCar):
        if not AddCar.objectName():
            AddCar.setObjectName(u"AddCar")
        AddCar.resize(400, 200)
        AddCar.setMinimumSize(QSize(400, 200))
        AddCar.setMaximumSize(QSize(400, 200))
        icon = QIcon()
        icon.addFile(u":/logo/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        AddCar.setWindowIcon(icon)
        AddCar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(AddCar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u".QPushButton { background-color: rgba(0, 205, 165, 255); color: white; font-size: 22px; font-family: Bahnschrift;font-weight:bold; border-radius:20px}\n"
".QPushButton:hover { background-color:  rgba(0, 205, 165, 205);}\n"
".QPushButton:pressed {background-color: rgba(0, 205, 165, 105);}\n"
".QLabel{\n"
"	font-size: 26px; \n"
"	font-family: Bahnschrift;\n"
"    text-align: center;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.car_name_edit_2 = QLabel(self.frame)
        self.car_name_edit_2.setObjectName(u"car_name_edit_2")

        self.verticalLayout.addWidget(self.car_name_edit_2)

        self.car_name_edit = QLineEdit(self.frame)
        self.car_name_edit.setObjectName(u"car_name_edit")
        self.car_name_edit.setStyleSheet(u"font-size: 26px; \n"
"font-family: Bahnschrift;\n"
"height: 35px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"margin-bottom:10px;")

        self.verticalLayout.addWidget(self.car_name_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.car_name_add_button = QPushButton(self.frame)
        self.car_name_add_button.setObjectName(u"car_name_add_button")
        self.car_name_add_button.setMinimumSize(QSize(0, 50))
        self.car_name_add_button.setStyleSheet(u"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;")

        self.horizontalLayout.addWidget(self.car_name_add_button)

        self.car_name_cancel_button = QPushButton(self.frame)
        self.car_name_cancel_button.setObjectName(u"car_name_cancel_button")
        self.car_name_cancel_button.setMinimumSize(QSize(0, 50))
        self.car_name_cancel_button.setStyleSheet(u"border-bottom-left-radius: 0px;\n"
"border-top-left-radius: 0px;")

        self.horizontalLayout.addWidget(self.car_name_cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        AddCar.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddCar)

        QMetaObject.connectSlotsByName(AddCar)
    # setupUi

    def retranslateUi(self, AddCar):
        AddCar.setWindowTitle(QCoreApplication.translate("AddCar", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u0448\u0438\u043d\u044b", None))
        self.car_name_edit_2.setText(QCoreApplication.translate("AddCar", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0448\u0438\u043d\u044b:", None))
        self.car_name_add_button.setText(QCoreApplication.translate("AddCar", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.car_name_cancel_button.setText(QCoreApplication.translate("AddCar", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

