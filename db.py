from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery

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
                            name TEXT)
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
        
    def closeConnection(self):
        self.db.close()
        print('Соединение закрыто')
