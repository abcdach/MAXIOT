
MyFifo_MaxLen = 64
MyFifo = [""] * MyFifo_MaxLen
MyFifo_X = 0
MyFifo_Y = 0
MyFifo_LEN = 0


def init():
	global MyFifo_X
	MyFifo_X = 0
	MyFifo_Y = 0
	MyFifo_LEN = 0

def Put(DATA):
	global MyFifo_X	
	global MyFifo_LEN
	
	if(MyFifo_LEN < MyFifo_MaxLen):
		if(MyFifo_X == MyFifo_MaxLen):
			MyFifo_X = 0
		MyFifo[MyFifo_X]=DATA
		MyFifo_X = MyFifo_X + 1
		MyFifo_LEN = MyFifo_LEN + 1
	
def Satus():
	if(MyFifo_LEN == MyFifo_MaxLen):
		return 1
	else:
		return 0
	
def Get():
	global MyFifo_Y	
	global MyFifo_LEN
	vel = ""	
	if(MyFifo_LEN != 0):
		if(MyFifo_Y == MyFifo_MaxLen):
			MyFifo_Y = 0		
		MyFifo_LEN = MyFifo_LEN - 1		
		vel = MyFifo[MyFifo_Y]
		MyFifo_Y = MyFifo_Y + 1		
	return vel

def Len():
	global MyFifo_LEN
	return MyFifo_LEN

#MyFifo_init()
#print MyFifo



#MyFifo_Put("5")
#print MyFifo
#print "X:"+str(MyFifo_X)+"  Y:"+str(MyFifo_Y)+"  L:"+str(MyFifo_LEN)+" S:"+str(MyFifo_Satus()) 
#MyFifo_Put("6")
#print MyFifo
#print "X:"+str(MyFifo_X)+"  Y:"+str(MyFifo_Y)+"  L:"+str(MyFifo_LEN) +" S:"+str(MyFifo_Satus())


