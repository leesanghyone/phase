import sys
from PyQt5.QtWidgets import *
from waitlist_dialog_gui import Ui_waitlistDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class WaitlistDialog(QDialog,Ui_waitlistDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initsiganal()
        self.tableWidget.keyPressEvent=self.keyPressEvent #주석: 이미 키보드함수 실행되고 있음, 그 값을 바꾸는 것 뿐이다.
    
    def initsiganal(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["순서","작업시간","플랫폼"])
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,70)

        #테이블 헤더 스타일 변경
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setStyleSheet("""
            QHeaderView::section {
                border-bottom: 1px solid black;
                background-color: lightgrey;
                padding: 4px;
                }
            """)
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            select_row = set(row.row() for row in self.tableWidget.selectedIndexes())
            for row in reversed(sorted(select_row)):
                self.tableWidget.removeRow(row)
        elif event.key() == QtCore.Qt.Key_W:
            self.tableWidget.selectRow(self.tableWidget.currentRow() - 1)
        elif event.key() == QtCore.Qt.Key_S:
            self.tableWidget.selectRow(self.tableWidget.currentRow() + 1)
        elif event.key() == QtCore.Qt.Key_Up:
            self.tableWidget.selectRow(self.tableWidget.currentRow() - 1)
        elif event.key() == QtCore.Qt.Key_Down:
            self.tableWidget.selectRow(self.tableWidget.currentRow() + 1)
        elif event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            selected_items = self.tableWidget.selectedItems()
            if selected_items:
                for item in selected_items:
                    self.tableWidget.editItem(item)
        elif event.key() == QtCore.Qt.Key_Backspace:
            selected_rows = set(index.row() for index in self.tableWidget.selectedIndexes())
            for row in reversed(sorted(selected_rows)):
                self.tableWidget.removeRow(row)
        else:
            pass
          


if __name__ == "__main__":
    app = QApplication(sys.argv)
    waitlistdialog = WaitlistDialog()
    waitlistdialog.show()
    app.exec_()