# Form implementation generated from reading ui file 'UI\ui_GiaiMaVigenere.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 384)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(236, 249, 255);\n"
"")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 100, 121, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pB_MaHoa = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pB_MaHoa.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.pB_MaHoa.setStyleSheet("background-color: rgb(248, 203, 166);\n"
"color: rgb(255, 255, 255);")
        self.pB_MaHoa.setObjectName("pB_MaHoa")
        self.pB_Refresh = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pB_Refresh.setGeometry(QtCore.QRect(20, 90, 81, 31))
        self.pB_Refresh.setStyleSheet("background-color: rgb(248, 203, 166);\n"
"color: rgb(255, 255, 255);")
        self.pB_Refresh.setObjectName("pB_Refresh")
        self.pB_LuuFile = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pB_LuuFile.setGeometry(QtCore.QRect(20, 150, 81, 31))
        self.pB_LuuFile.setStyleSheet("background-color: rgb(248, 203, 166);\n"
"color: rgb(255, 255, 255);")
        self.pB_LuuFile.setObjectName("pB_LuuFile")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 101, 21))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 101, 21))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lE_FileIn = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lE_FileIn.setGeometry(QtCore.QRect(160, 30, 351, 21))
        self.lE_FileIn.setText("")
        self.lE_FileIn.setObjectName("lE_FileIn")
        self.lE_Key = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lE_Key.setGeometry(QtCore.QRect(160, 60, 281, 21))
        self.lE_Key.setText("")
        self.lE_Key.setObjectName("lE_Key")
        self.pB_ChooseFile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pB_ChooseFile.setGeometry(QtCore.QRect(530, 30, 75, 23))
        self.pB_ChooseFile.setObjectName("pB_ChooseFile")
        self.tB_Content = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.tB_Content.setGeometry(QtCore.QRect(160, 100, 461, 201))
        self.tB_Content.setObjectName("tB_Content")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 22))
        self.menubar.setObjectName("menubar")
        self.menuM_H_a = QtWidgets.QMenu(parent=self.menubar)
        self.menuM_H_a.setObjectName("menuM_H_a")
        self.menuRSA = QtWidgets.QMenu(parent=self.menuM_H_a)
        self.menuRSA.setObjectName("menuRSA")
        self.menuGi_i_M = QtWidgets.QMenu(parent=self.menubar)
        self.menuGi_i_M.setObjectName("menuGi_i_M")
        self.menuRSA_2 = QtWidgets.QMenu(parent=self.menuGi_i_M)
        self.menuRSA_2.setObjectName("menuRSA_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ac_MH_RSA = QtGui.QAction(parent=MainWindow)
        self.ac_MH_RSA.setObjectName("ac_MH_RSA")
        self.ac_MH_SDES = QtGui.QAction(parent=MainWindow)
        self.ac_MH_SDES.setObjectName("ac_MH_SDES")
        self.ac_MH_Belasco = QtGui.QAction(parent=MainWindow)
        self.ac_MH_Belasco.setObjectName("ac_MH_Belasco")
        self.ac_MH_ChuyenVi = QtGui.QAction(parent=MainWindow)
        self.ac_MH_ChuyenVi.setObjectName("ac_MH_ChuyenVi")
        self.ac_GM_RSA = QtGui.QAction(parent=MainWindow)
        self.ac_GM_RSA.setObjectName("ac_GM_RSA")
        self.ac_GM_SDES = QtGui.QAction(parent=MainWindow)
        self.ac_GM_SDES.setObjectName("ac_GM_SDES")
        self.ac_GM_Belasco = QtGui.QAction(parent=MainWindow)
        self.ac_GM_Belasco.setObjectName("ac_GM_Belasco")
        self.ac_GM_ChuyenVi = QtGui.QAction(parent=MainWindow)
        self.ac_GM_ChuyenVi.setObjectName("ac_GM_ChuyenVi")
        self.ac_MH_Vigenere = QtGui.QAction(parent=MainWindow)
        self.ac_MH_Vigenere.setObjectName("ac_MH_Vigenere")
        self.ac_GM_Vigenre = QtGui.QAction(parent=MainWindow)
        self.ac_GM_Vigenre.setObjectName("ac_GM_Vigenre")
        self.ac_MH_TaoKhoa = QtGui.QAction(parent=MainWindow)
        self.ac_MH_TaoKhoa.setObjectName("ac_MH_TaoKhoa")
        self.ac_MH_RSA_2 = QtGui.QAction(parent=MainWindow)
        self.ac_MH_RSA_2.setObjectName("ac_MH_RSA_2")
        self.ac_GM_TaoKhoa = QtGui.QAction(parent=MainWindow)
        self.ac_GM_TaoKhoa.setObjectName("ac_GM_TaoKhoa")
        self.ac_GM_RSA_2 = QtGui.QAction(parent=MainWindow)
        self.ac_GM_RSA_2.setObjectName("ac_GM_RSA_2")
        self.menuRSA.addAction(self.ac_MH_TaoKhoa)
        self.menuRSA.addSeparator()
        self.menuRSA.addAction(self.ac_MH_RSA_2)
        self.menuM_H_a.addAction(self.ac_MH_SDES)
        self.menuM_H_a.addSeparator()
        self.menuM_H_a.addAction(self.ac_MH_Belasco)
        self.menuM_H_a.addSeparator()
        self.menuM_H_a.addAction(self.ac_MH_ChuyenVi)
        self.menuM_H_a.addSeparator()
        self.menuM_H_a.addAction(self.ac_MH_Vigenere)
        self.menuM_H_a.addSeparator()
        self.menuM_H_a.addAction(self.menuRSA.menuAction())
        self.menuRSA_2.addAction(self.ac_GM_TaoKhoa)
        self.menuRSA_2.addSeparator()
        self.menuRSA_2.addAction(self.ac_GM_RSA_2)
        self.menuGi_i_M.addAction(self.ac_GM_SDES)
        self.menuGi_i_M.addSeparator()
        self.menuGi_i_M.addAction(self.ac_GM_Belasco)
        self.menuGi_i_M.addSeparator()
        self.menuGi_i_M.addAction(self.ac_GM_ChuyenVi)
        self.menuGi_i_M.addSeparator()
        self.menuGi_i_M.addAction(self.ac_GM_Vigenre)
        self.menuGi_i_M.addSeparator()
        self.menuGi_i_M.addAction(self.menuRSA_2.menuAction())
        self.menubar.addAction(self.menuM_H_a.menuAction())
        self.menubar.addAction(self.menuGi_i_M.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giải Mã Vigenere"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Chức năng"))
        self.pB_MaHoa.setText(_translate("MainWindow", "Giải mã"))
        self.pB_Refresh.setText(_translate("MainWindow", "Làm mới"))
        self.pB_LuuFile.setText(_translate("MainWindow", "Lưu file"))
        self.label.setText(_translate("MainWindow", "File văn bản"))
        self.label_2.setText(_translate("MainWindow", "Nhập khóa"))
        self.pB_ChooseFile.setText(_translate("MainWindow", "Chọn file"))
        self.menuM_H_a.setTitle(_translate("MainWindow", "Mã Hóa"))
        self.menuRSA.setTitle(_translate("MainWindow", "RSA"))
        self.menuGi_i_M.setTitle(_translate("MainWindow", "Giải Mã"))
        self.menuRSA_2.setTitle(_translate("MainWindow", "RSA"))
        self.ac_MH_RSA.setText(_translate("MainWindow", "RSA"))
        self.ac_MH_SDES.setText(_translate("MainWindow", "SDES"))
        self.ac_MH_Belasco.setText(_translate("MainWindow", "Belasco"))
        self.ac_MH_ChuyenVi.setText(_translate("MainWindow", "Chuyển vị"))
        self.ac_GM_RSA.setText(_translate("MainWindow", "RSA"))
        self.ac_GM_SDES.setText(_translate("MainWindow", "SDES"))
        self.ac_GM_Belasco.setText(_translate("MainWindow", "Belasco"))
        self.ac_GM_ChuyenVi.setText(_translate("MainWindow", "Chuyển vị"))
        self.ac_MH_Vigenere.setText(_translate("MainWindow", "Vigenere"))
        self.ac_GM_Vigenre.setText(_translate("MainWindow", "Vigenere"))
        self.ac_MH_TaoKhoa.setText(_translate("MainWindow", "Tạo khóa"))
        self.ac_MH_RSA_2.setText(_translate("MainWindow", "Mã hóa"))
        self.ac_GM_TaoKhoa.setText(_translate("MainWindow", "Tạo Khóa"))
        self.ac_GM_RSA_2.setText(_translate("MainWindow", "Giải Mã"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
