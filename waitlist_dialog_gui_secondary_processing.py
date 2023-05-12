import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from waitlist_dialog_gui import Ui_waitlistDialog

class WaitlistDialog(QDialog,Ui_waitlistDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initsiganal()
        self.tableWidget.keyPressEvent=self.keyPressEvent #주석: 이미 키보드함수 실행되고 있음, 그 값을 바꾸는 것 뿐이다.
        self.request="서버수정없음" #이게없다면, 그냥X눌렀을떄 에러가 난다.(서버수정없음이라는 값이 없기때문에)

    def initsiganal(self):
        self.setWindowTitle("작업대기목록")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["작업시간","플랫폼","URL","URL2","체류시간","구매수량","배송메세지"])
        #칼럼간의 간격을 조정한다.
        for i in range(7):
            if i==0:#작업시간
                self.tableWidget.setColumnWidth(i,150)
            elif i==1:#플랫폼
                self.tableWidget.setColumnWidth(i,70)
            elif i==2 or i==3:#URL,URL2
                self.tableWidget.setColumnWidth(i,150)
            elif i==4:#체류시간.
                self.tableWidget.setColumnWidth(i,70)
            elif i==5: #구매수량
                self.tableWidget.setColumnWidth(i,70)
            else:#배송메세지
                self.tableWidget.setColumnWidth(i,150)
    

        #시그널과 슬롯을 연결한다.
        self.edit_request_btn.clicked.connect(self.edit_request)
        self.cancle_btn.clicked.connect(self.closbty)

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
        #테스트용 나중에 지워도됨.
        # self.tableWidget.setRowCount(2)
        # self.tableWidget.setItem(0,0,QTableWidgetItem(f"슈바"))
        # self.tableWidget.setItem(1,0,QTableWidgetItem(f"작당"))
        # self.tableWidget.setRowHeight(0, 30)
        # self.tableWidget.setRowHeight(1, 30)
    
    #데이터를 수정해서 보내는 역할을 한다.
    def edit_request(self):
        print("수정요청을 하였습니다.")
        row_count = self.tableWidget.rowCount()
        column_count = self.tableWidget.columnCount()
        #-------------수정요청시 값을 waitlist에 저장한다.-------#
        for row in range(row_count):
            for col in range(column_count):
                item = self.tableWidget.item(row, col)
                if col==0:
                    cell_value = str(item.text())
                    waitlist[row]["작업시간"]=cell_value
                elif col==1:
                    cell_value = str(item.text())
                    waitlist[row]["플랫폼"]=cell_value
                elif col==2:
                    cell_value = str(item.text())
                    waitlist[row]["URL"]=cell_value
                elif col==3:
                    cell_value = str(item.text())
                    waitlist[row]["URL2"]=cell_value
                elif col==4:
                    cell_value = int(item.text())
                    waitlist[row]["페이지체류시간"]=cell_value
                elif col==5:
                    cell_value = int(item.text())
                    waitlist[row]["구매수량"]=cell_value
                elif col==6:
                    cell_value = str(item.text())
                    waitlist[row]["배송메세지"]=cell_value
                else:
                    print(f"셀 ({row}, {col})은 비어있습니다.")
        self.request="서버수정데이터"
        self.close()
    
    def closbty(self):
        self.request="서버수정없음"
        self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            select_row = set(row.row() for row in self.tableWidget.selectedIndexes())
            for row in reversed(sorted(select_row)): 
                try:
                    waitlist.remove(waitlist[row])
                    print(waitlist)
                except:
                    pass
                self.tableWidget.removeRow(row)
        elif event.key() == QtCore.Qt.Key_W:
            current_row = self.tableWidget.currentRow()
            if current_row > 0:
                try:
                    self.swap_elements(waitlist,current_row,current_row-1)
                    print(waitlist)
                except:
                    pass
            self.move_row(current_row, current_row - 1)
            self.tableWidget.setCurrentCell(current_row - 1, 0)
       
        elif event.key() == QtCore.Qt.Key_S:
            current_row = self.tableWidget.currentRow()
            max_row = self.tableWidget.rowCount()
            if current_row < max_row-1:
                try:
                    self.swap_elements(waitlist,current_row,current_row+1)
                    print(waitlist)
                except:
                    pass
                self.move_row(current_row, current_row + 1)
                self.tableWidget.setCurrentCell(current_row + 1, 0)
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
    
    #테이블의 행을 이동시키는 함수다.
    def move_row(self, source_row, destination_row):
        for col in range(self.tableWidget.columnCount()):
            source_item = self.tableWidget.takeItem(source_row, col)
            destination_item = self.tableWidget.takeItem(destination_row, col)
            self.tableWidget.setItem(destination_row, col, source_item)
            self.tableWidget.setItem(source_row, col, destination_item)

    def inputwaitlist(self,data):
        global waitlist
        waitlist=data

    def waitlist_gui(self):
        self.tableWidget.setRowCount(len(waitlist))
        for i in range(len(waitlist)):
            self.tableWidget.setItem(i,0,QTableWidgetItem(str(waitlist[i]["작업시간"])))
            self.tableWidget.setItem(i,1,QTableWidgetItem(str(waitlist[i]["플랫폼"])))
            self.tableWidget.setItem(i,2,QTableWidgetItem(str(waitlist[i]["URL"])))
            self.tableWidget.setItem(i,3,QTableWidgetItem(str(waitlist[i]["URL2"])))
            self.tableWidget.setItem(i,4,QTableWidgetItem(str(waitlist[i]["페이지체류시간"])))
            self.tableWidget.setItem(i,5,QTableWidgetItem(str(waitlist[i]["구매수량"])))
            self.tableWidget.setItem(i,6,QTableWidgetItem(str(waitlist[i]["배송메세지"])))
    
    #인덱스를 바꾸는 함수다.
    def swap_elements(self,lst, index1, index2):
        if not (0 <= index1 < len(lst)) or not (0 <= index2 < len(lst)):
            raise ValueError("인덱스가 리스트의 범위를 벗어났습니다.")
        lst[index1], lst[index2] = lst[index2], lst[index1]
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    waitlistdialog = WaitlistDialog()
    waitlistdialog.show()
    app.exec_()