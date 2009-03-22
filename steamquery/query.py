#!/usr/bin/python
""" 	Query script for HLDS Source servers 
	http://github.com/davidk/hlquery
        WTFPL license 
	Sample output:
	% ./query.py XXX.XXX.XXX.XXX:27015
	
	hostname : Test
	game : Team Fortress
	map : ctf_2fort
	players : 24
	maxplayers : 24
	dedicated : Dedicated
	os : Linux
	passworded : Yes
	secure : Yes
	********************
	Player: cake!	Score: 1047	Time: 15155.6621094
	Player: Bot07	Score: 0	Time: -1.0
	Player: Bot30	Score: 0	Time: -1.0
	Player: Bot09	Score: 0	Time: -1.0
	Player: Bot31	Score: 0	Time: -1.0
	Player: Bot11	Score: 0	Time: -1.0
	Player: Bot12	Score: 0	Time: -1.0
	Player: Bot32	Score: 0	Time: -1.0
	Player: Bot14	Score: 1	Time: -1.0
	Player: Bot15	Score: 0	Time: -1.0
	Player: Bot16	Score: 0	Time: -1.0
	Player: Bot17	Score: 0	Time: -1.0
	Player: Bot18	Score: 1	Time: -1.0
	Player: Bot19	Score: 1	Time: -1.0
	Player: Bot20	Score: 0	Time: -1.0
	Player: Bot21	Score: 2	Time: -1.0
	Player: Bot22	Score: 1	Time: -1.0
	Player: Bot23	Score: 3	Time: -1.0
	Player: Bot24	Score: 1	Time: -1.0
	Player: Bot25	Score: 0	Time: -1.0
	Player: Bot26	Score: 0	Time: -1.0
	Player: Bot27	Score: 0	Time: -1.0
	Player: Bot28	Score: 0	Time: -1.0
	Player: Bot29	Score: 0	Time: -1.0
"""
import sys,re
import socket
from struct import unpack

class HLQuery:
        def __init__(self,host,port):
                self.host = host
                self.port = int(port)
		self.a2s_player_challenge = "\xFF\xFF\xFF\xFF\x55\xFF\xFF\xFF\xFF"
		self.a2s_info = "\xFF\xFF\xFF\xFF\x54\x53\x6F\x75\x72\x63\x65\x20\x45\x6E\x67\x69\x6E\x65\x20\x51\x75\x65\x72\x79\x00"

        def get(self,msg):
		""" Send a message to the server. This needs to use 
			one of the provided payloads -- it can also use
			one provided to it 
		"""
                buf = 2048
                addr = (self.host,self.port)    
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.settimeout(4)
			s.sendto(msg,addr)
 	                output = s.recv(buf)
			s.close()
		except socket.error, msg:
			print "ERROR: The socket has %s" % (msg)
			raise
		finally: 
			s.close()
                return output

	def get_a2s_player(self):
		""" Get/Send the challenge request, and 
			ship off the resulting response to be parsed 
		"""
		# Initiate challenge request
		reply = self.get(self.a2s_player_challenge)

		# Send challenge back out to server
		players = self.get(self._a2s_player_query(reply))
		return self._a2s_player_parse(players)

	def _a2s_player_parse(self,recv):
		""" Parse the response from the server into a reasonably 
			human-readable format 
			Walking the string is necessary here unfortunately..
			(This is how the handy SRCDSpy and others handle this)
		"""
		players = []
		recv = recv[+5:] # Punch out header
		count = int(ord(recv[0]))+1
		recv = recv[+1:]
		for player in range(1,count):
			try:
				p = {}
				#print unpack("%ds" % len(recv), recv)
				p['num'] = ord(recv[0]) # Single Byte
				recv = recv[+1:]
				p['player'] = re.search(r'(.*?)\x00',recv).group(0) # Var-length string
				recv = recv[+len(p['player']):]
				p['score'] = unpack("1l",recv[0:4])[0] # Long (~4 bytes)
				recv = recv[+4:]
				p['time'] = unpack("1f",recv[0:4])[0] # Float (~4 bytes)
				recv = recv[+4:]
				players.append(p)
			except:
				pass
		return players

	def _a2s_player_query(self,challenge):
		""" Run after sending challenge
		    The challenge itself is an argument so that it can
		    be used in the query.
		"""
		return "\xFF\xFF\xFF\xFF\x55"+challenge[5:]
	
        def get_a2s_info(self):
		""" Send and parse a2s_info 

		"""
                reply = self.get(self.a2s_info)
                return self._parse_a2s_info_reply(reply) 

        def _parse_a2s_info_reply(self,recv):
		""" Parse the reply packet from an a2s_info request 

		"""
		str = '\xff\xff\xff\xff\x49(.?)(?P<hostname>.*?)\x00(?P<map>.*?)\x00(?P<folder>.*?)\x00(?P<game>.*?)\x00(.)(.)(?P<players>.)(?P<maxplayers>.)(.)(?P<dedicated>.)(?P<os>.)(?P<pass>.)(?P<secure>.).'
		cre = re.compile(str,re.DOTALL)
		try:
			return self._translate_a2s_info(cre.search(recv).groupdict())	
		except AttributeError:
			print "Error in parsing protocol response. Printing packet dump .."
			print recv
			print "Dumping parseable elements .."
			print cre.findall(recv)
			print "Dumping hex representation of reply packet .."
			print unpack("%ds" % len(recv),recv)
			return None

	def _translate_a2s_info(self,result):
		""" Changes information returned by _parse_a2s_info_reply into 
		    a more readable format 
		"""
		result['players'] = ord(result['players'])
		result['maxplayers'] = ord(result['maxplayers'])
		result['dedicated'] = {'l':'Listen','d':'Dedicated'}[result['dedicated']]
		result['os'] = {'w':'Windows','l':'Linux'}[result['os']]
		result['pass'] = {True:'Yes',False:'No'}[bool(ord(result['pass']))]
		result['secure'] = {True:'Yes',False:'No'}[bool(ord(result['secure']))]	
		return result

if __name__ == "__main__":
	if ":" in sys.argv[1]:
		host, port = sys.argv[1].split(':')
		h = HLQuery(host,port)
		s = h.get_a2s_info()
		players = h.get_a2s_player()
	else:
		print "Usage: %s host:port" % (sys.argv[0])
		raise SystemExit(1)

	print "hostname :",s['hostname']
	print "game :",s['game']
	print "map :",s['map']
	print "players :",s['players']
	print "maxplayers :",s['maxplayers']
	print "dedicated :",s['dedicated']
	print "os :",s['os']
	print "passworded :",s['pass']
	print "secure :",s['secure'] 
	print "*"*20
	for player in players:
		print "Player: %s\tScore: %s\tTime: %s" % (player['player'],player['score'],player['time'])
	print "Total players in list: ", len(players)
