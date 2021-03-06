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
        waitlist.resize(1440, 847)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        waitlist.setFont(font)
        self.centralwidget = QtWidgets.QWidget(waitlist)
        self.centralwidget.setObjectName("centralwidget")
        self.newpatient = QtWidgets.QPushButton(self.centralwidget)
        self.newpatient.setGeometry(QtCore.QRect(1250, 30, 131, 32))
        self.newpatient.setObjectName("newpatient")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(630, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("font: 40pt \"Times New Roman\";")
        self.title.setObjectName("title")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 1361, 671))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 1, item)
        self.delpatient = QtWidgets.QPushButton(self.centralwidget)
        self.delpatient.setGeometry(QtCore.QRect(1130, 30, 113, 32))
        self.delpatient.setObjectName("delpatient")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 30, 71, 32))
        self.backButton.setObjectName("backButton")
        waitlist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(waitlist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
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
        item.setText(_translate("waitlist", "Status"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("waitlist", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("waitlist", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("waitlist", "Details"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("waitlist", "Isolation"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("waitlist", "Diagnosis"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("waitlist", "discharge summary"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("waitlist", "Timer"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.delpatient.setText(_translate("waitlist", "Delete Patient"))
        self.backButton.setText(_translate("waitlist", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    waitlist = QtWidgets.QMainWindow()
    ui = Ui_waitlist()
    ui.setupUi(waitlist)
    waitlist.show()
    sys.exit(app.exec_())
