#!/usr/bin/python
import urllib2, socket, re
from lxml.html import fromstring, tostring

class SteamQuery:
	def __init__(self,steamid):
		self.steamid = steamid
		self.url = ''
		# Set default socket timeout to 4, which affects urllib2's timeout
		socket.setdefaulttimeout(4)
		
	def parse_steamid(self):
                if re.match(r'http://.*steamcommunity.com/id/.*',self.steamid):
                        self.url = self.steamid
                elif re.match(r'http://.*steamcommunity.com/profiles/.*',self.steamid):
                        self.url = self.steamid
                elif self.url == '':
                        if re.match(r'\d',self.steamid):
                                        self.url = 'http://steamcommunity.com/profiles/%s/friends' % (self.steamid)

                        elif re.match(r'([a-zA-Z0-9])',self.steamid):
                                        self.url = 'http://steamcommunity.com/id/%s/friends' % (self.steamid)
                else:
			return None	
	def get_friend_status(self):
		""" Retrive friend status, returns two things 
		    This returns in_game_friends with a list containing dictionaries, and
                    online_friends, which is a list of friends that are just online. Contained in 
		    a tuple.

		    Structure of in_game_friends:
			Friend $n -> $n['friend'] - Friend NAme
				  -> $n['game'] - Game name
				  -> $n['server'] - Server IP:Port	
		"""
		self.parse_steamid()
		if self.url == None:
			print "Failed to parse friend URL"
			return (None,None)
		content = urllib2.build_opener()
                content.addheaders = [('User-agent', 'Mozilla/5.0')]
		try:
                        data = content.open(self.url).read()
                        content.close()
                except ValueError, e:
			return (None,None)
		except urllib2.URLError, e:
                        print 'Failed to connect'
                        print 'Reason: ',e.reason
                        return (None,None)
                except urllib2.HTTPError, e:
                        print 'Remote server error'
                        print 'Error code: ',e.code
                        return (None,None)

		doc = fromstring(data)
                doc.make_links_absolute(self.url)

                cre = re.compile(r'steam://connect/(.*)')
                cre_game = re.compile(r'In-Game(.*)\s')

                in_game_friends = []
		online_friends = []

                # Parse in game friends and their information 
		# This ends up being a list of dictionaries
                f = {}
                for i in doc.find_class('linkFriend_in-game'):
                        f_ingame = i.text_content()
                        game = cre_game.search(f_ingame)

                        for (element, attr, link, pos) in i.iterlinks():
                                s = cre.search(link)
                                if s:
                                        f['server'] = s.group(1)
                        if 'server' not in f:
                                f['server'] = 'No server'
                        if game:
                                g = re.sub('\s-\sJoin', '', re.sub(r'\t\t', '', game.group(1)))
                                f['game'] = g
                        else:
                                f['friend'] = f_ingame
                        if 'server' in f and 'friend' in f and 'game' in f:
                                in_game_friends.append(f)
                                f = {}

                # Online friends        
                for i in doc.find_class('linkFriend_online'):
			online_friends.append("%s" % (i.text_content()))

		# This returns in_game_friends with a list containing dictionaries, and
		# online_friends, which is a list of friends that are just online	
		return (in_game_friends,online_friends)

if __name__ == "__main__":
	pass	
