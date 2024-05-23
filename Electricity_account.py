# قم بعمل مخطط تدفقي يقوم بحساب فاتورة الكهرباء وفقاً لعدد الوحدات الكهربائية المتسخدمة.

# أول 50 وحدة = 1 ليرة للوحدة الواحدة   ،      ال 100 وحدة التالية = 1,5 ليرة للوحدة
# ال 150 وحدة التالية = 2 ليرة للوحدة
# (مثال : إذا كان عدد الوحدات المستخدمة 140 عندها تكون الفاتورة بالشكل 50 * 1 + 90 * 1,5)


# def calculate_electricity_bill(units):
#     bill = 0 
#     if units <= 50 : 
#         bill = units * 1
        
#     elif units <= 150 :
#         bill = 50*1 + (units - 50)*1.5
        
#     else:
#         bill = 50*1 + 100*1.5 + (units - 150)*2 
    

# units_used = 345
# total_bill = calculate_electricity_bill(units_used)
# print("Total electricity bill = ", total_bill)


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def calculate_electricity_bill(units):
    bill = 0
    if units <= 50:
        bill = units * 1
    elif units <= 150:
        bill = 50 * 1 + (units - 50) * 1.5
    else:
        bill = 50 * 1 + 100 * 1.5 + (units - 150) * 2
    return bill

class BillDetailsDialog(QtWidgets.QDialog):
    def __init__(self, units, bill, parent=None):
        super().__init__(parent)
        self.units = units
        self.bill = bill
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(f"Units used: {self.units}")
        label.setFont(QtGui.QFont("Arial", 14))
        layout.addWidget(label)

        bill_label = QtWidgets.QLabel(f"Total bill: {self.bill} TL")
        bill_label.setFont(QtGui.QFont("Arial", 14))
        layout.addWidget(bill_label)

        plot_button = QtWidgets.QPushButton("Show Bill Breakdown")
        plot_button.setFont(QtGui.QFont("Arial", 12))
        plot_button.setStyleSheet("background-color: #5DADE2; color: white;")
        plot_button.clicked.connect(self.show_breakdown)
        layout.addWidget(plot_button)

        self.setLayout(layout)
        self.setWindowTitle("Bill Details")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #EAEDED;")

    def show_breakdown(self):
        fig, ax = plt.subplots()

        parts = []
        costs = []

        if self.units > 0:
            parts.append("First 50 units")
            costs.append(min(self.units, 50) * 1)
        if self.units > 50:
            parts.append("Next 100 units")
            costs.append(min(max(self.units - 50, 0), 100) * 1.5)
        if self.units > 150:
            parts.append("Beyond 150 units")
            costs.append(max(self.units - 150, 0) * 2)

        ax.pie(costs, labels=parts, autopct='%1.1f%%', startangle=140, colors=['#FF9999', '#66B2FF', '#99FF99'])
        ax.axis('equal')

        canvas = FigureCanvas(fig)
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Bill Breakdown")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(canvas)
        dialog.setLayout(layout)
        dialog.setFixedSize(500, 400)
        dialog.exec_()

class ElectricityBillCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QtWidgets.QFormLayout()

        label = QtWidgets.QLabel("Enter the number of units used:")
        label.setFont(QtGui.QFont("Arial", 12))
        layout.addRow(label)

        self.units_input = QtWidgets.QLineEdit()
        self.units_input.setFont(QtGui.QFont("Arial", 12))
        layout.addRow(self.units_input)

        self.calculate_button = QtWidgets.QPushButton("Calculate Bill")
        self.calculate_button.setFont(QtGui.QFont("Arial", 12))
        self.calculate_button.setStyleSheet("background-color: #5DADE2; color: white;")
        self.calculate_button.clicked.connect(self.show_bill)
        layout.addWidget(self.calculate_button)

        central_widget.setLayout(layout)

        self.setWindowTitle('Electricity Bill Calculator')
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #EAEDED;")

    def show_bill(self):
        try:
            units_used = int(self.units_input.text())
            total_bill = calculate_electricity_bill(units_used)
            dialog = BillDetailsDialog(units_used, total_bill, self)
            dialog.exec_()
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Invalid Input", "Please enter a valid number of units")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ElectricityBillCalculator()
    ex.show()
    sys.exit(app.exec_())
