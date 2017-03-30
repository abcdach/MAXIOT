import re
import MAXIOT
import ILI9341


import threading
import time

DevThread_STATUS=0
event_is_set = 0
DataEvent = 0
RX_DATA = "  "


class DevThread (threading.Thread):
	def __init__(self, threadID, name, DataEvent):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		#global DataEvent
		DataEvent = 0
		while 1:
			print "xxxxx = " + str(DataEvent)
			if(DevThread_STATUS==0):break	
#			if(DataEvent==1):
#				DataEvent = 0
#				print ":))))))"
#			else:
#				print "----"
			time.sleep(0.01)
	
#		while 1:
#			print "wait_for_event starting !!!!!!"
#			event_is_set = e.wait(1)			
#			if(DevThread_STATUS==0):break
#
#			if event_is_set:
#				print ":))))))" + xDATA
#				e.clear()
#			else:
#				print ":("


		




#def START():
	#global DataEvent
	#DataEvent = 0
	#global e
	#e = threading.Event()
	#t1 = threading.Thread(name='blocking',target=wait_for_event,args=(e,))
    #t1.start()
    
    
	#global DataEvent
	#DataEvent = 0
	#xSATELIT = DevThread(1, "Thread-1", DataEvent)
	#xSATELIT.start()   
    
	#time.sleep(10)
	#e.set()






def RX(_SLOT,_DATA):
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	print "--> S("+SLOT+") "+DATA
	global RX_DATA
	
	global DataEvent
	if(DataEvent==0):
		RX_DATA = DATA
		DataEvent = 1
	#e.set()
	#Text(DATA)
	
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
		

	
	
def TX(_SLOT,_DATA):
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	print "<-- S("+SLOT+") "+DATA
	MAXIOT.SEND(SLOT,DATA)

















