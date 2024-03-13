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
        else:
            print('Successful connection')

    
    def tables(self):
        query = QSqlQuery()

        if not query.exec("""
                        CREATE TABLE IF NOT EXISTS cars(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE,
                            date_of_added DATE DEFAULT CURRENT_DATE)
                          """):
            return False
        else:
            print('Table with cars was created!')
        
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
            print('Resale has been reseted.')
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

