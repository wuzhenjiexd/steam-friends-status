# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverList.ui'
#
# Created: Thu Mar 12 05:16:15 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_serverList(object):
    def setupUi(self, serverList):
        serverList.setObjectName("serverList")
        serverList.resize(392, 376)
        self.okButtonBox = QtGui.QDialogButtonBox(serverList)
        self.okButtonBox.setGeometry(QtCore.QRect(30, 340, 351, 32))
        self.okButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.okButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.okButtonBox.setObjectName("okButtonBox")
        self.serverInfoWidget = QtGui.QListWidget(serverList)
        self.serverInfoWidget.setGeometry(QtCore.QRect(10, 10, 371, 151))
        self.serverInfoWidget.setObjectName("serverInfoWidget")
        self.tableScores = QtGui.QTableWidget(serverList)
        self.tableScores.setGeometry(QtCore.QRect(10, 170, 371, 171))
        self.tableScores.setAlternatingRowColors(True)
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

        self.retranslateUi(serverList)
        QtCore.QObject.connect(self.okButtonBox, QtCore.SIGNAL("clicked(QAbstractButton*)"), serverList.close)
        QtCore.QMetaObject.connectSlotsByName(serverList)

    def retranslateUi(self, serverList):
        serverList.setWindowTitle(QtGui.QApplication.translate("serverList", "Server Information", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("serverList", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("serverList", "Score", None, QtGui.QApplication.UnicodeUTF8))
        self.tableScores.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("serverList", "Time", None, QtGui.QApplication.UnicodeUTF8))

