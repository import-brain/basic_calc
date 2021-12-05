import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('calculator')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{background-color: white; color: #000; font-size: 45px;}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''),
                     'background: #d5580d;'
                     'color: #fff;'
                     'font-weight: 700;')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('<'), 2, 4, 1, 1, lambda: self.display.setText(
            self.display.text()[:-1]
        ), 'background: #13823a;'
           'color: #fff;'
            'font-weight: 700;')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1, self.calc, 'background: #095177;' 'color: #fff;' 'font-weight: 700;')

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not function:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(function)
        if style:
            btn.setStyleSheet(style)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def calc(self):
        try:
            # calc..
            ...
        except Exception as e:
            # error...
            ...


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
