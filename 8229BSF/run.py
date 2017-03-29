






#from MAXIOT import *
import time
import MAXIOT
import MEDIATOR



try:
	MAXIOT.START()
	while 1:
		time.sleep(1)
		#MAXIOT.SEND(1,"12345")
		MEDIATOR.TX(1,"12345")	
finally:
	print "SYSTEM Exiting !!!!!"
	MAXIOT.CLIENT_STATUS  = 0
	MAXIOT.SATELIT_STATUS = 0

















