# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGui.ui'
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
        self.Naver_grop = QtWidgets.QGroupBox(self.workcom)
        self.Naver_grop.setEnabled(True)
        self.Naver_grop.setGeometry(QtCore.QRect(10, 20, 101, 211))
        self.Naver_grop.setMouseTracking(False)
        self.Naver_grop.setAcceptDrops(False)
        self.Naver_grop.setAutoFillBackground(False)
        self.Naver_grop.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Naver_grop.setFlat(False)
        self.Naver_grop.setCheckable(True)
        self.Naver_grop.setChecked(False)
        self.Naver_grop.setObjectName("Naver_grop")
        self.parck_check_btn = QtWidgets.QCheckBox(self.Naver_grop)
        self.parck_check_btn.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.parck_check_btn.setObjectName("parck_check_btn")
        self.itw_check_btn = QtWidgets.QCheckBox(self.Naver_grop)
        self.itw_check_btn.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.itw_check_btn.setObjectName("itw_check_btn")
        self.sangjun_check_btn = QtWidgets.QCheckBox(self.Naver_grop)
        self.sangjun_check_btn.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.sangjun_check_btn.setObjectName("sangjun_check_btn")
        self.sanghyone_check_btn = QtWidgets.QCheckBox(self.Naver_grop)
        self.sanghyone_check_btn.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.sanghyone_check_btn.setObjectName("sanghyone_check_btn")
        self.all_check_btn = QtWidgets.QCheckBox(self.Naver_grop)
        self.all_check_btn.setGeometry(QtCore.QRect(10, 160, 81, 16))
        self.all_check_btn.setObjectName("all_check_btn")
        self.Copang_group = QtWidgets.QGroupBox(self.workcom)
        self.Copang_group.setGeometry(QtCore.QRect(121, 19, 101, 211))
        self.Copang_group.setFlat(False)
        self.Copang_group.setCheckable(True)
        self.Copang_group.setChecked(False)
        self.Copang_group.setObjectName("Copang_group")
        self.C_parck_check_btn = QtWidgets.QCheckBox(self.Copang_group)
        self.C_parck_check_btn.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.C_parck_check_btn.setObjectName("C_parck_check_btn")
        self.C_itw_check_btn = QtWidgets.QCheckBox(self.Copang_group)
        self.C_itw_check_btn.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.C_itw_check_btn.setObjectName("C_itw_check_btn")
        self.C_sangjun_check_btn = QtWidgets.QCheckBox(self.Copang_group)
        self.C_sangjun_check_btn.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.C_sangjun_check_btn.setObjectName("C_sangjun_check_btn")
        self.C_sanghyone_check_btn = QtWidgets.QCheckBox(self.Copang_group)
        self.C_sanghyone_check_btn.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.C_sanghyone_check_btn.setObjectName("C_sanghyone_check_btn")
        self.C_all_check_btn = QtWidgets.QCheckBox(self.Copang_group)
        self.C_all_check_btn.setGeometry(QtCore.QRect(10, 160, 81, 16))
        self.C_all_check_btn.setObjectName("C_all_check_btn")
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
        self.reviewupdate_radiobtn.setGeometry(QtCore.QRect(10, 60, 90, 16))
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
        self.accountupdate_radiobtn.setGeometry(QtCore.QRect(10, 180, 90, 16))
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
        self.Naver_grop.setTitle(_translate("mainWindow", "네이버"))
        self.parck_check_btn.setText(_translate("mainWindow", "박경희"))
        self.itw_check_btn.setText(_translate("mainWindow", "임태원"))
        self.sangjun_check_btn.setText(_translate("mainWindow", "이상준"))
        self.sanghyone_check_btn.setText(_translate("mainWindow", "이상현"))
        self.all_check_btn.setText(_translate("mainWindow", "전부"))
        self.Copang_group.setTitle(_translate("mainWindow", "쿠팡"))
        self.C_parck_check_btn.setText(_translate("mainWindow", "박경희"))
        self.C_itw_check_btn.setText(_translate("mainWindow", "임태원"))
        self.C_sangjun_check_btn.setText(_translate("mainWindow", "이상준"))
        self.C_sanghyone_check_btn.setText(_translate("mainWindow", "이상현"))
        self.C_all_check_btn.setText(_translate("mainWindow", "전부"))
        self.yes_btn.setText(_translate("mainWindow", "확인"))
        self.close_btn.setText(_translate("mainWindow", "닫기"))
        self.worway_grop.setTitle(_translate("mainWindow", "작업방식"))
        self.purchasework_radiobtn.setText(_translate("mainWindow", "구매작업"))
        self.reviewupdate_radiobtn.setText(_translate("mainWindow", "리뷰업데이트"))
        self.aireview_radiobtn.setText(_translate("mainWindow", "Ai리뷰"))
        self.review_write_radiobtn.setText(_translate("mainWindow", "리뷰작성"))
        self.pinch_radiobtn.setText(_translate("mainWindow", "재촉하기"))
        self.accountupdate_radiobtn.setText(_translate("mainWindow", "계좌업데이트"))
        self.accountupdate_radiobtn.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
