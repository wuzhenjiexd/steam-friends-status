#!/usr/bin/python
import urllib2, re, sys
from lxml.html import fromstring, tostring
from PyQt4 import QtCore, QtGui
from steamfriendsui import Ui_SteamFriendsStatus

# Generate with pyuic4
class FetchFriends(QtGui.QMainWindow, Ui_SteamFriendsStatus):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.setupUi(self)
	self.connect(self.FetchButton, QtCore.SIGNAL("clicked()"), self.get_friend_status)
    def get_friend_status(self):
	""" Populates the list and doodles on the list """
	steamid = self.SteamUsername.displayText()
	steamid = str(steamid)
	url = ''
	if re.search(r'\d',steamid):
		url = 'http://steamcommunity.com/profiles/%s/friends' % (steamid)
	elif re.search(r'\w',steamid):
		url = 'http://steamcommunity.com/id/%s/friends' % (steamid)
	else: 
		self.ListSteamFriends.addItem("Invalid Steam Identity -- The ID numbers or name can be found by browsing to your Steam Community page and looking in the URL.")
		self.ListSteamFriends.addItem("Short name: steamcommunity.com/id/$n")
		self.ListSteamFriends.addItem("ID number: steamcommunity.com/profiles/$n")	
	
	content = urllib2.build_opener()
	content.addheaders = [('User-agent', 'Mozilla/5.0')]
	try:
		data = content.open(url).read()
	except urllib2.URLError, e:
		print 'Failed to connect'
		print 'Reason: ',e.reason
	except urllib2.HTTPError, e:
		print 'Remote server error'
		print 'Error code: ',e.code

	doc = fromstring(data)
	doc.make_links_absolute(url)

	c = 0
	line = ''
	for f_ingame in [i.text_content() for i in doc.find_class('linkFriend_in-game')]:
			f_ingame = re.sub('\s-\sJoin', '', re.sub('In-Game', '', f_ingame))
			if c == 1:	
				line += " + (%s)" % (f_ingame)
				self.ListSteamFriends.addItem(line)
				c = 0
				line = ''
			else:
				line += "(In-game) %s" % (f_ingame)
				c += 1
	for i in doc.find_class('linkFriend_online'):
		line = "(Online) %s" % (i.text_content())
		self.ListSteamFriends.addItem(line)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FetchFriends()
    myapp.show()
    sys.exit(app.exec_())
