import MEDIATOR
import time
#############################################
import RPi.GPIO as GPIO
#############################################
GPIO_PIN = 4
#############################################
def RUN_INIT():
	print "--> RUN_INIT : "
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT, initial=0)
	GPIO.cleanup()
	time.sleep(0.1)
#############################################	
def RUN_MEM_DATA_PROCESSING(DATA):
	print "--> XXX : " + str(DATA)
	time.sleep(1)
#############################################
def RUN_DATA_PROCESSING(DATA):
	print "--> XXXv : " + str(DATA)
	if(DATA=="1"):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(4, GPIO.OUT, initial=1)
		time.sleep(0.3)
		GPIO.output(4,0)
		GPIO.cleanup()
#############################################
def RUN_LOOP():
	time.sleep(1)
	#print "LOOP"



