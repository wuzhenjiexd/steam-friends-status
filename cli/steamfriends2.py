#!/usr/bin/python
import urllib2, re, sys
from lxml.html import fromstring, tostring
from optparse import OptionParser

usage = "usage: %prog [options]"
parser = OptionParser(usage,version="%prog 0.01A")
parser.add_option("--name", dest="name", type="string", help="Query using the short-name for your profile")
parser.add_option("--id", dest="id", type="string", help="Query using the long ID number from your profile")
(options, args) = parser.parse_args()

if options.name == None and options.id == None:
	parser.error("Please specify either the --name or --id to your profile")
elif options.name:
	url = 'http://www.steamcommunity.com/id/%s/friends' % (options.name)	
elif options.id:
	url = 'http://www.steamcommunity.com/profiles/%s/friends' % (options.id)
else:
	parser.error("Unable to set URL from --name or --id")

content = urllib2.build_opener()
content.addheaders = [('User-agent', 'Mozilla/5.0')]
try:
	data = content.open(url).read()
except URLError, e:
	print 'Failed to connect'
	print 'Reason: ',e.reason
except HTTPError, e:
	print 'Remote server error'
	print 'Error code: ',e.code

doc = fromstring(data)
doc.make_links_absolute(url)

# Online friends
for i in doc.find_class('linkFriend_online'):
	print "[ONLINE] %s" % (i.text_content())

# Handle in-game friends
cre = re.compile(r'steam://connect/(.*)')
cre_game = re.compile(r'In-Game(.*)\s')
in_game_friends = []
f = {}
for i in doc.find_class('linkFriend_in-game'):
	f_ingame = i.text_content()
	game = cre_game.search(f_ingame)

	for (element, attr, link, pos) in i.iterlinks():
		s = cre.search(link)
		if s:
			f['server'] = s.group(1)
	if 'server' not in f:
		f['server'] = None
	if game:
		g = re.sub('\s-\sJoin', '', game.group(1))
		f['game'] = g
	else:
		f['friend'] = f_ingame		
	if 'server' in f and 'friend' in f and 'game' in f:
		in_game_friends.append(f)
		f = {}

for friend in in_game_friends:
	print "[IN-GAME]", friend['friend']
	print "\tGame:", friend['game']
	print "\tServer:", friend['server']
