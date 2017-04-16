#import MEDIATOR
import time
#############################################
from pyA20 import i2c
#from ctypes import c_short
#############################################
#----------------------------------------------------------------------
#	Operational status/single-shot conversion start
#----------------------------------------------------------------------
#ADS1115_OS = 0 << 7		#No effect
ADS1115_OS = 1 << 7			#Begin a single conversion (when in power-down mode)
#----------------------------------------------------------------------
#	Input multiplexer configuration
#----------------------------------------------------------------------
#ADS1115_MUX = 0 << 4		#000 : AINP = AIN0 and AINN = AIN1 -- default
#ADS1115_MUX = 1 << 4		#001 : AINP = AIN0 and AINN = AIN3
#ADS1115_MUX = 2 << 4		#010 : AINP = AIN1 and AINN = AIN3
ADS1115_MUX = 3 << 4		#011 : AINP = AIN2 and AINN = AIN3
#ADS1115_MUX = 4 << 4		#100 : AINP = AIN0 and AINN = GND
#ADS1115_MUX = 5 << 4		#101 : AINP = AIN1 and AINN = GND
#ADS1115_MUX = 6 << 4		#110 : AINP = AIN2 and AINN = GND
#ADS1115_MUX = 7 << 4		#111 : AINP = AIN3 and AINN = GND
#----------------------------------------------------------------------
#	Programmable gain amplifier configuration
#----------------------------------------------------------------------
#ADS1115_PGA = 0 << 1		#000 : FS = +/-6.144V --	This parameter expresses the full-scale range of the ADC scaling. In no event should more than VDD + 0.3V be applied to this device.
ADS1115_PGA = 1 << 1		#001 : FS = +/-4.096V -- This parameter expresses the full-scale range of the ADC scaling. In no event should more than VDD + 0.3V be applied to this device.
#ADS1115_PGA = 2 << 1		#010 : FS = +/-2.048V
#ADS1115_PGA = 3 << 1		#011 : FS = +/-1.024V
#ADS1115_PGA = 4 << 1		#100 : FS = +/-0.512V
#ADS1115_PGA = 5 << 1		#101 : FS = +/-0.256V
#ADS1115_PGA = 6 << 1		#110 : FS = +/-0.256V -- default)
#ADS1115_PGA = 7 << 1		#111 : FS = +/-0.256V
#----------------------------------------------------------------------
#	Device operating mode
#----------------------------------------------------------------------
ADS1115_MODE = 0 << 0		#Continuous conversion mode
# ADS1115_MODE = 1 << 0		#Power-down single-shot mode -- default
##----------------------------------------------------------------------
##	Data rate
##----------------------------------------------------------------------
ADS1115_DR = 0 << 5			#000 : 8SPS
#ADS1115_DR = 1 << 5		#001 : 16SPS
#ADS1115_DR = 2 << 5		#010 : 32SPS
#ADS1115_DR = 3 << 5		#011 : 64SPS
#ADS1115_DR = 4 << 5		#100 : 128SPS -- default
#ADS1115_DR = 5 << 5		#101 : 250SPS
#ADS1115_DR = 6 << 5		#110 : 475SPS
#ADS1115_DR = 7 << 5		#111 : 860SPS
#----------------------------------------------------------------------
#	Comparator mode
#----------------------------------------------------------------------
ADS1115_COMP_MODE = 0 << 4		#Traditional comparator with hysteresis -- default
#ADS1115_COMP_MODE = 1 << 4		#Window comparator
#----------------------------------------------------------------------
#	Comparator polarity
#----------------------------------------------------------------------
ADS1115_COMP_POL = 0 << 3		#Active low -- default
#ADS1115_COMP_POL = 1 << 3		#Active high
#----------------------------------------------------------------------
#	Latching comparator
#----------------------------------------------------------------------
ADS1115_COMP_LAT = 0 << 2		#Non-latching comparator -- default
#ADS1115_COMP_LAT = 1 << 2		#Latching comparator
#----------------------------------------------------------------------
#	Comparator queue and disable
#----------------------------------------------------------------------
#ADS1115_COMP_QUE = 0 << 0		#00 : Assert after one conversion
#ADS1115_COMP_QUE = 1 << 0		#01 : Assert after two conversions
#ADS1115_COMP_QUE = 2 << 0		#10 : Assert after four conversions
ADS1115_COMP_QUE = 3 << 0		#11 : Disable comparator (default)
#############################################
ADS1115_ADDRESS = 0x48
i2c.init("/dev/i2c-0")

MSB_Config = ADS1115_OS | ADS1115_MUX | ADS1115_PGA | ADS1115_MODE
LSB_Config = ADS1115_DR | ADS1115_COMP_MODE | ADS1115_COMP_POL | ADS1115_COMP_LAT | ADS1115_COMP_QUE

def ADS1115_INIT():
	print str(MSB_Config)
	print str(LSB_Config)
	print str(ADS1115_ADDRESS)
	i2c.open(ADS1115_ADDRESS)
	i2c.write([0x01,MSB_Config,LSB_Config])
	i2c.close()


def ADS1115_GetVal():
	i2c.open(ADS1115_ADDRESS)
	i2c.write([0x00])
	time.sleep(0.1)
	(MSB, LSB) = i2c.read(2)
	i2c.close()
	Vel = (MSB << 8)+LSB
	if(Vel > 32767):
		Vel = 0
	print str(Vel)









ADS1115_INIT()
while 1:
	time.sleep(0.1)
	ADS1115_GetVal()



#addr = 0x48 # Default device I2C address


#i2c.open(addr)
#i2c.write([0x00])
#(msb, lsb) = i2c.read(2)
#i2c.close()
