
import time
import ILI9341


while True:
	time.sleep(0.01)
	ILI9341.INIT()
	ILI9341.TEST()

spi.closeSPI()
