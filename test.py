import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class CustomTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            current_row = self.currentRow()
            if current_row > 0:
                self.move_row(current_row, current_row - 1)
                self.setCurrentCell(current_row - 1, 0)
        else:
            super().keyPressEvent(event)

    def move_row(self, source_row, destination_row):
        for col in range(self.columnCount()):
            source_item = self.takeItem(source_row, col)
            destination_item = self.takeItem(destination_row, col)
            self.setItem(destination_row, col, source_item)
            self.setItem(source_row, col, destination_item)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 테이블 위젯 예제')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.table_widget = CustomTableWidget()
        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(1)

        for i in range(10):
            item = QTableWidgetItem(f"항목 {i+1}")
            self.table_widget.setItem(i, 0, item)

        layout.addWidget(self.table_widget)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
