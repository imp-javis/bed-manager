from PyQt5 import QtCore
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

########################## Create table ##############################

tableWidget = QtWidgets.QTableWidget()
tableWidget.setGeometry(QtCore.QRect(200, 200, 250, 300))
tableWidget.setColumnCount(2)
tableWidget.setRowCount(9)
tableWidget.show()

################# Create tablecontent & comboboxes ###################

def dosomething(index):
    widget = app.sender()
    print('widget object:', widget)
    print('widget myname:', widget.my_name)
    print('widget index:', combo_list.index(widget))
    print('option index:', index)
    print('index name:', widget.currentText())

    print(combo_list)

#---------------------------------------------------------------------

names = ['Name 1', 'Name 2', 'Name 3', 'Name 4']
combo_option_list = ["Choose...", "Option 1", "Option 2", "Option 3", "Option 4"]

combo_list = []

for i, name in enumerate(names):

    tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(name))

    combobox = QtWidgets.QComboBox()
    combobox.addItems(combo_option_list)
    combobox.my_name = name + ' (i=' + str(i) + ')'
    combobox.currentIndexChanged.connect(dosomething)

    combo_list.append(combobox)

    tableWidget.setCellWidget(i, 1, combobox)

#---------------------------------------------------------------------

sys.exit(app.exec_())
