# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steamfriends.ui'
#
# Created: Sat Apr 25 02:08:36 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SteamFriendsStatus(object):
    def setupUi(self, SteamFriendsStatus):
        SteamFriendsStatus.setObjectName("SteamFriendsStatus")
        SteamFriendsStatus.resize(257, 360)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SteamFriendsStatus.sizePolicy().hasHeightForWidth())
        SteamFriendsStatus.setSizePolicy(sizePolicy)
        SteamFriendsStatus.setMaximumSize(QtCore.QSize(257, 360))
        self.SteamUsername = QtGui.QLineEdit(SteamFriendsStatus)
        self.SteamUsername.setGeometry(QtCore.QRect(10, 20, 191, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SteamUsername.sizePolicy().hasHeightForWidth())
        self.SteamUsername.setSizePolicy(sizePolicy)
        self.SteamUsername.setObjectName("SteamUsername")
        self.LabelSteamID = QtGui.QLabel(SteamFriendsStatus)
        self.LabelSteamID.setGeometry(QtCore.QRect(10, 0, 241, 20))
        self.LabelSteamID.setFrameShape(QtGui.QFrame.NoFrame)
        self.LabelSteamID.setFrameShadow(QtGui.QFrame.Plain)
        self.LabelSteamID.setObjectName("LabelSteamID")
        self.ListSteamFriends = QtGui.QListWidget(SteamFriendsStatus)
        self.ListSteamFriends.setGeometry(QtCore.QRect(0, 50, 256, 311))
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
        self.ListSteamFriends.setSelectionRectVisible(False)
        self.ListSteamFriends.setObjectName("ListSteamFriends")
        QtGui.QListWidgetItem(self.ListSteamFriends)
        self.GoButton = QtGui.QPushButton(SteamFriendsStatus)
        self.GoButton.setGeometry(QtCore.QRect(210, 20, 41, 21))
        self.GoButton.setObjectName("GoButton")
        self.actionFetchData = QtGui.QAction(SteamFriendsStatus)
        self.actionFetchData.setObjectName("actionFetchData")
        self.actionPopulateListSteamFriends = QtGui.QAction(SteamFriendsStatus)
        self.actionPopulateListSteamFriends.setObjectName("actionPopulateListSteamFriends")
        self.actionGetServerData = QtGui.QAction(SteamFriendsStatus)
        self.actionGetServerData.setObjectName("actionGetServerData")

        self.retranslateUi(SteamFriendsStatus)
        QtCore.QObject.connect(self.ListSteamFriends, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.actionGetServerData.toggle)
        QtCore.QObject.connect(self.GoButton, QtCore.SIGNAL("clicked()"), self.actionFetchData.toggle)
        QtCore.QObject.connect(self.GoButton, QtCore.SIGNAL("clicked()"), self.ListSteamFriends.clear)
        QtCore.QObject.connect(self.SteamUsername, QtCore.SIGNAL("returnPressed()"), self.actionFetchData.toggle)
        QtCore.QObject.connect(self.SteamUsername, QtCore.SIGNAL("returnPressed()"), self.ListSteamFriends.clear)
        QtCore.QMetaObject.connectSlotsByName(SteamFriendsStatus)

    def retranslateUi(self, SteamFriendsStatus):
        SteamFriendsStatus.setWindowTitle(QtGui.QApplication.translate("SteamFriendsStatus", "Steam Friends Status", None, QtGui.QApplication.UnicodeUTF8))
        self.SteamUsername.setToolTip(QtGui.QApplication.translate("SteamFriendsStatus", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can provide one of the following:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:600;\">entire URL</span> to your Steam Community page: <span style=\" font-weight:600;\">http://steamcommunity.com/id/example</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:600;\">profile ID</span> from the URL: http://steamcommunity.com/profiles/<span style=\" font-weight:600;\">(profile ID)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:600;\">c</span><span style=\" font-weight:600;\">ustom UR</span><span style=\" font-weight:600;\">L</span>: http://steamcommunity.com/id/<span style=\" font-weight:600;\">(custom URL)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelSteamID.setToolTip(QtGui.QApplication.translate("SteamFriendsStatus", "The ID numbers or name can be found by browsing to your Steam Community page and looking in the URL.\n"
"Short name: http://steamcommunity.com/id/$Name\n"
"ID number: http://steamcommunity.com/profiles/$Numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelSteamID.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Steam Community ID / Custom URL:", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.ListSteamFriends.isSortingEnabled()
        self.ListSteamFriends.setSortingEnabled(False)
        self.ListSteamFriends.item(0).setText(QtGui.QApplication.translate("SteamFriendsStatus", "Enter your Steam Community information above and click Go. Mouse over the box above for more information.", None, QtGui.QApplication.UnicodeUTF8))
        self.ListSteamFriends.setSortingEnabled(__sortingEnabled)
        self.GoButton.setText(QtGui.QApplication.translate("SteamFriendsStatus", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFetchData.setText(QtGui.QApplication.translate("SteamFriendsStatus", "FetchData", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPopulateListSteamFriends.setText(QtGui.QApplication.translate("SteamFriendsStatus", "populateListSteamFriends", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGetServerData.setText(QtGui.QApplication.translate("SteamFriendsStatus", "GetServerData", None, QtGui.QApplication.UnicodeUTF8))

