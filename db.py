from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import datetime
import sqlite3

class ConnectToDB:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('dates.db')
    
        if not self.db.open():
            print('Connection failed')

    
    def tables(self):
        query = QSqlQuery()

        if not query.exec("""
                        CREATE TABLE IF NOT EXISTS cars(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE,
                            date_of_added DATE DEFAULT CURRENT_DATE)
                          """):
            return False
        if not query.exec("""
                          CREATE TABLE IF NOT EXISTS income(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            car_id INTEGER,
                            amount_profit INTEGER,
                            hours_quantity INTEGER,
                            rent_day DATE DEFAULT CURRENT_DATE,
                            FOREIGN KEY(car_id) REFERENCES cars(id))
                          """):
            return False
        if not query.exec("""CREATE TABLE IF NOT EXISTS resale(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            info TEXT,
                            profit INTEGER,
                            timedate TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                          """):
            return False
        return True
    
    def add_resale(self,info,profit):
        query = QSqlQuery()
        query.prepare('INSERT INTO resale(info, profit) VALUES (?, ?)')
        query.bindValue(0,info)
        query.bindValue(1,profit)
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            query.finish()
            return True
        
    def get_last_resales(self):
        last_resales_list = []
        query = QSqlQuery()
        query.prepare('SELECT info, profit, timedate FROM resale ORDER BY id DESC LIMIT 8;')
        if query.exec():
            while query.next():
                info = query.value(0)
                profit = query.value(1)
                timestamp = query.value(2)
                time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').time().strftime('%H:%M:%S')
                last_resales_list.append((info, profit, time))
        else:
            print("Error executing query:", query.lastError().text())
        query.finish()
        return last_resales_list
    
    def get_total_profit(self):
        total_profit = ''
        query = QSqlQuery()
        query.prepare('SELECT SUM(profit) FROM resale;')
        if query.exec():
            while query.next():
                total_profit = query.value(0)
                query.finish()
            return total_profit
        else:
            print("Error executing query:", query.lastError().text())

    def resale_reset(self):
        query = QSqlQuery()
        query.prepare('DELETE FROM resale;')
        if not query.exec():
            print("Error executing query:", query.lastError().text())
            return False
        else:
            print('All resale entries have been deleted.')
            return True
        
    def new_point(self):
        query = QSqlQuery()
        query.prepare('INSERT INTO resale(info,profit) VALUES(?, ?)')
        query.bindValue(0,'НОВАЯ СЕРИЯ')
        query.bindValue(1, '0')
        if not query.exec():
            print("Error executing query:", query.lastError().text())
            return False
        else:
            print('New point created...')
            return True
        
    def get_max_id_from_point(self):
        max_id = 0
        connection = sqlite3.connect("dates.db")
        cursor = connection.cursor()
        cursor.execute('SELECT id FROM resale WHERE info = ?', ("НОВАЯ СЕРИЯ",))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result is not None:
            max_id = result[0]
            return max_id
        else: 
            return max_id
        
    def get_profit_from_last_point(self):
        profit = 0
        max_id = self.get_max_id_from_point()
        connection = sqlite3.connect("dates.db")
        cursor = connection.cursor()
        cursor.execute('SELECT SUM(profit) FROM resale WHERE id > ?', (max_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result is not None:
            profit = result[0]
            return profit
        else:
            return 0

    def add_car(self, carname):
        query = QSqlQuery()
        query.prepare('INSERT INTO cars(name) VALUES (?)')
        query.bindValue(0, carname)
        if not query.exec():
            print(f'Adding car - error: {query.lastError().text()}')
            return False
        else:
            query.finish()
            print(f'{carname} has been added.')
            return True

    def get_car_list(self):
        car_list = []
        query = QSqlQuery()
        query.prepare('SELECT * FROM cars')
        if query.exec():
            while query.next():
                id = query.value(0)
                car = query.value(1)
                date = query.value(2)
                car_list.append((id,car,date))
            return car_list
        else:
            print(f'Getting car list - error: {query.lastError().text()}')          

    def add_rent_profit(self, car_id, profit, hours):
        query = QSqlQuery()
        query.prepare('INSERT INTO income(car_id,amount_profit,hours_quantity) VALUES (?,?,?)')
        query.bindValue(0, int(car_id))
        query.bindValue(1, int(profit))
        query.bindValue(2, int(hours))
        if not query.exec():
            print(f'Adding profit from rent - error: {query.lastError().text()}')
            return False
        else:
            query.finish()
            print(f'Profit {profit}({hours}) has been added.')
            return True

    def get_last_car_profit(self):
        last_car_profit = []
        query = QSqlQuery()
        query.prepare('SELECT cars.name, income.amount_profit, income.hours_quantity, income.rent_day FROM income JOIN cars ON income.car_id = cars.id ORDER BY income.id DESC LIMIT 8;')
        if query.exec():
            while query.next():
                car_id = query.value(0)
                profit = query.value(1)
                hours = query.value(2)
                date_str = query.value(3)
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').strftime('%d.%m')
                last_car_profit.append((car_id, profit, hours, date))
        else:
            print("Getting last profit from cars - error: ", query.lastError().text())
        query.finish()
        return last_car_profit
    
    def get_resale_stats_for_day(self):
        resale_stats_for_day = []
        query = QSqlQuery()
        query.prepare('SELECT SUM(profit),AVG(profit),COUNT(*) FROM resale WHERE DATE(timedate) = CURRENT_DATE')
        if query.exec():
            while query.next():
                profit = query.value(0)
                avg_profit = round(query.value(1))
                quantity = query.value(2)
                resale_stats_for_day.append(profit)
                resale_stats_for_day.append(avg_profit)
                resale_stats_for_day.append(quantity)
            return resale_stats_for_day
        else:
            print("Getting resales profit for this day - error: ", query.lastError().text())
            return False
        
    def get_resale_stats_for_week(self):
        resale_stats_for_week = []
        query = QSqlQuery()
        query.prepare("""SELECT SUM(profit),AVG(profit),COUNT(*) FROM resale WHERE DATE(timedate) BETWEEN DATE(CURRENT_DATE, '-7 days') AND CURRENT_DATE;""")
        if query.exec():
            while query.next():
                profit = query.value(0)
                avg_profit = round(query.value(1))
                quantity = query.value(2)
                resale_stats_for_week.append(profit)
                resale_stats_for_week.append(avg_profit)
                resale_stats_for_week.append(quantity)
            query.finish()
            return resale_stats_for_week
        else:
            print("Getting resales profit for this day - error: ", query.lastError().text())
            return False
    
    def get_resale_stats_for_month(self):
        resale_stats_for_month = []
        query = QSqlQuery()
        query.prepare("""SELECT SUM(profit),AVG(profit),COUNT(*) FROM resale WHERE DATE(timedate) BETWEEN DATE(CURRENT_DATE, '-30 days') AND CURRENT_DATE;""")
        if query.exec():
            while query.next():
                profit = query.value(0)
                avg_profit = round(query.value(1))
                quantity = query.value(2)
                resale_stats_for_month.append(profit)
                resale_stats_for_month.append(avg_profit)
                resale_stats_for_month.append(quantity)
            query.finish()
            return resale_stats_for_month
        else:
            print("Getting resales profit for this day - error: ", query.lastError().text())
            return False