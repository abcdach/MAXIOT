
from pyA20 import spi
from pyA20.gpio import gpio
from pyA20.gpio import port

spi_dev   = "/dev/spidev0.0"
spi_speed = 48000000
#spi_speed = 10000000


pin_RST = port.PA1
pin_DC  = port.PA0
pin_LED = port.PA3

pin_CS  = port.PA8










