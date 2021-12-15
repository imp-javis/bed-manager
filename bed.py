from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(150,100,1000,500)
    win.setWindowTitle("Bed Manager")

    win.show()
    sys.exit(app.exec_())

window()

