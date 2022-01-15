# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from amu_database import getColournum, bedAvailability, getPatientsinBed
from waitlist import Ui_waitlist
from PyQt5.QtCore import QTimer, QTime, Qt, pyqtPickleProtocol
import threading 

class Ui_MainWindow2(object):
        
    def showBox(self): #display access error message
        msg= QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Access Error")
        msg.setText("You don't have access to this function.")
        msg.setStandardButtons(QtWidgets.QMessageBox.Abort)
        x= msg.exec_()
        msg.buttonClicked.connect(self.closeBox)

    def closeBox(self, msg): #close message box
            pass

    def showWaitlist(self, monitor, user, phototag, pos): #show waitlist window
        if self.pos == 'amu' or self.pos == 'juniordoc' or self.pos == 'consultant'  :
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_waitlist()
                self.ui.setupUi(self.window, user, phototag, pos)
                self.ui.phototag= self.phototag
                self.ui.user= self.user
                self.ui.pos= self.pos
                self.window.show()
                monitor.close()
        else: 
                self.showBox()

    def showBed(self, monitor, user, phototag, pos): #show Bed allocation window
        from bed_allocation import Ui_MainWindow
        if self.pos == 'amu' or self.pos == 'juniordoc' or self.pos == 'consultant'  :
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window, user, phototag, pos)
                self.window.show()
                monitor.close()
        else: 
                self.showBox()
                
    def showPatientinBed(self, monitor,  user, phototag, pos): # show patient window
        from patientStatus import Ui_patientStatus
        if self.pos == 'amu' or self.pos == 'juniordoc' or self.pos == 'consultant'  :
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_patientStatus()
                self.ui.setupUi(self.window, user, phototag, pos)
                self.window.show()
                monitor.close()
        else: 
                self.showBox()

    def showdownWard(self, user, phototag, pos): # show patient window
        from wardBedEdit import Ui_MainWindow
        if self.pos == 'staff' or self.pos == 'amu':
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window, user, phototag, pos)
                self.window.show()
        else: 
                self.showBox()

    def setupUi(self, MainWindow2, user, phototag, pos):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow2.resize(1440, 847)
        MainWindow2.setStyleSheet("background-color: white;")
        self.pos= pos
        self.user= user
        self.phototag= phototag
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.title_AMU = QtWidgets.QLabel(self.centralwidget)
        self.title_AMU.setGeometry(QtCore.QRect(50, -10, 241, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.title_AMU.setFont(font)
        self.title_AMU.setObjectName("title_AMU")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(1060, 670, 371, 131))
        self.widget_6.setStyleSheet("background-color: transparent;\n"
"border-image:url(:/Icons/imperial-college-healthcare-nhs-trust-logo-vector.png);\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;")
        self.widget_6.setObjectName("widget_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(470, 90, 551, 241))
        self.frame.setStyleSheet("background-color: transparent;\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.green = QtWidgets.QLabel(self.frame)
        self.green.setGeometry(QtCore.QRect(70, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.green.setFont(font)
        self.green.setObjectName("green")
        self.yellow = QtWidgets.QLabel(self.frame)
        self.yellow.setGeometry(QtCore.QRect(70, 110, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.yellow.setFont(font)
        self.yellow.setObjectName("yellow")
        self.red = QtWidgets.QLabel(self.frame)
        self.red.setGeometry(QtCore.QRect(70, 160, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.red.setFont(font)
        self.red.setObjectName("red")
        self.black = QtWidgets.QLabel(self.frame)
        self.black.setGeometry(QtCore.QRect(70, 210, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.black.setFont(font)
        self.black.setObjectName("black")
        self.waitstatbckground = QtWidgets.QLabel(self.frame)
        self.waitstatbckground.setGeometry(QtCore.QRect(10, 0, 501, 241))
        self.waitstatbckground.setText("")
        self.waitstatbckground.setPixmap(QtGui.QPixmap(":/graphics/Graphics_Monitor/Highlight.png"))
        self.waitstatbckground.setScaledContents(True)
        self.waitstatbckground.setObjectName("waitstatbckground")
        self.bedavailable = QtWidgets.QLabel(self.frame)
        self.bedavailable.setGeometry(QtCore.QRect(320, 70, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.bedavailable.setFont(font)
        self.bedavailable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bedavailable.setObjectName("bedavailable")
        self.waitstatbckground.raise_()
        self.green.raise_()
        self.yellow.raise_()
        self.red.raise_()
        self.black.raise_()
        self.bedavailable.raise_()
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(1190, 110, 121, 121))
        self.photo.setStyleSheet("background-image:url(:/graphics/Graphics_Monitor/{});\n"
"background-repeat: no-repeat; \n"
"background-position: center;\n"
"border-radius: 60px;".format(self.phototag))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(1110, 250, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        if self.pos== 'juniordoc' or self.pos== 'consultant':
                self.username.setText("Dr {}".format(self.user))
        else: 
                self.username.setText("{}".format(self.user))
        self.username.setFont(font)
        self.username.setScaledContents(False)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setWordWrap(True)
        self.username.setObjectName("username")

        # waitlist button on side menu
        self.editbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.showWaitlist(MainWindow2, self.user, self.phototag, self.pos))
        self.editbutton.setGeometry(QtCore.QRect(50, 130, 261, 171))
        self.editbutton.setStyleSheet("background-color: transparent;\n"
"border-image:url(:/graphics/Graphics_Monitor/New Icon Waitlist.png);\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;\n"
"")
        self.editbutton.setText("")
        self.editbutton.setObjectName("editbutton")

        # bed allocation button on side menu
        self.allocationbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.showBed(MainWindow2, self.user, self.phototag, self.pos))
        self.allocationbutton.setGeometry(QtCore.QRect(50, 300, 261, 141))
        self.allocationbutton.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/graphics/Graphics_Monitor/New Icon Bed Allocation.png);\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;\n"
"")
        self.allocationbutton.setText("")
        self.allocationbutton.setObjectName("allocationbutton")

        # patient status button on side menu
        self.patientinbedbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.showPatientinBed(MainWindow2, self.user, self.phototag, self.pos))
        self.patientinbedbutton.setGeometry(QtCore.QRect(50, 440, 271, 141))
        self.patientinbedbutton.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/graphics/Graphics_Monitor/New Icon Patient Status.png);\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;\n"
"")
        
        self.patientinbedbutton.setObjectName("patientinbedbutton")

        # edit downstream ward bed availability button on side menu
        self.downWardButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.showdownWard(self.user, self.phototag, self.pos))
        self.downWardButton.setGeometry(QtCore.QRect(50, 580, 271, 141))
        self.downWardButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/graphics/Graphics_Monitor/New Icon Ward Availability.png);\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;\n"
"")
        self.downWardButton.setObjectName("downWardButton")

        # title box for "waitlist status"
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(460, 20, 61, 61))
        self.groupBox_2.setStyleSheet("background-color: transparent;\n"
"border-image:url(:/graphics/Graphics_Monitor/output-onlinepngtools(21).png);\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;")
        self.groupBox_2.setObjectName("groupBox_2")

        self.title_AMUstatus = QtWidgets.QLabel(self.centralwidget)
        self.title_AMUstatus.setGeometry(QtCore.QRect(540, 30, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.title_AMUstatus.setFont(font)
        self.title_AMUstatus.setObjectName("title_AMUstatus")

        # title box for "amu bed live monitor"
        self.title_bedMonitor = QtWidgets.QLabel(self.centralwidget)
        self.title_bedMonitor.setGeometry(QtCore.QRect(530, 360, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.title_bedMonitor.setFont(font)
        self.title_bedMonitor.setObjectName("title_bedMonitor")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(460, 350, 61, 51))
        self.groupBox.setStyleSheet("background-color: transparent;\n"
"border-image:url(:/graphics/Graphics_Monitor/output-onlinepngtools(12).png);\n"
"background: none;\n"
"border:none;\n"
"background-repeat:none;")
        self.groupBox.setObjectName("groupBox")

        # map of bed layout in amu
        self.bedlayoutframe = QtWidgets.QFrame(self.centralwidget)
        self.bedlayoutframe.setGeometry(QtCore.QRect(480, 420, 581, 341))
        self.bedlayoutframe.setStyleSheet("background-color:rgba(239, 239, 239, 211)")
        self.bedlayoutframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bedlayoutframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bedlayoutframe.setObjectName("bedlayoutframe")

        # self isolation room 1
        self.sr1 = QtWidgets.QFrame(self.bedlayoutframe)
        self.sr1.setGeometry(QtCore.QRect(20, 20, 101, 51))
        self.sr1.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.sr1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sr1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sr1.setObjectName("sr1")
        self.R1 = QtWidgets.QLabel(self.sr1)
        self.R1.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.R1.setAlignment(QtCore.Qt.AlignCenter)
        self.R1.setText("R1")
        self.R1.setObjectName("R1")

        # self isolation room 2
        self.sr2 = QtWidgets.QFrame(self.bedlayoutframe)
        self.sr2.setGeometry(QtCore.QRect(20, 100, 101, 51))
        self.sr2.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.sr2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sr2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sr2.setObjectName("sr2")
        self.R2 = QtWidgets.QLabel(self.sr2)
        self.R2.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.R2.setAlignment(QtCore.Qt.AlignCenter)
        self.R2.setText("R2")
        self.R2.setObjectName("R2")

        # self isolation room 3
        self.sr3 = QtWidgets.QFrame(self.bedlayoutframe)
        self.sr3.setGeometry(QtCore.QRect(20, 180, 101, 51))
        self.sr3.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.sr3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sr3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sr3.setObjectName("sr3")
        self.R3 = QtWidgets.QLabel(self.sr3)
        self.R3.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.R3.setAlignment(QtCore.Qt.AlignCenter)
        self.R3.setText("R3")
        self.R3.setObjectName("R3")

        # self isolation room 4
        self.sr4 = QtWidgets.QFrame(self.bedlayoutframe)
        self.sr4.setGeometry(QtCore.QRect(20, 260, 101, 51))
        self.sr4.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.sr4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sr4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sr4.setObjectName("sr4")
        self.R4 = QtWidgets.QLabel(self.sr4)
        self.R4.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.R4.setAlignment(QtCore.Qt.AlignCenter)
        self.R4.setText("R4")
        self.R4.setObjectName("R4")

        # bay A
        self.bayA = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayA.setGeometry(QtCore.QRect(160, 20, 181, 131))
        self.bayA.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.bayA.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bayA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayA.setObjectName("bayA")

        self.A1 = QtWidgets.QLabel(self.bayA)
        self.A1.setGeometry(QtCore.QRect(25, 10, 31, 51))
        self.A1.setAlignment(QtCore.Qt.AlignCenter)
        self.A1.setText("A1")
        self.A1.setObjectName("A1")

        self.A2 = QtWidgets.QLabel(self.bayA)
        self.A2.setGeometry(QtCore.QRect(25, 70, 31, 51))
        self.A2.setAlignment(QtCore.Qt.AlignCenter)
        self.A2.setText("A2")
        self.A2.setObjectName("A2")

        self.A3 = QtWidgets.QLabel(self.bayA)
        self.A3.setGeometry(QtCore.QRect(120, 10, 31, 51))
        self.A3.setAlignment(QtCore.Qt.AlignCenter)
        self.A3.setText("A3")
        self.A3.setObjectName("A3")

        self.A4 = QtWidgets.QLabel(self.bayA)
        self.A4.setGeometry(QtCore.QRect(120, 70, 31, 51))
        self.A4.setAlignment(QtCore.Qt.AlignCenter)
        self.A4.setText("A4")
        self.A4.setObjectName("A4")

        # bay B
        self.bayB = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayB.setGeometry(QtCore.QRect(370, 20, 181, 131))
        self.bayB.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.bayB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bayB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayB.setObjectName("bayB")

        self.B1 = QtWidgets.QLabel(self.bayB)
        self.B1.setGeometry(QtCore.QRect(25, 10, 31, 51))
        self.B1.setAlignment(QtCore.Qt.AlignCenter)
        self.B1.setText("B1")
        self.B1.setObjectName("B1")

        self.B2 = QtWidgets.QLabel(self.bayB)
        self.B2.setGeometry(QtCore.QRect(25, 70, 31, 51))
        self.B2.setAlignment(QtCore.Qt.AlignCenter)
        self.B2.setText("B2")
        self.B2.setObjectName("B2")

        self.B3 = QtWidgets.QLabel(self.bayB)
        self.B3.setGeometry(QtCore.QRect(120, 10, 31, 51))
        self.B3.setAlignment(QtCore.Qt.AlignCenter)
        self.B3.setText("B3")
        self.B3.setObjectName("B3")

        self.B4 = QtWidgets.QLabel(self.bayB)
        self.B4.setGeometry(QtCore.QRect(120, 70, 31, 51))
        self.B4.setAlignment(QtCore.Qt.AlignCenter)
        self.B4.setText("B4")
        self.B4.setObjectName("B4")

        # bay C
        self.bayC = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayC.setGeometry(QtCore.QRect(160, 180, 181, 131))
        self.bayC.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.bayC.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bayC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayC.setObjectName("bayC")

        self.C1 = QtWidgets.QLabel(self.bayC)
        self.C1.setGeometry(QtCore.QRect(25, 10, 31, 51))
        self.C1.setAlignment(QtCore.Qt.AlignCenter)
        self.C1.setText("C1")
        self.C1.setObjectName("C1")

        self.C2 = QtWidgets.QLabel(self.bayC)
        self.C2.setGeometry(QtCore.QRect(25, 70, 31, 51))
        self.C2.setAlignment(QtCore.Qt.AlignCenter)
        self.C2.setText("C2")
        self.C2.setObjectName("C2")

        self.C3 = QtWidgets.QLabel(self.bayC)
        self.C3.setGeometry(QtCore.QRect(120, 10, 31, 51))
        self.C3.setAlignment(QtCore.Qt.AlignCenter)
        self.C3.setText("C3")
        self.C3.setObjectName("C3")

        self.C4 = QtWidgets.QLabel(self.bayC)
        self.C4.setGeometry(QtCore.QRect(120, 70, 31, 51))
        self.C4.setAlignment(QtCore.Qt.AlignCenter)
        self.C4.setText("C4")
        self.C4.setObjectName("C4")

        # bay D
        self.bayD = QtWidgets.QFrame(self.bedlayoutframe)
        self.bayD.setGeometry(QtCore.QRect(370, 180, 181, 131))
        self.bayD.setStyleSheet("background-color:rgb(31, 127, 90)")
        self.bayD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bayD.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bayD.setObjectName("bayD")

        self.D1 = QtWidgets.QLabel(self.bayD)
        self.D1.setGeometry(QtCore.QRect(25, 10, 31, 51))
        self.D1.setAlignment(QtCore.Qt.AlignCenter)
        self.D1.setText("D1")
        self.D1.setObjectName("D1")

        self.D2 = QtWidgets.QLabel(self.bayD)
        self.D2.setGeometry(QtCore.QRect(25, 70, 31, 51))
        self.D2.setAlignment(QtCore.Qt.AlignCenter)
        self.D2.setText("D2")
        self.D2.setObjectName("D2")

        self.D3 = QtWidgets.QLabel(self.bayD)
        self.D3.setGeometry(QtCore.QRect(120, 10, 31, 51))
        self.D3.setAlignment(QtCore.Qt.AlignCenter)
        self.D3.setText("D3")
        self.D3.setObjectName("D3")

        self.D4 = QtWidgets.QLabel(self.bayD)
        self.D4.setGeometry(QtCore.QRect(120, 70, 31, 51))
        self.D4.setAlignment(QtCore.Qt.AlignCenter)
        self.D4.setText("D4")
        self.D4.setObjectName("D4")

        self.title_AMU.raise_()
        self.widget_6.raise_()
        self.frame.raise_()
        self.editbutton.raise_()
        self.allocationbutton.raise_()
        self.patientinbedbutton.raise_()
        self.downWardButton.raise_()
        self.photo.raise_()
        self.username.raise_()
        self.groupBox_2.raise_()
        self.title_bedMonitor.raise_()
        self.groupBox.raise_()
        self.bedlayoutframe.raise_()
        self.title_AMUstatus.raise_()

        # update number of patients in waitlist of their respective priority categories
        collist= getColournum()
        self.green.setText(str(collist[0][0]))
        self.yellow.setText(str(collist[0][1]))
        self.red.setText(str(collist[0][2]))
        self.black.setText(str(collist[0][3]))

        self.setBedStatusCol()

        MainWindow2.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)



## ----------------------------colour coding for bed allocation--------------------------------------------

# occupied      grey    rgb(190, 190, 190)
# discharge     red     rgb(239, 83, 80)
# downstream    blue    rgb(79, 195, 247)
# free          green   rgb(115, 255, 104)

    
    # fetch list of occupied beds and their corrresponding destination plan status colours
    def getBedStatus(self):
        
        patsBeds = getPatientsinBed()   # pat in patsBeds, pat[1] = bed, pat[2] = discharge, pat[6] = downstream
        bedStatus = []
        # print(patsBeds)

        for pat in patsBeds:

            if pat[2] > 0:                  # check if discharge is selected
                brush = "background-color: rgb(239, 83, 80)"    # set red
                bedStatus.append([pat[1],brush])
            elif pat[6] != "Select":        # check if downstream is selected (by checking if ward has been assigned)
                brush = "background-color: rgb(79, 195, 247)"   # set blue
                bedStatus.append([pat[1],brush])
            else:                           # else, this bed is marked as occupied
                brush = "background-color: rgb(190, 190, 190)"  # set grey
                bedStatus.append([pat[1],brush])
            
        return bedStatus


    def setBedStatusCol(self):

        bedStatus = self.getBedStatus()     # gets list of beds that are currently occupied + their status (from function above)
        # print(bedStatus)

        # fetch list of bed labels:
        bedLabel = self.bedlayoutframe.findChildren(QtWidgets.QLabel)
        
        # for bed in bedLabel:
        #     print(bed.objectName())

        for label in bedLabel:
            for bed in bedStatus:
                if label.objectName() == bed[0]:       # for each label, cross check with corresponding info
                    label.setStyleSheet(bed[1])        # if bed is occupied, update colour accordingly with "brush" (aka. red, blue, or grey)
                    break
                else:
                    label.setStyleSheet("background-color: rgb(154, 255, 117)")  # if bed is not occupied, default is to mark bed as free (aka. green)



    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Bed Manager"))
        self.title_AMU.setText(_translate("MainWindow2", "<html><head/><body><p>Acute Medical Unit </p><p>Management Systems</p></body></html>"))
        freeBeds = 20 - len(getPatientsinBed())
        self.bedavailable.setText(_translate("MainWindow2", str(freeBeds)))
        self.title_bedMonitor.setText(_translate("MainWindow2", "AMU Bed Live Monitoring"))
        self.title_AMUstatus.setText(_translate("MainWindow2", "AMU Status"))

import mongraphics




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
