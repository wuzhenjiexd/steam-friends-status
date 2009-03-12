# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverList.ui'
#
# Created: Thu Mar 12 15:26:11 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_serverList(object):
    def setupUi(self, serverList):
        serverList.setObjectName("serverList")
        serverList.resize(428, 466)
        serverList.setMaximumSize(QtCore.QSize(428, 466))
        self.serverInfoWidget = QtGui.QListWidget(serverList)
        self.serverInfoWidget.setGeometry(QtCore.QRect(0, 10, 421, 191))
        self.serverInfoWidget.setMaximumSize(QtCore.QSize(421, 191))
        self.serverInfoWidget.setObjectName("serverInfoWidget")
        self.tableScores = QtGui.QTableWidget(serverList)
        self.tableScores.setGeometry(QtCore.QRect(0, 210, 421, 221))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableScores.sizePolicy().hasHeightForWidth())
        self.tableScores.setSizePolicy(sizePolicy)
        self.tableScores.setMaximumSize(QtCore.QSize(421, 221))
        self.tableScores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableScores.setAlternatingRowColors(True)
        self.tableScores.setShowGrid(False)
        self.tableScores.setWordWrap(False)
        self.tableScores.setCornerButtonEnabled(False)
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
        self.closeButton = QtGui.QPushButton(serverList)
        self.closeButton.setGeometry(QtCore.QRect(330, 430, 80, 29))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(serverList)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), serverList.close)
        QtCore.QMetaObject.connectSlotsByName(serverList)

    def retranslateUi(self, serverList):
        serverList.setWindowTitle(QtGui.QApplication.translate("serverList", "Server Information", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.setSortingEnabled(True)
        self.tableScores.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("serverList", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("serverList", "Score", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("serverList", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("serverList", "Close", None, QtGui.QApplication.UnicodeUTF8))

