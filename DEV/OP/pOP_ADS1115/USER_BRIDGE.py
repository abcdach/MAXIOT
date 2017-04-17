##############################################
# v0.01	test !!!		export PS1='> '
##############################################
import MEDIATOR
import time
import ADS1115
#############################################
def RUN_INIT():
	ADS1115.INIT()
#############################################	
def RUN_MEM_DATA_PROCESSING(SLOT,DATA):
	time.sleep(0.1)
	#print "--> LCD :"+str(SLOT)+": " + str(DATA)
	#GUI.Text(DATA)
#############################################
def RUN_DATA_PROCESSING(SLOT,DATA):
	time.sleep(0.1)
	#print "--> LCD :"+str(SLOT)+": " + str(DATA)
	#GUI.Text(DATA)
#############################################
xCOU = 0;
def RUN_LOOP():
	global xCOU
	time.sleep(0.5)
	print "LOOP("+str(xCOU)+")"
	VEL = ADS1115.GetVal()
	VEL = VEL*0.000125
	X =  '%.4f' % float(VEL)
	print str(X)	
	MEDIATOR.TX(1,str(X))
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



