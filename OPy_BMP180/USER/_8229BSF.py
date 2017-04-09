from Config import *
from pyA20.gpio import gpio
from pyA20.gpio import port
import time

import MEDIATOR

gpio.init()
gpio.setcfg(pin_SLC, gpio.OUTPUT)
gpio.setcfg(pin_SDO, gpio.INPUT)
xkeySTAT = 0

def INIT():
	global xkeySTAT
	xkeySTAT = 0
	
def RUN():
	global xkeySTAT
	xkey = 0
	for x in range(17):
		gpio.output(pin_SLC, gpio.HIGH)
		if(gpio.input(pin_SDO) != 1):
			xkey = x
		gpio.output(pin_SLC, gpio.LOW)
	
	if(xkeySTAT == 0):
		if(xkey == 0):
			xkeySTAT = 1
		
	if(xkeySTAT == 1):
		if(xkey != 0):
			xkeySTAT = 0
			print xkey
			MEDIATOR.TX(0,xkey)	
	


			
			
			
			
			