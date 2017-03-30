#data1 = str(sys.argv[1])
#data2 = str(sys.argv[2])
#data3 = str(sys.argv[3])
#data4 = str(sys.argv[4])

#data1 = 111
#data2 = 222
#data3 = 333
#data4 = 444

#if(MAX_dbg==1):print ( data1 )
#if(MAX_dbg==1):print ( data2 )
#if(MAX_dbg==1):print ( data3 )
#if(MAX_dbg==1):print ( data4 )






#from MAXIOT import *
import time
import MAXIOT
import MEDIATOR
import _8229BSF


try:
	MAXIOT.START()
	_8229BSF.START()
	while 1:
		time.sleep(1)
		#MEDIATOR.TX(1,"12345")	
finally:
	print "SYSTEM Exiting !!!!!"
	MAXIOT.CLIENT_STATUS  = 0
	MAXIOT.SATELIT_STATUS = 0

















