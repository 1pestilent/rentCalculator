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

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.resale_button.clicked.connect(self.open_resale_page)
        self.cars_button.clicked.connect(self.open_cars_page)
        self.header.mouseMoveEvent = self.moveWindow
        self.resale_add_button.clicked.connect(self.add_resale_profit_in_db)
        self.resale_reset_button.clicked.connect(self.resale_reset)
        self.resale_new_button.clicked.connect(self.interim_profit)

        self.add_notes()
        self.resale_button.click()

    def open_resale_page(self):
        self.stackedWidget.setCurrentWidget(self.resale_page)

    def open_cars_page(self):
        self.stackedWidget.setCurrentWidget(self.cars_page)    

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
