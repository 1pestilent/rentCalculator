from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlDatabase, QSqlQuery
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
                            date_of_added DATE,
                            name TEXT UNIQUE)
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
                            rent_day DATE,
                            FOREIGN KEY(car_id) REFERENCES cars(id))
                          """):
            return False
        else:
            print('Table with income was created!')
        
        return True
    
    def add_car_in_db(self,carname):
        current_date = QDate.currentDate()
        print(current_date.toString('yyyy-MM-dd'))
        query = QSqlQuery()
        query.prepare('INSERT INTO cars(name, date_of_added) VALUES (?, ?)')
        query.bindValue(0,carname)
        query.bindValue(1,current_date.toString('yyyy-MM-dd'))
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            query.finish()
            return True

    def add_income_in_db(self, car_id, income, hours):
        current_date = QDate.currentDate().toString('yyyy-MM-dd')
        print(car_id, income, hours, current_date)
        query = QSqlQuery()
        query.prepare('INSERT INTO income(car_id, amount_profit, hours_quantity, rent_day) VALUES (?, ?, ?, ?)')
        query.bindValue(0,car_id)
        query.bindValue(1,income)
        query.bindValue(2,hours)
        query.bindValue(3,current_date)
        if not query.exec_():
            print(query.lastError().text())
            return False
        else:
            query.finish()
            return True
        
    def get_car_list(self):
        car_list=[]
        query = QSqlQuery()
        query.prepare('SELECT name FROM cars')
        if query.exec():
            while query.next():
                car_name = query.value(0)
                car_list.append(car_name)
        else:
            print("Error executing query:", query.lastError().text())
        print(car_list)
        query.finish()  
        return car_list
    
    def get_car_id(self, car_name):
        conn = sqlite3.connect('dates.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM cars WHERE name = ?", (car_name,))
        car_id = cursor.fetchone()
        conn.close()
        if car_id:
            return car_id[0]
        else:
            print('Car id - empty')
            return None



    def closeConnection(self):
        self.db.close()
        print('Соединение закрыто')
