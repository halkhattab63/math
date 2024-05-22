# import math
# import tkinter as tk
# from tkinter import messagebox

# def is_prime(number):
#     if number < 2:
#         return False
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(number)) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# def check_prime():
#     try:
#         number = int(entry.get())        
#         if is_prime(number):
#             result = f"Your number is {number}\nThis number is a prime number."
#         else:
#             result = f"Your number is {number}\nThis number is not a prime number."

#         messagebox.showinfo("Result", result)
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# # إنشاء نافذة الواجهة
# root = tk.Tk()
# root.title("Prime Number Checker")

# # إضافة عناصر الواجهة
# label = tk.Label(root, text="Please enter your number for checking if it's a prime number:")
# label.pack(pady=10)

# entry = tk.Entry(root)
# entry.pack(pady=10)

# check_button = tk.Button(root, text="Check", command=check_prime)
# check_button.pack(pady=10)

# # تشغيل حلقة الرسائل الرئيسية للواجهة
# root.mainloop()



# import sys
# import math
# import time
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

# def is_prime(number):
#     if number < 2:
#         return False
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(number)) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# class PrimeCheckerApp(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Prime Number Checker')

#         layout = QVBoxLayout()

#         self.label = QLabel('Please enter your number for checking if it\'s a prime number:')
#         layout.addWidget(self.label)

#         self.entry = QLineEdit(self)
#         layout.addWidget(self.entry)

#         self.check_button = QPushButton('Check', self)
#         self.check_button.clicked.connect(self.check_prime)
#         layout.addWidget(self.check_button)

#         self.setLayout(layout)

#     def check_prime(self):
#         try:
#             number = int(self.entry.text())
#             start_time = time.time()

#             if is_prime(number):
#                 result = f"Your number is {number}\nThis number is a prime number."
#             else:
#                 result = f"Your number is {number}\nThis number is not a prime number."

#             end_time = time.time()
#             execution_time = end_time - start_time
#             result += f"\nRunning time: {execution_time:.6f} seconds"

#             QMessageBox.information(self, 'Result', result)
#         except ValueError:
#             QMessageBox.critical(self, 'Invalid Input', 'Please enter a valid integer.')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = PrimeCheckerApp()
#     ex.show()
#     sys.exit(app.exec_())

import sys
import math
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSlider, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

class PrimeCheckerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Prime Number Checker')

        layout = QVBoxLayout()

        self.label = QLabel('Enter your number or use the slider:')
        layout.addWidget(self.label)

        self.entry = QLineEdit(self)
        layout.addWidget(self.entry)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10000)
        self.slider.setValue(0)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.update_entry)
        layout.addWidget(self.slider)

        self.check_button = QPushButton('Check', self)
        self.check_button.clicked.connect(self.check_prime)
        layout.addWidget(self.check_button)

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(['Number', 'Is Prime?'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        self.setLayout(layout)

        # تطبيق بعض الأنماط لتحسين الشكل
        self.setStyleSheet("""
            QWidget {
                font-size: 16px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: white;
                color: black;
                border: 2px solid #4CAF50;
            }
        """)

    def update_entry(self):
        self.entry.setText(str(self.slider.value()))

    def check_prime(self):
        try:
            number = int(self.entry.text())
            start_time = time.time()

            if is_prime(number):
                result = "Yes"
            else:
                result = "No"

            end_time = time.time()
            execution_time = end_time - start_time

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(str(number)))
            self.table.setItem(row_position, 1, QTableWidgetItem(result))

            QMessageBox.information(self, 'Result', f"Checked number: {number}\nIs prime? {result}\nRunning time: {execution_time:.6f} seconds")
        except ValueError:
            QMessageBox.critical(self, 'Invalid Input', 'Please enter a valid integer.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PrimeCheckerApp()
    ex.show()
    sys.exit(app.exec_())
