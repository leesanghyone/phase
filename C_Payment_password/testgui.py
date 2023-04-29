import sys 
from PyQt5.QtWidgets  import*
from PyQt5.QtCore import* 
from youtube import Ui_MainWindow
from passwordgui import AuthDialog

class youtube_player(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initlock()
        self.initsignal()
        self.user_id=None
        self.user_pw=None

    def initsignal(self):
        self.pushButton.clicked.connect(self.autocheck)

    def autocheck(self):
        dlg=AuthDialog()
        dlg.show()
        dlg.exec_()

        self.user_id=dlg.user_id
        self.user_pw=dlg.user_pw

        #만약 인증에 성공한다면,
        if True:
            self.initActive()
            self.pushButton.setText("인증완료")
            self.pushButton.setEnabled(False)
        #인증에 실패한다면,
        else:
            pass #현재 아무것도 없다.



    def initlock(self):
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.toolButton.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.showStatusMsg("인증안됨")
      
        
    def initActive(self):
        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.toolButton.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.showStatusMsg("인증완료")



    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)



if __name__=="__main__":
    #큐어플리케이션은 작업반장이다. 
    app=QApplication(sys.argv)
    window=youtube_player()
    window.show()
    sys.exit(app.exec_())