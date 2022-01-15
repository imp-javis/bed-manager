# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bed_allocation.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


## colour coding for bed allocation

# occupied      grey    rgb(158, 158, 158)
# discharge     red     rgb(239, 83, 80)
# downstream    blue    rgb(79, 195, 247)
# free          green   rgb(115, 255, 104)

# set colours based on current allocation, taken from database (?)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from amu_database import getListSize, getPatientInfo, deletePatfromWaitlist, getPatientinWaitlist, addtoBed, getPatientsinBed

idColumn = 0
nameColumn = 1
detailsColumn = 2
isoColumn = 3
bedColumn = 4

class Ui_MainWindow(QtWidgets.QMainWindow):
    def showMonitor(self, main_win):
        from monitor import Ui_MainWindow2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
        main_win.close()               

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1370, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 120, 580, 580))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        # row length set in displayList() function
        self.tableWidget.setColumnWidth(idColumn,50)
        self.tableWidget.setColumnWidth(nameColumn,180)
        self.tableWidget.setColumnWidth(detailsColumn,135)
        self.tableWidget.setColumnWidth(isoColumn,90)
        self.tableWidget.setColumnWidth(bedColumn,90)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)

        # display waiting list patient info on table
        self.displayList()

        self.titleBA = QtWidgets.QLabel(self.centralwidget)
        self.titleBA.setGeometry(QtCore.QRect(580, 20, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.titleBA.setFont(font)
        self.titleBA.setObjectName("titleBA")

        ## bed layout frame
        self.bedlayoutframe = QtWidgets.QFrame(self.centralwidget)
        self.bedlayoutframe.setGeometry(QtCore.QRect(630, 120, 711, 491))
        self.bedlayoutframe.setAutoFillBackground(True)
        self.bedlayoutframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bedlayoutframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bedlayoutframe.setObjectName("bedlayoutframe")

        ## isolation room 1
        self.isoR1 = QtWidgets.QFrame(self.bedlayoutframe)
        self.isoR1.setGeometry(QtCore.QRect(50, 50, 111, 51))
        self.isoR1.setAutoFillBackground(True)
        self.isoR1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.isoR1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.isoR1.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.isoR1.setObjectName("isoR1")
        self.R1 = QtWidgets.QPushButton(self.isoR1)
        self.R1.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.R1.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.R1.setObjectName("R1")

        ## isolation room 2
        self.isoR2 = QtWidgets.QFrame(self.bedlayoutframe)
        self.isoR2.setGeometry(QtCore.QRect(50, 160, 111, 51))
        self.isoR2.setAutoFillBackground(True)
        self.isoR2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.isoR2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.isoR2.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.isoR2.setObjectName("isoR2")
        self.R2 = QtWidgets.QPushButton(self.isoR2)
        self.R2.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.R2.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.R2.setObjectName("R2")

        ## isolation room 3
        self.isoR3 = QtWidgets.QFrame(self.bedlayoutframe)
        self.isoR3.setGeometry(QtCore.QRect(50, 280, 111, 51))
        self.isoR3.setAutoFillBackground(True)
        self.isoR3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.isoR3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.isoR3.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.isoR3.setObjectName("isoR3")
        self.R3 = QtWidgets.QPushButton(self.isoR3)
        self.R3.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.R3.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.R3.setObjectName("R3")

        ## isolation room 4
        self.isoR4 = QtWidgets.QFrame(self.bedlayoutframe)
        self.isoR4.setGeometry(QtCore.QRect(50, 390, 111, 51))
        self.isoR4.setAutoFillBackground(True)
        self.isoR4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.isoR4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.isoR4.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.isoR4.setObjectName("isoR4")
        self.R4 = QtWidgets.QPushButton(self.isoR4)
        self.R4.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.R4.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.R4.setObjectName("R4")

        ## bay A
        self.bayA = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayA.setGeometry(QtCore.QRect(200, 30, 231, 201))
        self.bayA.setAutoFillBackground(True)
        self.bayA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bayA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayA.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.bayA.setObjectName("bayA")

        self.A1 = QtWidgets.QPushButton(self.bayA)
        self.A1.setGeometry(QtCore.QRect(30, 20, 31, 71))
        self.A1.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.A1.setObjectName("A1")

        self.A2 = QtWidgets.QPushButton(self.bayA)
        self.A2.setGeometry(QtCore.QRect(30, 110, 31, 71))
        self.A2.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.A2.setObjectName("A2")

        self.A3 = QtWidgets.QPushButton(self.bayA)
        self.A3.setGeometry(QtCore.QRect(170, 20, 31, 71))
        self.A3.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.A3.setObjectName("A3")

        self.A4 = QtWidgets.QPushButton(self.bayA)
        self.A4.setGeometry(QtCore.QRect(170, 110, 31, 71))
        self.A4.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.A4.setObjectName("A4")

        ## Bay B
        self.bayB = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayB.setGeometry(QtCore.QRect(450, 30, 231, 201))
        self.bayB.setAutoFillBackground(True)
        self.bayB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bayB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayB.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.bayB.setObjectName("bayB")

        self.B1 = QtWidgets.QPushButton(self.bayB)
        self.B1.setGeometry(QtCore.QRect(40, 20, 31, 71))
        self.B1.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.B1.setObjectName("B1")

        self.B2 = QtWidgets.QPushButton(self.bayB)
        self.B2.setGeometry(QtCore.QRect(40, 110, 31, 71))
        self.B2.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.B2.setObjectName("B2")

        self.B3 = QtWidgets.QPushButton(self.bayB)
        self.B3.setGeometry(QtCore.QRect(160, 20, 31, 71))
        self.B3.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.B3.setObjectName("B3")

        self.B4 = QtWidgets.QPushButton(self.bayB)
        self.B4.setGeometry(QtCore.QRect(160, 110, 31, 71))
        self.B4.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.B4.setObjectName("B4")

        ## Bay C
        self.bayC = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayC.setGeometry(QtCore.QRect(200, 260, 231, 201))
        self.bayC.setAutoFillBackground(True)
        self.bayC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bayC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayC.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.bayC.setObjectName("bayC")

        self.C1 = QtWidgets.QPushButton(self.bayC)
        self.C1.setGeometry(QtCore.QRect(30, 20, 31, 71))
        self.C1.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.C1.setObjectName("C1")

        self.C2 = QtWidgets.QPushButton(self.bayC)
        self.C2.setGeometry(QtCore.QRect(30, 110, 31, 71))
        self.C2.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.C2.setObjectName("C2")

        self.C3 = QtWidgets.QPushButton(self.bayC)
        self.C3.setGeometry(QtCore.QRect(170, 20, 31, 71))
        self.C3.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.C3.setObjectName("C3")

        self.C4 = QtWidgets.QPushButton(self.bayC)
        self.C4.setGeometry(QtCore.QRect(170, 110, 31, 71))
        self.C4.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.C4.setObjectName("C4")

        ## Bay D
        self.bayD = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayD.setGeometry(QtCore.QRect(450, 260, 231, 201))
        self.bayD.setAutoFillBackground(True)
        self.bayD.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bayD.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayD.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.bayD.setObjectName("bayD")

        self.D1 = QtWidgets.QPushButton(self.bayD)
        self.D1.setGeometry(QtCore.QRect(40, 20, 31, 71))
        self.D1.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.D1.setObjectName("D1")

        self.D2 = QtWidgets.QPushButton(self.bayD)
        self.D2.setGeometry(QtCore.QRect(40, 110, 31, 71))
        self.D2.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.D2.setObjectName("D2")

        self.D3 = QtWidgets.QPushButton(self.bayD)
        self.D3.setGeometry(QtCore.QRect(160, 20, 31, 71))
        self.D3.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.D3.setObjectName("D3")

        self.D4 = QtWidgets.QPushButton(self.bayD)
        self.D4.setGeometry(QtCore.QRect(160, 110, 31, 71))
        self.D4.setStyleSheet("background-color: rgb(115, 255, 104);")
        self.D4.setObjectName("D4")

        ## Assign/Back buttons
        self.buttAssign = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.assignBed(MainWindow))
        self.buttAssign.setGeometry(QtCore.QRect(1130, 640, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buttAssign.setFont(font)
        self.buttAssign.setObjectName("buttAssign")

        self.buttBack = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.showMonitor(MainWindow))
        self.buttBack.setGeometry(QtCore.QRect(50, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttBack.setFont(font)
        self.buttBack.setObjectName("buttBack")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1370, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setBedColours()

        ## BUTTON CONNECTIONS ##

        # bed buttons to choose bed
        self.A1.clicked.connect(self.chooseBed)
        self.A2.clicked.connect(self.chooseBed)
        self.A3.clicked.connect(self.chooseBed)
        self.A4.clicked.connect(self.chooseBed)
        self.B1.clicked.connect(self.chooseBed)
        self.B2.clicked.connect(self.chooseBed)
        self.B3.clicked.connect(self.chooseBed)
        self.B4.clicked.connect(self.chooseBed)
        self.C1.clicked.connect(self.chooseBed)
        self.C2.clicked.connect(self.chooseBed)
        self.C3.clicked.connect(self.chooseBed)
        self.C4.clicked.connect(self.chooseBed)
        self.D1.clicked.connect(self.chooseBed)
        self.D2.clicked.connect(self.chooseBed)
        self.D3.clicked.connect(self.chooseBed)
        self.D4.clicked.connect(self.chooseBed)
        self.R1.clicked.connect(self.chooseBed)
        self.R2.clicked.connect(self.chooseBed)
        self.R3.clicked.connect(self.chooseBed)
        self.R4.clicked.connect(self.chooseBed)
        #self.buttAssign.clicked.connect(self.assignBed)
        #self.buttBack.clicked.connect(________)


        ## array with all bed indices

        # bays = ["A", "B", "C", "D", "R"]
        # beds = ["1", "2", "3", "4"]
        # bedIndex = []
        # for bay in bays:
            # for bed in beds:
                # bedIndex.append(bay+bed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Details"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isolation"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Bed"))
        self.titleBA.setText(_translate("MainWindow", "Bed Allocation"))
        self.R1.setText(_translate("MainWindow", "R1"))
        self.R2.setText(_translate("MainWindow", "R2"))
        self.R3.setText(_translate("MainWindow", "R3"))
        self.R4.setText(_translate("MainWindow", "R4"))
        self.A1.setText(_translate("MainWindow", "A1"))
        self.A2.setText(_translate("MainWindow", "A2"))
        self.A3.setText(_translate("MainWindow", "A3"))
        self.A4.setText(_translate("MainWindow", "A4"))
        self.B1.setText(_translate("MainWindow", "B1"))
        self.B2.setText(_translate("MainWindow", "B2"))
        self.B3.setText(_translate("MainWindow", "B3"))
        self.B4.setText(_translate("MainWindow", "B4"))
        self.C1.setText(_translate("MainWindow", "C1"))
        self.C2.setText(_translate("MainWindow", "C2"))
        self.C3.setText(_translate("MainWindow", "C3"))
        self.C4.setText(_translate("MainWindow", "C4"))
        self.D1.setText(_translate("MainWindow", "D1"))
        self.D3.setText(_translate("MainWindow", "D3"))
        self.D2.setText(_translate("MainWindow", "D2"))
        self.D4.setText(_translate("MainWindow", "D4"))
        self.buttAssign.setText(_translate("MainWindow", "Assign"))
        self.buttBack.setText(_translate("MainWindow", "Back"))


##----------------------- FUNCTION TO DISPLAY WAITING LIST ON TABLE -------------------------##

    def displayList(self):

        size = getListSize() # from here, this is the function to update the waitlist from registrations saved in the database
        self.tableWidget.setRowCount(size) #setting the table row size
        row = 0
        listnow = getPatientinWaitlist() # get the waitlist in the database as a list

        for waitlistPat in listnow: #looping through each row of waitlist and add it to the table {first, last, age, gender, diagnosis, time, isolate}
            
            patient = getPatientInfo(waitlistPat[0])

            isoStatus = ""
            if patient[6] == 0:
                isoStatus = "N"
            elif patient[6] > 0:
                isoStatus = "Y"

            self.tableWidget.setRowHeight(row, 70)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)

            item.setText(str(patient[0]))
            self.tableWidget.setItem(row, idColumn, item) #id
            self.tableWidget.setItem(row, nameColumn, QtWidgets.QTableWidgetItem("{} {}".format(patient[1], patient[2]))) # name
            self.tableWidget.setItem(row, detailsColumn, QtWidgets.QTableWidgetItem(("Age: {} \nGender: {}").format(patient[3],patient[4]))) #age and gender
            self.tableWidget.setItem(row, isoColumn, QtWidgets.QTableWidgetItem(isoStatus)) # isolation

            row = row+1



##--------------------- FUNCTION TO ASSIGN BED BASED ON BUTTON PRESSED ----------------------------##

    def chooseBed(self):

        bedIndex = self.sender()    # listens to which button has been selected
        currRow = self.tableWidget.currentRow()
                  
        bedAvailable = self.bedStatusCheck(bedIndex)                # checking for current bed status availability 
        noDuplicates = self.duplicateCheck(bedColumn, bedIndex)     # checking for bed assignment duplicates in other rows
        isolation = self.isolationCheck(currRow, isoColumn)         # checking for isolation requirement

        # officially assigning bed to patient
        if noDuplicates and bedAvailable:
            if isolation:
                if bedIndex.text() == "R1" or bedIndex.text() == "R2" or bedIndex.text() == "R3" or bedIndex.text() == "R4":
                    self.tableWidget.setItem(currRow,bedColumn,QtWidgets.QTableWidgetItem(bedIndex.text()))     
            else:
                if bedIndex.text() != "R1" and bedIndex.text() != "R2" and bedIndex.text() != "R3" and bedIndex.text() != "R4":
                    self.tableWidget.setItem(currRow,bedColumn,QtWidgets.QTableWidgetItem(bedIndex.text()))

        # self.sender().setStyleSheet("background-color: white;")
        # if add colour, need to find way to revert the original back if another bed is chosen


    def duplicateCheck(self, column, bedIndex):
        noDuplicates = True
        for row in range(self.tableWidget.rowCount()): 
            _item = self.tableWidget.item(row, column)          # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
            if _item:            
                item = self.tableWidget.item(row, column).text()       # gets cell item name
                if item == bedIndex.text():
                    noDuplicates = False
        return noDuplicates

    def bedStatusCheck(self, bedIndex): 
        bedAvailable = True
        bedOccupied = self.getOccupiedBeds()

        for bed in bedOccupied:     # checking current bed against list of occupied beds
            if bedIndex.text() == bed:     # if current bed is an occupied bed
                bedAvailable = False        # then bed is set as unavailable
                break
        
        return bedAvailable
    
    def isolationCheck(self, currRow, isoColumn):
        isolation = False
        i_item = self.tableWidget.item(currRow, isoColumn)          # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
        if i_item:
            item = self.tableWidget.item(currRow, isoColumn).text()
            if item == "Y":
                isolation = True
            elif item == "N":
                isolation = False
        return isolation



##------------------------- FUNCTIONS TO COLOUR AVAILABLE BEDS ---------------------------##

    # fetching for list of beds currently being occupied
    def getOccupiedBeds(self):
        patsBeds = getPatientsinBed()   
        bedOccupied = []

        for pat in patsBeds:
            bedOccupied.append(pat[1])

        return bedOccupied

    def setBedColours(self):
        bedOccupied = self.getOccupiedBeds()
        bedButtons = self.bedlayoutframe.findChildren(QPushButton)      # fetches list of bed buttons
        
        for button in bedButtons:
            for bed in bedOccupied:
                if button.objectName() == bed:                      # if bed is occupied,
                    brush = "background-color: rgb(190, 190, 190)"
                    button.setStyleSheet(brush)



##---------------------- FUNCTION TO CONTROL ACTIONS AFTER "ASSIGN" IS PRESSED -------------------------------##             


    def assignBed(self, MainWindow):                               
        self.buttAssign.setEnabled(False)

        patsWithBeds = self.findPatsWithBeds()      # collect a list of patients that have been assigned beds
        print("patsWithBeds")
        print(patsWithBeds)

        for pat in patsWithBeds:
            addtoBed(pat[0],pat[1],0,0,0,0,"Select",0) # add patsWithBeds to "patientStatus" table in DB
            deletePatfromWaitlist(pat[0])         # delete patsWithBeds from "waitlist" table in DB
            print("added patient")

        #return to main screen
        print("about to close window")
        self.showMonitor(MainWindow)
     
            
    def findPatsWithBeds(self):
        totRowNum = self.tableWidget.rowCount()
        patsWithBeds = []

        for row in range(totRowNum):
            # check if bedColumn is filled
            item = self.tableWidget.item(row, bedColumn)       # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
            if item:  # if patient has been given a bed
                # fetch patID (in idColumn) + bedIndex (in bedColumn)
                patID = int(self.tableWidget.item(row, idColumn).text())
                bedIndex = self.tableWidget.item(row, bedColumn).text()
                patBed = [patID, bedIndex]  # patID & bed for ONE patient

                patsWithBeds.append(patBed) # add to list of ALL patients with beds

        return patsWithBeds

    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
