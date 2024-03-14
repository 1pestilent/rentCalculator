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
        self.analyse_page = QWidget()
        self.analyse_page.setObjectName(u"analyse_page")
        self.verticalLayout_8 = QVBoxLayout(self.analyse_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.analyse_header = QFrame(self.analyse_page)
        self.analyse_header.setObjectName(u"analyse_header")
        self.analyse_header.setMinimumSize(QSize(0, 60))
        self.analyse_header.setMaximumSize(QSize(16777215, 60))
        self.analyse_header.setStyleSheet(u"QPushButton{	\n"
"	color: rgb(180,0,63);\n"
"	font-family:Impact;\n"
"	font-size:22px;\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(55, 55, 55);\n"
"}")
        self.analyse_header.setFrameShape(QFrame.StyledPanel)
        self.analyse_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.analyse_header)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.analyse_resale_button = QPushButton(self.analyse_header)
        self.analyse_resale_button.setObjectName(u"analyse_resale_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyse_resale_button.sizePolicy().hasHeightForWidth())
        self.analyse_resale_button.setSizePolicy(sizePolicy)
        self.analyse_resale_button.setStyleSheet(u"border-left: 1px solid rgb(180,0,63);")
        self.analyse_resale_button.setIcon(icon2)
        self.analyse_resale_button.setIconSize(QSize(40, 40))
        self.analyse_resale_button.setCheckable(True)
        self.analyse_resale_button.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.analyse_resale_button)

        self.analyse_cars_button = QPushButton(self.analyse_header)
        self.analyse_cars_button.setObjectName(u"analyse_cars_button")
        sizePolicy.setHeightForWidth(self.analyse_cars_button.sizePolicy().hasHeightForWidth())
        self.analyse_cars_button.setSizePolicy(sizePolicy)
        self.analyse_cars_button.setIcon(icon3)
        self.analyse_cars_button.setIconSize(QSize(40, 40))
        self.analyse_cars_button.setCheckable(True)
        self.analyse_cars_button.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.analyse_cars_button)


        self.verticalLayout_8.addWidget(self.analyse_header)

        self.frame_4 = QFrame(self.analyse_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.analyse_resale_page = QWidget()
        self.analyse_resale_page.setObjectName(u"analyse_resale_page")
        self.frame_6 = QFrame(self.analyse_resale_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(50, 30, 931, 441))
        self.frame_6.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-family:Impact;\n"
"	font-size:16px;\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setSpacing(30)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(30)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"border:none;")

        self.verticalLayout_11.addWidget(self.label_4)

        self.analyse_resale_income_for_day = QLabel(self.frame_7)
        self.analyse_resale_income_for_day.setObjectName(u"analyse_resale_income_for_day")
        self.analyse_resale_income_for_day.setStyleSheet(u"font-size: 40px;\n"
"border:none;")

        self.verticalLayout_11.addWidget(self.analyse_resale_income_for_day)

        self.line_4 = QFrame(self.frame_7)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_4)

        self.analyse_resale_quantity_for_day = QLabel(self.frame_7)
        self.analyse_resale_quantity_for_day.setObjectName(u"analyse_resale_quantity_for_day")
        self.analyse_resale_quantity_for_day.setStyleSheet(u"border:none;")

        self.verticalLayout_11.addWidget(self.analyse_resale_quantity_for_day)

        self.line_10 = QFrame(self.frame_7)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_10)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"border:none;")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_25)

        self.analyse_resale_avgprice_for_day = QLabel(self.frame_7)
        self.analyse_resale_avgprice_for_day.setObjectName(u"analyse_resale_avgprice_for_day")
        self.analyse_resale_avgprice_for_day.setStyleSheet(u"border:none;")

        self.verticalLayout_11.addWidget(self.analyse_resale_avgprice_for_day)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border:none;")

        self.verticalLayout_14.addWidget(self.label_8)

        self.analyse_resale_income_for_week = QLabel(self.frame_8)
        self.analyse_resale_income_for_week.setObjectName(u"analyse_resale_income_for_week")
        self.analyse_resale_income_for_week.setStyleSheet(u"font-size: 40px;\n"
"border:none;")

        self.verticalLayout_14.addWidget(self.analyse_resale_income_for_week)

        self.line_5 = QFrame(self.frame_8)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_5)

        self.analyse_resale_quantity_for_week = QLabel(self.frame_8)
        self.analyse_resale_quantity_for_week.setObjectName(u"analyse_resale_quantity_for_week")
        self.analyse_resale_quantity_for_week.setStyleSheet(u"border:none;")

        self.verticalLayout_14.addWidget(self.analyse_resale_quantity_for_week)

        self.line_11 = QFrame(self.frame_8)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_11)

        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border:none;")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_24)

        self.analyse_resale_avgprice_for_week = QLabel(self.frame_8)
        self.analyse_resale_avgprice_for_week.setObjectName(u"analyse_resale_avgprice_for_week")
        self.analyse_resale_avgprice_for_week.setStyleSheet(u"border:none;")

        self.verticalLayout_14.addWidget(self.analyse_resale_avgprice_for_week)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)


        self.horizontalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setSpacing(12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border:none;")

        self.verticalLayout_13.addWidget(self.label_10)

        self.analyse_resale_income_for_month = QLabel(self.frame_9)
        self.analyse_resale_income_for_month.setObjectName(u"analyse_resale_income_for_month")
        self.analyse_resale_income_for_month.setStyleSheet(u"font-size: 40px;\n"
"border:none;")

        self.verticalLayout_13.addWidget(self.analyse_resale_income_for_month)

        self.line_6 = QFrame(self.frame_9)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_6)

        self.analyse_resale_quantity_for_month = QLabel(self.frame_9)
        self.analyse_resale_quantity_for_month.setObjectName(u"analyse_resale_quantity_for_month")
        self.analyse_resale_quantity_for_month.setStyleSheet(u"border:none;")

        self.verticalLayout_13.addWidget(self.analyse_resale_quantity_for_month)

        self.line_12 = QFrame(self.frame_9)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_12)

        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"border:none;")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_23)

        self.analyse_resale_avgprice_for_month = QLabel(self.frame_9)
        self.analyse_resale_avgprice_for_month.setObjectName(u"analyse_resale_avgprice_for_month")
        self.analyse_resale_avgprice_for_month.setStyleSheet(u"border:none;")

        self.verticalLayout_13.addWidget(self.analyse_resale_avgprice_for_month)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_7)


        self.horizontalLayout_9.addWidget(self.frame_9)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.stackedWidget_2.addWidget(self.analyse_resale_page)
        self.analyse_cars_page = QWidget()
        self.analyse_cars_page.setObjectName(u"analyse_cars_page")
        self.horizontalLayout_11 = QHBoxLayout(self.analyse_cars_page)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.analyse_cars_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.analyse_car_combobox = QComboBox(self.frame_10)
        self.analyse_car_combobox.setObjectName(u"analyse_car_combobox")
        self.analyse_car_combobox.setGeometry(QRect(90, 10, 851, 61))
        self.analyse_car_combobox.setStyleSheet(u"QComboBox{\n"
"	font-size: 32px; \n"
"	font-family: Impact;\n"
"	height: 35px;\n"
"	border-radius: 15px;\n"
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
"	padding-top:12px;\n"
"	padding-right:16px;\n"
"	height: 35px;\n"
"	width: 35px;\n"
"}")
        self.analyse_cars_statsframe = QFrame(self.frame_10)
        self.analyse_cars_statsframe.setObjectName(u"analyse_cars_statsframe")
        self.analyse_cars_statsframe.setGeometry(QRect(50, 100, 931, 371))
        self.analyse_cars_statsframe.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	font-family:Impact;\n"
"	font-size:16px;\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.analyse_cars_statsframe.setFrameShape(QFrame.StyledPanel)
        self.analyse_cars_statsframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.analyse_cars_statsframe)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(30)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_12 = QFrame(self.analyse_cars_statsframe)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font-size:22px;\n"
"border:none;")

        self.verticalLayout_15.addWidget(self.label_15)

        self.analyse_cars_income_for_week = QLabel(self.frame_12)
        self.analyse_cars_income_for_week.setObjectName(u"analyse_cars_income_for_week")
        self.analyse_cars_income_for_week.setStyleSheet(u"font-size: 40px;\n"
"border:none;")

        self.verticalLayout_15.addWidget(self.analyse_cars_income_for_week)

        self.line = QFrame(self.frame_12)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line)

        self.analyse_cars_quantity_for_week = QLabel(self.frame_12)
        self.analyse_cars_quantity_for_week.setObjectName(u"analyse_cars_quantity_for_week")
        self.analyse_cars_quantity_for_week.setStyleSheet(u"border:none;")

        self.verticalLayout_15.addWidget(self.analyse_cars_quantity_for_week)

        self.line_7 = QFrame(self.frame_12)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_7)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border:none;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_17)

        self.analyse_cars_avgprice_for_week = QLabel(self.frame_12)
        self.analyse_cars_avgprice_for_week.setObjectName(u"analyse_cars_avgprice_for_week")
        self.analyse_cars_avgprice_for_week.setStyleSheet(u"border:none;")

        self.verticalLayout_15.addWidget(self.analyse_cars_avgprice_for_week)

        self.analyse_cars_avghours_for_week = QLabel(self.frame_12)
        self.analyse_cars_avghours_for_week.setObjectName(u"analyse_cars_avghours_for_week")
        self.analyse_cars_avghours_for_week.setStyleSheet(u"border:none;")

        self.verticalLayout_15.addWidget(self.analyse_cars_avghours_for_week)

        self.analyse_cars_price_per_hours_for_week = QLabel(self.frame_12)
        self.analyse_cars_price_per_hours_for_week.setObjectName(u"analyse_cars_price_per_hours_for_week")
        self.analyse_cars_price_per_hours_for_week.setStyleSheet(u"border:none;")
        self.analyse_cars_price_per_hours_for_week.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.analyse_cars_price_per_hours_for_week)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)


        self.horizontalLayout_13.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.analyse_cars_statsframe)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setSpacing(12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font-size:22px;\n"
"border:none;")

        self.verticalLayout_16.addWidget(self.label_18)

        self.analyse_cars_income_for_month = QLabel(self.frame_13)
        self.analyse_cars_income_for_month.setObjectName(u"analyse_cars_income_for_month")
        self.analyse_cars_income_for_month.setStyleSheet(u"font-size: 40px;\n"
"border:none;")

        self.verticalLayout_16.addWidget(self.analyse_cars_income_for_month)

        self.line_2 = QFrame(self.frame_13)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_2)

        self.analyse_cars_quantity_for_month = QLabel(self.frame_13)
        self.analyse_cars_quantity_for_month.setObjectName(u"analyse_cars_quantity_for_month")
        self.analyse_cars_quantity_for_month.setStyleSheet(u"border:none;")

        self.verticalLayout_16.addWidget(self.analyse_cars_quantity_for_month)

        self.line_8 = QFrame(self.frame_13)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_8)

        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border:none;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_20)

        self.analyse_cars_avgprice_for_month = QLabel(self.frame_13)
        self.analyse_cars_avgprice_for_month.setObjectName(u"analyse_cars_avgprice_for_month")
        self.analyse_cars_avgprice_for_month.setStyleSheet(u"border:none;")

        self.verticalLayout_16.addWidget(self.analyse_cars_avgprice_for_month)

        self.analyse_cars_avghours_for_month = QLabel(self.frame_13)
        self.analyse_cars_avghours_for_month.setObjectName(u"analyse_cars_avghours_for_month")
        self.analyse_cars_avghours_for_month.setStyleSheet(u"border:none;")

        self.verticalLayout_16.addWidget(self.analyse_cars_avghours_for_month)

        self.analyse_cars_price_per_hours_for_month = QLabel(self.frame_13)
        self.analyse_cars_price_per_hours_for_month.setObjectName(u"analyse_cars_price_per_hours_for_month")
        self.analyse_cars_price_per_hours_for_month.setStyleSheet(u"border:none;")
        self.analyse_cars_price_per_hours_for_month.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.analyse_cars_price_per_hours_for_month)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)


        self.horizontalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.analyse_cars_statsframe)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(183, 0, 65);\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setSpacing(12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_21 = QLabel(self.frame_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font-size:22px;\n"
"border:none;")

        self.verticalLayout_17.addWidget(self.label_21)

        self.analyse_cars_income_for_alltime = QLabel(self.frame_14)
        self.analyse_cars_income_for_alltime.setObjectName(u"analyse_cars_income_for_alltime")
        self.analyse_cars_income_for_alltime.setStyleSheet(u"font-size: 40px;\n"
"border:none;")

        self.verticalLayout_17.addWidget(self.analyse_cars_income_for_alltime)

        self.line_3 = QFrame(self.frame_14)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_3)

        self.analyse_cars_quantity_for_alltime = QLabel(self.frame_14)
        self.analyse_cars_quantity_for_alltime.setObjectName(u"analyse_cars_quantity_for_alltime")
        self.analyse_cars_quantity_for_alltime.setStyleSheet(u"border:none;")

        self.verticalLayout_17.addWidget(self.analyse_cars_quantity_for_alltime)

        self.line_9 = QFrame(self.frame_14)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_9)

        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border:none;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_22)

        self.analyse_cars_avgprice_for_alltime = QLabel(self.frame_14)
        self.analyse_cars_avgprice_for_alltime.setObjectName(u"analyse_cars_avgprice_for_alltime")
        self.analyse_cars_avgprice_for_alltime.setStyleSheet(u"border:none;")

        self.verticalLayout_17.addWidget(self.analyse_cars_avgprice_for_alltime)

        self.analyse_cars_avghours_for_alltime = QLabel(self.frame_14)
        self.analyse_cars_avghours_for_alltime.setObjectName(u"analyse_cars_avghours_for_alltime")
        self.analyse_cars_avghours_for_alltime.setStyleSheet(u"border:none;")

        self.verticalLayout_17.addWidget(self.analyse_cars_avghours_for_alltime)

        self.analyse_cars_price_per_hours_for_alltime = QLabel(self.frame_14)
        self.analyse_cars_price_per_hours_for_alltime.setObjectName(u"analyse_cars_price_per_hours_for_alltime")
        self.analyse_cars_price_per_hours_for_alltime.setStyleSheet(u"border:none;")
        self.analyse_cars_price_per_hours_for_alltime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_17.addWidget(self.analyse_cars_price_per_hours_for_alltime)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)


        self.horizontalLayout_13.addWidget(self.frame_14)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.stackedWidget_2.addWidget(self.analyse_cars_page)

        self.horizontalLayout_8.addWidget(self.stackedWidget_2)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.analyse_page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.workplace)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close_button.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(1)


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
        self.cars_addcar_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c", None))
        self.analyse_resale_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0441\u0435\u0439\u043b", None))
        self.analyse_cars_button.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0435\u043d\u0434\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0441\u0435\u0433\u043e\u0434\u043d\u044f:", None))
        self.analyse_resale_income_for_day.setText(QCoreApplication.translate("MainWindow", u"123123$", None))
        self.analyse_resale_quantity_for_day.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0434\u0435\u043b\u043e\u043a:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438:", None))
        self.analyse_resale_avgprice_for_day.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0446\u0435\u043d\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0437\u0430 \u043d\u0435\u0434\u0435\u043b\u044e:", None))
        self.analyse_resale_income_for_week.setText(QCoreApplication.translate("MainWindow", u"123123$", None))
        self.analyse_resale_quantity_for_week.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0434\u0435\u043b\u043e\u043a:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438:", None))
        self.analyse_resale_avgprice_for_week.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0446\u0435\u043d\u0430:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0437\u0430 \u043c\u0435\u0441\u044f\u0446:", None))
        self.analyse_resale_income_for_month.setText(QCoreApplication.translate("MainWindow", u"123123$", None))
        self.analyse_resale_quantity_for_month.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0434\u0435\u043b\u043e\u043a:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438:", None))
        self.analyse_resale_avgprice_for_month.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0446\u0435\u043d\u0430:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0437\u0430 \u043d\u0435\u0434\u0435\u043b\u044e:", None))
        self.analyse_cars_income_for_week.setText(QCoreApplication.translate("MainWindow", u"123123$", None))
        self.analyse_cars_quantity_for_week.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0434\u0435\u043b\u043e\u043a:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438:", None))
        self.analyse_cars_avgprice_for_week.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430:", None))
        self.analyse_cars_avghours_for_week.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.analyse_cars_price_per_hours_for_week.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u0447\u0430\u0441:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0437\u0430 \u043c\u0435\u0441\u044f\u0446:", None))
        self.analyse_cars_income_for_month.setText(QCoreApplication.translate("MainWindow", u"123123$", None))
        self.analyse_cars_quantity_for_month.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0434\u0435\u043b\u043e\u043a:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438:", None))
        self.analyse_cars_avgprice_for_month.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430:", None))
        self.analyse_cars_avghours_for_month.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.analyse_cars_price_per_hours_for_month.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u0447\u0430\u0441:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0437\u0430 \u0432\u0441\u0451 \u0432\u0440\u0435\u043c\u044f:", None))
        self.analyse_cars_income_for_alltime.setText(QCoreApplication.translate("MainWindow", u"123123$", None))
        self.analyse_cars_quantity_for_alltime.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0434\u0435\u043b\u043e\u043a:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438:", None))
        self.analyse_cars_avgprice_for_alltime.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430:", None))
        self.analyse_cars_avghours_for_alltime.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.analyse_cars_price_per_hours_for_alltime.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u0447\u0430\u0441:", None))
    # retranslateUi

