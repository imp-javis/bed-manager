# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waitinglist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_waitlist(object):
    def setupUi(self, waitlist):
        waitlist.setObjectName("waitlist")
        waitlist.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(waitlist)
        self.centralwidget.setObjectName("centralwidget")
        self.newpatient = QtWidgets.QPushButton(self.centralwidget)
        self.newpatient.setGeometry(QtCore.QRect(632, 30, 131, 32))
        self.newpatient.setObjectName("newpatient")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(290, 30, 171, 51))
        self.title.setStyleSheet("font: 25pt \"Avenir Next\";")
        self.title.setObjectName("title")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 731, 441))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.delpatient = QtWidgets.QPushButton(self.centralwidget)
        self.delpatient.setGeometry(QtCore.QRect(510, 30, 113, 32))
        self.delpatient.setObjectName("delpatient")
        waitlist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(waitlist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        waitlist.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(waitlist)
        self.statusbar.setObjectName("statusbar")
        waitlist.setStatusBar(self.statusbar)

        self.retranslateUi(waitlist)
        QtCore.QMetaObject.connectSlotsByName(waitlist)

    def retranslateUi(self, waitlist):
        _translate = QtCore.QCoreApplication.translate
        waitlist.setWindowTitle(_translate("waitlist", "Waiting List"))
        self.newpatient.setText(_translate("waitlist", "Add New Patient"))
        self.title.setText(_translate("waitlist", "Waiting List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("waitlist", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("waitlist", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("waitlist", "Details"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("waitlist", "Isolation"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("waitlist", "Diagnosis"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("waitlist", "discharge summary"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("waitlist", "Timer"))
        self.delpatient.setText(_translate("waitlist", "Delete Patient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    waitlist = QtWidgets.QMainWindow()
    ui = Ui_waitlist()
    ui.setupUi(waitlist)
    waitlist.show()
    sys.exit(app.exec_())
