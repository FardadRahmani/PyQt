# Form implementation generated from reading ui file 'ui\formular.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Formular(object):
    def setupUi(self, Formular):
        Formular.setObjectName("Formular")
        Formular.resize(800, 498)
        self.centralwidget = QtWidgets.QWidget(parent=Formular)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 10, 171, 211))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 113, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 70, 113, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 93, 29))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 110, 76, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 270, 104, 75))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(340, 280, 104, 75))
        self.plainTextEdit.setObjectName("plainTextEdit")
        Formular.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Formular)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Formular.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Formular)
        self.statusbar.setObjectName("statusbar")
        Formular.setStatusBar(self.statusbar)

        self.retranslateUi(Formular)
        QtCore.QMetaObject.connectSlotsByName(Formular)

    def retranslateUi(self, Formular):
        _translate = QtCore.QCoreApplication.translate
        Formular.setWindowTitle(_translate("Formular", "MainWindow"))
        self.groupBox.setTitle(_translate("Formular", "GroupBox"))
        self.lineEdit.setPlaceholderText(_translate("Formular", "Vorname"))
        self.lineEdit_2.setPlaceholderText(_translate("Formular", "Nachname"))
        self.pushButton.setText(_translate("Formular", "Speichern!"))
        self.comboBox.setItemText(0, _translate("Formular", "Mathematik"))
        self.comboBox.setItemText(1, _translate("Formular", "Informatik"))
        self.comboBox.setItemText(2, _translate("Formular", "Philosophie"))
        self.comboBox.setItemText(3, _translate("Formular", "Kulturwissenschaften"))
        self.comboBox.setItemText(4, _translate("Formular", "Psychologie"))
        self.textEdit.setHtml(_translate("Formular", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hier <span style=\" text-decoration: underline;\">bearbeiteter</span> <span style=\" font-weight:700;\">Text</span> <span style=\" font-style:italic;\">möglich</span></p></body></html>"))
        self.plainTextEdit.setPlainText(_translate("Formular", "Hier nur normaler Text möglich"))
