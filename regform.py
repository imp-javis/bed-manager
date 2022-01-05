# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from amu_database import addtowaitlist


class Ui_registerform(object):
    def addedPatient(self, reg_win, wait_win):
        import waitlist
        import time
        seconds = time.time()
        addtowaitlist(self.first.text(), self.last.text(), self.ageBox.text(), self.genderBox.currentText(), self.diagnosis.toPlainText(), int(seconds), self.checkBox.checkState())
        self.window = QtWidgets.QMainWindow()
        self.ui = waitlist.Ui_waitlist()
        self.ui.setupUi(self.window)
        self.window.show()          #first = variable for first name, ageBox = variable for age etc.
        wait_win.close()
        reg_win.close()

    def setupUi(self, registerform, waitlist):
        registerform.setObjectName("registerform")
        registerform.setWindowModality(QtCore.Qt.WindowModal)
        registerform.resize(588, 469)
        registerform.setTitle("")
        self.first = QtWidgets.QLineEdit(registerform)
        self.first.setGeometry(QtCore.QRect(120, 30, 341, 21))
        self.first.setObjectName("first")
        self.firstlabel = QtWidgets.QLabel(registerform)
        self.firstlabel.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.firstlabel.setObjectName("firstlabel")
        self.last = QtWidgets.QLineEdit(registerform)
        self.last.setGeometry(QtCore.QRect(120, 70, 341, 21))
        self.last.setText("")
        self.last.setObjectName("last")
        self.lastlabel = QtWidgets.QLabel(registerform)
        self.lastlabel.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.lastlabel.setObjectName("lastlabel")
        self.label_2 = QtWidgets.QLabel(registerform)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 60, 16))
        self.label_2.setObjectName("label_2")
        self.ageBox = QtWidgets.QSpinBox(registerform)
        self.ageBox.setGeometry(QtCore.QRect(120, 110, 31, 24))
        self.ageBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ageBox.setWrapping(True)
        self.ageBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ageBox.setSuffix("")
        self.ageBox.setMaximum(150)
        self.ageBox.setObjectName("ageBox")
        self.label_3 = QtWidgets.QLabel(registerform)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 60, 16))
        self.label_3.setObjectName("label_3")
        self.si = QtWidgets.QLabel(registerform)
        self.si.setGeometry(QtCore.QRect(290, 110, 91, 16))
        self.si.setObjectName("si")
        self.checkBox = QtWidgets.QCheckBox(registerform)
        self.checkBox.setGeometry(QtCore.QRect(380, 110, 16, 20))
        self.checkBox.setObjectName("checkBox")
        self.genderBox = QtWidgets.QComboBox(registerform)
        self.genderBox.setGeometry(QtCore.QRect(90, 140, 105, 28))
        self.genderBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.genderBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.genderBox.setEditable(False)
        self.genderBox.setCurrentText("")
        self.genderBox.setMaxVisibleItems(2)
        self.genderBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.genderBox.setObjectName("genderBox")
        self.diagnosis = QtWidgets.QTextEdit(registerform)
        self.diagnosis.setGeometry(QtCore.QRect(30, 200, 531, 191))
        self.diagnosis.setObjectName("diagnosis")
        self.dlabel = QtWidgets.QLabel(registerform)
        self.dlabel.setGeometry(QtCore.QRect(30, 180, 121, 16))
        self.dlabel.setScaledContents(False)
        self.dlabel.setWordWrap(False)
        self.dlabel.setObjectName("dlabel")
        self.pushButton = QtWidgets.QPushButton(registerform,  clicked = lambda: self.addedPatient(registerform, waitlist))
        self.pushButton.setGeometry(QtCore.QRect(240, 420, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.genderBox.addItem("Select")
        self.genderBox.addItem("Male")
        self.genderBox.addItem("Female")
        self.invalid = QtWidgets.QLabel(registerform)
        self.invalid.setGeometry(QtCore.QRect(90, 400, 411, 20))
        self.invalid.setStyleSheet("color: red")
        self.invalid.setAlignment(QtCore.Qt.AlignCenter)
        self.invalid.setObjectName("invalid")

        self.retranslateUi(registerform)
        QtCore.QMetaObject.connectSlotsByName(registerform)

    def retranslateUi(self, registerform):
        _translate = QtCore.QCoreApplication.translate
        registerform.setWindowTitle(_translate("registerform", "Patient Registration Form"))
        self.firstlabel.setText(_translate("registerform", "First name:"))
        self.label_2.setText(_translate("registerform", "Age:"))
        self.label_3.setText(_translate("registerform", "Gender:"))
        self.dlabel.setText(_translate("registerform", "Top-line Diagnosis"))
        self.pushButton.setText(_translate("registerform", "Register"))
        self.lastlabel.setText(_translate("registerform", "Last name:"))
        self.si.setText(_translate("registerform", "Self-isolation:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerform = QtWidgets.QGroupBox()
    ui = Ui_registerform()
    ui.setupUi(registerform)
    registerform.show()
    sys.exit(app.exec_())
