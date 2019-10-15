# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Algo.cns import cns 




class Ui_MainWindow(object):

    def encrypt(self):
        txt = self.pt_inp.toPlainText()
        # txt = "sdsds"
        key = self.key_label.text()
        enc = cns.encpt(txt, key)
        self.op_textBrowser.clear()
        self.op_textBrowser.append(enc)
        
        
    def decrypt(self):
        txt = self.pt_inp.toPlainText()
        # txt = "sdsds"
        key = self.key_label.text()
        dec = cns.dcpt(txt, key)
        self.op_textBrowser.clear()
        self.op_textBrowser.append(dec)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pt_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_label.setObjectName("pt_label")
        self.verticalLayout.addWidget(self.pt_label)
        self.pt_inp = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pt_inp.setObjectName("pt_inp")
        self.verticalLayout.addWidget(self.pt_inp)
        self.key_label = QtWidgets.QLabel(self.centralwidget)
        self.key_label.setObjectName("key_label")
        self.verticalLayout.addWidget(self.key_label)
        self.key_input = QtWidgets.QTextEdit(self.centralwidget)
        self.key_input.setObjectName("key_input")
        self.verticalLayout.addWidget(self.key_input)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.op_label = QtWidgets.QLabel(self.centralwidget)
        self.op_label.setObjectName("op_label")
        self.verticalLayout.addWidget(self.op_label)
        self.op_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.op_textBrowser.setObjectName("op_textBrowser")
        self.verticalLayout.addWidget(self.op_textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_btn.setObjectName("decrypt_btn")
        self.verticalLayout.addWidget(self.decrypt_btn)
        self.encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.verticalLayout.addWidget(self.encrypt_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.encrypt_btn.clicked.connect(self.encrypt)
        self.decrypt_btn.clicked.connect(self.decrypt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pt_label.setText(_translate("MainWindow", "Enter Plain Text:"))
        self.key_label.setText(_translate("MainWindow", "Key:"))
        self.op_label.setText(_translate("MainWindow", "Output:"))
        self.op_textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Text Comes here...</p></body></html>"))
        self.decrypt_btn.setText(_translate("MainWindow", "Decrypt"))
        self.encrypt_btn.setText(_translate("MainWindow", "Encrypt"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
