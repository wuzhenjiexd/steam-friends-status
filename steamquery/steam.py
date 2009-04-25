#!/usr/bin/python
""" SteamQuery class. This screen scrapes the Steam Community website for in-game and
    online players.

    This part of Steam Friends Status is given under the WTFPL license
"""         
import urllib2, socket, re
from lxml.html import fromstring, tostring

class SteamQuery:
    def __init__(self,steamid):
        """ steamid -- The information passed from the UI to SteamQuery (URL, Custom URL)
            
        """
        self.steamid = steamid
        # URL that will eventually be used to query Steam
        self.url = ''
        # Set default socket timeout to 4, which affects urllib2's timeout
        socket.setdefaulttimeout(4)
		
    def parse_steamid(self):
        """ Try to guess whether the user gave us a:
            * Steam Community ID URL (which has a custom URL appended to it)
            * Steam Community Profile ID URL (with a bunch of numbers following)
            * Their custom URL name 

        """
        if re.match(r'http://.*steamcommunity.com/id/.*',self.steamid):
            self.url = self.steamid
            return self.url
        elif re.match(r'http://.*steamcommunity.com/profiles/.*',self.steamid):
            self.url = self.steamid
            return self.url
        elif self.url == '':
            if re.match(r'\d',self.steamid):
                self.url = 'http://steamcommunity.com/profiles/%s/friends' % (self.steamid)
                return self.url
            elif re.match(r'([a-zA-Z0-9])',self.steamid):
                self.url = 'http://steamcommunity.com/id/%s/friends' % (self.steamid)
                return self.url
        else:
            self.url = None
            return None	
    def get_friend_status(self):
        """ Retrive friend status, returns two things 
		    This returns in_game_friends with a list of dictionaries, and
            online_friends, which is a list of friends that are just online. Contained in 
		    a tuple.

		    Structure of in_game_friends (list of dictionaries):
			$n['friend'] - Friend Name
            $n['game']   - Game name
            $n['server'] - Server IP:Port	

            Structure of online_friends (list of friends (no pun intended)):
            [friend, friend2, friend3]

            Errors while acquiring friends cause (None,None) to be returned
		"""
        # See what kind of URL we need to assemble and open
        self.parse_steamid()

        # If parse_steamid() failed, send us back
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
                g = re.sub('\s-\sJoin', '', re.sub(r'\s\s', '', game.group(1)))
                f['game'] = g
            else:
                f['friend'] = f_ingame
            # If all elements were filled out above during the iterative passes,
            # go ahead and append it to the list of hashes, and start anew
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
