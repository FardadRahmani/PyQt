import sys
import os

# Set the QT_API environment variable to use PyQt6
os.environ["QT_API"] = "pyqt6"

from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Studierendenverwaltung")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.result.hide()
        self.ui.result_label.hide()

        # bmi = [Körpergewicht in kg] / [Körpergröße in m] ^ 2

        self.ui.calculate.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        height = self.ui.height.value()
        weight = self.ui.weigth.value()

        if height != 0:
            self.ui.result.show()
            self.ui.result_label.show()

            bmi = round(weight / (height ** 2), 2)
            self.ui.result.setText(str(bmi))
        else:
            self.ui.result.setText("")




window = MainWindow()

window.show()

sys.exit(app.exec_())
