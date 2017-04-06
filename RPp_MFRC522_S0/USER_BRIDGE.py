import MEDIATOR
import time
#############################################

import MFRC522
import signal
import time

counter = 0
#############################################
def RUN_INIT():
	#time.sleep(1)
	global counter
	counter = 0
	global continue_reading
	continue_reading = True
	global MIFAREReader
	MIFAREReader = MFRC522.MFRC522()
#############################################	
def RUN_MEM_DATA_PROCESSING(DATA):
	print "--> RFID : " + str(DATA)
	time.sleep(1)
#############################################
def RUN_DATA_PROCESSING(DATA):
	print "--> RFID : " + str(DATA)
	time.sleep(1)
#############################################
def RUN_LOOP():
	global counter
	time.sleep(0.3)
	#print "LOOP"
	MIFAREReader.MFRC522_Init()
	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	counter = counter + 1
	print "Waiting for RFID Card : "+str(counter)
	if status == MIFAREReader.MI_OK:
		print "-------------------------------------------"
		print "Card detected"
		counter = 0
	(status,backData) = MIFAREReader.MFRC522_Anticoll()
  
	if status == MIFAREReader.MI_OK:
	    v0 = "%0.2X" % backData[0]
	    v1 = "%0.2X" % backData[1]
	    v2 = "%0.2X" % backData[2]
	    v3 = "%0.2X" % backData[3]
	    v4 = "%0.2X" % backData[4]
	    RFID_DATA = v0+v1+v2+v3+v4
	
	    print "Card read UID: "+RFID_DATA
	    MEDIATOR.TX(0,RFID_DATA)
	    time.sleep (1.5)

#		RFID_DATA = str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
#		print "Card read UID: "+RFID_DATA
#		MEDIATOR.TX(0,RFID_DATA)
#		time.sleep(1)


def end_read(signal, frame):
	global continue_reading
	continue_reading = False
	print "Ctrl+C captured, ending read."
	MIFAREReader.GPIO_CLEEN()




#############################################
#def RUN_INIT():
#	time.sleep(0.2)
#############################################	
#def RUN_MEM_DATA_PROCESSING(DATA):
#	time.sleep(0.2)
#############################################
#def RUN_DATA_PROCESSING(DATA):
#	time.sleep(0.2)
#############################################



