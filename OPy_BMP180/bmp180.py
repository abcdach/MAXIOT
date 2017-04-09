
from pyA20 import i2c
import time
from ctypes import c_short
 
DEVICE = 0x77 # Default device I2C address

i2c.init("/dev/i2c-0")
 
def convertToString(data):
	# Simple function to convert binary data into
	# a string
	return str((data[1] + (256 * data[0])) / 1.2)

def getShort(data, index):
	# return two bytes from data as a signed 16-bit value
	return c_short((data[index] << 8) + data[index + 1]).value

def getUshort(data, index):
	# return two bytes from data as an unsigned 16-bit value
	return (data[index] << 8) + data[index + 1]

def readBmp180Id(addr=DEVICE):
	# Chip ID Register Address
	REG_ID     = 0xD0
	i2c.open(addr)
	i2c.write([REG_ID])
	(chip_id, chip_version) = i2c.read(2)
	i2c.close()
	return (chip_id, chip_version)
  
def readBmp180(addr=DEVICE):
	# Register Addresses
	REG_CALIB  = 0xAA
	REG_MEAS   = 0xF4
	REG_MSB    = 0xF6
	REG_LSB    = 0xF7
	# Control Register Address
	CRV_TEMP   = 0x2E
	CRV_PRES   = 0x34 
	# Oversample setting
	OVERSAMPLE = 3    # 0 - 3
  
	# Read calibration data
	# Read calibration data from EEPROM
	i2c.open(addr)
	i2c.write([REG_CALIB])
	cal = i2c.read(22)
	i2c.close()
	
	# Convert byte data to word values
	AC1 = getShort(cal, 0)
	AC2 = getShort(cal, 2)
	AC3 = getShort(cal, 4)
	AC4 = getUshort(cal, 6)
	AC5 = getUshort(cal, 8)
	AC6 = getUshort(cal, 10)
	B1  = getShort(cal, 12)
	B2  = getShort(cal, 14)
	MB  = getShort(cal, 16)
	MC  = getShort(cal, 18)
	MD  = getShort(cal, 20)

	# Read temperature
	i2c.open(addr)
	i2c.write([REG_CALIB,CRV_TEMP])
	i2c.close()
	
	time.sleep(0.005)
	i2c.open(addr)
	i2c.write([REG_MSB])
	(msb, lsb) = i2c.read(2)
	i2c.close()
	UT = (msb << 8) + lsb

	# Read pressure
	i2c.open(addr)
	i2c.write([REG_MEAS,CRV_PRES + (OVERSAMPLE << 6)])
	i2c.close()
	time.sleep(0.04)
	i2c.open(addr)
	i2c.write([REG_MSB])
	(msb, lsb, xsb) = i2c.read(3)
	i2c.close()
	UP = ((msb << 16) + (lsb << 8) + xsb) >> (8 - OVERSAMPLE)

	# Refine temperature
	X1 = ((UT - AC6) * AC5) >> 15
	X2 = (MC << 11) / (X1 + MD)
	B5 = X1 + X2
	temperature = int(B5 + 8) >> 4

	# Refine pressure
	B6  = B5 - 4000
	B62 = int(B6 * B6) >> 12
	X1  = (B2 * B62) >> 11
	X2  = int(AC2 * B6) >> 11
	X3  = X1 + X2
	B3  = (((AC1 * 4 + X3) << OVERSAMPLE) + 2) >> 2

	X1 = int(AC3 * B6) >> 13
	X2 = (B1 * B62) >> 16
	X3 = ((X1 + X2) + 2) >> 2
	B4 = (AC4 * (X3 + 32768)) >> 15
	B7 = (UP - B3) * (50000 >> OVERSAMPLE)

	P = (B7 * 2) / B4

	X1 = (int(P) >> 8) * (int(P) >> 8)
	X1 = (X1 * 3038) >> 16
	X2 = int(-7357 * P) >> 16
	pressure = int(P + ((X1 + X2 + 3791) >> 4))

	return (temperature/10.0,pressure/100.0) 
  
def main():
    
  (chip_id, chip_version) = readBmp180Id()
  print("Chip ID     : {0}".format(chip_id))
  print("Version     : {0}".format(chip_version))

  print
  
  (temperature,pressure)=readBmp180()
  temperature_c  = (temperature - 32) * 5/9
  _temperature_c = ("%.2f" % temperature_c) 
  print("Temperature : {0} C".format(_temperature_c))
  print("Pressure    : {0} mbar".format(pressure))
    
if __name__=="__main__":
   main()
