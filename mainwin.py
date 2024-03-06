from PySide6.QtWidgets import QMainWindow
from gui.mainwindow import Ui_MainWindow
from gui.addcar import Ui_AddCar
from gui.addincome import Ui_AddIncome
from db import ConnectToDB


class AddCarWindow(QMainWindow, Ui_AddCar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.car_name_cancel_button.clicked.connect(self.close)

class AddIncomeWindow(QMainWindow, Ui_AddIncome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel_income_button.clicked.connect(self.close)


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

        self.cars_add.clicked.connect(self.open_add_car_window)
        self.income_add_button.clicked.connect(self.open_add_income_window)

    def income_page_open(self):
        self.stackedWidget.setCurrentWidget(self.income_page)

    def cars_page_open(self):
        self.stackedWidget.setCurrentWidget(self.cars_page)

    def open_add_car_window(self):
        self.addCarWindow = AddCarWindow()
        self.addCarWindow.show()

    def open_add_income_window(self):
        self.addIncomeWindow = AddIncomeWindow()
        self.addIncomeWindow.show()
    