import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QAbstractItemView, QTableWidgetItem

from main import Ui_MainWindow
import random


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.comboBox.addItem("Super Lotto")
        self.comboBox.addItem("Color Ball")
        self.pushButton.clicked.connect(self.createTicket)


    def createTicket(self):
        ticketList = []
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        if self.comboBox.currentText() == "Super Lotto":
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(['前区', '后区'])
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
            self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置整行选中
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止列表编辑
            for i in range(0, 5):
                number1 = list(range(1, 36))
                number2 = list(range(1, 13))
                ticket_up = random.sample(number1, 5)
                ticket_up = str(ticket_up).replace('[', '').replace(']', '')  # 去除[]
                ticket_down = random.sample(number2, 2)
                ticket_down = str(ticket_down).replace('[', '').replace(']', '')  # 去除[]
                ticketList.append(str(ticket_up) + "  " + str(ticket_down))
                strValue1 = QTableWidgetItem(str(ticket_up))
                strValue2 = QTableWidgetItem(str(ticket_down))
                self.tableWidget.setItem(i, 0, strValue1)
                self.tableWidget.setItem(i, 1, strValue2)
        elif self.comboBox.currentText() == "Color Ball":
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(['前区', '后区'])
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
            self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置整行选中
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止列表编辑
            for i in range(0, 5):
                number1 = list(range(1, 34))
                number2 = list(range(1, 17))
                ticket_up = random.sample(number1, 7)
                ticket_up = str(ticket_up).replace('[', '').replace(']', '')  # 去除[]
                ticket_down = random.sample(number2, 1)
                ticket_down = str(ticket_down).replace('[', '').replace(']', '')  # 去除[]
                ticketList.append(str(ticket_up) + "  " + str(ticket_down))
                strValue1 = QTableWidgetItem(str(ticket_up))
                strValue2 = QTableWidgetItem(str(ticket_down))
                self.tableWidget.setItem(i, 0, strValue1)
                self.tableWidget.setItem(i, 1, strValue2)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())