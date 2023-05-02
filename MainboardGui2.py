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
        self.initsiganal()

    def initsiganal(self):
        self.Platform_group.setEnabled(False)
        if self.purchasework_radiobtn.isChecked():
           
        self.lcdNumber.clicked.connect(lcdtest)




if __name__=="__main__":
    #큐어플리케이션은 작업반장이다. 
    app=QApplication(sys.argv)
    window=Main_Gui()
    window.show()
    sys.exit(app.exec_())