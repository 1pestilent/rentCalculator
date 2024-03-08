from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
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
        self.refresh_car_list()


    def open_add_car_window(self):
        self.addCarWindow = AddCarWindow()
        self.addCarWindow.car_name_add_button.clicked.connect(self.add_car)
        self.addCarWindow.show()

    def refresh_car_list(self):
        cars = self.connect.get_car_list()
        for car in cars:
            exists = False
            for i in range(self.cars_list.count()):
                item = self.cars_list.item(i)
                if item.text() == car:
                    exists = True
                    break
            if not exists:
                self.cars_list.addItem(car)

    def open_add_income_window(self):
        self.addIncomeWindow = AddIncomeWindow()
        cars = self.connect.get_car_list()
        for car in cars:
            self.addIncomeWindow.cars_combobox.addItem(car)
        self.addIncomeWindow.add_income_button.clicked.connect(self.add_income)
        self.addIncomeWindow.show()

    def add_car(self):
        carname = self.addCarWindow.car_name_edit.text().strip()
        if not carname == '':  
            if self.connect.add_car_in_db(carname):
                print('Add new line in table(cars)')
                self.addCarWindow.close()
                self.refresh_car_list()
        else:
            print('Поля ввода пустое!')

    def add_income(self):
        car_name = self.addIncomeWindow.cars_combobox.currentText().strip()
        income = self.addIncomeWindow.income_income_edit.text()
        hours = self.addIncomeWindow.time_income_edit.text()
        car_id = self.connect.get_car_id(car_name)
        if self.connect.add_income_in_db(car_id, income, hours):
            print('Income was added in table')
            self.addIncomeWindow.close()

    
