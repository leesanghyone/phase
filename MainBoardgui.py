import sys 
from PyQt5.QtWidgets  import*
from PyQt5.QtCore import* 
from maingui import Ui_mainWindow
from coupang_input_Gui_secondary_processing import * 
from soket_client import *


class Main_Gui(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initSignal()


    def initSignal(self):
        #오류방지,워크컴퓨터 기능끄기.
        def active_workcom(active=bool):
                self.workcom.setEnabled(active)
#-------------------------변수값 초기화 하기-----------------(중복제거)
        def 초기화작업():
            self.url=None
            self.포인트=None
            self.구매수량=None
            self.장바구니=None
            self.체류시간=None
            self.옵션1=None
            self.옵션2=None
            self.찜작업=None
            self.최소가격=None
            self.최대가격=None
            self.배송메세지=None
        초기화작업()

#-----------------작업컴퓨터 실시간 업데이트 기능-------------------------
        def 쿠팡컴퓨터활성화상태저장소():
            self.박경희_작업컴상태=True
            self.임태원_작업컴상태=True
            self.이상준_작업컴상태=True
            self.이상현_작업컴상태=True
            self.모두_작업컴상태=True
        쿠팡컴퓨터활성화상태저장소()

        def 쿠팡체크박스누를시():
            ####################Data_input_Gui창 띄우기################################
            if self.Copang_group.isChecked(): #쿠팡체크박스 누를시
                초기화작업() #변수값 초기화
                self.inputgui=Coupang_inputData_Gui()
                self.inputgui.setWindowModality(Qt.ApplicationModal)
                self.inputgui.show()
                self.inputgui.exec_()

                ####################Gui에서 데이터 받아옴################################
                try: #그냥 x버튼 누르면 오류나서 예외처리함.
                    self.url=self.inputgui.url
                    self.포인트=self.inputgui.포인트
                    self.구매수량=self.inputgui.구매수량
                    self.장바구니=self.inputgui.장바구니
                    self.체류시간=self.inputgui.체류시간
                    self.옵션1=self.inputgui.옵션1
                    self.옵션2=self.inputgui.옵션2
                    self.찜작업=self.inputgui.찜작업
                    self.최소가격=self.inputgui.최소가격
                    self.최대가격=self.inputgui.최대가격
                    self.배송메세지=self.inputgui.배송메세지
                except:
                    print("아무 입력없이 창을 종료함.")
                    초기화작업()
            
                ####컴퓨터 활성화 상태 적용하기####
                self.C_parck_check_btn.setEnabled(self.박경희_작업컴상태)
                self.C_itw_check_btn.setEnabled(self.임태원_작업컴상태)
                self.C_sangjun_check_btn.setEnabled(self.이상준_작업컴상태)
                self.C_sanghyone_check_btn.setEnabled(self.이상현_작업컴상태)
                self.C_all_check_btn.setEnabled(self.이상현_작업컴상태)

#---------------------------------작업별 실행함수.----------------------------
        def 구매작업():
            active_workcom(True)
            
        def 리뷰업데이트():
            active_workcom(False)

        def Ai리뷰():
            active_workcom(False)

        def 리뷰작성():
            active_workcom(False)

        def 재촉하기():
            active_workcom(False)
             
        def 계좌업데이트():
            active_workcom(False)
            
    #---------------------------------소켓통신파트.-----------------------------------    
        def 확인버튼누를시():  
        #-----------------구매작업 버튼 체크시.-----------------
            if self.purchasework_radiobtn.isChecked():
                print("구매작업")

                #-----------------자체생성 데이터.-----------------
                #1.플랫폼
                if self.Copang_group.isChecked():
                    플랫폼="쿠팡"
                elif self.Naver_grop.isChecked():
                    플랫폼="네이버"

                #-----------------유효성 검사--------------------
                    #1.#플랫폼 선택안한경우.
                if self.Copang_group.isChecked()==False and self.Naver_grop.isChecked()==False: #플랫폼
                    print("플랫폼이 입력되지 않았습니다.")
                    QMessageBox.warning(self, "경고", "플랫폼이 입력되지 않았습니다.", QMessageBox.Ok)
                    return
                    #2.URL이 입력되지 않았을때.
                if self.url==None or self.url[0]==None or self.url[0]=="" or self.url[1]==None or self.url[1]=="" : #URL:
                    print("URL이 입력되지 않았습니다.")
                    QMessageBox.warning(self, "경고", "URL이 입력되지 않았습니다.", QMessageBox.Ok)
                    return
                #-----------------소켓보낼 데이터 정리.-----------------
                url=[self.url[0],self.url[1]] #URL1, URL2
                platforminfo=[플랫폼,"개발중"] #플랫폼,카카오톡, 
                PaymentOptions=[self.장바구니,False] #결제방식(일반,장바구니) ,포인트
                ActionOption=[self.최소가격,self.최대가격,self.찜작업,False,self.체류시간] #(최소가격,최대가격), (찜작업,알림받기) , 페이지체류시간
                PurchaseOptions=[[self.옵션1,self.옵션2],self.구매수량,self.배송메세지] #([[옵션1],[옵션2]...]) , 구매수량 , 배송메세지
                print(
                    url,
                    platforminfo,
                    PaymentOptions,
                    ActionOption,
                    PurchaseOptions,
                )
                
                #-----------------전송데이터 준비-----------------
                so_inputdata(url=url,platforminfo=platforminfo,PaymentOptions=PaymentOptions,ActionOption=ActionOption,PurchaseOptions=PurchaseOptions)
                # so_Send_data("127.0.0.1",12000,self) #2.데이터보내는 역할.(복사용으로 남겨둠.)
            #-----------------쿠팡 버튼 체크시.-----------------
                #-----------------(박경희).-----------------
                if self.C_parck_check_btn.isChecked():
                    print("박경희 작업컴퓨터 보냄.")
                    self.C_parck_check_btn.setChecked(False)
                    self.C_parck_check_btn.setEnabled(False)
                    self.박경희_작업컴상태=False
                    so_Send_data("127.0.0.1",12000,self) #2.데이터를 보낸다.
                #-----------------(임태원).-----------------
                if self.C_itw_check_btn.isChecked():
                    print("임태원 작업컴퓨터 보냄.")
                    self.C_itw_check_btn.setChecked(False)
                    self.C_itw_check_btn.setEnabled(False)
                    self.임태원_작업컴상태=False
                    # so_Send_data("127.0.0.1",12000,self) #2.데이터를 보낸다.
                #-----------------(이상준).-----------------
                if self.C_sangjun_check_btn.isChecked():
                    print("이상준 작업컴퓨터 보냄.")
                    self.C_sangjun_check_btn.setChecked(False)
                    self.C_sangjun_check_btn.setEnabled(False)
                    self.이상준_작업컴상태=False
                    # so_Send_data("127.0.0.1",12000,self) #2.데이터를 보낸다.
                #-----------------(이상현).-----------------
                if self.C_sanghyone_check_btn.isChecked():
                    print("이상현 작업컴퓨터 보냄.")
                    self.C_sanghyone_check_btn.setChecked(False)
                    self.C_sanghyone_check_btn.setEnabled(False)
                    self.이상현_작업컴상태=False
                    # so_Send_data("127.0.0.1",12000,self) #2.데이터를 보낸다.
                #-----------------(모두).-----------------
                if self.all_check_btn.isChecked():
                    print("모든 작업컴퓨터 보냄.")
                    self.all_check_btn.setChecked(False)
                    self.all_check_btn.setEnabled(False)
                    self.모두_작업컴상태=False
            #-----------------네이버 버튼 체크시.-----------------
                

    
        #-----------------ai리뷰업데이트 버튼 체크시.-----------------
            if self.aireview_radiobtn.isChecked():
                print("ai리뷰업데이트.")
        #-----------------리뷰작성 버튼 체크시.-----------------
            if self.review_write_radiobtn.isChecked():
                print("리뷰작성")
        #-----------------재촉하기 버튼 체크시.-----------------
            if self.pinch_radiobtn.isChecked():
                print("재촉하기")
        #-----------------계좌업데이트 버튼 체크시.-----------------
            if self.accountupdate_radiobtn.isChecked():
                print("계좌업데이트")
                
        
        #-----------------시그널 연결.-----------------
        self.purchasework_radiobtn.clicked.connect(구매작업)
        self.reviewupdate_radiobtn.clicked.connect(리뷰업데이트)
        self.aireview_radiobtn.clicked.connect(Ai리뷰)
        self.review_write_radiobtn.clicked.connect(리뷰작성)
        self.pinch_radiobtn.clicked.connect(재촉하기)
        self.accountupdate_radiobtn.clicked.connect(계좌업데이트)
        self.close_btn.clicked.connect(self.close)
        self.yes_btn.clicked.connect(확인버튼누를시)
        self.Copang_group.clicked.connect(쿠팡체크박스누를시) #쿠팡그룹버튼 클릭시.
 


if __name__=="__main__":
    #큐어플리케이션은 작업반장이다. 
    app=QApplication(sys.argv)
    window=Main_Gui()
    window.show()
    sys.exit(app.exec_())