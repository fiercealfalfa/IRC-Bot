#IRC bot
#Written with hrlp from wiki.shellium.org and the wayback machine (because wiki.shellium.org appears to be down)

#import libraries
import socket

#Server, channel, nick, and password variables
from ircpasswords import settings

server = settings['server']
channel = settings['channel']
botnick = settings['botnick']

#Respond to server pings
def ping():
	ircsock.send("PONG :Pong\n")
	
	
#Send Messages
def sendmsg(chan , msg):
	ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

#Join Channels
def joinchan(chan):
	ircsock.send("JOIN "+ chan +"\n")

#Simple Reply to Hello
def hello(newnick):
	ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

#Connecting to server, joining channel and authenticating
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :devCodeIRCbot - A work in Progress")
ircsock.send("NICK "+botnick +"\n")


while 1:
	ircmsg = ircsock.recv(2048) #receiving info from IRC
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)
	
	if ircmsg.find("PING :") != -1:
		ping()
	
	if ircmsg.find(":Hello "+ botnick)!= -1:
		hello()
