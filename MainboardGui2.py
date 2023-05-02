import sys 
from PyQt5.QtWidgets  import*
from PyQt5.QtCore import* 
from maingui import Ui_mainWindow
from coupang_input_Gui_secondary_processing import * 
from soket_client import *
from waitlist_dialog import * 


class Main_Gui(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initsiganal()

    def initsiganal(self):
#------------------작업컴퓨터 클리시 서버리스트창 켜는함수.----------#
        def 박경희서버창():
          pass



       
        
#----------------------작업방식 기능함수.----------------------#
        def 구매조건():
          self.Platform_group.setEnabled(True)
          self.WorkCom_grop.setEnabled(True)
        def 리뷰업데이트():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)
        def Ai리뷰():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)
        def 리뷰작성():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)
        def 재촉하기():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)
        def 계좌업데이트():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)

        #----------------------시그널 슬롯 연결----------------------#
        ###1.시그널 슬롯 연결
        self.purchasework_radiobtn.clicked.connect(구매조건)
        self.reviewupdate_radiobtn.clicked.connect(리뷰업데이트)
        self.aireview_radiobtn.clicked.connect(Ai리뷰)
        self.review_write_radiobtn.clicked.connect(리뷰작성)
        self.pinch_radiobtn.clicked.connect(재촉하기)
        self.accountupdate_radiobtn.clicked.connect(계좌업데이트)
        ###2.서버창켜는 슬롯.
        self.server1_btn.clicked.connect(박경희서버창)



        

      


if __name__=="__main__":
    #큐어플리케이션은 작업반장이다. 
    app=QApplication(sys.argv)
    window=Main_Gui()
    window.show()
    sys.exit(app.exec_())