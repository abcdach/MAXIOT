##############################################
# v0.04	test !!!		export PS1='> '
##############################################
import sys
sys.path.append('USER')
import re
import MAXIOT
import threading
import time
import USER_BRIDGE
##############################################
USER_STATUS     = 0
TXD_STATUS       = 0
MEM_USER_STATUS = 0
USER_LOOP       = 0
MED_dbg = 0
USR_dbg = 1
##############################################
class mem_userThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : MEM : USER START !!!"
		if(MED_dbg==1):print "###################################"
		global MEM_USER_STATUS
		while 1:
			global mem_user_event_is_set
			if(MED_dbg==1):print "... MED : MEM : EVENT : wait"
			mem_user_event_is_set = mem_userEvent.wait(3)			
			if(MEM_USER_STATUS==0):break
			if mem_user_event_is_set:
				if(MED_dbg==1):print "... MED : MEM : EVENT : detected !!!"
				mem_userEvent.clear()
				while(RX_FIFO_Len()):
					(s,d) = RX_FIFO_Get()
					USER_BRIDGE.RUN_MEM_DATA_PROCESSING(s,d)
			else:
				if(MEM_USER_STATUS==0):break
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : MEM : USER STOP !!!"
		if(MED_dbg==1):print "###################################"
		MEM_USER_STATUS = 0
#########################################################
class userThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : ... : USER START !!!"
		if(MED_dbg==1):print "###################################"
		global USER_STATUS
		while 1:
			global user_event_is_set
			if(MED_dbg==1):print "... MED : ... : EVENT : wait"
			user_event_is_set = userEvent.wait(3)			
			if(USER_STATUS==0):break
			if user_event_is_set:
				if(MED_dbg==1):print "... MED : ... : EVENT : detected !!!"
				userEvent.clear()
				#print "RX_FIFO_Len : "+str(RX_FIFO_Len())
				TX(2,RX_FIFO_Len())
				while(RX_FIFO_Len()):
					(s,d) = RX_FIFO_Get()
					USER_BRIDGE.RUN_DATA_PROCESSING(s,d)
			else:
				if(USER_STATUS==0):break
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : ... : USER STOP !!!"
		if(MED_dbg==1):print "###################################"
		USER_STATUS = 0	
#########################################################		
class loop_userThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : ... : USER LOOP !!!"
		if(MED_dbg==1):print "###################################"
		global USER_LOOP
		while 1:		
			if(USER_LOOP==0):break
			USER_BRIDGE.RUN_LOOP()
			if(USER_LOOP==0):break
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : ... : USER LOOP !!!"
		if(MED_dbg==1):print "###################################"
		USER_LOOP = 0
		
#########################################################		
class TXD_Thread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... TXD : ... : START !!!"
		if(MED_dbg==1):print "###################################"
		global TXD_STATUS
		while 1:
			global txd_event_is_set
			if(MED_dbg==1):print "... TXD : ... : EVENT : wait"
			txd_event_is_set = txdEvent.wait(3)			
			if(TXD_STATUS==0):break
			if txd_event_is_set:
				if(MED_dbg==1):print "... TXD : ... : EVENT : detected !!!"
				txdEvent.clear()
				#print "TX_FIFO_Len = "+str(TX_FIFO_Len())
				while(TX_FIFO_Len()):
					(s,d) = TX_FIFO_Get()
					MAXIOT.SEND(s,d)
					time.sleep(0.05)#gagavnis dacdis dayovneba
			else:
				if(TXD_STATUS==0):break
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... TXD : ... : STOP !!!"
		if(MED_dbg==1):print "###################################"
		TXD_STATUS = 0				
#########################################################
def START():
	RX_FIFO_init()
	TX_FIFO_init()
	USER_BRIDGE.RUN_INIT()
	global USER_STATUS
	global TXD_STATUS
	global MEM_USER_STATUS
	global USER_LOOP
	USER_LOOP       = 1
	USER_STATUS     = 1
	TXD_STATUS		= 1
	MEM_USER_STATUS = 1
	#-------------------------------
	time.sleep(0.2)	
	global txdEvent
	txdEvent = threading.Event()
	_TXD_Thread = TXD_Thread(1, "TXD_Thread")
	_TXD_Thread.start()
	#-------------------------------
	time.sleep(0.2)	
	global userEvent
	userEvent = threading.Event()
	_userThread = userThread(1, "userThread")
	_userThread.start()
	#-------------------------------
	time.sleep(0.2)
	global mem_userEvent
	mem_userEvent = threading.Event()
	_mem_userThread = mem_userThread(1, "mem_userThread")
	_mem_userThread.start()
	#-------------------------------
	time.sleep(0.2)
	_loop_userThread = loop_userThread(1, "mem_userThread")
	_loop_userThread.start()
#########################################################
def MEM_RX(_SLOT,_DATA):#damaxsovrebuli monacemebis migeba
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	if(MED_dbg==1):print "... MED : MEM_RX("+SLOT+") "+DATA
	RX_FIFO_Put(SLOT,DATA)
	if(MED_dbg==1):print "... MED : MEM : Event RX--> "
	mem_userEvent.set()
#########################################################
def RX(_SLOT,_DATA):#pirdapiri monacemebis migeba
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	if(MED_dbg==1):print "... MED : RX("+SLOT+") "+DATA
	RX_FIFO_Put(SLOT,DATA)
	if(MED_dbg==1):print "... MED : Event RX--> "
	userEvent.set()
#########################################################
def TX(_SLOT,_DATA):#gadasacemi monacemebis porti
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	if(MED_dbg==1):print "... MED : TX("+SLOT+") "+DATA
	TX_FIFO_Put(SLOT,DATA)
	if(MED_dbg==1):print "... MED : Event TX--> "
	txdEvent.set()
	
#########################################################
# RX_FIFO
#########################################################
RX_FIFO_MaxLen = 64
RX_FIFO = [""] * RX_FIFO_MaxLen
RX_FIFO_X = 0
RX_FIFO_Y = 0
RX_FIFO_X_COU = 0
RX_FIFO_Y_COU = 0
#-------------------------------
def RX_FIFO_init():
	global RX_FIFO_X
	global RX_FIFO_Y	
	global RX_FIFO_X_COU
	global RX_FIFO_Y_COU
	global RX_FIFO_lock
	RX_FIFO_X = 0
	RX_FIFO_Y = 0
	RX_FIFO_X_COU = 0
	RX_FIFO_Y_COU = 0
	RX_FIFO_lock = threading.Lock()
#-------------------------------
def RX_FIFO_Put(SLOT,DATA):
	global RX_FIFO_X
	global RX_FIFO_Y	
	global RX_FIFO_X_COU
	global RX_FIFO_Y_COU
	global RX_FIFO_lock
	RX_FIFO_lock.acquire()
	xxx =  RX_FIFO_X_COU*RX_FIFO_MaxLen + RX_FIFO_X
	yyy =  RX_FIFO_Y_COU*RX_FIFO_MaxLen + RX_FIFO_Y
	ddd =  xxx - yyy
	if(xxx == yyy):
		RX_FIFO_X_COU = 0
		RX_FIFO_Y_COU = 0
		RX_FIFO_X = 0
		RX_FIFO_Y = 0
	if(ddd < RX_FIFO_MaxLen):	
		if(RX_FIFO_X == RX_FIFO_MaxLen):
			RX_FIFO_X = 0
			RX_FIFO_X_COU = RX_FIFO_X_COU + 1			
		RX_FIFO[RX_FIFO_X]=(SLOT,DATA)
		RX_FIFO_X = RX_FIFO_X + 1
	RX_FIFO_lock.release()
#-------------------------------	
def RX_FIFO_Satus():
	if(RX_FIFO_MaxLen):
		return 1
	else:
		return 0
#-------------------------------	
def RX_FIFO_Get():
	global RX_FIFO_X
	global RX_FIFO_Y	
	global RX_FIFO_X_COU
	global RX_FIFO_Y_COU
	global RX_FIFO_lock
	RX_FIFO_lock.acquire()
	xxx =  RX_FIFO_X_COU*RX_FIFO_MaxLen + RX_FIFO_X
	yyy =  RX_FIFO_Y_COU*RX_FIFO_MaxLen + RX_FIFO_Y
	ddd =  xxx - yyy
	if(ddd == 0):
		RX_FIFO_lock.release()	
		return ("0","0")
	if(RX_FIFO_Y == RX_FIFO_MaxLen):
		RX_FIFO_Y = 0
		RX_FIFO_Y_COU = RX_FIFO_Y_COU + 1		
	(VEL_SLOT,VEL_DATA) = RX_FIFO[RX_FIFO_Y]
	RX_FIFO_Y = RX_FIFO_Y + 1
	RX_FIFO_lock.release()	
	return (VEL_SLOT,VEL_DATA)
#-------------------------------
def RX_FIFO_Len():
	global RX_FIFO_lock
	RX_FIFO_lock.acquire()
	xxx =  RX_FIFO_X_COU*RX_FIFO_MaxLen + RX_FIFO_X
	yyy =  RX_FIFO_Y_COU*RX_FIFO_MaxLen + RX_FIFO_Y
	ddd = xxx - yyy
	RX_FIFO_lock.release()
	return ddd
#########################################################

#########################################################
# TX_FIFO
#########################################################
TX_FIFO_MaxLen = 64
TX_FIFO = [""] * TX_FIFO_MaxLen
TX_FIFO_X = 0
TX_FIFO_Y = 0
TX_FIFO_X_COU = 0
TX_FIFO_Y_COU = 0
#-------------------------------
def TX_FIFO_init():
	global TX_FIFO_X
	global TX_FIFO_Y	
	global TX_FIFO_X_COU
	global TX_FIFO_Y_COU
	global TX_FIFO_lock
	TX_FIFO_X = 0
	TX_FIFO_Y = 0
	TX_FIFO_X_COU = 0
	TX_FIFO_Y_COU = 0
	TX_FIFO_lock = threading.Lock()
#-------------------------------
def TX_FIFO_Put(SLOT,DATA):
	global TX_FIFO_X
	global TX_FIFO_Y	
	global TX_FIFO_X_COU
	global TX_FIFO_Y_COU
	global TX_FIFO_lock
	TX_FIFO_lock.acquire()
	xxx =  TX_FIFO_X_COU*TX_FIFO_MaxLen + TX_FIFO_X
	yyy =  TX_FIFO_Y_COU*TX_FIFO_MaxLen + TX_FIFO_Y
	ddd =  xxx - yyy
	if(xxx == yyy):
		TX_FIFO_X_COU = 0
		TX_FIFO_Y_COU = 0
		TX_FIFO_X = 0
		TX_FIFO_Y = 0
	if(ddd < TX_FIFO_MaxLen):	
		if(TX_FIFO_X == TX_FIFO_MaxLen):
			TX_FIFO_X = 0
			TX_FIFO_X_COU = TX_FIFO_X_COU + 1			
		TX_FIFO[TX_FIFO_X]=(SLOT,DATA)
		TX_FIFO_X = TX_FIFO_X + 1
	TX_FIFO_lock.release()
#-------------------------------	
def TX_FIFO_Satus():
	if(TX_FIFO_MaxLen):
		return 1
	else:
		return 0
#-------------------------------	
def TX_FIFO_Get():
	global TX_FIFO_X
	global TX_FIFO_Y	
	global TX_FIFO_X_COU
	global TX_FIFO_Y_COU
	global TX_FIFO_lock
	TX_FIFO_lock.acquire()
	xxx =  TX_FIFO_X_COU*TX_FIFO_MaxLen + TX_FIFO_X
	yyy =  TX_FIFO_Y_COU*TX_FIFO_MaxLen + TX_FIFO_Y
	ddd =  xxx - yyy
	if(ddd == 0):
		TX_FIFO_lock.release()	
		return ("0","0")
	if(TX_FIFO_Y == TX_FIFO_MaxLen):
		TX_FIFO_Y = 0
		TX_FIFO_Y_COU = TX_FIFO_Y_COU + 1		
	(VEL_SLOT,VEL_DATA) = TX_FIFO[TX_FIFO_Y]
	TX_FIFO_Y = TX_FIFO_Y + 1
	TX_FIFO_lock.release()	
	return (VEL_SLOT,VEL_DATA)
#-------------------------------
def TX_FIFO_Len():
	global TX_FIFO_lock
	TX_FIFO_lock.acquire()
	xxx =  TX_FIFO_X_COU*TX_FIFO_MaxLen + TX_FIFO_X
	yyy =  TX_FIFO_Y_COU*TX_FIFO_MaxLen + TX_FIFO_Y
	ddd = xxx - yyy
	TX_FIFO_lock.release()
	return ddd
#########################################################







		

	
	


















