#!/usr/bin/python
from time import gmtime, strftime
import threading
import time
import commands
import ILI9341
ILI9341.INIT()
ILI9341.CLS3()
import os


global xTime

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
		while 1:
			cmd = 'mplayer -vo null -ao alsa:device=hw=0.0 -playlist http://www.radiofeeds.co.uk/bbcradio2.pls'
			os.system(cmd)
			#commands.getoutput("mplayer -vo null -ao alsa:device=hw=0.0 -playlist http://www.radiofeeds.co.uk/bbcradio2.pls")

class myThread2 (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
		while 1:
			time.sleep(1)
			xTime = strftime("%d/%m/%Y %H:%M:%S", gmtime())
			print xTime
			



def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
#thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 2)

# Start new Threads
#thread1.start()
thread2.start()

print "Exiting Main Thread"
while 1:
	time.sleep(1)
	ILI9341.Text_16(0,16,str(xTime),ILI9341.YELLOW,ILI9341.BLACK)
	print "Exiting Main Thread"






