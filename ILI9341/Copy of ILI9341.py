import spi
from pyA20.gpio import gpio
from pyA20.gpio import port
import time

spi.openSPI(device="/dev/spidev0.0", speed=48000000)

gpio.init()
gpio.setcfg(port.PA20, gpio.OUTPUT)
gpio.setcfg(port.PA10, gpio.OUTPUT)
gpio.setcfg(port.PA9,  gpio.OUTPUT)
gpio.setcfg(port.PA8,  gpio.OUTPUT)

GPIO_LED = port.PA20
GPIO_RST = port.PA10
GPIO_DC  = port.PA9
GPIO_CS  = port.PA8

RED     = 0xf800
GREEN   = 0x07e0
BLUE    = 0x001f
BLACK   = 0x0000
YELLOW  = 0xffe0
WHITE   = 0xffff
CYAN    = 0x07ff
BRIGHT_RED = 0xf810
GRAY1   = 0x8410
GRAY2   = 0x4208




IME = 0.001
def LED(val):
	gpio.output(GPIO_LED, val)
def RST(val):
	gpio.output(GPIO_RST, val)
def DC(val):
	gpio.output(GPIO_DC,  val)
def CS(val):
	gpio.output(GPIO_CS,  val)
	
	
def INIT():
	LED(1)
	CS(1)
	
	RST(0)
	RST(1)	

	time.sleep(IME)
	SEND_COMMAND(0xCB)#Power control A
	SEND_DATA_1_Byte(0x39)
	SEND_DATA_1_Byte(0x2C)
	SEND_DATA_1_Byte(0x00)
	SEND_DATA_1_Byte(0x34)
	SEND_DATA_1_Byte(0x02)

	#time.sleep(IME)
	SEND_COMMAND(0xCF)#Power control B 
	SEND_DATA_1_Byte(0x00)
	SEND_DATA_1_Byte(0xC1)
	SEND_DATA_1_Byte(0x30)

	#time.sleep(IME)
	SEND_COMMAND(0xE8)#Driver timing control A 
	SEND_DATA_1_Byte(0x85)
	SEND_DATA_1_Byte(0x00)
	SEND_DATA_1_Byte(0x78)

	#time.sleep(IME)
	SEND_COMMAND(0xEA)#Driver timing control B 
	SEND_DATA_1_Byte(0x00)
	SEND_DATA_1_Byte(0x00)

	#time.sleep(IME)
	SEND_COMMAND(0xED)# Power on sequence control 
	SEND_DATA_1_Byte(0x64)
	SEND_DATA_1_Byte(0x03)
	SEND_DATA_1_Byte(0x12)
	SEND_DATA_1_Byte(0x81)

	#time.sleep(IME)
	SEND_COMMAND(0xF7)#Pump ratio control 
	SEND_DATA_1_Byte(0x20)
 
	#time.sleep(IME)
	SEND_COMMAND(0xC0)#Power Control 1 
	SEND_DATA_1_Byte(0x23)     #VRH[5:0]

	#time.sleep(IME)
	SEND_COMMAND(0xC1)#Power Control 2 
	SEND_DATA_1_Byte(0x10)     #SAP[2:0];BT[3:0]

	#time.sleep(IME)
	SEND_COMMAND(0xC5)#VCOM Control 1
	SEND_DATA_1_Byte(0x3e)     #Contrast
	SEND_DATA_1_Byte(0x28)

	#time.sleep(IME)
	SEND_COMMAND(0xC7)#VCOM Control 2
	SEND_DATA_1_Byte(0x86)      #--

	#time.sleep(IME)
	SEND_COMMAND(0x36)      # Memory Access Control
	SEND_DATA_1_Byte(0x48)
	#ILI9341_SEND_DATA_1_Byte(0xA8) 
        
        
	#time.sleep(IME)
	SEND_COMMAND(0x3A) # Pixel Format Set 
	SEND_DATA_1_Byte(0x55) 

	#time.sleep(IME)
	SEND_COMMAND(0xB1) #Frame Rate Control (In Normal Mode/Full Colors) 
	SEND_DATA_1_Byte(0x00) 
	SEND_DATA_1_Byte(0x18) 

	#time.sleep(IME)
	SEND_COMMAND(0xB6)      # Display Function Control
	SEND_DATA_1_Byte(0x08) 
	SEND_DATA_1_Byte(0x82) 
	SEND_DATA_1_Byte(0x27) 

	#time.sleep(IME)
	SEND_COMMAND(0xF2)      # 3Gamma Function Disable
	SEND_DATA_1_Byte(0x00) 

	#time.sleep(IME)
	SEND_COMMAND(0x26)      #Gamma curve selected
	SEND_DATA_1_Byte(0x01)  

	#time.sleep(IME)
	SEND_COMMAND(0xE0)      #Set Gamma
	SEND_DATA_1_Byte(0x0F) 
	SEND_DATA_1_Byte(0x31) 
	SEND_DATA_1_Byte(0x2B) 
	SEND_DATA_1_Byte(0x0C) 
	SEND_DATA_1_Byte(0x0E) 
	SEND_DATA_1_Byte(0x08) 
	SEND_DATA_1_Byte(0x4E) 
	SEND_DATA_1_Byte(0xF1) 
	SEND_DATA_1_Byte(0x37) 
	SEND_DATA_1_Byte(0x07) 
	SEND_DATA_1_Byte(0x10) 
	SEND_DATA_1_Byte(0x03) 
	SEND_DATA_1_Byte(0x0E) 
	SEND_DATA_1_Byte(0x09) 
	SEND_DATA_1_Byte(0x00) 

	#time.sleep(IME)
	SEND_COMMAND(0xE1)      #Set Gamma
	SEND_DATA_1_Byte(0x00) 
	SEND_DATA_1_Byte(0x0E) 
	SEND_DATA_1_Byte(0x14) 
	SEND_DATA_1_Byte(0x03) 
	SEND_DATA_1_Byte(0x11) 
	SEND_DATA_1_Byte(0x07) 
	SEND_DATA_1_Byte(0x31) 
	SEND_DATA_1_Byte(0xC1) 
	SEND_DATA_1_Byte(0x48) 
	SEND_DATA_1_Byte(0x08) 
	SEND_DATA_1_Byte(0x0F) 
	SEND_DATA_1_Byte(0x0C) 
	SEND_DATA_1_Byte(0x31) 
	SEND_DATA_1_Byte(0x36) 
	SEND_DATA_1_Byte(0x0F) 
        
	#time.sleep(IME)
	SEND_COMMAND(0x11)      #Exit Sleep
	#time.sleep(IME)
	SEND_COMMAND(0x29)    #Display on
	#time.sleep(IME)
	SEND_COMMAND(0x2c)
	time.sleep(IME)
	
#####################################	
def SEND_COMMAND(val):
	CS(1)
	DC(0)
	CS(0)
	Send_1_Byte(val)		
def SEND_DATA_1_Byte(val):
	DC(1)
	Send_1_Byte(val)	
def SEND_DATA_2_Byte(val_1,val_2):
	DC(1)
	Send_2_Byte(val_1,val_2)	
def SEND_DATA_4_Byte(val_1,val_2,val_3,val_4):
	DC(1)
	Send_4_Byte(val_1,val_2,val_3,val_4)	
#####################################	
def Send_1_Byte(val):	
	spi.transfer((val,))
def Send_2_Byte(val_1,val_2):	
	spi.transfer((val_1,val_2))	
def Send_4_Byte(val_1,val_2,val_3,val_4):	
	spi.transfer((val_1,val_2,val_3,val_4))			
#####################################	
def SET_COL(StartCol,EndCol):
	SEND_COMMAND(0x2A)
	SEND_DATA_4_Byte( StartCol >> 8, StartCol & 0x00ff, EndCol >> 8, EndCol & 0x00ff)       
def SET_PAGE(StartPage,EndPage):
	SEND_COMMAND(0x2B)
	SEND_DATA_4_Byte( StartPage >> 8, StartPage & 0x00ff, EndPage >> 8, EndPage & 0x00ff)
#####################################
def setPixel(poX,poY,color):
	T   = poX 
	poX = poY 
	poY = T
	poX = 240 - poX
	
	SET_COL( poX , poX )
	SET_PAGE( poY , poY )
   
	SEND_COMMAND(0x2C)
	SEND_DATA_2_Byte( color >> 8, color & 0x00ff)
#####################################
def CLS():
	SET_COL(0, 239);
	SET_PAGE(0, 319);
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)
	for x in range(38400):
		Send_4_Byte(0,0,0,0)
		#Send_1_Byte(0);
		#Send_1_Byte(0);
		#Send_1_Byte(0);
		#Send_1_Byte(0);    
	CS(1)
#####################################
bytearray(4)

def CLS1():
	xx = (0,) * 2*240
	dd = [xx,] * 320
	
	dd[150] = (255,255)+dd[150][4:]
	dd[150] = (255,255)+dd[150][32:]
	
	#dd[150] = (255,)+dd[150][64:]
	
	#dd[150] = (dd[150][100],255)
	#dd[150] = (dd[150][101],255)
	
	SET_COL(0, 239);
	SET_PAGE(0, 319);
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)
	#for x in range(76800/(240)):
	for x in range(320):
		#bytearray(x)
		#spi.transfer((0,111,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
		spi.transfer(dd[x])    
	CS(1)
#####################################





def TEST():
	CLS1();
	for i in range(360):
		setPixel(i, 50, RED);
		setPixel(i, 51, RED);
		setPixel(i, 52, RED);
		#setPixel(50, i, GREEN);
		#setPixe#l(51, i, GREEN);






