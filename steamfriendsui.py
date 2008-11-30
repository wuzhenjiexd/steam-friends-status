# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steamfriends.ui'
#
# Created: Sun Nov 30 05:33:16 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SteamFriendsStatus(object):
    def setupUi(self, SteamFriendsStatus):
        SteamFriendsStatus.setObjectName("SteamFriendsStatus")
        SteamFriendsStatus.resize(382, 284)
        self.FetchButton = QtGui.QPushButton(SteamFriendsStatus)
        self.FetchButton.setGeometry(QtCore.QRect(290, 40, 80, 27))
        self.FetchButton.setObjectName("FetchButton")
        self.QuitButton = QtGui.QPushButton(SteamFriendsStatus)
        self.QuitButton.setGeometry(QtCore.QRect(290, 250, 80, 27))
        self.QuitButton.setObjectName("QuitButton")
        self.ListSteamFriends = QtGui.QListWidget(SteamFriendsStatus)
        self.ListSteamFriends.setGeometry(QtCore.QRect(10, 80, 271, 181))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListSteamFriends.sizePolicy().hasHeightForWidth())
        self.ListSteamFriends.setSizePolicy(sizePolicy)
        self.ListSteamFriends.setObjectName("ListSteamFriends")
        QtGui.QListWidgetItem(self.ListSteamFriends)
        QtGui.QListWidgetItem(self.ListSteamFriends)
        self.LabelSteamID = QtGui.QLabel(SteamFriendsStatus)
        self.LabelSteamID.setGeometry(QtCore.QRect(10, 10, 271, 17))
        self.LabelSteamID.setObjectName("LabelSteamID")
        self.label = QtGui.QLabel(SteamFriendsStatus)
        self.label.setGeometry(QtCore.QRect(10, 60, 111, 17))
        self.label.setObjectName("label")
        self.SteamUsername = QtGui.QLineEdit(SteamFriendsStatus)
        self.SteamUsername.setGeometry(QtCore.QRect(10, 30, 271, 23))
        self.SteamUsername.setObjectName("SteamUsername")
        self.actionFetchData = QtGui.QAction(SteamFriendsStatus)
        self.actionFetchData.setObjectName("actionFetchData")
        self.actionPopulateListSteamFriends = QtGui.QAction(SteamFriendsStatus)
        self.actionPopulateListSteamFriends.setObjectName("actionPopulateListSteamFriends")

        self.retranslateUi(SteamFriendsStatus)
        QtCore.QObject.connect(self.QuitButton, QtCore.SIGNAL("clicked()"), SteamFriendsStatus.close)
        QtCore.QObject.connect(self.SteamUsername, QtCore.SIGNAL("returnPressed()"), self.FetchButton.click)
        QtCore.QObject.connect(self.FetchButton, QtCore.SIGNAL("clicked()"), self.ListSteamFriends.clear)
        QtCore.QObject.connect(self.FetchButton, QtCore.SIGNAL("clicked()"), self.actionFetchData.toggle)
        QtCore.QMetaObject.connectSlotsByName(SteamFriendsStatus)

    def retranslateUi(self, SteamFriendsStatus):
        SteamFriendsStatus.setWindowTitle(QtGui.QApplication.translate("SteamFriendsStatus", "Steam Friends Status", None, QtGui.QApplication.UnicodeUTF8))
        self.FetchButton.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Fetch", None, QtGui.QApplication.UnicodeUTF8))
        self.QuitButton.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.ListSteamFriends.isSortingEnabled()
        self.ListSteamFriends.setSortingEnabled(False)
        self.ListSteamFriends.item(0).setText(QtGui.QApplication.translate("SteamFriendsStatus", "Enter your Steam Community ID above", None, QtGui.QApplication.UnicodeUTF8))
        self.ListSteamFriends.item(1).setText(QtGui.QApplication.translate("SteamFriendsStatus", "and click fetch!", None, QtGui.QApplication.UnicodeUTF8))
        self.ListSteamFriends.setSortingEnabled(__sortingEnabled)
        self.LabelSteamID.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Steam Community ID (Numeric or Name)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Your Friends", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFetchData.setText(QtGui.QApplication.translate("SteamFriendsStatus", "FetchData", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPopulateListSteamFriends.setText(QtGui.QApplication.translate("SteamFriendsStatus", "populateListSteamFriends", None, QtGui.QApplication.UnicodeUTF8))

