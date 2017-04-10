import MEDIATOR
import time
#############################################
import commands
#############################################
def RUN_INIT():
	time.sleep(0.1)
#############################################	
def RUN_MEM_DATA_PROCESSING(DATA):
	time.sleep(0.1)
#############################################
def RUN_DATA_PROCESSING(DATA):
	time.sleep(0.1)
#############################################
def RUN_LOOP():
	time.sleep(3)
	sysIP = commands.getoutput("hostname -I")
	MEDIATOR.TX(0,sysIP)
	#print "LOOP"



