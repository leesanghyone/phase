import sys
from PyQt5.QtWidgets import *

class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.user_id=None
        self.user_pw=None

    def setupUi(self):
        self.setGeometry(300,300,300,100)
        self.setWindowTitle("회원여부체크")
        self.setFixedSize(300,100)

        label1=QLabel("ID:")
        label2=QLabel("PW:")

        self.lineedit1=QLineEdit()
        self.lineedit2=QLineEdit()

        self.pushButton=QPushButton("로그인")

        layout=QGridLayout()
        layout.addWidget(label1,0,0)
        layout.addWidget(self.lineedit1,0,1)
        layout.addWidget(self.pushButton,0,2)
        layout.addWidget(label2,1,0)
        layout.addWidget(self.lineedit2,1,1)

        self.setLayout(layout)

        self.pushButton.clicked.connect(self.submitlogin)


    def submitlogin(self):

        self.user_id=self.lineedit1.text()
        self.user_pw=self.lineedit2.text()
        print(self.user_id,self.user_pw)

        if self.user_id is None or self.user_id == " " or not self.user_id:
            QMessageBox.about(self,"인증오류입니다","아이디를 입력하세요.")
            self.lineedit1.setFocus()
            return None
        
        if self.user_pw is None or self.user_pw == "" or not self.user_pw:
            QMessageBox.about(self,"인증오류입니다","아이디를 입력하세요.")
            self.lineedit2.setFocus()
            return None
        
        self.close()


if __name__=="__main__":
    #큐어플리케이션은 작업반장이다. 
    app=QApplication(sys.argv)
    window=AuthDialog()
    window.show()
    app.exec_()