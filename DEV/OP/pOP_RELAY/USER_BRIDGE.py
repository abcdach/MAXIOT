#import MEDIATOR
import time
#############################################
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
#############################################


#############################################
def RUN_INIT():
	print "--> RUN_INIT : "
	gpio.init()
	gpio.setcfg(port.PA6, gpio.OUTPUT)
	gpio.pullup(port.PA6, gpio.PULLDOWN)
	gpio.output(port.PA6, gpio.HIGH)
	time.sleep(0.1)
#############################################	
def RUN_MEM_DATA_PROCESSING(DATA):
	print "--> XXX : " + str(DATA)
	time.sleep(1)
#############################################
def RUN_DATA_PROCESSING(DATA):
	print "--> XXXv : " + str(DATA)
	if(DATA=="1"):
		gpio.output(port.PA6, gpio.LOW)
		time.sleep(0.3)
		gpio.output(port.PA6, gpio.HIGH)
#############################################
def RUN_LOOP():
	time.sleep(0.2)



#gpio.output(port.PA6, gpio.HIGH)
#gpio.output(port.PA6, gpio.LOW)
#sleep(2)



