from gui.mainwindow import Ui_MainWindow
from db import ConnectToDB
from profit_frame import profitNote
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect = ConnectToDB()
        self.connect.tables()

        int_validator = QIntValidator()
        self.resale_profit_edit.setValidator(int_validator)
        self.cars_profit_edit.setValidator(int_validator)
        self.cars_profit_edit.setMaxLength(6)
        self.cars_hours_edit.setValidator(int_validator)
        self.cars_hours_edit.setMaxLength(2)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.minimize_button.clicked.connect(self.showMinimized)

        self.resale_button.clicked.connect(self.open_resale_page)
        self.cars_button.clicked.connect(self.open_cars_page)
        self.analyse_button.clicked.connect(self.open_analyse_page)
        self.analyse_cars_button.clicked.connect(self.open_analyse_cars_page)
        self.analyse_resale_button.clicked.connect(self.open_analyse_resale_page)
        self.analyse_cars_button.clicked.connect(self.refresh_analyse_car_page)
        self.analyse_car_combobox.currentIndexChanged.connect(self.refresh_analyse_car_page)

        self.header.mouseMoveEvent = self.moveWindow

        self.resale_add_button.clicked.connect(self.add_resale_profit_in_db)
        self.resale_reset_button.clicked.connect(self.resale_reset)
        self.resale_new_button.clicked.connect(self.interim_profit)

        self.cars_addcar_button.clicked.connect(self.add_car)
        self.cars_addincome_button.clicked.connect(self.add_rent_profit)

        
        
        self.refresh_car_page()
        self.refresh_carcombo()
        self.add_notes()
        self.resale_button.click()
        self.analyse_resale_button.click()

    def open_resale_page(self):
        self.stackedWidget.setCurrentWidget(self.resale_page)

    def open_cars_page(self):
        self.stackedWidget.setCurrentWidget(self.cars_page)

    def open_analyse_page(self):
        self.stackedWidget.setCurrentWidget(self.analyse_page)
        self.refresh_analyse_resale_page()

    def open_analyse_cars_page(self):
        self.stackedWidget_2.setCurrentWidget(self.analyse_cars_page)

    def open_analyse_resale_page(self):
        self.stackedWidget_2.setCurrentWidget(self.analyse_resale_page)

    def moveWindow(self, event):
        self.move(self.pos() + event.globalPos() - self.clickPosition)
        self.clickPosition = event.globalPos()
        event.accept()
        pass
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass

    def add_resale_profit_in_db(self):
        name = self.resale_name_edit.text().strip()
        profit = int(self.resale_profit_edit.text().strip())
        if not name == '' or profit == '':
            if self.connect.add_resale(name,profit):
                self.add_notes()
                print('Resale add in db')

    def add_notes(self):
        if self.connect.get_total_profit():
            total_profit = self.connect.get_total_profit()
            total_profit = '{:,.0f}'.format(total_profit).replace(',', '.')
            self.resale_total_profit_label.setText(f'{total_profit}$')
        if self.connect.get_profit_from_last_point():
            seria_profit = self.connect.get_profit_from_last_point()
            seria_profit = '{:,.0f}'.format(seria_profit).replace(',', '.')
            self.resale_profit_label.setText(f'{seria_profit}$')
        while self.resale_story_layout.count():
            widget = self.resale_story_layout.itemAt(0).widget()
            if widget:
                self.resale_story_layout.removeWidget(widget)
                widget.deleteLater()
        if self.connect.get_last_resales():
            last_resales = self.connect.get_last_resales()
            for resale in last_resales:
                note = profitNote()
                profit = resale[1]
                if resale[0] == 'НОВАЯ СЕРИЯ':
                    note.profit.setText('$')
                    note.setStyleSheet('QFrame{background-color: rgb(85, 85, 85);border-radius:15px;border: 2px solid white;}QLabel{color: rgb(255, 255, 255);font-size: 12px;border:none;font-family: Impact;}')
                elif profit >= 0:
                    profit = '{:,.0f}'.format(profit).replace(',', '.')
                    note.profit.setText(f'{str(profit)}$')
                    note.setStyleSheet('QFrame{background-color: rgb(85, 85, 85);border-radius:15px;border: 2px solid green;}QLabel{color: rgb(255, 255, 255);font-size: 12px;border:none;font-family: Impact;}')
                else:
                    profit = '{:,.0f}'.format(profit).replace(',', '.')
                    note.profit.setText(f'{str(profit)}$')
                    note.setStyleSheet('QFrame{background-color: rgb(85, 85, 85);border-radius:15px;border: 2px solid red;}QLabel{color: rgb(255, 255, 255);font-size: 12px;border:none;font-family: Impact;}')
                note.profit_name.setText(resale[0])
                note.time.setText(resale[2])
                if self.resale_story_layout.count() >= 8:
                    self.resale_story_layout.removeWidget(self.resale_story_layout.itemAt(0).widget())
                    self.resale_story_layout.insertWidget(7,note)
                else:
                    self.resale_story_layout.addWidget(note)
            self.resale_name_edit.clear()
            self.resale_profit_edit.clear()

    def interim_profit(self):
        if self.connect.new_point():
            self.add_notes()
            self.resale_profit_label.setText('0$')

    def resale_reset(self):
        if self.connect.resale_reset():
            self.clear_resale_story()
            self.resale_profit_label.setText('0$')
            self.resale_total_profit_label.setText('0$')

    def clear_resale_story(self):
            while self.resale_story_layout.count():
                widget = self.resale_story_layout.itemAt(0).widget()
                if widget:
                    self.resale_story_layout.removeWidget(widget)
                    widget.deleteLater()

    def add_car(self):
        carname = self.cars_carname_edit.text().strip()
        print(carname)
        if self.connect.add_car(carname):
            self.refresh_carcombo()
            self.cars_carname_edit.clear()
            
    def refresh_carcombo(self):
        self.cars_car_combo.clear()
        if self.connect.get_car_list():
            car_list = self.connect.get_car_list()
            for car in car_list:
                self.cars_car_combo.addItem(f'[ID{car[0]}] {car[1]}')
                
    def add_rent_profit(self):
        id = self.cars_car_combo.currentText().split('[ID')[-1].split(']')[0]
        profit = self.cars_profit_edit.text()
        hours = self.cars_hours_edit.text()
        print(id, profit, hours)
        if self.connect.add_rent_profit(id, profit, hours):
            self.refresh_car_page()
    
    def refresh_car_page(self):
        while self.cars_story_layout.count():
            widget = self.cars_story_layout.itemAt(0).widget()
            if widget:
                self.cars_story_layout.removeWidget(widget)
                widget.deleteLater()
        if self.connect.get_last_car_profit():
            car_profits = self.connect.get_last_car_profit()
            for car_profit in car_profits:
                profit = '{:,.0f}'.format(car_profit[1]).replace(',', '.')
                note = profitNote()
                note.profit.setText(f'{profit}$ ({car_profit[2]})')
                note.profit_name.setText(f'{car_profit[0]}')
                note.time.setText(car_profit[3])
                if self.cars_story_layout.count() >= 8:
                    self.cars_story_layout.removeWidget(self.cars_story_layout.itemAt(0).widget())
                    self.cars_story_layout.insertWidget(7,note)
                else:
                    self.cars_story_layout.addWidget(note)
            self.cars_profit_edit.clear()
            self.cars_hours_edit.clear()

    def refresh_resale_stats_for_day(self):
        if self.connect.get_resale_stats_for_day():
            stats_for_day = self.connect.get_resale_stats_for_day()
            profit = '{:,.0f}'.format(stats_for_day[0]).replace(',', '.')
            avg_profit = '{:,.0f}'.format(stats_for_day[1]).replace(',', '.')
            self.analyse_resale_income_for_day.setText(f'{profit}$')
            self.analyse_resale_avgprice_for_day.setText(f'Прибыль: {avg_profit}$')
            self.analyse_resale_quantity_for_day.setText(f'Количество сделок: {stats_for_day[2]}')

    def refresh_resale_stats_for_week(self):
        if self.connect.get_resale_stats_for_week():
            stats_for_day = self.connect.get_resale_stats_for_week()
            profit = '{:,.0f}'.format(stats_for_day[0]).replace(',', '.')
            avg_profit = '{:,.0f}'.format(stats_for_day[1]).replace(',', '.')
            self.analyse_resale_income_for_week.setText(f'{profit}$')
            self.analyse_resale_avgprice_for_week.setText(f'Прибыль: {avg_profit}$')
            self.analyse_resale_quantity_for_week.setText(f'Количество сделок: {stats_for_day[2]}')

    def refresh_resale_stats_for_month(self):
        if self.connect.get_resale_stats_for_month():
            stats_for_day = self.connect.get_resale_stats_for_month()
            profit = '{:,.0f}'.format(stats_for_day[0]).replace(',', '.')
            avg_profit = '{:,.0f}'.format(stats_for_day[1]).replace(',', '.')
            self.analyse_resale_income_for_month.setText(f'{profit}$')
            self.analyse_resale_avgprice_for_month.setText(f'Прибыль: {avg_profit}$')
            self.analyse_resale_quantity_for_month.setText(f'Количество сделок: {stats_for_day[2]}')

    def refresh_analyse_carcombo(self):
        self.analyse_car_combobox.clear()
        if self.connect.get_car_list():
            car_list = self.connect.get_car_list()
            for car in car_list:
                self.analyse_car_combobox.addItem(f'[ID{car[0]}] {car[1]}')

    def refresh_cars_stats_for_week(self):
        id = self.analyse_car_combobox.currentText().split('[ID')[-1].split(']')[0]
        if self.connect.get_car_stats_for_week(id):
            stats = self.connect.get_car_stats_for_week(id)
            income = '{:,.0f}'.format(stats[0]).replace(',', '.')
            avgincome = '{:,.0f}'.format(stats[1]).replace(',', '.')
            avg_price = '{:,.0f}'.format(stats[3]).replace(',', '.')
            self.analyse_cars_income_for_week.setText(f'{income}$')
            self.analyse_cars_avgprice_for_week.setText(f'Цена: {avgincome}$')
            self.analyse_cars_avghours_for_week.setText(f'Время: {stats[2]}ч')
            self.analyse_cars_price_per_hours_for_week.setText(f'Цена за час: {avg_price}$')
            self.analyse_cars_quantity_for_week.setText(f'Количество сделок: {stats[4]}')

    def refresh_cars_stats_for_month(self):
        id = self.analyse_car_combobox.currentText().split('[ID')[-1].split(']')[0]
        if self.connect.get_car_stats_for_month(id):
            stats = self.connect.get_car_stats_for_month(id)
            income = '{:,.0f}'.format(stats[0]).replace(',', '.')
            avgincome = '{:,.0f}'.format(stats[1]).replace(',', '.')
            avg_price = '{:,.0f}'.format(stats[3]).replace(',', '.')
            self.analyse_cars_income_for_month.setText(f'{income}$')
            self.analyse_cars_avgprice_for_month.setText(f'Цена: {avgincome}$')
            self.analyse_cars_avghours_for_month.setText(f'Время: {stats[2]}ч')
            self.analyse_cars_price_per_hours_for_month.setText(f'Цена за час: {avg_price}$')
            self.analyse_cars_quantity_for_month.setText(f'Количество сделок: {stats[4]}')

    def refresh_cars_stats_for_alltime(self):
        id = self.analyse_car_combobox.currentText().split('[ID')[-1].split(']')[0]
        if self.connect.get_car_stats_for_alltime(id):
            stats = self.connect.get_car_stats_for_alltime(id)
            income = '{:,.0f}'.format(stats[0]).replace(',', '.')
            avgincome = '{:,.0f}'.format(stats[1]).replace(',', '.')
            avg_price = '{:,.0f}'.format(stats[3]).replace(',', '.')
            self.analyse_cars_income_for_alltime.setText(f'{income}$')
            self.analyse_cars_avgprice_for_alltime.setText(f'Цена: {avgincome}$')
            self.analyse_cars_avghours_for_alltime.setText(f'Время: {stats[2]}ч')
            self.analyse_cars_price_per_hours_for_alltime.setText(f'Цена за час: {avg_price}$')
            self.analyse_cars_quantity_for_alltime.setText(f'Количество сделок: {stats[4]}')

    def refresh_analyse_resale_page(self):
        self.refresh_resale_stats_for_day()
        self.refresh_resale_stats_for_week()
        self.refresh_resale_stats_for_month()
        self.refresh_analyse_carcombo()

    def refresh_analyse_car_page(self):
        self.refresh_cars_stats_for_week()
        self.refresh_cars_stats_for_month()
        self.refresh_cars_stats_for_alltime()