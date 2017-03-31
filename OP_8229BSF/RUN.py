##############################################
# v0.03			export PS1='> '
##############################################
#data1 = str(sys.argv[1])
#data2 = str(sys.argv[2])
#data3 = str(sys.argv[3])
#data4 = str(sys.argv[4])
#if(MAX_dbg==1):print ( data1 )
#if(MAX_dbg==1):print ( data2 )
#if(MAX_dbg==1):print ( data3 )
#if(MAX_dbg==1):print ( data4 )
##############################################
import MAXIOT_CONFIG
import time
import MAXIOT
import MEDIATOR
##############################################
SYS_dbg = 1
##############################################
try:
	print "\n\n\n"
	if(SYS_dbg==1):print "###################################"
	if(SYS_dbg==1):print "... SYS : SYSTEM START !!!"
	if(SYS_dbg==1):print "###################################"
	########################
	MEDIATOR.START()
	time.sleep(0.2)
	########################
	MAXIOT.reconnect		  = MAXIOT_CONFIG.reconnect
	MAXIOT.Server_IP          = MAXIOT_CONFIG.Server_IP
	MAXIOT.Server_PORT        = MAXIOT_CONFIG.Server_PORT
	MAXIOT.DEVICE_NAME        = MAXIOT_CONFIG.DEVICE_NAME
	MAXIOT.DEVICE_DESCRIPTION = MAXIOT_CONFIG.DEVICE_DESCRIPTION
	MAXIOT.START()
	########################
	while 1:
		time.sleep(0.001)
		####################################################	
		if(MAXIOT.reconnect==1):
			if(MAXIOT.CLIENT_STATUS==0):
				time.sleep(1)
				print "... MAX : [#      ]"
				time.sleep(1)
				print "... MAX : [##     ]"
				time.sleep(1)
				print "... MAX : [###    ]"
				time.sleep(1)
				print "... MAX : [####   ]"	
				time.sleep(1)
				print "... MAX : [#####  ]"
				time.sleep(1)
				print "... MAX : [###### ]"
				time.sleep(1)
				print "... MAX : [#######]"
				print "###################################"
				print "... MAX : RECONNECTING !!!"
				MAXIOT.START()
	
		#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER END
#		while(fifo.Len()):
#			d = fifo.Get()
#			print "... LCD : " + str(d)
#			MEDIATOR.Text(d)
		#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER END
	

finally:
	if(SYS_dbg==1):print "###################################"
	if(SYS_dbg==1):print "... MAX : SYSTEM STOP !!!"
	if(SYS_dbg==1):print "###################################"
	MAXIOT.CLIENT_STATUS     = 0
	MAXIOT.PING_STATUS       = 0
	MEDIATOR.USER_STATUS     = 0
	MEDIATOR.MEM_USER_STATUS = 0
	MEDIATOR.USER_LOOP       = 0 
















