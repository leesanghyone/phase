import sys , random
from PyQt5.QtWidgets  import*
from PyQt5.QtCore import* 
from maingui import Ui_mainWindow
from coupang_input_Gui_secondary_processing import * 
from sokey_client import *
import sokey_client
from waitlist_dialog_gui_secondary_processing import WaitlistDialog
from datetime import datetime,timedelta

class Main_Gui(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initsiganal()
        self.initinputdata()


    def initinputdata(self):
      #가구매 작업의 필수데이터.
      self.url1=None
      self.url2=None
      self.플랫폼=None
      self.카카오톡=None
      self.작업시간=None
      self.알림받기=None
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
      self.유효성검사= lambda :[self.url1,self.url2,self.플랫폼,self.카카오톡,self.작업시간,self.알림받기,self.포인트,self.장바구니,self.구매수량,self.체류시간,self.옵션1,self.옵션2,self.찜작업,self.최소가격,self.최대가격,self.배송메세지]
      #가구매 작업의 선택데이터.
      self.컴작업간격=None

    def initsiganal(self):
  #------------------소켓활성화 함수들----------#
        try:
          self.박경희컴퓨터sock=soket_start("127.0.0.1",12000,self) #한번실행되면 계속 연결을 유지한다.
        except:
          pass

  #-------------서버에서일 받아오고, 수정하고 보내는 역할을 해준다.--------#
        def 서버일감불러오기(soket):
          self.serverinfo=WaitlistDialog()
          self.serverinfo.show()  
          작업방식="서버정보업데이트" #추후에 gui에서 일회용으로 계속 데이터를 보낼것이다.
          socket_sender(soket,작업방식) #데이터를 보낸다.
    #-------------클라이언트 소켓에서 waitlist데이터를 로드한다.---------#
          while True:
            if sokey_client.waitlist != None: #타이밍에 따라서 waitlist값이 바뀐다.
              self.waitlist=sokey_client.waitlist
              break
          #--------------#웨잇리스트로 gui를 구현한다.---------#
          #소켓->서버데이터->waitgui->구현.
          self.serverinfo.inputwaitlist(self.waitlist) 
          self.serverinfo.waitlist_gui() 
          self.serverinfo.exec_() 
    #------------서버일감 수정데이터를 보낸다.----------#
          try:# 그냥 창 닫으면x 누르면 에러나서 만듬. 
            작업방식=self.serverinfo.request
            if 작업방식=="서버수정데이터":
              socket_sender(soket,작업방식) #데이터를 보낸다.
              ##데이터초기화 하기
              sokey_client.waitlist=None
              self.waitlist=None
            elif 작업방식=="서버수정없음":
              print("일감데이터 수정할게없다.")
          except:
             pass
        #-----------------이코드는 쓰지 않지만 교육용으로 남겨놓는다.----------#
        def 서버미니정보얻기(sock,btn):
          #모든 서버에게 갱신요청을 보낸다.
          socket_sender(sock,"서버간소화정보")
          while True:
            try:
              if len(sokey_client.miniwaitlist) >= 1: #서버가 1개이상이면
                서버미니작업갯수=sokey_client.miniwaitlist
                ip,port=sock.getpeername()
                서버미니작업갯수=서버미니작업갯수.get(ip)
                btn.setText(서버미니작업갯수)
                break
            except:
              print("서버간소화정보를 받아오지 못했습니다.")
              break

        def 갱신버튼누름():
          # 서버미니정보얻기(self.박경희컴퓨터sock,self.server1_btn)
          socket_sender(self.박경희컴퓨터sock,"서버간소화정보")
        

  #------------------작업컴퓨터 클리시 서버리스트창 켜는함수.----------#
        def 박경희서버창():
           서버일감불러오기(self.박경희컴퓨터sock)
             
        def 두번째서버창():
           print(self.waitlist)

  #----------------------작업방식 기능함수.----------------------#
        
        def 구매조건():
          self.Platform_group.setEnabled(True)
          self.WorkCom_grop.setEnabled(True)
        def 리뷰업데이트():
          self.Platform_group.setEnabled(True)
          self.WorkCom_grop.setEnabled(True)
        def Ai리뷰():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)
        def 리뷰작성():
          self.Platform_group.setEnabled(True)
          self.WorkCom_grop.setEnabled(True)
        def 재촉하기():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)
        def 계좌업데이트():
          self.Platform_group.setEnabled(False)
          self.WorkCom_grop.setEnabled(False)
        
        ###컴퓨터 추가시+++작업필요함.
        def 확인버튼():
              #------------------작업할 컴퓨터 체크하기.-------------------#
              작업컴퓨터리스트=[]
              #모든 컴퓨터를 작업을 진행한다.
              if self.all_check_btn.isChecked():
                print("모든 컴퓨터가 가구매 작업을 진행합니다.")
                pass
              #체크된 컴퓨터만 작업을 진행한다.
              elif not self.all_check_btn.isChecked():
                print("체크된 컴퓨터만 가구매 작업을 진행합니다.")
                if self.parck_check_btn.isChecked():
                  작업컴퓨터리스트.append(self.박경희컴퓨터sock)
                if self.itw_check_btn.isChecked():
                  작업컴퓨터리스트.append("임태원테스트")
                if self.sangjun_check_btn.isChecked():
                  작업컴퓨터리스트.append("테스트")
                if self.sanghyone_check_btn.isChecked():
                  작업컴퓨터리스트.append("테스트")
              random.shuffle(작업컴퓨터리스트) #작업컴퓨터 무작위로 순서 바꾸기.
              print(작업컴퓨터리스트)
              #------------------가구매 데이터 유효성 검사--------------------#
              print("유효성검사를 시작합니다.")
              print(self.유효성검사())
    
              print("유효성검사 리스트 끝.")
              for 가구매데이터 in self.유효성검사():
                print(가구매데이터)
                if 가구매데이터 == None:
                  QMessageBox.warning(self,"경고","데이터를 입력해주세요.")
                  return
              #------------------가구매 데이터 작업컴에 보내기.------------------#
              for 작업컴 in 작업컴퓨터리스트:
                가구매작업데이터={ 
                "URL": self.url1,
                "URL2" : self.url2,
                "플랫폼" : self.플랫폼,
                "카카오톡" : self.카카오톡,
                "작업시간" : datetime.strftime((self.작업시간+timedelta(minutes=self.컴작업간격*작업컴퓨터리스트.index(작업컴))),"%Y-%m-%d-%H:%M"), #받아온데이터->객체화->시간더하기->문자열로변환
                "장바구니" : self.장바구니,
                "포인트" : self.포인트,
                "최소가격" : self.최소가격,
                "최대가격" : self.최대가격,
                "찜작업" : self.찜작업,
                "알림받기" : self.알림받기,
                "페이지체류시간" : self.체류시간,
                "옵션1" : self.옵션1,
                "옵션2" : self.옵션2,
                "구매수량" : self.구매수량,
                "배송메세지" : self.배송메세지
                }
                print(가구매작업데이터)
                socket_sender(작업컴,"가구매작업",가구매작업데이터)
                #------------------작업컴퓨터 간소화 정보 받기..------------------
              for 작업컴 in 작업컴퓨터리스트:
                socket_sender(작업컴,"서버간소화정보")
              #초기화작업
              self.initinputdata()
                        
  #----------------------데이터 인풋받는 창----------------------#
        def 쿠팡데이터입력창():
          if self.platform_check_coopang.isChecked():
            coupang_input=Coupang_inputData_Gui()
            coupang_input.show()
            coupang_input.exec_()

            self.url1=coupang_input.url1
            self.url2=coupang_input.url2
            self.플랫폼=coupang_input.플랫폼
            self.카카오톡="개발중"
            try: #그냥 x누를시, 값이 선언이 안되어서 트라이처리.
              self.작업시간=datetime.strptime(coupang_input.작업시간,"%Y-%m-%d-%H:%M")
            except:
              self.작업시간=None
            self.알림받기=coupang_input.알림받기
            self.포인트=coupang_input.포인트
            self.장바구니=coupang_input.장바구니
            self.구매수량=coupang_input.구매수량
            self.체류시간=coupang_input.체류시간
            self.옵션1=coupang_input.옵션1
            self.옵션2=coupang_input.옵션2
            self.찜작업=coupang_input.찜작업
            self.최소가격=coupang_input.최소가격
            self.최대가격=coupang_input.최대가격
            self.배송메세지=coupang_input.배송메세지
            print(self.url1,self.url2,self.작업시간,self.포인트,self.장바구니,self.구매수량,self.체류시간,self.옵션1,self.옵션2,self.찜작업,self.최소가격,self.최대가격,self.배송메세지)
            #필수데이터 항목이 아닌경우다.
            self.컴작업간격=coupang_input.컴작업간격  #2개이상의 컴퓨터 작업시만 필요하다.
        
        #----------------------시그널 슬롯 연결----------------------#
        #기본적인기능
        self.close_btn.clicked.connect(self.close)
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
        self.allserver_btn.clicked.connect(갱신버튼누름)
        ###3.데이터입력창
        self.platform_check_coopang.clicked.connect(쿠팡데이터입력창)


if __name__=="__main__":
    #큐어플리케이션은 작업반장이다. 
    app=QApplication(sys.argv)
    window=Main_Gui()
    window.show()
    sys.exit(app.exec_())