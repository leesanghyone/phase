# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(382, 506)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(382, 506))
        mainWindow.setMaximumSize(QtCore.QSize(382, 506))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.workcom = QtWidgets.QGroupBox(self.centralwidget)
        self.workcom.setEnabled(True)
        self.workcom.setGeometry(QtCore.QRect(10, 10, 231, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workcom.sizePolicy().hasHeightForWidth())
        self.workcom.setSizePolicy(sizePolicy)
        self.workcom.setMinimumSize(QtCore.QSize(0, 0))
        self.workcom.setMaximumSize(QtCore.QSize(999999, 999999))
        self.workcom.setFlat(False)
        self.workcom.setCheckable(False)
        self.workcom.setObjectName("workcom")
        self.Platform_group = QtWidgets.QGroupBox(self.workcom)
        self.Platform_group.setGeometry(QtCore.QRect(10, 20, 91, 101))
        self.Platform_group.setFlat(False)
        self.Platform_group.setCheckable(False)
        self.Platform_group.setChecked(False)
        self.Platform_group.setObjectName("Platform_group")
        self.platform_check_naver = QtWidgets.QCheckBox(self.Platform_group)
        self.platform_check_naver.setGeometry(QtCore.QRect(13, 30, 61, 16))
        self.platform_check_naver.setObjectName("platform_check_naver")
        self.platform_check_coopang = QtWidgets.QCheckBox(self.Platform_group)
        self.platform_check_coopang.setGeometry(QtCore.QRect(13, 60, 51, 16))
        self.platform_check_coopang.setObjectName("platform_check_coopang")
        self.augomation_group = QtWidgets.QGroupBox(self.workcom)
        self.augomation_group.setGeometry(QtCore.QRect(10, 130, 91, 101))
        self.augomation_group.setFlat(False)
        self.augomation_group.setCheckable(False)
        self.augomation_group.setChecked(False)
        self.augomation_group.setObjectName("augomation_group")
        self.auto_reviewbtn = QtWidgets.QRadioButton(self.augomation_group)
        self.auto_reviewbtn.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.auto_reviewbtn.setObjectName("auto_reviewbtn")
        self.WorkCom_grop = QtWidgets.QGroupBox(self.workcom)
        self.WorkCom_grop.setEnabled(True)
        self.WorkCom_grop.setGeometry(QtCore.QRect(110, 20, 111, 211))
        self.WorkCom_grop.setMouseTracking(False)
        self.WorkCom_grop.setAcceptDrops(False)
        self.WorkCom_grop.setAutoFillBackground(False)
        self.WorkCom_grop.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.WorkCom_grop.setFlat(False)
        self.WorkCom_grop.setCheckable(False)
        self.WorkCom_grop.setChecked(False)
        self.WorkCom_grop.setObjectName("WorkCom_grop")
        self.parck_check_btn = QtWidgets.QCheckBox(self.WorkCom_grop)
        self.parck_check_btn.setGeometry(QtCore.QRect(10, 33, 81, 16))
        self.parck_check_btn.setObjectName("parck_check_btn")
        self.itw_check_btn = QtWidgets.QCheckBox(self.WorkCom_grop)
        self.itw_check_btn.setGeometry(QtCore.QRect(10, 63, 81, 16))
        self.itw_check_btn.setObjectName("itw_check_btn")
        self.sangjun_check_btn = QtWidgets.QCheckBox(self.WorkCom_grop)
        self.sangjun_check_btn.setGeometry(QtCore.QRect(10, 93, 81, 16))
        self.sangjun_check_btn.setObjectName("sangjun_check_btn")
        self.sanghyone_check_btn = QtWidgets.QCheckBox(self.WorkCom_grop)
        self.sanghyone_check_btn.setGeometry(QtCore.QRect(10, 123, 81, 16))
        self.sanghyone_check_btn.setObjectName("sanghyone_check_btn")
        self.all_check_btn = QtWidgets.QCheckBox(self.WorkCom_grop)
        self.all_check_btn.setGeometry(QtCore.QRect(10, 163, 81, 16))
        self.all_check_btn.setObjectName("all_check_btn")
        self.server1_btn = QtWidgets.QPushButton(self.WorkCom_grop)
        self.server1_btn.setGeometry(QtCore.QRect(70, 33, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server1_btn.setFont(font)
        self.server1_btn.setObjectName("server1_btn")
        self.server2_btn = QtWidgets.QPushButton(self.WorkCom_grop)
        self.server2_btn.setGeometry(QtCore.QRect(70, 63, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server2_btn.setFont(font)
        self.server2_btn.setObjectName("server2_btn")
        self.server3_btn = QtWidgets.QPushButton(self.WorkCom_grop)
        self.server3_btn.setGeometry(QtCore.QRect(70, 93, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server3_btn.setFont(font)
        self.server3_btn.setObjectName("server3_btn")
        self.server4_btn = QtWidgets.QPushButton(self.WorkCom_grop)
        self.server4_btn.setGeometry(QtCore.QRect(70, 123, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server4_btn.setFont(font)
        self.server4_btn.setObjectName("server4_btn")
        self.allserver_btn = QtWidgets.QPushButton(self.WorkCom_grop)
        self.allserver_btn.setGeometry(QtCore.QRect(60, 160, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.allserver_btn.setFont(font)
        self.allserver_btn.setObjectName("allserver_btn")
        self.log_plainEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log_plainEdit.setGeometry(QtCore.QRect(10, 260, 361, 161))
        self.log_plainEdit.setReadOnly(True)
        self.log_plainEdit.setObjectName("log_plainEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 430, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.yes_btn.setObjectName("yes_btn")
        self.horizontalLayout.addWidget(self.yes_btn)
        self.close_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.worway_grop = QtWidgets.QGroupBox(self.centralwidget)
        self.worway_grop.setGeometry(QtCore.QRect(250, 10, 121, 241))
        self.worway_grop.setMouseTracking(False)
        self.worway_grop.setTabletTracking(False)
        self.worway_grop.setAcceptDrops(False)
        self.worway_grop.setObjectName("worway_grop")
        self.purchasework_radiobtn = QtWidgets.QRadioButton(self.worway_grop)
        self.purchasework_radiobtn.setGeometry(QtCore.QRect(10, 30, 90, 16))
        self.purchasework_radiobtn.setChecked(True)
        self.purchasework_radiobtn.setObjectName("purchasework_radiobtn")
        self.reviewupdate_radiobtn = QtWidgets.QRadioButton(self.worway_grop)
        self.reviewupdate_radiobtn.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.reviewupdate_radiobtn.setObjectName("reviewupdate_radiobtn")
        self.aireview_radiobtn = QtWidgets.QRadioButton(self.worway_grop)
        self.aireview_radiobtn.setGeometry(QtCore.QRect(10, 90, 90, 16))
        self.aireview_radiobtn.setObjectName("aireview_radiobtn")
        self.review_write_radiobtn = QtWidgets.QRadioButton(self.worway_grop)
        self.review_write_radiobtn.setGeometry(QtCore.QRect(10, 120, 90, 16))
        self.review_write_radiobtn.setObjectName("review_write_radiobtn")
        self.pinch_radiobtn = QtWidgets.QRadioButton(self.worway_grop)
        self.pinch_radiobtn.setGeometry(QtCore.QRect(10, 150, 90, 16))
        self.pinch_radiobtn.setObjectName("pinch_radiobtn")
        self.accountupdate_radiobtn = QtWidgets.QRadioButton(self.worway_grop)
        self.accountupdate_radiobtn.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.accountupdate_radiobtn.setObjectName("accountupdate_radiobtn")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "LEE"))
        self.workcom.setTitle(_translate("mainWindow", "작업컴퓨터"))
        self.Platform_group.setTitle(_translate("mainWindow", "플랫폼"))
        self.platform_check_naver.setText(_translate("mainWindow", "네이버"))
        self.platform_check_coopang.setText(_translate("mainWindow", "쿠팡"))
        self.augomation_group.setTitle(_translate("mainWindow", "자동화 설정"))
        self.auto_reviewbtn.setText(_translate("mainWindow", "개발중"))
        self.WorkCom_grop.setTitle(_translate("mainWindow", "작업컴"))
        self.parck_check_btn.setText(_translate("mainWindow", "박경희"))
        self.itw_check_btn.setText(_translate("mainWindow", "임태원"))
        self.sangjun_check_btn.setText(_translate("mainWindow", "이상준"))
        self.sanghyone_check_btn.setText(_translate("mainWindow", "이상현"))
        self.all_check_btn.setText(_translate("mainWindow", "전부"))
        self.server1_btn.setText(_translate("mainWindow", "0"))
        self.server2_btn.setText(_translate("mainWindow", "0"))
        self.server3_btn.setText(_translate("mainWindow", "0"))
        self.server4_btn.setText(_translate("mainWindow", "0"))
        self.allserver_btn.setText(_translate("mainWindow", "갱신"))
        self.yes_btn.setText(_translate("mainWindow", "확인"))
        self.close_btn.setText(_translate("mainWindow", "닫기"))
        self.worway_grop.setTitle(_translate("mainWindow", "작업방식"))
        self.purchasework_radiobtn.setText(_translate("mainWindow", "1.구매작업"))
        self.reviewupdate_radiobtn.setText(_translate("mainWindow", "2.리뷰업데이트"))
        self.aireview_radiobtn.setText(_translate("mainWindow", "3.Ai리뷰"))
        self.review_write_radiobtn.setText(_translate("mainWindow", "4.리뷰작성"))
        self.pinch_radiobtn.setText(_translate("mainWindow", "5.재촉하기"))
        self.accountupdate_radiobtn.setText(_translate("mainWindow", "6.계좌업데이트"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
