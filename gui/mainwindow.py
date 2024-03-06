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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import gui.res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 585)
        MainWindow.setMinimumSize(QSize(595, 0))
        MainWindow.setMaximumSize(QSize(900, 800))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QFrame(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy)
        self.icon_only_widget.setMaximumSize(QSize(90, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 201, 165)\n"
"}\n"
"QPushButton{\n"
"	color: black;\n"
"	height: 50px;\n"
"	border: none;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	padding-right: 11px;\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(0, 201, 165);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.icon_only_widget.setFrameShape(QFrame.StyledPanel)
        self.icon_only_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.logo_label = QLabel(self.icon_only_widget)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy1)
        self.logo_label.setMinimumSize(QSize(70, 50))
        self.logo_label.setMaximumSize(QSize(70, 50))
        self.logo_label.setStyleSheet(u"padding-right: 5px;")
        self.logo_label.setPixmap(QPixmap(u":/logo/icons/icon.png"))
        self.logo_label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.logo_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 10, -1, -1)
        self.income_button = QPushButton(self.icon_only_widget)
        self.income_button.setObjectName(u"income_button")
        icon1 = QIcon()
        icon1.addFile(u":/black-icons/icons/savings.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/color-icons/icons/savings-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.income_button.setIcon(icon1)
        self.income_button.setIconSize(QSize(30, 30))
        self.income_button.setCheckable(True)
        self.income_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.income_button)

        self.cars_button = QPushButton(self.icon_only_widget)
        self.cars_button.setObjectName(u"cars_button")
        self.cars_button.setStyleSheet(u"color: white")
        icon2 = QIcon()
        icon2.addFile(u":/black-icons/icons/cars.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/color-icons/icons/cars-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.cars_button.setIcon(icon2)
        self.cars_button.setIconSize(QSize(30, 30))
        self.cars_button.setCheckable(True)
        self.cars_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cars_button)

        self.analysis_button = QPushButton(self.icon_only_widget)
        self.analysis_button.setObjectName(u"analysis_button")
        icon3 = QIcon()
        icon3.addFile(u":/black-icons/icons/monitoring.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/color-icons/icons/monitoring-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.analysis_button.setIcon(icon3)
        self.analysis_button.setIconSize(QSize(30, 30))
        self.analysis_button.setCheckable(True)
        self.analysis_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.analysis_button)

        self.settings_button = QPushButton(self.icon_only_widget)
        self.settings_button.setObjectName(u"settings_button")
        icon4 = QIcon()
        icon4.addFile(u":/black-icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/color-icons/icons/settings-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.settings_button.setIcon(icon4)
        self.settings_button.setIconSize(QSize(30, 30))
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 231, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.expand_button = QPushButton(self.icon_only_widget)
        self.expand_button.setObjectName(u"expand_button")
        self.expand_button.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/black-icons/icons/arrow_forward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_button.setIcon(icon5)
        self.expand_button.setIconSize(QSize(30, 30))
        self.expand_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.expand_button)

        self.exit_button = QPushButton(self.icon_only_widget)
        self.exit_button.setObjectName(u"exit_button")
        icon6 = QIcon()
        icon6.addFile(u":/black-icons/icons/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon6)
        self.exit_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.exit_button)


        self.horizontalLayout_3.addWidget(self.icon_only_widget)

        self.icon_name_widget = QFrame(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMaximumSize(QSize(190, 16777215))
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 201, 165)\n"
"}\n"
"QPushButton{\n"
"	color: black;\n"
"	font-family: Bahnschrift;\n"
"	font-size: 20px;\n"
"	font-weight:bold;\n"
"	height: 50px;\n"
"	border:none;\n"
"	padding-left: 0px;\n"
"	text-align: left;\n"
"	padding-left: 15px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(0, 201, 165);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.icon_name_widget.setFrameShape(QFrame.StyledPanel)
        self.icon_name_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 5, -1)
        self.flogo_label = QLabel(self.icon_name_widget)
        self.flogo_label.setObjectName(u"flogo_label")
        sizePolicy1.setHeightForWidth(self.flogo_label.sizePolicy().hasHeightForWidth())
        self.flogo_label.setSizePolicy(sizePolicy1)
        self.flogo_label.setMinimumSize(QSize(70, 50))
        self.flogo_label.setMaximumSize(QSize(70, 50))
        self.flogo_label.setStyleSheet(u"padding-right: 5px;")
        self.flogo_label.setPixmap(QPixmap(u":/logo/icons/icon.png"))
        self.flogo_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.flogo_label)

        self.fappname_label = QLabel(self.icon_name_widget)
        self.fappname_label.setObjectName(u"fappname_label")
        self.fappname_label.setStyleSheet(u"font-family: Bahnschrift;font-weight:bold;")

        self.horizontalLayout.addWidget(self.fappname_label)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.fincome_button = QPushButton(self.icon_name_widget)
        self.fincome_button.setObjectName(u"fincome_button")
        self.fincome_button.setIcon(icon1)
        self.fincome_button.setIconSize(QSize(30, 30))
        self.fincome_button.setCheckable(True)
        self.fincome_button.setChecked(False)
        self.fincome_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.fincome_button)

        self.fcars_button = QPushButton(self.icon_name_widget)
        self.fcars_button.setObjectName(u"fcars_button")
        self.fcars_button.setIcon(icon2)
        self.fcars_button.setIconSize(QSize(30, 30))
        self.fcars_button.setCheckable(True)
        self.fcars_button.setChecked(True)
        self.fcars_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.fcars_button)

        self.fanalysis_button = QPushButton(self.icon_name_widget)
        self.fanalysis_button.setObjectName(u"fanalysis_button")
        self.fanalysis_button.setIcon(icon3)
        self.fanalysis_button.setIconSize(QSize(30, 30))
        self.fanalysis_button.setCheckable(True)
        self.fanalysis_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.fanalysis_button)

        self.fsettings_button = QPushButton(self.icon_name_widget)
        self.fsettings_button.setObjectName(u"fsettings_button")
        self.fsettings_button.setIcon(icon4)
        self.fsettings_button.setIconSize(QSize(30, 30))
        self.fsettings_button.setCheckable(True)
        self.fsettings_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.fsettings_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 229, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.fturn_button = QPushButton(self.icon_name_widget)
        self.fturn_button.setObjectName(u"fturn_button")
        self.fturn_button.setStyleSheet(u"text-align: center;\n"
"padding-left:12px;")
        icon7 = QIcon()
        icon7.addFile(u":/black-icons/icons/arrow_back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fturn_button.setIcon(icon7)
        self.fturn_button.setIconSize(QSize(30, 30))
        self.fturn_button.setCheckable(True)

        self.verticalLayout_4.addWidget(self.fturn_button)

        self.fexit_button = QPushButton(self.icon_name_widget)
        self.fexit_button.setObjectName(u"fexit_button")
        self.fexit_button.setStyleSheet(u"font-family: Bahnschrift;\n"
"font-size: 18px;\n"
"text-align: center;\n"
"\n"
"")
        self.fexit_button.setIcon(icon6)
        self.fexit_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.fexit_button)


        self.horizontalLayout_3.addWidget(self.icon_name_widget)

        self.main_menu = QFrame(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setMinimumSize(QSize(400, 0))
        self.main_menu.setMaximumSize(QSize(11111, 16777215))
        self.main_menu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.main_menu.setFrameShape(QFrame.StyledPanel)
        self.main_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(400, 0))
        self.stackedWidget.setMaximumSize(QSize(800, 16777215))
        self.income_page = QWidget()
        self.income_page.setObjectName(u"income_page")
        self.verticalLayout_5 = QVBoxLayout(self.income_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.income_frame = QFrame(self.income_page)
        self.income_frame.setObjectName(u"income_frame")
        self.income_frame.setMinimumSize(QSize(0, 480))
        self.income_frame.setFrameShape(QFrame.StyledPanel)
        self.income_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.income_frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.income_add_button = QPushButton(self.income_page)
        self.income_add_button.setObjectName(u"income_add_button")
        self.income_add_button.setMinimumSize(QSize(140, 0))
        self.income_add_button.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 201, 165)\n"
"}\n"
"QPushButton{\n"
"	color: black;\n"
"	font-family: Bahnschrift;\n"
"	font-size: 20px;\n"
"	font-weight:bold;\n"
"	height: 50px;\n"
"	border:none;\n"
"	padding-left: 0px;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
".QPushButton:hover { background-color:  rgba(0, 201, 165,200);}\n"
".QPushButton:pressed {background-color: rgba(0, 201, 165,105);}")

        self.horizontalLayout_2.addWidget(self.income_add_button)

        self.income_delete_button = QPushButton(self.income_page)
        self.income_delete_button.setObjectName(u"income_delete_button")
        self.income_delete_button.setMinimumSize(QSize(140, 0))
        self.income_delete_button.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 201, 165)\n"
"}\n"
"QPushButton{\n"
"	color: black;\n"
"	font-family: Bahnschrift;\n"
"	font-size: 20px;\n"
"	font-weight:bold;\n"
"	height: 50px;\n"
"	border:none;\n"
"	padding-right: 20px;\n"
"	text-align: right;\n"
"	padding-left: 15px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
".QPushButton:hover { background-color:  rgba(0, 201, 165,200);}\n"
".QPushButton:pressed {background-color: rgba(0, 201, 165,105);}")

        self.horizontalLayout_2.addWidget(self.income_delete_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.income_page)
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.verticalLayout_6 = QVBoxLayout(self.cars_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cars_frame = QFrame(self.cars_page)
        self.cars_frame.setObjectName(u"cars_frame")
        self.cars_frame.setMinimumSize(QSize(0, 480))
        self.cars_frame.setFrameShape(QFrame.StyledPanel)
        self.cars_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.cars_frame)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.cars_add = QPushButton(self.cars_page)
        self.cars_add.setObjectName(u"cars_add")
        self.cars_add.setMinimumSize(QSize(140, 0))
        self.cars_add.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 201, 165)\n"
"}\n"
"QPushButton{\n"
"	color: black;\n"
"	font-family: Bahnschrift;\n"
"	font-size: 20px;\n"
"	font-weight:bold;\n"
"	height: 50px;\n"
"	border:none;\n"
"	padding-left: 0px;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
".QPushButton:hover { background-color:  rgba(0, 201, 165,200);}\n"
".QPushButton:pressed {background-color: rgba(0, 201, 165,105);}")

        self.horizontalLayout_4.addWidget(self.cars_add)

        self.cars_delete = QPushButton(self.cars_page)
        self.cars_delete.setObjectName(u"cars_delete")
        self.cars_delete.setMinimumSize(QSize(140, 0))
        self.cars_delete.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 201, 165)\n"
"}\n"
"QPushButton{\n"
"	color: black;\n"
"	font-family: Bahnschrift;\n"
"	font-size: 20px;\n"
"	font-weight:bold;\n"
"	height: 50px;\n"
"	border:none;\n"
"	padding-right: 20px;\n"
"	text-align: right;\n"
"	padding-left: 15px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
".QPushButton:hover { background-color:  rgba(0, 201, 165,200);}\n"
".QPushButton:pressed {background-color: rgba(0, 201, 165,105);}")

        self.horizontalLayout_4.addWidget(self.cars_delete)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.cars_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.main_menu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.fturn_button.pressed.connect(self.icon_name_widget.hide)
        self.fturn_button.pressed.connect(self.icon_only_widget.show)
        self.expand_button.pressed.connect(self.icon_name_widget.show)
        self.expand_button.pressed.connect(self.icon_only_widget.hide)
        self.exit_button.clicked.connect(MainWindow.close)
        self.fexit_button.clicked.connect(MainWindow.close)
        self.fincome_button.toggled.connect(self.income_button.setChecked)
        self.fcars_button.toggled.connect(self.cars_button.setChecked)
        self.fanalysis_button.toggled.connect(self.analysis_button.setChecked)
        self.fsettings_button.toggled.connect(self.settings_button.setChecked)
        self.settings_button.toggled.connect(self.fsettings_button.setChecked)
        self.analysis_button.toggled.connect(self.fanalysis_button.setChecked)
        self.cars_button.toggled.connect(self.fcars_button.setChecked)
        self.income_button.toggled.connect(self.fincome_button.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"rentCalc", None))
        self.logo_label.setText("")
        self.income_button.setText("")
        self.cars_button.setText("")
        self.analysis_button.setText("")
        self.settings_button.setText("")
        self.expand_button.setText("")
        self.exit_button.setText("")
        self.flogo_label.setText("")
        self.fappname_label.setText(QCoreApplication.translate("MainWindow", u"rentCalculator", None))
        self.fincome_button.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u0438\u0431\u044b\u043b\u044c", None))
        self.fcars_button.setText(QCoreApplication.translate("MainWindow", u" \u041c\u0430\u0448\u0438\u043d\u044b", None))
        self.fanalysis_button.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.fsettings_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.fturn_button.setText("")
        self.fexit_button.setText("")
        self.income_add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.income_delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.cars_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cars_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

