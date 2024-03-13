# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import gui.res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 600)
        MainWindow.setMinimumSize(QSize(1100, 600))
        MainWindow.setMaximumSize(QSize(1100, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 40))
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(40, 40, 40)\n"
"}\n"
"QLabel{\n"
"	color: rgb(180,0,63);\n"
"	font-family:Impact;\n"
"	font-size:18px;\n"
"}\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 0, 5, 0)
        self.logo_label = QLabel(self.header)
        self.logo_label.setObjectName(u"logo_label")

        self.horizontalLayout_2.addWidget(self.logo_label)

        self.horizontalSpacer = QSpacerItem(919, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minimize_button = QPushButton(self.header)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(30, 30))
        self.minimize_button.setStyleSheet(u"border-top-left-radius: 4px;\n"
"border-bottom-left-radius: 4px;")
        icon = QIcon()
        icon.addFile(u":/icon-color/icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.header)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(30, 30))
        self.close_button.setStyleSheet(u"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;")
        icon1 = QIcon()
        icon1.addFile(u":/icon-color/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.close_button)


        self.verticalLayout.addWidget(self.header)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menubar = QFrame(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setMinimumSize(QSize(70, 0))
        self.menubar.setMaximumSize(QSize(70, 16777215))
        self.menubar.setStyleSheet(u"QPushButton:checked{\n"
"	color: white;\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"	color: white;\n"
"	font-family: Impact;\n"
"	font-size: 18px;\n"
"	border:none;\n"
"	text-align: left;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	background-color: rgb(25, 25, 25);\n"
"	padding-left:12px;\n"
"}\n"
"QFrame{\n"
"background-color: rgb(25, 25, 25);\n"
"}")
        self.menubar.setFrameShape(QFrame.StyledPanel)
        self.menubar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menubar)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 5)
        self.resale_button = QPushButton(self.menubar)
        self.resale_button.setObjectName(u"resale_button")
        self.resale_button.setMinimumSize(QSize(100, 45))
        icon2 = QIcon()
        icon2.addFile(u":/icon-color/icons/money.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resale_button.setIcon(icon2)
        self.resale_button.setIconSize(QSize(40, 40))
        self.resale_button.setCheckable(True)
        self.resale_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.resale_button)

        self.cars_button = QPushButton(self.menubar)
        self.cars_button.setObjectName(u"cars_button")
        self.cars_button.setMinimumSize(QSize(100, 45))
        icon3 = QIcon()
        icon3.addFile(u":/icon-color/icons/cars.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cars_button.setIcon(icon3)
        self.cars_button.setIconSize(QSize(40, 40))
        self.cars_button.setCheckable(True)
        self.cars_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.cars_button)

        self.analyse_button = QPushButton(self.menubar)
        self.analyse_button.setObjectName(u"analyse_button")
        self.analyse_button.setMinimumSize(QSize(100, 45))
        icon4 = QIcon()
        icon4.addFile(u":/icon-color/icons/analysis.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analyse_button.setIcon(icon4)
        self.analyse_button.setIconSize(QSize(40, 40))
        self.analyse_button.setCheckable(True)
        self.analyse_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.analyse_button)

        self.settings_button = QPushButton(self.menubar)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(100, 45))
        icon5 = QIcon()
        icon5.addFile(u":/icon-color/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon5)
        self.settings_button.setIconSize(QSize(40, 40))
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.settings_button)

        self.verticalSpacer = QSpacerItem(20, 167, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.by_label = QLabel(self.menubar)
        self.by_label.setObjectName(u"by_label")
        self.by_label.setStyleSheet(u"color: rgb(111, 111, 111);")
        self.by_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.by_label)

        self.me_label = QLabel(self.menubar)
        self.me_label.setObjectName(u"me_label")
        self.me_label.setStyleSheet(u"color: rgb(111, 111, 111);")
        self.me_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.me_label)

        self.version_label = QLabel(self.menubar)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setStyleSheet(u"color: rgb(111, 111, 111);")
        self.version_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.version_label)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.menubar)

        self.workplace = QFrame(self.centralwidget)
        self.workplace.setObjectName(u"workplace")
        self.workplace.setStyleSheet(u"border:none;")
        self.workplace.setFrameShape(QFrame.StyledPanel)
        self.workplace.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.workplace)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.workplace)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(70, 70, 70);")
        self.resale_page = QWidget()
        self.resale_page.setObjectName(u"resale_page")
        self.frame_2 = QFrame(self.resale_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 140, 501, 211))
        self.frame_2.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	font-family: impact;\n"
"	height:40px;\n"
"	padding-left: 10px;\n"
"}\n"
".QPushButton {\n"
"	background-color: rgba(180,0,63,255); \n"
"	color: white; \n"
"	font-size: 18px;\n"
"	font-family: Impact;\n"
"	border-radius:10px;\n"
"}\n"
".QPushButton:hover {\n"
"	background-color:  rgba(180,0,63,225);\n"
"}\n"
".QPushButton:pressed {\n"
"background-color: rgba(180,0,63,155);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: impact;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.resale_profit_edit = QLineEdit(self.frame_2)
        self.resale_profit_edit.setObjectName(u"resale_profit_edit")

        self.verticalLayout_6.addWidget(self.resale_profit_edit)

        self.resale_name_edit = QLineEdit(self.frame_2)
        self.resale_name_edit.setObjectName(u"resale_name_edit")

        self.verticalLayout_6.addWidget(self.resale_name_edit)

        self.resale_add_button = QPushButton(self.frame_2)
        self.resale_add_button.setObjectName(u"resale_add_button")
        self.resale_add_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.resale_add_button)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 8, -1, 8)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.resale_profit_label = QLabel(self.frame_2)
        self.resale_profit_label.setObjectName(u"resale_profit_label")
        self.resale_profit_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.resale_profit_label)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.resale_new_button = QPushButton(self.frame_2)
        self.resale_new_button.setObjectName(u"resale_new_button")
        self.resale_new_button.setMinimumSize(QSize(100, 40))
        self.resale_new_button.setMaximumSize(QSize(100, 16777215))
        self.resale_new_button.setStyleSheet(u"font-size:14px;")

        self.horizontalLayout_4.addWidget(self.resale_new_button)

        self.resale_reset_button = QPushButton(self.frame_2)
        self.resale_reset_button.setObjectName(u"resale_reset_button")
        self.resale_reset_button.setMinimumSize(QSize(100, 40))
        self.resale_reset_button.setMaximumSize(QSize(100, 40))
        self.resale_reset_button.setStyleSheet(u"font-size:14px;")

        self.horizontalLayout_4.addWidget(self.resale_reset_button)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 8, -1, 8)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.resale_total_profit_label = QLabel(self.frame_2)
        self.resale_total_profit_label.setObjectName(u"resale_total_profit_label")
        self.resale_total_profit_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.resale_total_profit_label)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.resale_story_frame = QFrame(self.resale_page)
        self.resale_story_frame.setObjectName(u"resale_story_frame")
        self.resale_story_frame.setGeometry(QRect(580, 20, 431, 521))
        self.resale_story_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}")
        self.resale_story_frame.setFrameShape(QFrame.StyledPanel)
        self.resale_story_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.resale_story_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.resale_story_layout = QVBoxLayout()
        self.resale_story_layout.setSpacing(10)
        self.resale_story_layout.setObjectName(u"resale_story_layout")

        self.verticalLayout_9.addLayout(self.resale_story_layout)

        self.stackedWidget.addWidget(self.resale_page)
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.frame = QFrame(self.cars_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 60, 411, 211))
        self.frame.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	font-family: impact;\n"
"	height:40px;\n"
"}\n"
".QPushButton {\n"
"	background-color: rgba(180,0,63,255); \n"
"	color: white; \n"
"	font-size: 18px;\n"
"	font-family: Impact;\n"
"	border-radius:10px;\n"
"}\n"
".QPushButton:hover {\n"
"	background-color:  rgba(180,0,63,225);\n"
"}\n"
".QPushButton:pressed {\n"
"background-color: rgba(180,0,63,155);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: impact;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cars_car_combo = QComboBox(self.frame)
        self.cars_car_combo.setObjectName(u"cars_car_combo")
        self.cars_car_combo.setMinimumSize(QSize(0, 40))
        self.cars_car_combo.setStyleSheet(u"QComboBox{\n"
"	font-size: 20px; \n"
"	font-family: Impact;\n"
"	height: 35px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: white;	\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"	color: white;\n"
"    selection-background-color: rgb(100,100,100);\n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: 1px solid white;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border:none;\n"
"	background-color:none;\n"
"    }\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"	image: url(:/icon-color/icons/menu.svg);\n"
"	padding-top:7px;\n"
"	padding-right:10px;\n"
"}")

        self.verticalLayout_7.addWidget(self.cars_car_combo)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(310, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 3))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.label_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cars_profit_edit = QLineEdit(self.frame)
        self.cars_profit_edit.setObjectName(u"cars_profit_edit")
        self.cars_profit_edit.setMinimumSize(QSize(300, 40))
        self.cars_profit_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.cars_profit_edit)

        self.cars_hours_edit = QLineEdit(self.frame)
        self.cars_hours_edit.setObjectName(u"cars_hours_edit")
        self.cars_hours_edit.setMinimumSize(QSize(0, 40))
        self.cars_hours_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.cars_hours_edit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.cars_addincome_button = QPushButton(self.frame)
        self.cars_addincome_button.setObjectName(u"cars_addincome_button")
        self.cars_addincome_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.cars_addincome_button)

        self.frame_3 = QFrame(self.cars_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(70, 330, 411, 151))
        self.frame_3.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 85, 85);\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	font-family: impact;\n"
"	height:40px;\n"
"}\n"
".QPushButton {\n"
"	background-color: rgba(180,0,63,255); \n"
"	color: white; \n"
"	font-size: 18px;\n"
"	font-family: Impact;\n"
"	border-radius:10px;\n"
"}\n"
".QPushButton:hover {\n"
"	background-color:  rgba(180,0,63,225);\n"
"}\n"
".QPushButton:pressed {\n"
"background-color: rgba(180,0,63,155);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: impact;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.cars_carname_edit = QLineEdit(self.frame_3)
        self.cars_carname_edit.setObjectName(u"cars_carname_edit")

        self.verticalLayout_10.addWidget(self.cars_carname_edit)

        self.cars_addcar_button = QPushButton(self.frame_3)
        self.cars_addcar_button.setObjectName(u"cars_addcar_button")
        self.cars_addcar_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout_10.addWidget(self.cars_addcar_button)

        self.cars_story_frame = QFrame(self.cars_page)
        self.cars_story_frame.setObjectName(u"cars_story_frame")
        self.cars_story_frame.setGeometry(QRect(580, 20, 431, 521))
        self.cars_story_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}")
        self.cars_story_frame.setFrameShape(QFrame.StyledPanel)
        self.cars_story_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.cars_story_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cars_story_layout = QVBoxLayout()
        self.cars_story_layout.setObjectName(u"cars_story_layout")

        self.verticalLayout_12.addLayout(self.cars_story_layout)

        self.stackedWidget.addWidget(self.cars_page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.workplace)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close_button.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"rentCalculator", None))
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"rentCalculator", None))
        self.minimize_button.setText("")
        self.close_button.setText("")
        self.resale_button.setText("")
        self.cars_button.setText("")
        self.analyse_button.setText("")
        self.settings_button.setText("")
        self.by_label.setText(QCoreApplication.translate("MainWindow", u"by", None))
        self.me_label.setText(QCoreApplication.translate("MainWindow", u"xirksome", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"v0.1", None))
        self.resale_add_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u043e\u043a \u0437\u0430 \u0441\u0435\u0440\u0438\u044e:", None))
        self.resale_profit_label.setText(QCoreApplication.translate("MainWindow", u"0$", None))
        self.resale_new_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0435\u0440\u0438\u044f", None))
        self.resale_reset_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e \u0432\u0441\u0435\u0433\u043e:", None))
        self.resale_total_profit_label.setText(QCoreApplication.translate("MainWindow", u"0$", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.cars_addincome_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0448\u0438\u043d\u044b:", None))
        self.cars_addcar_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
    # retranslateUi

