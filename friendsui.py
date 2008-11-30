#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
from steamfriendsui import Ui_SteamFriendsStatus

# Generate with pyuic4
class FetchFriends(QtGui.QMainWindow, Ui_SteamFriendsStatus):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.setupUi(self)
	self.connect(self.FetchButton, QtCore.SIGNAL("clicked()"), self.get_friend_status)

    # Update and populate the list
    def get_friend_status(self):
	pass 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FetchFriends()
    myapp.show()
    sys.exit(app.exec_())
