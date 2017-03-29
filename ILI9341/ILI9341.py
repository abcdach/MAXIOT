import sys
sys.path.append('FONTS')



from pyA20 import spi
from pyA20.gpio import gpio
from pyA20.gpio import port
import time
#import FONT1616
from FONT1616 import *

from GroteskBold16x32 import *
from GroteskBold24x48 import *
from GroteskBold32x64 import *

#from FONTS import GroteskBold32x64

#from FONTS import GroteskBold32x64


from SevenSegmentFull import *





#spi.openSPI(device="/dev/spidev0.0", speed=48000000)
#spi.open("/dev/spidev0.0")
spi.close()
spi.open("/dev/spidev0.0", mode=0, delay=0, bits_per_word=8, speed=48000000)
#spi.close()

#spi.open("/dev/spidev0.0")

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

	SEND_COMMAND(0xCF)#Power control B 
	SEND_DATA_1_Byte(0x00)
	SEND_DATA_1_Byte(0xC1)
	SEND_DATA_1_Byte(0x30)

	SEND_COMMAND(0xE8)#Driver timing control A 
	SEND_DATA_1_Byte(0x85)
	SEND_DATA_1_Byte(0x00)
	SEND_DATA_1_Byte(0x78)

	SEND_COMMAND(0xEA)#Driver timing control B 
	SEND_DATA_1_Byte(0x00)
	SEND_DATA_1_Byte(0x00)

	SEND_COMMAND(0xED)# Power on sequence control 
	SEND_DATA_1_Byte(0x64)
	SEND_DATA_1_Byte(0x03)
	SEND_DATA_1_Byte(0x12)
	SEND_DATA_1_Byte(0x81)

	SEND_COMMAND(0xF7)#Pump ratio control 
	SEND_DATA_1_Byte(0x20)
 
	SEND_COMMAND(0xC0)#Power Control 1 
	SEND_DATA_1_Byte(0x23)     #VRH[5:0]

	SEND_COMMAND(0xC1)#Power Control 2 
	SEND_DATA_1_Byte(0x10)     #SAP[2:0];BT[3:0]

	SEND_COMMAND(0xC5)#VCOM Control 1
	SEND_DATA_1_Byte(0x3e)     #Contrast
	SEND_DATA_1_Byte(0x28)

	SEND_COMMAND(0xC7)#VCOM Control 2
	SEND_DATA_1_Byte(0x86)

	SEND_COMMAND(0x36)      # Memory Access Control
	#SEND_DATA_1_Byte(0x48)  # Horizontaluri -->
	#SEND_DATA_1_Byte(0x88)  # Horizontaluri <--	 
	SEND_DATA_1_Byte(0x28)   # vertikaluri
	
	
	 
        
	time.sleep(IME)
	SEND_COMMAND(0x3A) #Pixel Format Set 
	SEND_DATA_1_Byte(0x55) 

	SEND_COMMAND(0xB1) #Frame Rate Control (In Normal Mode/Full Colors) 
	SEND_DATA_1_Byte(0x00) 
	SEND_DATA_1_Byte(0x18) 

	SEND_COMMAND(0xB6) #Display Function Control
	SEND_DATA_1_Byte(0x08) 
	SEND_DATA_1_Byte(0x82) 
	SEND_DATA_1_Byte(0x27) 

	SEND_COMMAND(0xF2) #3Gamma Function Disable
	SEND_DATA_1_Byte(0x00) 

	SEND_COMMAND(0x26) #Gamma curve selected
	SEND_DATA_1_Byte(0x01)  

	SEND_COMMAND(0xE0) #Set Gamma
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
        
	SEND_COMMAND(0x11)    #Exit Sleep
	SEND_COMMAND(0x29)    #Display on
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
	#spi.transfer((val,))
	spi.write([val])
def Send_2_Byte(val_1,val_2):	
	#spi.transfer((val_1,val_2))
	spi.write([val_1,val_2])	
def Send_4_Byte(val_1,val_2,val_3,val_4):	
	#spi.transfer((val_1,val_2,val_3,val_4))
	spi.write([val_1,val_2,val_3,val_4])			
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

#####################################

kk = [0] * 240 * 2
vv = [kk] * 320 * 2




	
f = [0] * 240 * 2
xx = [0] * 240 * 2

def CLS2():
 	
	#global vv
	#vv[50][50] = 255
	
	xx[30] = 255
	xx[31] = 255
	
	SET_COL(0, 239);
	SET_PAGE(0, 319);
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)
	for x in range(300):
		for c1 in range(4):
		
			for c2 in range(120):
				f[c2] = ascii_16x16[c1*120+c2]	
		
			spi.write([
			f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],
			f[8],f[9],f[10],f[11],f[12],f[13],f[14],f[15],
			f[16],f[17],f[18],f[19],f[20],f[21],f[22],f[23],
			f[24],f[25],f[26],f[27],f[28],f[29],f[30],f[31],
			f[32],f[33],f[34],f[35],f[36],f[37],f[38],f[39],
			f[40],f[41],f[42],f[43],f[44],f[45],f[46],f[47],
			f[48],f[49],f[50],f[51],f[52],f[53],f[54],f[55],
			f[56],f[57],f[58],f[59],f[60],f[61],f[62],f[63],		
			f[64],f[65],f[66],f[67],f[68],f[69],f[70],f[71],
			f[72],f[73],f[74],f[75],f[76],f[77],f[78],f[79],
			f[80],f[81],f[82],f[83],f[84],f[85],f[86],f[87],
			f[88],f[89],f[90],f[91],f[92],f[93],f[94],f[95],
			f[96],f[97],f[98],f[99],f[100],f[101],f[102],f[103],
			f[104],f[105],f[106],f[107],f[108],f[109],f[110],f[111],
			f[112],f[113],f[114],f[115],f[116],f[117],f[118],f[119]				
			])
  
	CS(1)
#####################################

#f[120],f[121],f[122],f[123],f[124],f[125],f[126],f[127]



#####################################
def CLS3():
	SET_COL(0, 319)
	SET_PAGE(0, 239)
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)
	for x in range(38400/4):
		spi.write([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) 
	CS(1)
#####################################
def Text_16(x,y,str,Color,bkColor):
	#x = x * 16
	#y = y * 16
	for j in range(len(str)):
		GUI_PutChar((x+8*j*2),y,str[j],Color,bkColor)
def Text2(x,y,str,Color,bkColor):
	#x = x * 16
	#y = y * 16
	for j in range(len(str)):
		GUI_PutChar2((x+16*j*2),y,str[j],Color,bkColor)
#####################################
p = [255] * 32 * 4
def GUI_PutChar(x,y,cc,Color,bkColor):	
	SET_COL(x, x+15)
	SET_PAGE(y, y+15)
	SEND_COMMAND(0x2c)                                                                                              
	DC(1)
	CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	cc = ((c-0x20)*(2*16))
	
	for i in range(16):
		tmp_char=ascii_16x16[cc+xx]
		for j in range(8):
			if ( (tmp_char >> 7-j) & 0x01 == 0x01):
				p[j*2] = color_H
				p[j*2+1] = color_L
			else:
				p[j*2] = bkcolor_H
				p[j*2+1] = bkcolor_L		
		xx = xx + 1
		tmp_char=ascii_16x16[cc+xx]		
		for j in range(8):
			if ( (tmp_char >> 7-j) & 0x01 == 0x01):
				p[16+j*2] = color_H
				p[16+j*2+1] = color_L
			else:
				p[16+j*2] = bkcolor_H
				p[16+j*2+1] = bkcolor_L
		xx = xx + 1	
		spi.write([
		p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],
		p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],
		p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],
		p[24],p[25],p[26],p[27],p[28],p[29],p[30],p[31],				
		])				
	CS(1)	
#####################################		
def GUI_PutChar2(x,y,cc,Color,bkColor):	
	SET_COL(x, x+31)
	SET_PAGE(y, y+31)
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	yy = 0
	cc = ((c-0x20)*32)
	
	for i in range(16):
		tmp_char=ascii_16x16[cc+xx]
		for j in range(8):
			if ( (tmp_char >> 7-j) & 0x01 == 0x01):
				p[j*4+0] = color_H
				p[j*4+1] = color_L
				p[j*4+2] = color_H
				p[j*4+3] = color_L
			else:
				p[j*4+0] = bkcolor_H
				p[j*4+1] = bkcolor_L
				p[j*4+2] = bkcolor_H
				p[j*4+3] = bkcolor_L		
		xx = xx + 1
		tmp_char=ascii_16x16[cc+xx]		
		for j in range(8):
			if ( (tmp_char >> 7-j) & 0x01 == 0x01):
				p[32+j*4+0] = color_H
				p[32+j*4+1] = color_L
				p[32+j*4+2] = color_H
				p[32+j*4+3] = color_L
			else:
				p[32+j*4+0] = bkcolor_H
				p[32+j*4+1] = bkcolor_L
				p[32+j*4+2] = bkcolor_H
				p[32+j*4+3] = bkcolor_L
		xx = xx + 1	
		
		tmp_char=ascii_16x16[cc+yy]
		for j in range(8):
			if ( (tmp_char >> 7-j) & 0x01 == 0x01):
				p[64+j*4+0] = color_H
				p[64+j*4+1] = color_L
				p[64+j*4+2] = color_H
				p[64+j*4+3] = color_L
			else:
				p[64+j*4+0] = bkcolor_H
				p[64+j*4+1] = bkcolor_L
				p[64+j*4+2] = bkcolor_H
				p[64+j*4+3] = bkcolor_L		
		yy = yy + 1
		tmp_char=ascii_16x16[cc+yy]		
		for j in range(8):
			if ( (tmp_char >> 7-j) & 0x01 == 0x01):
				p[96+j*4+0] = color_H
				p[96+j*4+1] = color_L
				p[96+j*4+2] = color_H
				p[96+j*4+3] = color_L
			else:
				p[96+j*4+0] = bkcolor_H
				p[96+j*4+1] = bkcolor_L
				p[96+j*4+2] = bkcolor_H
				p[96+j*4+3] = bkcolor_L
		yy = yy + 1			
		
		
		
		spi.write([
		p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],
		p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],
		p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],
		p[24],p[25],p[26],p[27],p[28],p[29],p[30],p[31],
		p[32],p[33],p[34],p[35],p[36],p[37],p[38],p[39],
		p[40],p[41],p[42],p[43],p[44],p[45],p[46],p[47],
		p[48],p[49],p[50],p[51],p[52],p[53],p[54],p[55],
		p[56],p[57],p[58],p[59],p[60],p[61],p[62],p[63],		
		p[64],p[65],p[66],p[67],p[68],p[69],p[70],p[71],
		p[72],p[73],p[74],p[75],p[76],p[77],p[78],p[79],
		p[80],p[81],p[82],p[83],p[84],p[85],p[86],p[87],
		p[88],p[89],p[90],p[91],p[92],p[93],p[94],p[95],
		p[96],p[97],p[98],p[99],p[100],p[101],p[102],p[103],
		p[104],p[105],p[106],p[107],p[108],p[109],p[110],p[111],
		p[112],p[113],p[114],p[115],p[116],p[117],p[118],p[119],
		p[120],p[121],p[122],p[123],p[124],p[125],p[126],p[127]			
		])				
	CS(1)	
#####################################	



def Text_24B(x,y,str,Color,bkColor):
	#x = x * 16
	#y = y * 16
	for j in range(len(str)):
		GUI_PutChar_GroteskBold24x48((x+13*j*2),y,str[j],Color,bkColor)

#####################################		
def GUI_PutChar_GroteskBold24x48(x,y,cc,Color,bkColor):	
	SET_COL(x, x+23)
	SET_PAGE(y, y+48)
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	yy = 0
	cc = ((c-0x20)*(3*48))

	for i in range(48):	
		char1 = GroteskBold24x48[cc+xx+0]
		char2 = GroteskBold24x48[cc+xx+1]
		char3 = GroteskBold24x48[cc+xx+2]
		xx = xx + 3
		
		charXX = (char1 << 16) + (char2 << 8) + (char3)
		
		#rol
		if(charXX&0x800000):
			charXX = charXX << 1 + 1
		else:
			charXX = charXX << 1
		#rol
		if(charXX&0x800000):
			charXX = charXX << 1 + 1
		else:
			charXX = charXX << 1		

		for j in range(24):
			if ( (charXX  >> 23 - j) & 0x000001 == 0x000001):
				p[j*2+0] = color_H
				p[j*2+1] = color_L
			else:
				p[j*2+0] = bkcolor_H
				p[j*2+1] = bkcolor_L		

		spi.write([
		p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],
		p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],
		p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],
		p[24],p[25],p[26],p[27],p[28],p[29],p[30],p[31],
		p[32],p[33],p[34],p[35],p[36],p[37],p[38],p[39],
		p[40],p[41],p[42],p[43],p[44],p[45],p[46],p[47]
		
		])				
	CS(1)	
	
	
	

#####################################
#		p[48],p[49],p[50],p[51],p[52],p[53],p[54],p[55],
#		p[56],p[57],p[58],p[59],p[60],p[61],p[62],p[63],		
#		p[64],p[65],p[66],p[67],p[68],p[69],p[70],p[71],
#		p[72],p[73],p[74],p[75],p[76],p[77],p[78],p[79],
#		p[80],p[81],p[82],p[83],p[84],p[85],p[86],p[87],
#		p[88],p[89],p[90],p[91],p[92],p[93],p[94],p[95]	






#####################################	
def Text_32B(x,y,str,Color,bkColor):
	#x = x * 16
	#y = y * 16
	for j in range(len(str)):
		GUI_PutChar_GroteskBold32x64((x+16*j*2),y,str[j],Color,bkColor)

#####################################		
def GUI_PutChar_GroteskBold32x64(x,y,cc,Color,bkColor):	
	SET_COL(x, x+31)
	SET_PAGE(y, y+63)
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	yy = 0
	cc = ((c-0x20)*(4*64))

	for i in range(64):	
		char1 = GroteskBold32x64[cc+xx+0]
		char2 = GroteskBold32x64[cc+xx+1]
		char3 = GroteskBold32x64[cc+xx+2]
		char4 = GroteskBold32x64[cc+xx+3]
		xx = xx + 4
		
		charXX = (char1 << 24) + (char2 << 16) + (char3 << 8) + (char4)
		
		#rol
		if(charXX&0x800000):
			charXX = charXX << 1 + 1
		else:
			charXX = charXX << 1
#		#rol
#		if(charXX&0x800000):
#			charXX = charXX << 1 + 1
#		else:
#			charXX = charXX << 1		
#
		for j in range(32):
			if ( (charXX  >> 31 - j) & 0x00000001 == 0x00000001):
				p[j*2+0] = color_H
				p[j*2+1] = color_L
			else:
				p[j*2+0] = bkcolor_H
				p[j*2+1] = bkcolor_L		

		spi.write([
		p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],
		p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],
		p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],
		p[24],p[25],p[26],p[27],p[28],p[29],p[30],p[31],
		p[32],p[33],p[34],p[35],p[36],p[37],p[38],p[39],
		p[40],p[41],p[42],p[43],p[44],p[45],p[46],p[47],
		p[48],p[49],p[50],p[51],p[52],p[53],p[54],p[55],
		p[56],p[57],p[58],p[59],p[60],p[61],p[62],p[63]		
		])				
	CS(1)



#####################################	
def Text_32x50(x,y,str,Color,bkColor):
	#x = x * 16
	#y = y * 16
	for j in range(len(str)):
		GUI_PutChar_SevenSegmentFull((x+16*j*2),y,str[j],Color,bkColor)

#####################################		
def GUI_PutChar_SevenSegmentFull(x,y,cc,Color,bkColor):	
	SET_COL(x, x+31)
	SET_PAGE(y, y+49)
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	yy = 0
	cc = ((c-0x20)*(4*50))

	for i in range(50):	
		char1 = SevenSegmentFull[cc+xx+0]
		char2 = SevenSegmentFull[cc+xx+1]
		char3 = SevenSegmentFull[cc+xx+2]
		char4 = SevenSegmentFull[cc+xx+3]
		xx = xx + 4
		
		charXX = (char1 << 24) + (char2 << 16) + (char3 << 8) + (char4)
		
		#rol
		if(charXX&0x800000):
			charXX = charXX << 1 + 1
		else:
			charXX = charXX << 1
		#rol
#		if(charXX&0x800000):
#			charXX = charXX << 1 + 1
#		else:
#			charXX = charXX << 1		
#
		for j in range(32):
			if ( (charXX  >> 31 - j) & 0x00000001 == 0x00000001):
				p[j*2+0] = color_H
				p[j*2+1] = color_L
			else:
				p[j*2+0] = bkcolor_H
				p[j*2+1] = bkcolor_L		

		spi.write([
		p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],
		p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],
		p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],
		p[24],p[25],p[26],p[27],p[28],p[29],p[30],p[31],
		p[32],p[33],p[34],p[35],p[36],p[37],p[38],p[39],
		p[40],p[41],p[42],p[43],p[44],p[45],p[46],p[47],
		p[48],p[49],p[50],p[51],p[52],p[53],p[54],p[55],
		p[56],p[57],p[58],p[59],p[60],p[61],p[62],p[63]		
		])				
	CS(1)


#####################################	
def Text_16B(x,y,str,Color,bkColor):
	#x = x * 16
	#y = y * 16
	for j in range(len(str)):
		GUI_PutChar_GroteskBold16x32((x+8*j*2),y,str[j],Color,bkColor)

#####################################		
def GUI_PutChar_GroteskBold16x32(x,y,cc,Color,bkColor):	
	SET_COL(x, x+15)
	SET_PAGE(y, y+31)
	SEND_COMMAND(0x2c);                                                                                              
	DC(1)
	CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	yy = 0
	cc = ((c-0x20)*(2*32))

	for i in range(32):	
		char1 = GroteskBold16x32[cc+xx+0]
		char2 = GroteskBold16x32[cc+xx+1]
		xx = xx + 2
		
		charXX = (char1 << 8) + char2
		
		#rol
		if(charXX&0x800000):
			charXX = charXX << 1 + 1
		else:
			charXX = charXX << 1
		#rol
		if(charXX&0x800000):
			charXX = charXX << 1 + 1
		else:
			charXX = charXX << 1		

		for j in range(16):
			if ( (charXX  >> 15 - j) & 0x0001 == 0x0001):
				p[j*2+0] = color_H
				p[j*2+1] = color_L
			else:
				p[j*2+0] = bkcolor_H
				p[j*2+1] = bkcolor_L		

		spi.write([
		p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],
		p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],
		p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],
		p[24],p[25],p[26],p[27],p[28],p[29],p[30],p[31]	
		])				
	CS(1)







def TEST():
	#CLS();
	CLS3();
	CLS3();
	for i in range(100000):
		Text_16(0,0,"ID:",GREEN,BLACK)
		Text_16(16*3,0,str(i),WHITE,BLACK)
		
		Text_16B(0,16,"SX:"+str(i),BRIGHT_RED,BLACK)
		Text_24B(0,16+32,"SX:"+str(i),BRIGHT_RED,BLACK)
		Text_32B(0,16+48+32,"SX:"+str(i),BRIGHT_RED,BLACK)
		
		
		#Text_7_32(0,16+48+64+17,"SX:"+str(i),BRIGHT_RED,BLACK)
		
		
	#GUI_PutChar_162(100,100,"1",RED,GREEN)
	#Text(0,100,"0123456789ABCDE",RED,GREEN)
	#for i in range(310):
		#setPixel(i, 50, RED);
		#setPixel(i, 51, RED);
		#setPixel(i, 52, RED);
		#setPixel(50, i, GREEN);
		#setPixe#l(51, i, GREEN);





# git add -A & git commit -a -m "Changed something" & git push origin master
# git commit -a -m "Changed something"
# git push origin master