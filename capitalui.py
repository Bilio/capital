# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/capital.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 765)
        MainWindow.setMaximumSize(QtCore.QSize(1360, 765))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBtn.setGeometry(QtCore.QRect(2, 2, 96, 96))
        self.connectBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/新前置字串/led_redoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/新前置字串/led_greenon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.connectBtn.setIcon(icon)
        self.connectBtn.setIconSize(QtCore.QSize(96, 96))
        self.connectBtn.setCheckable(True)
        self.connectBtn.setObjectName("connectBtn")
        self.msgBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.msgBrowser.setGeometry(QtCore.QRect(2, 626, 257, 93))
        self.msgBrowser.setObjectName("msgBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 2, 160, 50))
        self.groupBox.setObjectName("groupBox")
        self.userIDLine = QtWidgets.QLineEdit(self.groupBox)
        self.userIDLine.setGeometry(QtCore.QRect(4, 12, 150, 32))
        self.userIDLine.setInputMask("")
        self.userIDLine.setText("")
        self.userIDLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userIDLine.setObjectName("userIDLine")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 48, 160, 50))
        self.groupBox_2.setObjectName("groupBox_2")
        self.passwordLine = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwordLine.setGeometry(QtCore.QRect(4, 12, 150, 32))
        self.passwordLine.setText("")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.skstockTab = QtWidgets.QTabWidget(self.centralwidget)
        self.skstockTab.setGeometry(QtCore.QRect(266, 6, 1087, 711))
        self.skstockTab.setTabsClosable(True)
        self.skstockTab.setObjectName("skstockTab")
        self.semTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.semTree.setGeometry(QtCore.QRect(2, 100, 256, 523))
        self.semTree.setObjectName("semTree")
        self.semTree.headerItem().setText(0, "1")
        self.semTree.header().setVisible(True)
        self.semTree.header().setCascadingSectionResizes(False)
        self.semTree.header().setDefaultSectionSize(120)
        self.semTree.header().setHighlightSections(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDataBase = QtWidgets.QMenu(self.menubar)
        self.menuDataBase.setObjectName("menuDataBase")
        self.menuAbou = QtWidgets.QMenu(self.menubar)
        self.menuAbou.setObjectName("menuAbou")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIntraCMD = QtWidgets.QAction(MainWindow)
        self.actionIntraCMD.setCheckable(True)
        self.actionIntraCMD.setChecked(False)
        self.actionIntraCMD.setEnabled(True)
        self.actionIntraCMD.setObjectName("actionIntraCMD")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.actionWarrant = QtWidgets.QAction(MainWindow)
        self.actionWarrant.setObjectName("actionWarrant")
        self.actionStockKLine = QtWidgets.QAction(MainWindow)
        self.actionStockKLine.setCheckable(True)
        self.actionStockKLine.setObjectName("actionStockKLine")
        self.menuFile.addAction(self.action_Exit)
        self.menuDataBase.addAction(self.actionWarrant)
        self.menuDataBase.addAction(self.actionStockKLine)
        self.menuAbou.addAction(self.actionIntraCMD)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDataBase.menuAction())
        self.menubar.addAction(self.menuAbou.menuAction())

        self.retranslateUi(MainWindow)
        self.skstockTab.setCurrentIndex(-1)
        self.action_Exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "User"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDataBase.setTitle(_translate("MainWindow", "DataBase"))
        self.menuAbou.setTitle(_translate("MainWindow", "Develop"))
        self.actionIntraCMD.setText(_translate("MainWindow", "IntraCMD"))
        self.action_Exit.setText(_translate("MainWindow", "Exit"))
        self.actionWarrant.setText(_translate("MainWindow", "Warrant"))
        self.actionStockKLine.setText(_translate("MainWindow", "Stock - Day-KLine"))

import capital_rc
