#data1 = str(sys.argv[1])
#data2 = str(sys.argv[2])
#data3 = str(sys.argv[3])
#data4 = str(sys.argv[4])
#if(MAX_dbg==1):print ( data1 )
#if(MAX_dbg==1):print ( data2 )
#if(MAX_dbg==1):print ( data3 )
#if(MAX_dbg==1):print ( data4 )


import time
import MAXIOT
import MEDIATOR
import fifo

try:
	fifo.init()
	########################
	MAXIOT.Server_IP          = "10.0.0.13"
	MAXIOT.Server_PORT        =  3004
	MAXIOT.DEVICE_NAME        = "9002"
	MAXIOT.DEVICE_DESCRIPTION = "LCD ILI9341"
	MAXIOT.START()
	########################
	MEDIATOR.DevThread_STATUS = 1
	MEDIATOR.START()
	########################	
	while 1:
		time.sleep(1)

finally:
	print "SYSTEM Exiting !!!!!"
	MAXIOT.CLIENT_STATUS  = 0
	MAXIOT.SATELIT_STATUS = 0
	MEDIATOR.DevThread_STATUS = 0
















