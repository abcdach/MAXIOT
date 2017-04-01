import MFRC522
import signal
from MAXIOT import *
import time

continue_reading = True
MIFAREReader = MFRC522.MFRC522()

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)
counter = 0
while continue_reading:
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
    RFID_DATA = str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
    print "Card read UID: "+RFID_DATA
    SEND_DATA_TO_IOT_SERVER(RFID_DATA)
    time.sleep (0.5)
    #
  time.sleep (0.5)
  

