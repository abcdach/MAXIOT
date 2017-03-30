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
import ILI9341
import fifo

try:

	fifo.init()

	MAXIOT.Server_IP          = "10.0.0.13"
	MAXIOT.Server_PORT        =  3004
	MAXIOT.DEVICE_NAME        = "9002"
	MAXIOT.DEVICE_DESCRIPTION = "LCD ILI9341"
	MAXIOT.START()
	########################
	ILI9341.INIT()
	ILI9341.CLS3()

	#MEDIATOR.DataEvent = 0
	#MEDIATOR.DevThread_STATUS = 1
	#MEDIATOR.START()
	
	while 1:
		#if(!=0):
		while(fifo.Len()):
			xData = fifo.Get()
			print "xxxxx = " + str(xData)
			MEDIATOR.Text(xData)

		time.sleep(0.1)	
	while 1:
		time.sleep(1)
		ILI9341.TEST()
		#MEDIATOR.TX(0,"12345")	
finally:
	print "SYSTEM Exiting !!!!!"
	MAXIOT.CLIENT_STATUS  = 0
	MAXIOT.SATELIT_STATUS = 0
	MEDIATOR.DevThread_STATUS = 0
















