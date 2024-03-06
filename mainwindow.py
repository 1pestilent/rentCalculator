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
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import res-rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(952, 695)
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QFrame(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy)
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
        self.logo_label.setPixmap(QPixmap(u":/icons/icons/icon.png"))
        self.logo_label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.logo_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 10, -1, -1)
        self.income_button = QPushButton(self.icon_only_widget)
        self.income_button.setObjectName(u"income_button")
        icon1 = QIcon()
        icon1.addFile(u"icons/savings.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons/savings-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.income_button.setIcon(icon1)
        self.income_button.setIconSize(QSize(30, 30))
        self.income_button.setCheckable(True)
        self.income_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.income_button)

        self.cars_button = QPushButton(self.icon_only_widget)
        self.cars_button.setObjectName(u"cars_button")
        self.cars_button.setStyleSheet(u"color: white")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cars.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/cars-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.cars_button.setIcon(icon2)
        self.cars_button.setIconSize(QSize(30, 30))
        self.cars_button.setCheckable(True)
        self.cars_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cars_button)

        self.analysis_button = QPushButton(self.icon_only_widget)
        self.analysis_button.setObjectName(u"analysis_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/monitoring.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/monitoring-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.analysis_button.setIcon(icon3)
        self.analysis_button.setIconSize(QSize(30, 30))
        self.analysis_button.setCheckable(True)
        self.analysis_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.analysis_button)

        self.settings_button = QPushButton(self.icon_only_widget)
        self.settings_button.setObjectName(u"settings_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icons/settings-color.svg", QSize(), QIcon.Normal, QIcon.On)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/arrow_forward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_button.setIcon(icon5)
        self.expand_button.setIconSize(QSize(30, 30))
        self.expand_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.expand_button)

        self.exit_button = QPushButton(self.icon_only_widget)
        self.exit_button.setObjectName(u"exit_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon6)
        self.exit_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.exit_button)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QFrame(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.main_menu.setFrameShape(QFrame.StyledPanel)
        self.main_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(1666666, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.income_page = QWidget()
        self.income_page.setObjectName(u"income_page")
        self.income_page.setStyleSheet(u"QLabel{\n"
"font-family: Bahnschrift;\n"
"font-weight:bold;\n"
"font-size:30px;\n"
"}\n"
".QPushButton { \n"
"	background-color: rgba(0, 205, 165,255);\n"
"	color: white; \n"
"	font-size: 26px;\n"
"	font-family:Bahnschrift;\n"
"	font-weight:bold;\n"
"	border-radius: 20px;\n"
"}\n"
".QPushButton:hover {\n"
"	background-color:  rgba(0, 205, 165,255);\n"
"}\n"
".QPushButton:pressed {\n"
"background-color: rgba(0, 205, 165,105);\n"
"}\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.income_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(300, -1, -1, -1)
        self.add_income_button = QPushButton(self.income_page)
        self.add_income_button.setObjectName(u"add_income_button")
        self.add_income_button.setMinimumSize(QSize(160, 40))
        self.add_income_button.setMaximumSize(QSize(160, 16777215))
        self.add_income_button.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.add_income_button)

        self.delete_income_button = QPushButton(self.income_page)
        self.delete_income_button.setObjectName(u"delete_income_button")
        self.delete_income_button.setMinimumSize(QSize(160, 40))
        self.delete_income_button.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_3.addWidget(self.delete_income_button)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.frame = QFrame(self.income_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 600))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.income_page)
        self.analysis_page = QWidget()
        self.analysis_page.setObjectName(u"analysis_page")
        self.stackedWidget.addWidget(self.analysis_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.stackedWidget.addWidget(self.settings_page)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.cars_page.setStyleSheet(u"QLabel{\n"
"font-family: Bahnschrift;\n"
"font-weight:bold;\n"
"font-size:30px;\n"
"}\n"
".QPushButton { \n"
"	background-color: rgba(0, 205, 165,255);\n"
"	color: white; \n"
"	font-size: 26px;\n"
"	font-family:Bahnschrift;\n"
"	font-weight:bold;\n"
"	border-radius: 20px;\n"
"}\n"
".QPushButton:hover {\n"
"	background-color:  rgba(0, 205, 165,255);\n"
"}\n"
".QPushButton:pressed {\n"
"background-color: rgba(0, 205, 165,105);\n"
"}\n"
"\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.cars_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.cars_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 600))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(300, -1, -1, -1)
        self.pushButton = QPushButton(self.cars_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(160, 40))
        self.pushButton.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.cars_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(160, 40))
        self.pushButton_2.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.cars_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_name_widget = QFrame(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
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
        self.flogo_label.setPixmap(QPixmap(u":/icons/icons/icon.png"))
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/savings.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/icons/savings-color.svg", QSize(), QIcon.Normal, QIcon.On)
        self.fincome_button.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/arrow_back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fturn_button.setIcon(icon8)
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


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

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

        self.stackedWidget.setCurrentIndex(4)


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
        self.add_income_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_income_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.flogo_label.setText("")
        self.fappname_label.setText(QCoreApplication.translate("MainWindow", u"rentCalculator", None))
        self.fincome_button.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u0438\u0431\u044b\u043b\u044c", None))
        self.fcars_button.setText(QCoreApplication.translate("MainWindow", u" \u041c\u0430\u0448\u0438\u043d\u044b", None))
        self.fanalysis_button.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.fsettings_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.fturn_button.setText("")
        self.fexit_button.setText("")
    # retranslateUi

