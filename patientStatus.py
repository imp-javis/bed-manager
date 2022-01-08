# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient_status.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from amu_database import getBedListSize, getPatientsinBed, getPatientInfo

bedColumn = 0
idColumn = 1
nameColumn = 2
detailsColumn = 3
diagnosisColumn = 4
isoColumn = 5
dischargeColumn = 6
dis_loungeColumn = 7
dis_sumColumn = 8
dis_medColumn = 9
downstreamColumn = 10
deathColumn = 11

class Ui_patientStatus(object):
    def setupUi(self, patientStatus):
        patientStatus.setObjectName("patientStatus")
        patientStatus.resize(1429, 885)
        font = QtGui.QFont()
        font.setFamily("Arial")
        patientStatus.setFont(font)
        self.centralwidget = QtWidgets.QWidget(patientStatus)
        self.centralwidget.setObjectName("centralwidget")

        self.patientListTitle = QtWidgets.QLabel(self.centralwidget)
        self.patientListTitle.setGeometry(QtCore.QRect(620, 30, 231, 51))
        self.patientListTitle.setStyleSheet("font: 25pt \"Arial\";")
        self.patientListTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.patientListTitle.setObjectName("patientListTitle")

        self.buttBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttBack.setGeometry(QtCore.QRect(30, 30, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.buttBack.setFont(font)
        self.buttBack.setObjectName("buttBack")

        self.buttConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.buttConfirm.setGeometry(QtCore.QRect(1252, 30, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.buttConfirm.setFont(font)
        self.buttConfirm.setObjectName("buttConfirm")

        self.buttEditWard = QtWidgets.QPushButton(self.centralwidget)
        self.buttEditWard.setGeometry(QtCore.QRect(1100, 30, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.buttEditWard.setFont(font)
        self.buttEditWard.setObjectName("buttEditWard")


        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 110, 1381, 751))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")


        self.bedTab = QtWidgets.QWidget()
        self.bedTab.setObjectName("bedTab")


        self.bedTable = QtWidgets.QTableWidget(self.bedTab)
        self.bedTable.setGeometry(QtCore.QRect(10, 20, 1131, 661))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bedTable.setFont(font)
        self.bedTable.setWordWrap(True)
        self.bedTable.setObjectName("bedTable")
        self.bedTable.setColumnCount(12)
        self.bedTable.setRowCount(0)

        self.bedTable.setColumnWidth(bedColumn,30)
        self.bedTable.setColumnWidth(idColumn,30)
        self.bedTable.setColumnWidth(nameColumn,135)
        self.bedTable.setColumnWidth(detailsColumn,110)
        self.bedTable.setColumnWidth(diagnosisColumn,165)
        self.bedTable.setColumnWidth(isoColumn,78)
        self.bedTable.setColumnWidth(dischargeColumn,78)
        self.bedTable.setColumnWidth(dis_loungeColumn,78)
        self.bedTable.setColumnWidth(dis_sumColumn,78)
        self.bedTable.setColumnWidth(dis_medColumn,78)
        self.bedTable.setColumnWidth(downstreamColumn,115)
        self.bedTable.setColumnWidth(deathColumn,60)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.bedTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.bedTable.setHorizontalHeaderItem(11, item)

        # frame for downstream ward bed availability
        self.wardFrame = QtWidgets.QFrame(self.bedTab)
        self.wardFrame.setGeometry(QtCore.QRect(1160, 30, 201, 641))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.wardFrame.setFont(font)
        self.wardFrame.setAutoFillBackground(True)
        self.wardFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wardFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wardFrame.setObjectName("wardFrame")

        self.wardBedTitle = QtWidgets.QLabel(self.wardFrame)
        self.wardBedTitle.setGeometry(QtCore.QRect(0, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wardBedTitle.setFont(font)
        self.wardBedTitle.setStyleSheet("font: 15pt \"Arial\";")
        self.wardBedTitle.setScaledContents(False)
        self.wardBedTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.wardBedTitle.setWordWrap(True)
        self.wardBedTitle.setObjectName("wardBedTitle")

        # cardiology ward
        self.cardioFrame = QtWidgets.QFrame(self.wardFrame)
        self.cardioFrame.setGeometry(QtCore.QRect(20, 90, 161, 91))
        self.cardioFrame.setAutoFillBackground(False)
        self.cardioFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cardioFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cardioFrame.setObjectName("cardioFrame")

        self.cardioTitle = QtWidgets.QLabel(self.cardioFrame)
        self.cardioTitle.setGeometry(QtCore.QRect(0, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.cardioTitle.setFont(font)
        self.cardioTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.cardioTitle.setObjectName("cardioTitle")

        self.cardio = QtWidgets.QLabel(self.cardioFrame)
        self.cardio.setGeometry(QtCore.QRect(40, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.cardio.setFont(font)
        self.cardio.setText("")
        self.cardio.setAlignment(QtCore.Qt.AlignCenter)
        self.cardio.setObjectName("cardio")

        # endocrinology ward
        self.endoFrame = QtWidgets.QFrame(self.wardFrame)
        self.endoFrame.setGeometry(QtCore.QRect(20, 200, 161, 91))
        self.endoFrame.setAutoFillBackground(False)
        self.endoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.endoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.endoFrame.setObjectName("endoFrame")

        self.endoTitle = QtWidgets.QLabel(self.endoFrame)
        self.endoTitle.setGeometry(QtCore.QRect(0, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.endoTitle.setFont(font)
        self.endoTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.endoTitle.setObjectName("endoTitle")

        self.endo = QtWidgets.QLabel(self.endoFrame)
        self.endo.setGeometry(QtCore.QRect(40, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.endo.setFont(font)
        self.endo.setText("")
        self.endo.setAlignment(QtCore.Qt.AlignCenter)
        self.endo.setObjectName("endo")

        # gastroentrology ward
        self.gastroFrame = QtWidgets.QFrame(self.wardFrame)
        self.gastroFrame.setGeometry(QtCore.QRect(20, 310, 161, 91))
        self.gastroFrame.setAutoFillBackground(False)
        self.gastroFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gastroFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gastroFrame.setObjectName("gastroFrame")

        self.gastroTitle = QtWidgets.QLabel(self.gastroFrame)
        self.gastroTitle.setGeometry(QtCore.QRect(0, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.gastroTitle.setFont(font)
        self.gastroTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.gastroTitle.setObjectName("gastroTitle")

        self.gastro = QtWidgets.QLabel(self.gastroFrame)
        self.gastro.setGeometry(QtCore.QRect(40, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.gastro.setFont(font)
        self.gastro.setText("")
        self.gastro.setAlignment(QtCore.Qt.AlignCenter)
        self.gastro.setObjectName("gastro")

        # geriatrics ward
        self.geriFrame = QtWidgets.QFrame(self.wardFrame)
        self.geriFrame.setGeometry(QtCore.QRect(20, 420, 161, 91))
        self.geriFrame.setAutoFillBackground(False)
        self.geriFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.geriFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.geriFrame.setObjectName("geriFrame")

        self.geriTitle = QtWidgets.QLabel(self.geriFrame)
        self.geriTitle.setGeometry(QtCore.QRect(0, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.geriTitle.setFont(font)
        self.geriTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.geriTitle.setObjectName("geriTitle")

        self.geri = QtWidgets.QLabel(self.geriFrame)
        self.geri.setGeometry(QtCore.QRect(40, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.geri.setFont(font)
        self.geri.setText("")
        self.geri.setAlignment(QtCore.Qt.AlignCenter)
        self.geri.setObjectName("geri")

        # respiratory ward
        self.respFrame = QtWidgets.QFrame(self.wardFrame)
        self.respFrame.setGeometry(QtCore.QRect(20, 530, 161, 91))
        self.respFrame.setAutoFillBackground(False)
        self.respFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.respFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.respFrame.setObjectName("respFrame")

        self.respTitle = QtWidgets.QLabel(self.respFrame)
        self.respTitle.setGeometry(QtCore.QRect(0, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.respTitle.setFont(font)
        self.respTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.respTitle.setObjectName("respTitle")

        self.resp = QtWidgets.QLabel(self.respFrame)
        self.resp.setGeometry(QtCore.QRect(40, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.resp.setFont(font)
        self.resp.setText("")
        self.resp.setAlignment(QtCore.Qt.AlignCenter)
        self.resp.setObjectName("resp")

        self.wardFrame.raise_()
        self.bedTable.raise_()
        self.tabWidget.addTab(self.bedTab, "")

        # tab for discharge lounge
        self.loungeTab = QtWidgets.QWidget()
        self.loungeTab.setObjectName("loungeTab")

        # lounge table for patient info
        self.loungeTable = QtWidgets.QTableWidget(self.loungeTab)
        self.loungeTable.setGeometry(QtCore.QRect(10, 20, 1021, 661))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.loungeTable.setFont(font)
        self.loungeTable.setWordWrap(True)
        self.loungeTable.setObjectName("loungeTable")
        self.loungeTable.setColumnCount(10)
        self.loungeTable.setRowCount(0)

        #self.bedTable.setColumnWidth(bedColumn,40)
        #self.bedTable.setColumnWidth(idColumn,40)
        #self.bedTable.setColumnWidth(nameColumn,160)
        #self.bedTable.setColumnWidth(detailsColumn,120)
        #self.bedTable.setColumnWidth(diagnosisColumn,120)
        #self.bedTable.setColumnWidth(isoColumn,90)
        #self.bedTable.setColumnWidth(dischargeColumn,80)
        #self.bedTable.setColumnWidth(dis_loungeColumn,80)
        #self.bedTable.setColumnWidth(dis_sumColumn,80)
        #self.bedTable.setColumnWidth(dis_medColumn,80)

        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.loungeTable.setHorizontalHeaderItem(9, item)

        self.tabWidget.addTab(self.loungeTab, "")
        self.tabWidget.raise_()
        self.patientListTitle.raise_()
        self.buttBack.raise_()
        self.buttConfirm.raise_()
        self.buttEditWard.raise_()
        patientStatus.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(patientStatus)
        self.statusbar.setObjectName("statusbar")
        patientStatus.setStatusBar(self.statusbar)


        # display patient info in tables on both tabs
        self.displayList(self.bedTable)
        #self.displayList(self.loungeTable)

        self.retranslateUi(patientStatus)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(patientStatus)

    def displayList(self, table):      # this function updates the list of patients currently in an AMU bed that is saved in database
        
        # listnow = getPatientsinBed, getPatientsinLounge
        # table = bedTable, loungeTable

        if table == self.bedTable:
            size = getBedListSize()
            listnow = getPatientsinBed()
        elif table == self.loungeTable:
            size = getLoungeListSize()
            listnow = getPatientsinLounge()

        table.setRowCount(size) #setting the table row size
        row = 0
       
        for pat in listnow: #looping through each row of bed list to display each line/patient
            
            patient = getPatientInfo(pat[0])

            isoStatus = ""
            if patient[6] == 0:
                isoStatus = "N"
            elif patient[6] != 0:
                isoStatus = "Y"

            comboBox_ward = QtWidgets.QComboBox()
            comboBox_ward.addItem("Select")
            comboBox_ward.addItem("Cardiology")
            comboBox_ward.addItem("Endocrinology")
            comboBox_ward.addItem("Gastroenterology")
            comboBox_ward.addItem("Geriatrics")
            comboBox_ward.addItem("Respiratory")

            checkBox_discharge = QtWidgets.QTableWidgetItem()
            checkBox_discharge.setCheckState(pat[2])

            checkBox_dischargeLounge = QtWidgets.QTableWidgetItem()
            checkBox_dischargeLounge.setCheckState(pat[3])

            checkBox_dischargeSum = QtWidgets.QTableWidgetItem()
            checkBox_dischargeSum.setCheckState(pat[4])

            checkBox_dischargeMed = QtWidgets.QTableWidgetItem()
            checkBox_dischargeMed.setCheckState(pat[5])

            checkBox_death = QtWidgets.QTableWidgetItem()
            checkBox_death.setCheckState(pat[7])

            self.bedTable.setRowHeight(row, 70)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)

            table.setItem(row, bedColumn, QtWidgets.QTableWidgetItem(pat[1])) # bed
            item.setText(str(patient[0]))
            table.setItem(row, idColumn, item) #id
            table.setItem(row, nameColumn, QtWidgets.QTableWidgetItem("{} {}".format(patient[1], patient[2]))) # name
            table.setItem(row, detailsColumn, QtWidgets.QTableWidgetItem(("Age: {} \nGender: {}").format(patient[3],patient[4]))) #age and gender
            table.setItem(row, diagnosisColumn, QtWidgets.QTableWidgetItem(("{}").format(patient[5]))) # diagnosis
            table.setItem(row, isoColumn, QtWidgets.QTableWidgetItem(isoStatus)) # isolation
            table.setItem(row, dischargeColumn, checkBox_discharge) # discharge status
            table.setItem(row, dis_loungeColumn, checkBox_dischargeLounge) # discharge lounge
            table.setItem(row, dis_sumColumn, checkBox_dischargeSum) # discharge summary
            table.setItem(row, dis_medColumn, checkBox_dischargeMed) # discharge medication
            table.setCellWidget(row, downstreamColumn, comboBox_ward) # downstream ward
            table.setItem(row, deathColumn, checkBox_death) # death

            row = row+1



    def retranslateUi(self, patientStatus):
        _translate = QtCore.QCoreApplication.translate
        patientStatus.setWindowTitle(_translate("patientStatus", "Waiting List"))
        self.patientListTitle.setText(_translate("patientStatus", "Patient Status"))
        self.buttBack.setText(_translate("patientStatus", "Return to Main"))
        self.buttConfirm.setText(_translate("patientStatus", "Confirm"))
        self.buttEditWard.setText(_translate("patientStatus", "Edit Ward Availability"))
        item = self.bedTable.horizontalHeaderItem(0)
        item.setText(_translate("patientStatus", "Bed"))
        item = self.bedTable.horizontalHeaderItem(1)
        item.setText(_translate("patientStatus", "ID"))
        item = self.bedTable.horizontalHeaderItem(2)
        item.setText(_translate("patientStatus", "Name"))
        item = self.bedTable.horizontalHeaderItem(3)
        item.setText(_translate("patientStatus", "Details"))
        item = self.bedTable.horizontalHeaderItem(4)
        item.setText(_translate("patientStatus", "Diagnosis"))
        item = self.bedTable.horizontalHeaderItem(5)
        item.setText(_translate("patientStatus", "Isolation"))
        item = self.bedTable.horizontalHeaderItem(6)
        item.setText(_translate("patientStatus", "Discharge"))
        item = self.bedTable.horizontalHeaderItem(7)
        item.setText(_translate("patientStatus", "Lounge"))
        item = self.bedTable.horizontalHeaderItem(8)
        item.setText(_translate("patientStatus", "Summary"))
        item = self.bedTable.horizontalHeaderItem(9)
        item.setText(_translate("patientStatus", "Medication"))
        item = self.bedTable.horizontalHeaderItem(10)
        item.setText(_translate("patientStatus", "Downstream"))
        item = self.bedTable.horizontalHeaderItem(11)
        item.setText(_translate("patientStatus", "Death"))
        self.wardBedTitle.setText(_translate("patientStatus", "Downstream Ward Bed Availabity"))
        self.cardioTitle.setText(_translate("patientStatus", "Cardiology"))
        self.endoTitle.setText(_translate("patientStatus", "Endocrinology"))
        self.gastroTitle.setText(_translate("patientStatus", "Gastroenterology"))
        self.geriTitle.setText(_translate("patientStatus", "Geriatrics"))
        self.respTitle.setText(_translate("patientStatus", "Respiratory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bedTab), _translate("patientStatus", "Beds"))
        item = self.loungeTable.horizontalHeaderItem(0)
        item.setText(_translate("patientStatus", "Bed"))
        item = self.loungeTable.horizontalHeaderItem(1)
        item.setText(_translate("patientStatus", "ID"))
        item = self.loungeTable.horizontalHeaderItem(2)
        item.setText(_translate("patientStatus", "Name"))
        item = self.loungeTable.horizontalHeaderItem(3)
        item.setText(_translate("patientStatus", "Details"))
        item = self.loungeTable.horizontalHeaderItem(4)
        item.setText(_translate("patientStatus", "Diagnosis"))
        item = self.loungeTable.horizontalHeaderItem(5)
        item.setText(_translate("patientStatus", "Isolation"))
        item = self.loungeTable.horizontalHeaderItem(6)
        item.setText(_translate("patientStatus", "Discharge"))
        item = self.loungeTable.horizontalHeaderItem(7)
        item.setText(_translate("patientStatus", "Lounge"))
        item = self.loungeTable.horizontalHeaderItem(8)
        item.setText(_translate("patientStatus", "Summary"))
        item = self.loungeTable.horizontalHeaderItem(9)
        item.setText(_translate("patientStatus", "Medication"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.loungeTab), _translate("patientStatus", "Discharge Lounge"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patientStatus = QtWidgets.QMainWindow()
    ui = Ui_patientStatus()
    ui.setupUi(patientStatus)
    patientStatus.show()
    sys.exit(app.exec_())
