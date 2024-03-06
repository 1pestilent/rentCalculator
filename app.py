from PySide6.QtWidgets import QApplication, QMainWindow
from mainwin import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()