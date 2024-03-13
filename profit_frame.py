from PySide6.QtWidgets import QFrame
from gui.profitnote import Ui_Frame

class profitNote(QFrame,Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)