




MyFifo = [""] * 5
MyFifo_X = 0
MyFifo_Y = 0
MyFifo_LEN = 0


def MyFifo_init():
	global MyFifo_X
	MyFifo_X = 0
	MyFifo_Y = 0
	MyFifo_LEN = 0


def MyFifo_Put(DATA):
	global MyFifo_X	
	global MyFifo_LEN
	MyFifo[MyFifo_X]=DATA
	MyFifo_X = MyFifo_X + 1
	MyFifo_LEN = MyFifo_LEN + 1
	
	


MyFifo_init()
print MyFifo

MyFifo_Put("1111")
print MyFifo
print "MyFifo_X : "+str(MyFifo_X)
print "MyFifo_LEN : "+str(MyFifo_LEN)

MyFifo_Put("2222")
print MyFifo
print "MyFifo_X : "+str(MyFifo_X)
print "MyFifo_LEN : "+str(MyFifo_LEN)





