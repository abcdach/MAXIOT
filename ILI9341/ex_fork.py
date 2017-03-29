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
try:
	thread.start_new_thread( print_time, ("Thread-1", 1, ) )
except:
	print "Error: unable to start thread"
##########################################################
try:
	thread.start_new_thread( run_radio, ("Thread-1", 1, ) )
except:
	print "Error: unable to start thread"
##########################################################  
   


while 1:
	pass
	
	
	
	
	
	
	
#mplayer -vo null -ao alsa:device=hw=0.0 -playlist http://www.radiofeeds.co.uk/bbcradio2.pls
	
	
	
	
	
	
	