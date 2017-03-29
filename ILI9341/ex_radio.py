#!/usr/bin/python
import commands
import thread
import time
import ILI9341
ILI9341.INIT()
ILI9341.CLS3()

from time import gmtime, strftime
print strftime("%Y_%m_%d__%H_%M_%S", gmtime())

def print_time( threadName, delay):
	count = 0
	while 1:
		time.sleep(delay)
		#count += 1
		#print "%s: %s" % ( threadName, time.ctime(time.time()) )
		
		xTime = strftime("%d/%m/%Y %H:%M:%S", gmtime())
		print xTime
		ILI9341.Text_16(0,16,str(xTime),ILI9341.YELLOW,ILI9341.BLACK)


def run_radio( threadName, delay):
	count = 0
	while 1:
		commands.getoutput("mplayer -vo null -ao alsa:device=hw=0.0 -playlist http://www.radiofeeds.co.uk/bbcradio2.pls")
##########################################################
sysIP = commands.getoutput("hostname -I")
ILI9341.Text_16(0,0,"IP:",ILI9341.GREEN,ILI9341.BLACK)
ILI9341.Text_16(16*3 + 2 ,0,str(sysIP),ILI9341.WHITE,ILI9341.BLACK)
##########################################################

rrr = commands.getoutput("screen -dmS xxx bash -c 'mplayer -vo null -ao alsa:device=hw=0.0 -playlist http://www.radiofeeds.co.uk/bbcradio2.pls'")

#print str(rrr)

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch



while 1:
	ch = getchar()
	print "You pressed "+ch
	time.sleep(1)
	xTime = strftime("%d/%m/%Y %H:%M:%S", gmtime())
	print xTime
	ILI9341.Text_16(0,16,str(xTime),ILI9341.YELLOW,ILI9341.BLACK)
	
	commands.getoutput("screen -S xxx -X quit")
	
	
	
	
	
	
#mplayer -vo null -ao alsa:device=hw=0.0 -playlist http://www.radiofeeds.co.uk/bbcradio2.pls
	
	
	
	
	
	
	