






#from MAXIOT import *
import time
import MAXIOT
import MEDIATOR
import 8229BSF


try:
	MAXIOT.START()
	8229BSF.START()
	while 1:
		time.sleep(1)
		MEDIATOR.TX(1,"12345")	
finally:
	print "SYSTEM Exiting !!!!!"
	MAXIOT.CLIENT_STATUS  = 0
	MAXIOT.SATELIT_STATUS = 0

















