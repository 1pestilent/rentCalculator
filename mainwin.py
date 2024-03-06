from PySide6.QtWidgets import QMainWindow
from gui.mainwindow import Ui_MainWindow
from db import ConnectToDB


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect = ConnectToDB()
        if not self.connect.tables():
            print('Table not created :(')
            self.connect.closeConnection()
        else:
            print('Table has been created :)')
            self.connect.closeConnection

        self.icon_name_widget.hide()
        self.income_button.clicked.connect(self.income_page_open)
        self.fincome_button.clicked.connect(self.income_page_open)
        self.cars_button.clicked.connect(self.cars_page_open)
        self.fcars_button.clicked.connect(self.cars_page_open)
        self.analysis_button.clicked.connect(self.analysis_page_open)
        self.fanalysis_button.clicked.connect(self.analysis_page_open)
        self.settings_button.clicked.connect(self.settings_page_open)
        self.fsettings_button.clicked.connect(self.settings_page_open)

    def income_page_open(self):
        self.stackedWidget.setCurrentWidget(self.income_page)

    def cars_page_open(self):
        self.stackedWidget.setCurrentWidget(self.cars_page)

    def analysis_page_open(self):
        self.stackedWidget.setCurrentWidget(self.analysis_page)

    def settings_page_open(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)
    
