##############################################
# v0.01			export PS1='> '
##############################################
from Config import *
import time
from FONTS.arial_bold       import *
from FONTS.arial_normal     import *
from FONTS.GroteskBold16x32 import *
from FONTS.GroteskBold24x48 import *
from FONTS.GroteskBold32x64 import *
from FONTS.SevenSegmentFull import *
##############################################
spi.close()
spi.open(spi_dev, mode=0, delay=0, bits_per_word=8, speed=spi_speed)
##############################################
gpio.init()
gpio.setcfg(pin_LED, gpio.OUTPUT)
gpio.setcfg(pin_RST, gpio.OUTPUT)
gpio.setcfg(pin_DC,  gpio.OUTPUT)
##############################################
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
##############################################



IME = 0.001
def LED(val):
	gpio.output(pin_LED, val)
def RST(val):
	gpio.output(pin_RST, val)
def DC(val):
	gpio.output(pin_DC,  val)
	
	
def INIT():
	LED(1)	
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
	SEND_DATA_1_Byte(0x10)     #SAxp[2:0];BT[3:0]

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
	DC(0)
	Send_1_Byte(val)
	DC(1)		
def SEND_DATA_1_Byte(val):
	#DC(1)
	Send_1_Byte(val)	
def SEND_DATA_2_Byte(val_1,val_2):
	#DC(1)
	Send_2_Byte(val_1,val_2)	
def SEND_DATA_4_Byte(val_1,val_2,val_3,val_4):
	#DC(1)
	Send_4_Byte(val_1,val_2,val_3,val_4)	
#####################################	
def Send_1_Byte(val):	
	spi.write([val])
def Send_2_Byte(val_1,val_2):	
	spi.write([val_1,val_2])	
def Send_4_Byte(val_1,val_2,val_3,val_4):	
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
	#DC(1)
	#CS(0)
	for x in range(38400):
		Send_4_Byte(0,0,0,0)
		#Send_1_Byte(0);
		#Send_1_Byte(0);
		#Send_1_Byte(0);
		#Send_1_Byte(0);    
	#CS(1)
#####################################

#####################################

f = [0] * 240 * 2


#####################################

#f[120],f[121],f[122],f[123],f[124],f[125],f[126],f[127]



#####################################
def CLS3():
	SET_COL(0, 319)
	SET_PAGE(0, 239)
	SEND_COMMAND(0x2c);                                                                                              
	#DC(1)
	#CS(0)
	for x in range(38400/4):
		spi.write([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) 
	#CS(1)
	
	
#####################################
xp = [255] * 32 * 8	
#####################################
def ARB(x,y,str,Color,bkColor):
	for j in range(len(str)):
		GUI_PutChar_ARB((x+8*j*2),y,str[j],Color,bkColor)
#####################################
def GUI_PutChar_ARB(x,y,cc,Color,bkColor):	
	SET_COL(x, x+15)
	SET_PAGE(y, y+15)
	SEND_COMMAND(0x2c)                                                                                              
	#DC(1)
	#CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	cc = ((c-0x20)*(2*16))
	
	for i in range(16):

		tmp_char1=arial_bold_16x16[cc+xx+0]
		tmp_char2=arial_bold_16x16[cc+xx+1]	
		xx = xx + 2
		
		tmp_char3 = (tmp_char1 << 8) + tmp_char2
		
		if(tmp_char3&0x8000):
			tmp_char3 = tmp_char3 << 1 + 1
		else:
			tmp_char3 = tmp_char3 << 1
		if(tmp_char3&0x8000):
			tmp_char3 = tmp_char3 << 1 + 1
		else:
			tmp_char3 = tmp_char3 << 1		
		
		#tmp_char3 = tmp_char3 << 1
		
		for j in range(16):
			if ( (tmp_char3 >> 15-j) & 0x01 == 0x01):
				xp[j*2] = color_H
				xp[j*2+1] = color_L
			else:
				xp[j*2] = bkcolor_H
				xp[j*2+1] = bkcolor_L		
		
		spi.write([
		xp[0],xp[1],xp[2],xp[3],xp[4],xp[5],xp[6],xp[7],
		xp[8],xp[9],xp[10],xp[11],xp[12],xp[13],xp[14],xp[15],
		xp[16],xp[17],xp[18],xp[19],xp[20],xp[21],xp[22],xp[23],
		xp[24],xp[25],xp[26],xp[27],xp[28],xp[29],xp[30],xp[31]				
		])				
	#CS(1)	
#####################################
def ARN(x,y,str,Color,bkColor):
	for j in range(len(str)):
		GUI_PutChar_ARN((x+8*j*2),y,str[j],Color,bkColor)
#####################################
def GUI_PutChar_ARN(x,y,cc,Color,bkColor):	
	SET_COL(x, x+15)
	SET_PAGE(y, y+15)
	SEND_COMMAND(0x2c)                                                                                              
	#DC(1)
	#CS(0)

	color_H   = Color >> 8
	color_L   = Color & 0x00ff
	bkcolor_H = bkColor >> 8
	bkcolor_L = bkColor & 0x00ff

	c = int(ord(cc))
	tmp_char = 0
	xx = 0
	cc = ((c-0x20)*(2*16))
	
	for i in range(16):

		tmp_char1=arial_normal_16x16[cc+xx+0]
		tmp_char2=arial_normal_16x16[cc+xx+1]	
		xx = xx + 2
		
		tmp_char3 = (tmp_char1 << 8) + tmp_char2
		
		if(tmp_char3&0x8000):
			tmp_char3 = tmp_char3 << 1 + 1
		else:
			tmp_char3 = tmp_char3 << 1
		if(tmp_char3&0x8000):
			tmp_char3 = tmp_char3 << 1 + 1
		else:
			tmp_char3 = tmp_char3 << 1
					
		for j in range(16):
			if ( (tmp_char3 >> 15-j) & 0x01 == 0x01):
				xp[j*2] = color_H
				xp[j*2+1] = color_L
			else:
				xp[j*2] = bkcolor_H
				xp[j*2+1] = bkcolor_L		
			
		spi.write([
		xp[0],xp[1],xp[2],xp[3],xp[4],xp[5],xp[6],xp[7],
		xp[8],xp[9],xp[10],xp[11],xp[12],xp[13],xp[14],xp[15],
		xp[16],xp[17],xp[18],xp[19],xp[20],xp[21],xp[22],xp[23],
		xp[24],xp[25],xp[26],xp[27],xp[28],xp[29],xp[30],xp[31]				
		])				
	#CS(1)	
#####################################
def Text_24B(x,y,str,Color,bkColor):
	for j in range(len(str)):
		GUI_PutChar_GroteskBold24x48((x+13*j*2),y,str[j],Color,bkColor)
#####################################		
def GUI_PutChar_GroteskBold24x48(x,y,cc,Color,bkColor):	
	SET_COL(x, x+23)
	SET_PAGE(y, y+48)
	SEND_COMMAND(0x2c);                                                                                              
	#DC(1)
	#CS(0)

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
				xp[j*2+0] = color_H
				xp[j*2+1] = color_L
			else:
				xp[j*2+0] = bkcolor_H
				xp[j*2+1] = bkcolor_L		

		spi.write([
		xp[0],xp[1],xp[2],xp[3],xp[4],xp[5],xp[6],xp[7],
		xp[8],xp[9],xp[10],xp[11],xp[12],xp[13],xp[14],xp[15],
		xp[16],xp[17],xp[18],xp[19],xp[20],xp[21],xp[22],xp[23],
		xp[24],xp[25],xp[26],xp[27],xp[28],xp[29],xp[30],xp[31],
		xp[32],xp[33],xp[34],xp[35],xp[36],xp[37],xp[38],xp[39],
		xp[40],xp[41],xp[42],xp[43],xp[44],xp[45],xp[46],xp[47]		
		])				
	#CS(1)	
	
#####################################	
def Text_32B(x,y,str,Color,bkColor):
	for j in range(len(str)):
		GUI_PutChar_GroteskBold32x64((x+16*j*2),y,str[j],Color,bkColor)
#####################################		
def GUI_PutChar_GroteskBold32x64(x,y,cc,Color,bkColor):	
	SET_COL(x, x+31)
	SET_PAGE(y, y+63)
	SEND_COMMAND(0x2c);                                                                                              
	#DC(1)
	##CS(0)

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
				xp[j*2+0] = color_H
				xp[j*2+1] = color_L
			else:
				xp[j*2+0] = bkcolor_H
				xp[j*2+1] = bkcolor_L		
		#CS(0)
		spi.write([
		xp[0],xp[1],xp[2],xp[3],xp[4],xp[5],xp[6],xp[7],
		xp[8],xp[9],xp[10],xp[11],xp[12],xp[13],xp[14],xp[15],
		xp[16],xp[17],xp[18],xp[19],xp[20],xp[21],xp[22],xp[23],
		xp[24],xp[25],xp[26],xp[27],xp[28],xp[29],xp[30],xp[31],
		xp[32],xp[33],xp[34],xp[35],xp[36],xp[37],xp[38],xp[39],
		xp[40],xp[41],xp[42],xp[43],xp[44],xp[45],xp[46],xp[47],
		xp[48],xp[49],xp[50],xp[51],xp[52],xp[53],xp[54],xp[55],
		xp[56],xp[57],xp[58],xp[59],xp[60],xp[61],xp[62],xp[63]		
		])
		#CS(1)				
	#CS(1)



#####################################	
def Text_32x50(x,y,str,Color,bkColor):
	for j in range(len(str)):
		GUI_PutChar_SevenSegmentFull((x+16*j*2),y,str[j],Color,bkColor)

#####################################		
def GUI_PutChar_SevenSegmentFull(x,y,cc,Color,bkColor):	
	SET_COL(x, x+31)
	SET_PAGE(y, y+49)
	SEND_COMMAND(0x2c);                                                                                              
	#DC(1)
	#CS(0)

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
				xp[j*2+0] = color_H
				xp[j*2+1] = color_L
			else:
				xp[j*2+0] = bkcolor_H
				xp[j*2+1] = bkcolor_L		

		spi.write([
		xp[0],xp[1],xp[2],xp[3],xp[4],xp[5],xp[6],xp[7],
		xp[8],xp[9],xp[10],xp[11],xp[12],xp[13],xp[14],xp[15],
		xp[16],xp[17],xp[18],xp[19],xp[20],xp[21],xp[22],xp[23],
		xp[24],xp[25],xp[26],xp[27],xp[28],xp[29],xp[30],xp[31],
		xp[32],xp[33],xp[34],xp[35],xp[36],xp[37],xp[38],xp[39],
		xp[40],xp[41],xp[42],xp[43],xp[44],xp[45],xp[46],xp[47],
		xp[48],xp[49],xp[50],xp[51],xp[52],xp[53],xp[54],xp[55],
		xp[56],xp[57],xp[58],xp[59],xp[60],xp[61],xp[62],xp[63]		
		])				
	#CS(1)


#####################################	
def Text_16B(x,y,str,Color,bkColor):
	for j in range(len(str)):
		GUI_PutChar_GroteskBold16x32((x+8*j*2),y,str[j],Color,bkColor)
#####################################		
def GUI_PutChar_GroteskBold16x32(x,y,cc,Color,bkColor):	
	SET_COL(x, x+15)
	SET_PAGE(y, y+31)
	SEND_COMMAND(0x2c);                                                                                              
	#DC(1)
	#CS(0)

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
				xp[j*2+0] = color_H
				xp[j*2+1] = color_L
			else:
				xp[j*2+0] = bkcolor_H
				xp[j*2+1] = bkcolor_L		

		spi.write([
		xp[0],xp[1],xp[2],xp[3],xp[4],xp[5],xp[6],xp[7],
		xp[8],xp[9],xp[10],xp[11],xp[12],xp[13],xp[14],xp[15],
		xp[16],xp[17],xp[18],xp[19],xp[20],xp[21],xp[22],xp[23],
		xp[24],xp[25],xp[26],xp[27],xp[28],xp[29],xp[30],xp[31]	
		])				
	#CS(1)


def TEST():
	CLS3();
	CLS3();
	for i in range(100000):
		ARN(0,0,"ID:",GREEN,BLACK)
		ARN(16*3,0,str(i),WHITE,BLACK)
		
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
