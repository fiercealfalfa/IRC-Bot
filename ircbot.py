#IRC bot
#Written with help from wiki.shellium.org and the wayback machine (because wiki.shellium.org appears to be down)

#import libraries
import socket
import ssl
import time

#Server, channel, nick, and password variables
from ircpasswords import settings

server = settings['server']
channel = settings['channel']
botnick = settings['botnick']
password = settings['botpass']

#Respond to server pings
def ping():
	irc.send("PONG " + ircmsg.split()[1] + "\r\n")
# For the bot to request OP from Chanserv
def opbot():
	irc.send("MODE " + channel + " +o " + botnick + "\r\n")
	print "I tried to OP myself", "PRIVMSG chanserv OP "+ channel + " " + botnick + "\r\n"
	
#Send Messages
def sendmsg(chan , msg):
	irc.send("PRIVMSG "+ chan +" :"+ msg +"\n")

#Join Channels
def joinchan(chan):
	irc.send("JOIN "+ chan +"\n")

#Simple Reply to Hello 
def hello():
	irc.send("PRIVMSG "+ channel +" :Hello!\n")
	
def reg():
	irc.send("PRIVMSG NickServ :identify %s %s \r\n" % (botnick, password))
	print("PRIVMSG NickServ :identify %s %s \r\n" % (botnick, password))
	
def joinmainchannel():
	irc.send("JOIN " + channel +"\n")

	
#Connecting to server, joining channel and authenticating

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting to : "+ server
#irc = ssl.wrap_socket(irc_C)
irc.connect((server,6667))
time.sleep(5)
#irc.setblocking(False)
#irc.send("PASS %s\n" % (password))
irc.send("NICK "+ botnick +"\n")
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :devCodeIRCbot - A work in Progress")



time.sleep(30)
irc.send("JOIN " + channel +"\n")

while 1:
	ircmsg = irc.recv(2048) #receiving info from IRC
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)
	#opbot() #- We are going to add code to detect deopping and call this function when it works
	if ircmsg.find("PING :") != -1:
		ping()
	
	if ircmsg.find("This nickname is registered.") != -1:
		reg()
	
	if ircmsg.find("You are now identified") != -1:
		joinmainchannel()
		
	if ircmsg.find(":Hello "+ botnick)!= -1:
		hello()
