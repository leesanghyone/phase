import sys 
from PyQt5.QtWidgets  import*
from PyQt5.QtCore import* 
from maingui import Ui_mainWindow
from coupang_input_Gui_secondary_processing import * 
from sokey_client import *
import sokey_client 
from waitlist_dialog_gui_secondary_processing import WaitlistDialog

class Main_Gui(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initsiganal()

    def initsiganal(self):
  #------------------소켓활성화 함수들----------#
        self.박경희컴퓨터sock=soket_start("127.0.0.1",12000) #한번실행되면 계속 연결을 유지한다. 
        self.가구매작업데이터={ 
              "URL": "Https://copang",
              "URL2" : "공백",
              "플랫폼" : "쿠팡",
              "카카오톡" : "개발중",
              "작업시간" : datetime.datetime.now().strftime('%Y-%m-%d-%H:%M'),
              "장바구니" : False,
              "포인트" : False,
              "최소가격" : 10000,
              "최대가격" : 10000,
              "찜작업" : True,
              "알림받기" : False,
              "페이지체류시간" : 130,
              "옵션1" : [["블랙,""화이트","그레이"]],
              "옵션2" : 3,
              "구매수량" : 1,
              "배송메세지" : "그냥 배송 잘 부탁드려요."
          }
  #-------------서버에서일 받아오고, 수정하고 보내는 역할을 해준다.--------#
        def 서버창관리(soket):
          self.serverinfo=WaitlistDialog()
          self.serverinfo.show()  
          작업방식="서버정보업데이트" #추후에 gui에서 일회용으로 계속 데이터를 보낼것이다.
          socket_sender(soket,작업방식,self.가구매작업데이터) #데이터를 보낸다.
    #-------------클라이언트 소켓에서 waitlist데이터를 로드한다.---------#
          while True:
            if sokey_client.waitlist != None:
              self.waitlist=sokey_client.waitlist
              break
          #--------------#웨잇리스트로 gui를 구현한다.---------#
          self.serverinfo.inputwaitlist(self.waitlist) 
          self.serverinfo.waitlist_gui() 
          self.serverinfo.exec_() 
    #------------서버일감 수정데이터를 보낸다.----------#
          작업방식=self.serverinfo.request
          if 작업방식=="서버수정데이터":
            socket_sender(soket,작업방식) #데이터를 보낸다.
            ##데이터초기화 하기
            sokey_client.waitlist=None
            self.waitlist=None
          elif 작업방식=="서버수정없음":
            print("일감데이터 수정할게없다.")
  #------------------작업컴퓨터 클리시 서버리스트창 켜는함수.----------#
        def 박경희서버창():
           서버창관리(self.박경희컴퓨터sock)
             
        def 두번째서버창():
           print(self.waitlist)

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
        def 확인버튼():
          print("확인버튼눌림")
          socket_sender(self.박경희컴퓨터sock,"서버수정데이터")
          if sokey_client.miniwaitlist != None:
            미리보기데이터=sokey_client.miniwaitlist
          

        #----------------------시그널 슬롯 연결----------------------#
        ###1.시그널 슬롯 연결
        self.purchasework_radiobtn.clicked.connect(구매조건)
        self.reviewupdate_radiobtn.clicked.connect(리뷰업데이트)
        self.aireview_radiobtn.clicked.connect(Ai리뷰)
        self.review_write_radiobtn.clicked.connect(리뷰작성)
        self.pinch_radiobtn.clicked.connect(재촉하기)
        self.accountupdate_radiobtn.clicked.connect(계좌업데이트)
        self.yes_btn.clicked.connect(확인버튼)
        ###2.서버창켜는 슬롯.
        self.server1_btn.clicked.connect(박경희서버창)
        self.server2_btn.clicked.connect(두번째서버창)
        


if __name__=="__main__":
    #큐어플리케이션은 작업반장이다. 
    app=QApplication(sys.argv)
    window=Main_Gui()
    window.show()
    sys.exit(app.exec_())