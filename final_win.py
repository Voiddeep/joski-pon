from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox)
from instr import* 
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def initUI(self):
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index)
        self.layout.addWidget(self.workheart)
        self.setLayout(self.layout)
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
app = QApplication([])
window = FinalWin()
app.exec()


        