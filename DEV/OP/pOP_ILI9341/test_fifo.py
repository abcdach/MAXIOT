##############################################
# v0.03	test !!!		export PS1='> '
import threading

TX_FIFO_MaxLen = 3
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
	
	
	
TX_FIFO_init()	
#print str(TX_FIFO)
print "--------------------------"
print str(TX_FIFO_Len())
TX_FIFO_Put("1","1")
print str(TX_FIFO)	
print str(TX_FIFO_Len())	

	
TX_FIFO_Put("2","2")
print str(TX_FIFO)	
print str(TX_FIFO_Len())		
print "--------------------------"
#print str(TX_FIFO_Len())	
#print str(TX_FIFO_Get())
#print str(TX_FIFO_Len())
#print str(TX_FIFO_Get())
#print str(TX_FIFO_Len())
print "--------------------------"	
print str(TX_FIFO_Len())	
TX_FIFO_Put("3","3")
print str(TX_FIFO)	
print str(TX_FIFO_Len())		
	
TX_FIFO_Put("4","4")
print str(TX_FIFO)	
print str(TX_FIFO_Len())	
print "--------------------------"
print str(TX_FIFO_Len())	
print str(TX_FIFO_Get())
print str(TX_FIFO_Len())	
print str(TX_FIFO_Get())	
print str(TX_FIFO_Len())
print "--------------------------"
print str(TX_FIFO_Len())	
TX_FIFO_Put("5","5")
print str(TX_FIFO)	
print str(TX_FIFO_Len())	
		
	
TX_FIFO_Put("6","6")
print str(TX_FIFO)	
print str(TX_FIFO_Len())	

print "--------------------------"
print str(TX_FIFO_Len())		
print str(TX_FIFO_Get())
print str(TX_FIFO_Len())	
print str(TX_FIFO_Get())	
print str(TX_FIFO_Len())
print str(TX_FIFO_Len())		
print str(TX_FIFO_Get())
print str(TX_FIFO_Len())	
print str(TX_FIFO_Get())	
print str(TX_FIFO_Len())	
print "--------------------------"		
	
	
print "--------------------------"	
print str(TX_FIFO_Len())	
TX_FIFO_Put("dd","dd")
print str(TX_FIFO)	
print str(TX_FIFO_Len())		
	
TX_FIFO_Put("ff","ff")
print str(TX_FIFO)	
print str(TX_FIFO_Len())	
print "--------------------------"	
	
	
	
	
	
	
	
	
	
	
	