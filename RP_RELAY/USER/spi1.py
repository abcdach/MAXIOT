
import spi

spi.openSPI(device="/dev/spidev1.1", speed=1000000)

d = spi.transfer((1,128,0)) # whatever you require here

print (d)

spi.closeSPI()