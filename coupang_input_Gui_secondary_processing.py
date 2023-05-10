import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from coupang_input_gui import Ui_C_inputDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime,timedelta

class Coupang_inputData_Gui(QDialog,Ui_C_inputDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #ui불러오고 있어야, 이름명이 바뀜.
        self.setWindowTitle("쿠팡입력") 
        #현재시각 표시하기.
        self.Reservation_time_edit.setTime(QtCore.QTime.currentTime())

        #쿠팡데이터 초기화.
        self.initdata()

        #시그널 슬롯연결.
        self.close_btn.clicked.connect(self.close)
        self.okay_btn.clicked.connect(self.okayclick)
        self.workinter_checkbox.clicked.connect(self.workinterbal)
        self.Reservationtime_checkbox.clicked.connect(self.timeswitch)

    def initdata(self):
        self.url1=None
        self.url2=None
        self.포인트=None
        self.장바구니=None
        self.구매수량=None
        self.체류시간=None
        self.옵션1=None
        self.옵션2=None
        self.찜작업=None
        self.최소가격=None
        self.최대가격=None
        self.배송메세지=None
        self.작업시간=None

    def workinterbal(self):
        if self.workinter_checkbox.isChecked():
            self.workinterbal_label.setEnabled(True)
            self.workinterbal_spinbox.setEnabled(True)
        else:
            self.workinterbal_label.setEnabled(False)
            self.workinterbal_spinbox.setEnabled(False)

    def timeswitch(self):
        if self.Reservationtime_checkbox.isChecked():
            self.Reservation_label.setEnabled(True)
            self.Reservation_time_edit.setEnabled(True)
        else:
            self.Reservation_label.setEnabled(False)
            self.Reservation_time_edit.setEnabled(False)

    def okayclick(self):
        self.url1=str(self.url1_inputEdit.text())
        self.url2="url2공백"
        self.포인트=self.pointuse.isChecked()  #결제옵션(포인트 하나면 된다) , if 아니면 , 그냥 노포인트
        self.장바구니=self.jangbaguni.isChecked() #결제방식(장바구니 값 하나면 된다),  if 아니면 , 그냥 일반결제다.
        self.구매수량=int(self.moq.text())
        self.체류시간=int(self.page_scroll_time.text())*60
        self.옵션1=int(self.options1.text())
        self.옵션2=int(self.options2.text())
        self.찜작업=self.jjim_check.isChecked()
        self.최소가격=int(self.minprice_spinbox.text())
        self.최대가격=int(self.maxprice_spinbox.text())
        self.배송메세지=str(self.basongmsg_LineEdit.text())
        self.작업시간=None

        #쿠팡작업데이터에 직접적으로 쓰이지않음, 다른것을 위한 재료다.
        self.작업간격=int(self.workinterbal_spinbox.text())
        self.예약시간=str(self.Reservation_time_edit.text())
       
        ############################유효성검사.##########################################
        if self.최소가격 > 1 and self.최대가격 <= 1:
            self.최대가격=self.최소가격 + 1000

        #1.데이터 필터링.
        if self.최소가격 < 1:
            self.최소가격=None
            self.최대가격=None
            #최대가격 자동입력(최소가격만 입력하면 됨)

        #2.작업시간, 예약시간 필터링.
        if self.workinter_checkbox.isChecked() == False:
            self.작업간격=0
        #3.작업시간 유효성검사.
        if self.Reservationtime_checkbox.isChecked() == False:
            self.작업시간=datetime.now().strftime("%Y-%m-%d-%H:%M")
        elif self.Reservationtime_checkbox.isChecked() == True:
            #예약시간만들기.(데이트타임 객체화 시킨다.)
            현재시간재료=datetime.strptime(self.예약시간,"%H:%M") #시간,분만 객체화(년,월,일이 없다.)
            현재시간=datetime.now() 
            self.작업시간=현재시간재료.replace(year=현재시간.year,month=현재시간.month,day=현재시간.day).strftime("%Y-%m-%d-%H:%M")

        #4.url필터링
        if self.url1.find("srp_product_ads&clickEventId") != -1:
            QMessageBox.warning(self,"광고상품링크","당신의 url은 광고상품이에요.")
        
        #테스트를 위한 출력.
        print("쿠팡입력데이터:",self.url1,self.url2,self.포인트,self.장바구니,self.구매수량,self.체류시간,self.옵션1,self.옵션2,self.찜작업,self.최소가격,self.최대가격,self.배송메세지,self.작업시간)
        #종료를 한다.
        # self.close()
        
        
        
       
 
    
if __name__ == '__main__':
    app=QApplication(sys.argv)
    # app.setStyle("fusion") #켜면 모양이 어그러진다.
    cou=Coupang_inputData_Gui()
    cou.show()
    sys.exit(app.exec_())