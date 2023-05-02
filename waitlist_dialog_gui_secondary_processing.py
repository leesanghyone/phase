import sys
from PyQt5.QtWidgets import *
from waitlist_dialog_gui import Ui_waitlistDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class WaitlistDialog(QDialog,Ui_waitlistDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initsiganal()
        self.show()
    
    def initsiganal(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["순서","작업시간","플랫폼"])
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,70)
        
        self.tableWidget.setRowCount(5) 
        self.tableWidget.setItem(0,1,QTableWidgetItem("할로"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("쇼부"))
        self.tableWidget.keyPressEvent=self.keyPressEvent
        self.tableWidget.cellChanged.connect(self.on_cell_changed)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            select_row = set(row.row() for row in self.tableWidget.selectedIndexes())
            for row in reversed(sorted(select_row)):
                self.tableWidget.removeRow(row)
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
          
    def on_cell_changed(self, row, column):
        item = self.tableWidget.item(row, column)
        if item:
            # 여기서 셀의 수정된 값을 저장하거나 처리할 수 있습니다.
            # 예를 들어, 셀 값을 출력하려면 다음 코드를 사용할 수 있습니다.
            print(f"셀 ({row}, {column})의 값이 '{item.text()}'로 변경되었습니다.")
           

if __name__ == "__main__":
    app = QApplication(sys.argv)
    waitlistdialog = WaitlistDialog()
    waitlistdialog.show()
    app.exec_()