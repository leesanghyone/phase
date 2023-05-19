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
        self.com_workinter_checkbox.clicked.connect(self.comworkinterbal)
        # self.com_workinter_checkbox.setEnabled(False) #임시로 비활성화 시킴.
    
    def initdata(self):
        self.url1=None
        self.url2=None
        self.포인트=None
        self.플랫폼=None
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
        self.알림받기=None
        self.컴작업간격=None
        
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
    
    def comworkinterbal(self):
        if self.com_workinter_checkbox.isChecked():
            self.com_workinterbal_label.setEnabled(True)
            self.com_workinterbal_spinbox.setEnabled(True)
        elif self.com_workinter_checkbox.isChecked() == False:
            self.com_workinterbal_label.setEnabled(False)
            self.com_workinterbal_spinbox.setEnabled(False)

    #창 닫는 코드다.
    def closeEvent(self, event: QtCore.QEvent):
        # 여기에 필요한 동작을 정의합니다.
        print("창이 닫힙니다.")
        event.accept()  # 이 코드는 창이 실제로 닫히도록 합니다.


    #작업컴퓨터 간격 활성화/비활성화
    def active_workcom_interbal(self,parent):

        #모든컴퓨터 작업시, 컴퓨터간 작업간격 활성화.
        if parent.all_check_btn.isChecked():
            self.com_workinter_checkbox.setEnabled(True)
            self.com_workinter_checkbox.setChecked(True)
            self.com_workinterbal_label.setEnabled(True)
            self.com_workinterbal_spinbox.setEnabled(True)
        elif parent.all_check_btn.isChecked() == False:
            self.com_workinter_checkbox.setEnabled(False)
            self.com_workinter_checkbox.setChecked(False)
            self.com_workinterbal_label.setEnabled(False)
            self.com_workinterbal_spinbox.setEnabled(False)
        
        #작업컴퓨터 1개 이상시,컴퓨터간 작업간격 활성화.
        작업컴퓨터리스트=[]
        if parent.parck_check_btn.isChecked():
            작업컴퓨터리스트.append("박경희")
        if parent.itw_check_btn.isChecked():
            작업컴퓨터리스트.append("임태원테스트")
        if parent.sangjun_check_btn.isChecked():
            작업컴퓨터리스트.append("이상준")
        if parent.sanghyone_check_btn.isChecked():
            작업컴퓨터리스트.append("이상현")
        
        if len(작업컴퓨터리스트) > 1:
            self.com_workinter_checkbox.setEnabled(True)
            self.com_workinter_checkbox.setChecked(True)
            self.com_workinterbal_label.setEnabled(True)
            self.com_workinterbal_spinbox.setEnabled(True)

        else:
            self.com_workinter_checkbox.setEnabled(False)
            self.com_workinter_checkbox.setChecked(False)
            self.com_workinterbal_label.setEnabled(False)
            self.com_workinterbal_spinbox.setEnabled(False)


    def okayclick(self):
        self.url1=str(self.url1_inputEdit.text())
        self.url2="url2공백"
        self.작업시간=None
        self.포인트=self.pointuse.isChecked()  #결제옵션(포인트 하나면 된다) , if 아니면 , 그냥 노포인트
        self.플랫폼="쿠팡"
        self.알림받기="X"
        self.장바구니=self.jangbaguni.isChecked() #결제방식(장바구니 값 하나면 된다),  if 아니면 , 그냥 일반결제다.
        self.구매수량=int(self.moq.text())
        self.체류시간=int(self.page_scroll_time.text())*60
        self.옵션1=int(self.options1.text())
        self.옵션2=int(self.options2.text())
        self.찜작업=self.jjim_check.isChecked()
        self.최소가격=int(self.minprice_spinbox.text())
        self.최대가격=int(self.maxprice_spinbox.text())
        self.배송메세지=str(self.basongmsg_LineEdit.text())

        #쿠팡작업데이터에 직접적으로 쓰이지않음, 다른것을 위한 재료다.
        self.작업간격=int(self.workinterbal_spinbox.text())
        self.예약시간=str(self.Reservation_time_edit.text())
        self.컴작업간격=None
        ############################유효성검사.##########################################
        if self.최소가격 > 1 and self.최대가격 <= 1:
            self.최대가격=self.최소가격 + 1000

        #1.데이터 필터링.
        if self.최소가격 < 1:
            self.최소가격=0
            self.최대가격=0
            #최대가격 자동입력(최소가격만 입력하면 됨)

        #2.작업시간, 예약시간 지정하기.(아지 개발하지 않았다.)
        if self.workinter_checkbox.isChecked() == False:
            self.작업간격=0

        #3.작업시간 유효성검사.
        if not self.Reservationtime_checkbox.isChecked():
            self.작업시간=datetime.now().strftime("%Y-%m-%d-%H:%M")
        elif self.Reservationtime_checkbox.isChecked():
            #예약시간만들기.(데이트타임 객체화 시킨다.)
            예약시간=datetime.strptime(self.예약시간,"%H:%M") #시간,분만 객체화(년,월,일이 없다.)
            현재시간=datetime.now() 
            self.작업시간=예약시간.replace(year=현재시간.year,month=현재시간.month,day=현재시간.day).strftime("%Y-%m-%d-%H:%M")
            
        #4.url필터링
        if self.url1.find("srp_product_ads&clickEventId") != -1:
            QMessageBox.warning(self,"광고상품링크","당신의 url은 광고상품이에요.")
        
        #5.컴퓨터간 작업간격.
        if self.com_workinter_checkbox.isChecked():
            self.컴작업간격=int(self.com_workinterbal_spinbox.text())
        else:
            self.컴작업간격=0

        #테스트를 위한 출력.
        print("쿠팡입력데이터:",self.url1,self.url2,self.포인트,self.장바구니,self.구매수량,self.체류시간,self.옵션1,self.옵션2,self.찜작업,self.최소가격,self.최대가격,self.배송메세지,self.작업시간)
        print("쿠팡입력데이터2:",self.컴작업간격,self.작업간격,self.작업시간,)
        #종료를 한다.
        self.close()

    
if __name__ == '__main__':
    app=QApplication(sys.argv)
    # app.setStyle("fusion") #켜면 모양이 어그러진다.
    cou=Coupang_inputData_Gui()
    cou.show()
    sys.exit(app.exec_())