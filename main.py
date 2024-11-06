import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PySide6.QtGui import QPixmap, QIcon
from UI.main_window import Ui_MainWindow
from services.calculations import linear_regression

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Iнтерполяцiя та екстраполяцiя, апроксимацiя, регресiя")
        self.setWindowIcon(QIcon("ico.png"))
        
        self.ui.calc_btn.clicked.connect(self.calculate)
        
        self.ui.X_input.setText("1 2 3 4 5 6 7 8")
        self.ui.Y_input.setText("521 308 240 204 183 175 159 152")
        
    def calculate(self):
        try:
            x = np.array(list(map(float, self.ui.X_input.text().replace(",", ".").split())))
        except ValueError:
            dlg = CustomDialog("Помилка вводу X")
            if dlg.exec():
                return
            
        try:
            y = np.array(list(map(float, self.ui.Y_input.text().replace(",", ".").split())))
        except ValueError:
            dlg = CustomDialog("Помилка вводу Y")
            if dlg.exec():
                return
        
        m, b = linear_regression(x, y)
        self.plot_regression(x, y, m, b)
    
    def plot_regression(self, x, y, m, b):
        
        plt.figure(figsize=(6, 4.5), dpi=100)
        plt.scatter(x, y, color='blue', label='Експериментальні точки')
        
        y_pred = m * x + b
        plt.plot(x, y_pred, color='green', label='Лінія регресії')
        
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Лінійна регресія методом найменших квадратів")
        plt.legend()
        plt.grid(True)
        plt.savefig('plot.png')
        self.ui.img_place.setPixmap(QPixmap("plot.png"))


class CustomDialog(QDialog):
    def __init__(self, msg:str):
        super().__init__()

        self.setWindowTitle("Помилка")

        QBtn = (
            QDialogButtonBox.Ok
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message = QLabel(msg)
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())