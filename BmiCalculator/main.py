import sys
import os

# Set the QT_API environment variable to use PyQt6
os.environ["QT_API"] = "pyqt6"

from qtpy import QtWidgets, QtCore
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Studierendenverwaltung")

window = MainWindow()

window.show()

sys.exit(app.exec())