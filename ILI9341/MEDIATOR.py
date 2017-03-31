##############################################
# v0.02			export PS1='> '
##############################################
import sys
sys.path.append('USER')
import re
import MAXIOT
import threading
import time
#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER START USER START
import ILI9341
#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER END
##############################################
USER_STATUS=0
MEM_USER_STATUS=0
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
				#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER START
				while(RX_FIFO_Len()):
					d = RX_FIFO_Get()
					if(USR_dbg==1):print "--> LCD : " + str(d)
					Text(d)
				#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER END
			else:
				if(MEM_USER_STATUS==0):break
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : MEM : USER STOP !!!"
		if(MED_dbg==1):print "###################################"
		MEM_USER_STATUS = 0


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
				#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER START
				while(RX_FIFO_Len()):
					d = RX_FIFO_Get()
					if(USR_dbg==1):print "--> LCD : " + str(d)
					Text(d)
				#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER END
			else:
				if(USER_STATUS==0):break
		if(MED_dbg==1):print "###################################"
		if(MED_dbg==1):print "... MED : ... : USER STOP !!!"
		if(MED_dbg==1):print "###################################"
		USER_STATUS = 0


def START():
	RX_FIFO_init()
	#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER START
	ILI9341.INIT()
	ILI9341.CLS3()
	ILI9341.CLS3()
	#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| USER END
	global USER_STATUS
	global MEM_USER_STATUS
	USER_STATUS     = 1
	MEM_USER_STATUS = 1
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
#########################################################
def MEM_RX(_SLOT,_DATA):#damaxsovrebuli monacemebis migeba
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	if(MED_dbg==1):print "... MED : MEM_RX("+SLOT+") "+DATA
	RX_FIFO_Put(DATA)
	if(MED_dbg==1):print "... MED : MEM : Event --> "
	mem_userEvent.set()
#########################################################
def RX(_SLOT,_DATA):#pirdapiri monacemebis migeba
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	if(MED_dbg==1):print "... MED : RX("+SLOT+") "+DATA
	RX_FIFO_Put(DATA)
	if(MED_dbg==1):print "... MED : Event --> "
	userEvent.set()
#########################################################
def TX(_SLOT,_DATA):#gadasacemi monacemebis porti
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	print "<-- S("+SLOT+") "+DATA
	MAXIOT.SEND(SLOT,DATA)
#########################################################
# RX_FIFO
#########################################################
RX_FIFO_MaxLen = 64
RX_FIFO = [""] * RX_FIFO_MaxLen
RX_FIFO_X = 0
RX_FIFO_Y = 0
RX_FIFO_LEN = 0
#-------------------------------
def RX_FIFO_init():
	global RX_FIFO_X
	RX_FIFO_X = 0
	RX_FIFO_Y = 0
	RX_FIFO_LEN = 0
#-------------------------------
def RX_FIFO_Put(DATA):
	global RX_FIFO_X	
	global RX_FIFO_LEN
	
	if(RX_FIFO_LEN < RX_FIFO_MaxLen):
		if(RX_FIFO_X == RX_FIFO_MaxLen):
			RX_FIFO_X = 0
		RX_FIFO[RX_FIFO_X]=DATA
		RX_FIFO_X = RX_FIFO_X + 1
		RX_FIFO_LEN = RX_FIFO_LEN + 1
#-------------------------------	
def RX_FIFO_Satus():
	if(RX_FIFO_LEN == RX_FIFO_MaxLen):
		return 1
	else:
		return 0
#-------------------------------	
def RX_FIFO_Get():
	global RX_FIFO_Y	
	global RX_FIFO_LEN
	vel = ""	
	if(RX_FIFO_LEN != 0):
		if(RX_FIFO_Y == RX_FIFO_MaxLen):
			RX_FIFO_Y = 0		
		RX_FIFO_LEN = RX_FIFO_LEN - 1		
		vel = RX_FIFO[RX_FIFO_Y]
		RX_FIFO_Y = RX_FIFO_Y + 1		
	return vel
#-------------------------------
def RX_FIFO_Len():
	global RX_FIFO_LEN
	return RX_FIFO_LEN
#########################################################













	
def ToCOLOR(color):
	if   color == "C1":return ILI9341.RED
	elif color == "C2":return ILI9341.GREEN
	elif color == "C3":return ILI9341.BLUE
	elif color == "C4":return ILI9341.BLACK
	elif color == "C5":return ILI9341.YELLOW
	elif color == "C6":return ILI9341.WHITE
	elif color == "C7":return ILI9341.CYAN
	elif color == "C8":return ILI9341.BRIGHT_RED
	elif color == "C9":return ILI9341.GRAY1
	elif color == "C0":return ILI9341.GRAY2
	else:return ILI9341.WHITE


def Text(DATA):

 	DAT = re.split(r',',DATA)
 	Array_len  = len(DAT)
 	
 	TEXT_FONT = DAT[0]
 	TEXT_X    = int(DAT[1])
	TEXT_Y    = int(DAT[2])	
	TEXT_COL1 = ToCOLOR(DAT[3])	
	TEXT_COL2 = ToCOLOR(DAT[4])
	TEXT_LIMI = int(DAT[5])	
	TEXT_DATA = DAT[6]
	TEXT_DATA = TEXT_DATA[0:TEXT_LIMI]
	
#	print "-----------------------------"
#	print "TEXT_FONT = "+str(TEXT_FONT)
#	print "TEXT_X    = "+str(TEXT_X)
#	print "TEXT_Y    = "+str(TEXT_Y)
#	print "TEXT_COL1 = "+str(TEXT_COL1)
#	print "TEXT_COL2 = "+str(TEXT_COL2)
#	print "TEXT_LIMI = "+str(TEXT_LIMI)	
#	print "TEXT_DATA = "+str(TEXT_DATA)
#	print "-----------------------------"
	
	if(len(TEXT_DATA) < TEXT_LIMI):
		n = TEXT_LIMI - len(TEXT_DATA)
		TEXT_DATA = TEXT_DATA + (" " * n)
	
	if   TEXT_FONT == "ARN":
		ILI9341.ARN( TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "ARB":
		ILI9341.ARB( TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "16B":
		ILI9341.Text_16B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "24B":
		ILI9341.Text_24B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)	
	elif TEXT_FONT == "32B":
		ILI9341.Text_32B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)	
		

	
	


















