# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steamfriends.ui'
#
# Created: Mon Dec  1 00:30:10 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SteamFriendsStatus(object):
    def setupUi(self, SteamFriendsStatus):
        SteamFriendsStatus.setObjectName("SteamFriendsStatus")
        SteamFriendsStatus.resize(257, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SteamFriendsStatus.sizePolicy().hasHeightForWidth())
        SteamFriendsStatus.setSizePolicy(sizePolicy)
        self.QuitButton = QtGui.QPushButton(SteamFriendsStatus)
        self.QuitButton.setGeometry(QtCore.QRect(100, 370, 71, 31))
        self.QuitButton.setObjectName("QuitButton")
        self.FetchButton = QtGui.QPushButton(SteamFriendsStatus)
        self.FetchButton.setGeometry(QtCore.QRect(100, 340, 71, 31))
        self.FetchButton.setObjectName("FetchButton")
        self.SteamUsername = QtGui.QLineEdit(SteamFriendsStatus)
        self.SteamUsername.setGeometry(QtCore.QRect(1, 27, 256, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SteamUsername.sizePolicy().hasHeightForWidth())
        self.SteamUsername.setSizePolicy(sizePolicy)
        self.SteamUsername.setObjectName("SteamUsername")
        self.label = QtGui.QLabel(SteamFriendsStatus)
        self.label.setGeometry(QtCore.QRect(0, 50, 256, 17))
        self.label.setObjectName("label")
        self.LabelSteamID = QtGui.QLabel(SteamFriendsStatus)
        self.LabelSteamID.setGeometry(QtCore.QRect(1, 1, 321, 17))
        self.LabelSteamID.setObjectName("LabelSteamID")
        self.ListSteamFriends = QtGui.QListWidget(SteamFriendsStatus)
        self.ListSteamFriends.setGeometry(QtCore.QRect(0, 70, 256, 271))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListSteamFriends.sizePolicy().hasHeightForWidth())
        self.ListSteamFriends.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.ListSteamFriends.setFont(font)
        self.ListSteamFriends.setAutoFillBackground(False)
        self.ListSteamFriends.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ListSteamFriends.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListSteamFriends.setAlternatingRowColors(True)
        self.ListSteamFriends.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ListSteamFriends.setMovement(QtGui.QListView.Static)
        self.ListSteamFriends.setProperty("isWrapping", QtCore.QVariant(False))
        self.ListSteamFriends.setResizeMode(QtGui.QListView.Fixed)
        self.ListSteamFriends.setViewMode(QtGui.QListView.ListMode)
        self.ListSteamFriends.setUniformItemSizes(False)
        self.ListSteamFriends.setWordWrap(True)
        self.ListSteamFriends.setObjectName("ListSteamFriends")
        QtGui.QListWidgetItem(self.ListSteamFriends)
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
        self.QuitButton.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.FetchButton.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Fetch", None, QtGui.QApplication.UnicodeUTF8))
        self.SteamUsername.setToolTip(QtGui.QApplication.translate("SteamFriendsStatus", "The ID numbers or name can be found by browsing to your Steam Community page and looking in the URL.\n"
"Short name: http://steamcommunity.com/id/$Name\n"
"ID number: http://steamcommunity.com/profiles/$Numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("SteamFriendsStatus", "Your online and in-game friends will appear below.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Your Friends", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelSteamID.setToolTip(QtGui.QApplication.translate("SteamFriendsStatus", "The ID numbers or name can be found by browsing to your Steam Community page and looking in the URL.\n"
"Short name: http://steamcommunity.com/id/$Name\n"
"ID number: http://steamcommunity.com/profiles/$Numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelSteamID.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Steam Community Identity (ID/Alias)", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.ListSteamFriends.isSortingEnabled()
        self.ListSteamFriends.setSortingEnabled(False)
        self.ListSteamFriends.item(0).setText(QtGui.QApplication.translate("SteamFriendsStatus", "Enter your Steam Community ID above and click fetch!", None, QtGui.QApplication.UnicodeUTF8))
        self.ListSteamFriends.setSortingEnabled(__sortingEnabled)
        self.actionFetchData.setText(QtGui.QApplication.translate("SteamFriendsStatus", "FetchData", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPopulateListSteamFriends.setText(QtGui.QApplication.translate("SteamFriendsStatus", "populateListSteamFriends", None, QtGui.QApplication.UnicodeUTF8))

