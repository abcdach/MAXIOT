import MEDIATOR
import time
#############################################


import ILI9341
import GUI


#############################################
def RUN_INIT():
	GUI.init()
#############################################	
def RUN_MEM_DATA_PROCESSING(DATA):
	print "--> LCD : " + str(DATA)
	GUI.Text(DATA)
#############################################
def RUN_DATA_PROCESSING(DATA):
	print "--> LCD : " + str(DATA)
	GUI.Text(DATA)
#############################################
def RUN_LOOP():
	time.sleep(1)
	print "LOOP"






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



