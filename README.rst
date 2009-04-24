Steam Friends Status
====================

Why?
-----------------
You're on a OS that Steam doesn't officially support,
or you don't want to/can't install Steam on the machine you're working on. 
Steam Friends Status will let you know what your friends are up to without 
having to keep a browser window open -- it'll also tell you server 
information to let you know if there is space to join your friend.

System Requirements
-------------------
**GUI**
 * Python
 * PyQT4
 * lxml.html (Available at: http://codespeak.net/lxml/index.html#download)

**Command-line (basic) client**
 * Python 
 * lxml.html (Available at: http://codespeak.net/lxml/index.html#download)

Running Steam Friends Status
----------------------------

**Command-line**
 Run ``'steamfriends2.py'`` under the ``'cli/'`` folder 

**GUI**
 To run the GUI version, run ``'steamfriends'`` in the root folder.

Steam Identity
--------------
The box at the top needs to take one of the following (where $NAME or $ID are your own):

* Short Name/Custom URL: http://www.steamcommunity.com/id/$NAME
* ID: http://www.steamcommunity.com/profiles/$ID

Your $NAME or $ID can be provided alone, or the entire URL can be pasted
in. For ease of use, it is probably easier to get yourself a Short Name/Custom URL.

Attaining your very own (awesome) Short Name/Custom URL
-------------------------------------------------------
To do that, log into your Steam Community page on http://steamcommunity.com and browse over to My Control Panel -> Edit my Profile. Set the Custom URL box to get a short name.

Click Save at the bottom.

Server information
------------------
If your friend is on a server that supports the GoldSrc/Source server query
format, you can find out:

* How many players there are on a server
* What map they're playing / game type
* How long each player has been on
* Scores
* The hosting server's operating system

The server must be accessible through the Internet to have its server information displayed.

License
-------
MIT License

Copyright (c) 2009 davidk

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

