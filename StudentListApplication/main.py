import sys
import os
import csv
from itertools import count

from adodbapi.apibase import onIronPython

# Set the QT_API environment variable to use PyQt6
os.environ["QT_API"] = "pyqt6"

from qtpy import QtWidgets, QtCore
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)



#bmi= [körpergewicht in kg] / ( [Körpergröße in m] ^2 )  -->kg ** 2

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Studierendenverwaltung")
        self.lineCount=0
        self.list= [[]]

        self.readCsvFile("students.csv")

        self.ui.newEntryButton.clicked.connect(self.onNewEntry)
        self.ui.saveButton.clicked.connect(self.onSave)

        self.ui.studentsTable.cellChanged.connect(self.onCellChanged)

        #self.ui.pushButton.clicked.connect(self.onPushButtonClick)

    def onSave(self):
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=",", quotechar='"')

            for i in range(0, self.lineCount):
                rowContent=[
                    self.ui.studentsTable.item(i, 0).text(),
                    self.ui.studentsTable.item(i, 1).text(),
                    self.ui.studentsTable.item(i, 2).text()
                ]
                writer.writerow(rowContent)

        QtWidgets.QApplication.quit()







    def onCellChanged(self, row, col):
        print(self.ui.studentsTable.item(row,col).text())
        print(row)
        print(col)

        self.list.append(row)
        self.list.append(col)
        self.list.append(self.ui.studentsTable.item(row,col).text())


    def readCsvFile(self, filename):
        with open(filename,"r", newline= '') as file:
            reader= csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                print(line)
                self.ui.studentsTable.insertRow(self.lineCount)
                self.ui.studentsTable.setItem(self.lineCount, 0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.studentsTable.setItem(self.lineCount, 1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.studentsTable.setItem(self.lineCount, 2, QtWidgets.QTableWidgetItem(line[2]))
                self.lineCount+=1
                print(self.lineCount)
                print(line[2])



    def onNewEntry(self):
        self.ui.studentsTable.insertRow(self.lineCount)

        #print(cell)#None, also lieber anlegen, auch wenn leer
        self.ui.studentsTable.setItem(self.lineCount, 0, QtWidgets.QTableWidgetItem(""))
        self.ui.studentsTable.setItem(self.lineCount, 1, QtWidgets.QTableWidgetItem(""))
        self.ui.studentsTable.setItem(self.lineCount, 2, QtWidgets.QTableWidgetItem(""))
        cell = self.ui.studentsTable.item(self.lineCount, 0)
        #jetzt cursor in zelle setzen um es gleich zu editieren
        self.ui.studentsTable.editItem(cell)
        self.lineCount += 1





            #     #self.ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem("20000000"))

    # def onCellChanged(self, row, col):
    #     print(row)
    #     print(col)
    #
    #
    # def onPushButtonClick(self):
    #     #self.ui.tableWidget.insertRow(2)
    #     #self.ui.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem("Budapest"))
    #     #self.ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem("20000000"))
    #
    #     row= self.ui.tableWidget.rowCount()
    #     self.ui.tableWidget.insertRow(row)
    #     self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Budapest"))
    #     self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("20000000"))
    #     #self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())#2 is not last cell! now rowCount increases
    #     #self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 0, QtWidgets.QTableWidgetItem("Budapest"))
    #     #self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 1, QtWidgets.QTableWidgetItem("20000000"))
    #     print("Button wurde geklickt!")


window = MainWindow()









window.show()

sys.exit(app.exec())