# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverList.ui'
#
# Created: Thu Mar 12 14:57:10 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_serverList(object):
    def setupUi(self, serverList):
        serverList.setObjectName("serverList")
        serverList.resize(428, 466)
        self.serverInfoWidget = QtGui.QListWidget(serverList)
        self.serverInfoWidget.setGeometry(QtCore.QRect(0, 10, 421, 231))
        self.serverInfoWidget.setObjectName("serverInfoWidget")
        self.tableScores = QtGui.QTableWidget(serverList)
        self.tableScores.setGeometry(QtCore.QRect(0, 250, 421, 171))
        self.tableScores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableScores.setAlternatingRowColors(False)
        self.tableScores.setRowCount(0)
        self.tableScores.setColumnCount(3)
        self.tableScores.setObjectName("tableScores")
        self.tableScores.setColumnCount(3)
        self.tableScores.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableScores.setHorizontalHeaderItem(2, item)
        self.refreshButton = QtGui.QPushButton(serverList)
        self.refreshButton.setGeometry(QtCore.QRect(240, 430, 80, 29))
        self.refreshButton.setObjectName("refreshButton")
        self.closeButton = QtGui.QPushButton(serverList)
        self.closeButton.setGeometry(QtCore.QRect(330, 430, 80, 29))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(serverList)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), serverList.close)
        QtCore.QObject.connect(self.refreshButton, QtCore.SIGNAL("clicked()"), serverList.update)
        QtCore.QMetaObject.connectSlotsByName(serverList)

    def retranslateUi(self, serverList):
        serverList.setWindowTitle(QtGui.QApplication.translate("serverList", "Server Information", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.setSortingEnabled(True)
        self.tableScores.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("serverList", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("serverList", "Score", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("serverList", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("serverList", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("serverList", "Close", None, QtGui.QApplication.UnicodeUTF8))

