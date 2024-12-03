# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(280, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 220))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(400, 300))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.showProcessBtn = QtWidgets.QPushButton(self.frame_4)
        self.showProcessBtn.setGeometry(QtCore.QRect(30, 60, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.showProcessBtn.setFont(font)
        self.showProcessBtn.setStyleSheet("background:white;\n"
"border:2px solid #CB1832;\n"
"border-radius:12px;\n"
"color:black;")
        self.showProcessBtn.setObjectName("showProcessBtn")
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background:#fff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(700, 280))
        self.frame_3.setStyleSheet("border-radius:20px;\n"
"color:white;\n"
"background:#232323;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.searchBar = QtWidgets.QLineEdit(self.frame_3)
        self.searchBar.setGeometry(QtCore.QRect(110, 80, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchBar.setFont(font)
        self.searchBar.setStyleSheet("padding:10px;\n"
"color:black;\n"
"background:#fff;")
        self.searchBar.setObjectName("searchBar")
        self.searchByWordBtn = QtWidgets.QPushButton(self.frame_3)
        self.searchByWordBtn.setGeometry(QtCore.QRect(130, 150, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.searchByWordBtn.setFont(font)
        self.searchByWordBtn.setStyleSheet("background:#CB1832;\n"
"border:none;\n"
"border-radius:12px;\n"
"color:white;")
        self.searchByWordBtn.setObjectName("searchByWordBtn")
        self.searchByContentBtn = QtWidgets.QPushButton(self.frame_3)
        self.searchByContentBtn.setGeometry(QtCore.QRect(330, 150, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.searchByContentBtn.setFont(font)
        self.searchByContentBtn.setStyleSheet("background:#CB1832;\n"
"border:none;\n"
"border-radius:12px;\n"
"color:white;")
        self.searchByContentBtn.setObjectName("searchByContentBtn")
        self.gridLayout_3.addWidget(self.frame_3, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 172, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 172, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showProcessBtn.setText(_translate("MainWindow", "Show Process"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Enter Query Here..."))
        self.searchByWordBtn.setText(_translate("MainWindow", "Search By Word"))
        self.searchByContentBtn.setText(_translate("MainWindow", "Search By Content"))
        self.label.setText(_translate("MainWindow", "Moogl e Azam"))
import resource_rc