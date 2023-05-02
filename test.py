from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # QLCDNumber 위젯 생성
        self.lcdNumber = QtWidgets.QLCDNumber(self)
        self.lcdNumber.setDigitCount(5)

        # QPushButton 위젯 생성
        self.button = QtWidgets.QPushButton('Click me!', self)

        # 버튼 시그널 연결
        self.button.clicked.connect(self.on_button_clicked)

        # 위젯 위치 설정
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.lcdNumber)
        layout.addWidget(self.button)

    # 버튼 클릭 시 호출될 메서드
    def on_button_clicked(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
