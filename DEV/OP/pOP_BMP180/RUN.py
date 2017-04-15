##############################################
# v0.03			export PS1='> '
##############################################
import sys

ARG_ID   = str(sys.argv[1])
ARG_DESC = str(sys.argv[2])
ARG_IP   = str(sys.argv[3])
ARG_PORT = str(sys.argv[4])

##############################################
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
	MAXIOT.reconnect		  = 1
	MAXIOT.Server_IP          = str(ARG_IP)
	MAXIOT.Server_PORT        = int(ARG_PORT)
	MAXIOT.DEVICE_ID          = str(ARG_ID)
	MAXIOT.DEVICE_DESCRIPTION = str(ARG_DESC)
	MAXIOT.START()	
	
	########################
	while 1:
		time.sleep(0.1)
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
















