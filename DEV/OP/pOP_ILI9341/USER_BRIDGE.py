##############################################
# v0.01	test !!!		export PS1='> '
##############################################
import MEDIATOR
import time
#############################################


import ILI9341
import GUI


#############################################
def RUN_INIT():
	GUI.init()
#############################################	
def RUN_MEM_DATA_PROCESSING(SLOT,DATA):
	#print "--> LCD :"+str(SLOT)+": " + str(DATA)
	GUI.Text(DATA)
#############################################
def RUN_DATA_PROCESSING(SLOT,DATA):
	#print "--> LCD :"+str(SLOT)+": " + str(DATA)
	GUI.Text(DATA)
#############################################
xCOU = 0;
def RUN_LOOP():
	global xCOU
	time.sleep(0.3)
	print "LOOP"
	MEDIATOR.TX(1,str(xCOU))
	xCOU=xCOU+1






#############################################
#def RUN_INIT():
#	time.sleep(0.2)
#############################################	
#def RUN_MEM_DATA_PROCESSING(DATA):
#	time.sleep(0.2)
#############################################
#def RUN_DATA_PROCESSING(DATA):
#	time.sleep(0.2)
#############################################



