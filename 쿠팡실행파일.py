import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from coupang_input_gui import Ui_C_inputDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from Coupang_work_fungtion import *

class Coupang(QWidget,Ui_C_inputDialog):
    def __init__(self):
        super().__init__()
    
        self.setupUi(self)
            #ui불러오고 있어야, 이름명이 바뀜.
        self.setWindowTitle("쿠팡입력") 

        #시그널 슬롯연결.
        self.close_btn.clicked.connect(sys.exit)
        self.okay_btn.clicked.connect(self.SendData)


    def SendData(self):
        url=self.url1_inputEdit.text()
        # 일반결제=self.sinyongcard.isChecked()
        구매수량=int(self.moq.text())
        장바구니=self.jangbaguni.isChecked()
        체류시간=int(self.page_scroll_time.text())*60
        옵션1=int(self.options1.text())
        옵션2=int(self.options2.text())
        찜작업=self.jjim_check.isChecked()
        # 결제창스크린샷=self.Payresult_check.isChecked()
        최소가격=int(self.minprice_spinbox.text())
        최대가격=int(self.maxprice_spinbox.text())
        배송메세지=str(self.basongmsg_LineEdit.text())
        # 포인트=self.point.isChecked()
        #유효성 검사.
        if 최소가격 > 1 and 최대가격 <= 1:
            최대가격=최소가격 + 1000

            #1.데이터 필터링.
        if 최소가격 < 1:
            최소가격=None
            최대가격=None
            #최대가격 자동입력(최소가격만 입력하면 됨)
                
            #2.url필터링
        if url.find("srp_product_ads&clickEventId") != -1:
            QMessageBox.warning(self,"광고상품링크","당신의 url은 광고상품이에요.")
        coupang_start(url=url,minprice=최소가격,maxprice=최대가격,page_view_time=체류시간,moq=구매수량,jjim=찜작업,optionmenus1=옵션1,optionmenus2=옵션2,jangbaguni=장바구니,point=False,msg=배송메세지)
        
        
        

if __name__ == '__main__':
    app=QApplication(sys.argv)
    # app.setStyle("fusion") #켜면 모양이 어그러진다.
    cou=Coupang()
    cou.show()
    sys.exit(app.exec_())