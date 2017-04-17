
import re
import ILI9341



def init():
	ILI9341.INIT()
	ILI9341.CLS3()
	ILI9341.CLS3()

def ToCOLOR(color):
	if   color == "C1":return ILI9341.RED
	elif color == "C2":return ILI9341.GREEN
	elif color == "C3":return ILI9341.BLUE
	elif color == "C4":return ILI9341.BLACK
	elif color == "C5":return ILI9341.YELLOW
	elif color == "C6":return ILI9341.WHITE
	elif color == "C7":return ILI9341.CYAN
	elif color == "C8":return ILI9341.BRIGHT_RED
	elif color == "C9":return ILI9341.GRAY1
	elif color == "C0":return ILI9341.GRAY2
	else:return ILI9341.WHITE


def Text(DATA):
 	DAT = re.split(r',',DATA)
 	Array_len  = len(DAT)
 	
 	TEXT_FONT = DAT[0]
 	TEXT_X    = int(DAT[1])
	TEXT_Y    = int(DAT[2])	
	TEXT_COL1 = ToCOLOR(DAT[3])	
	TEXT_COL2 = ToCOLOR(DAT[4])
	TEXT_LIMI = int(DAT[5])	
	TEXT_DATA = DAT[6]
	TEXT_DATA = TEXT_DATA[0:TEXT_LIMI]
	
#	print "-----------------------------"
#	print "TEXT_FONT = "+str(TEXT_FONT)
#	print "TEXT_X    = "+str(TEXT_X)
#	print "TEXT_Y    = "+str(TEXT_Y)
#	print "TEXT_COL1 = "+str(TEXT_COL1)
#	print "TEXT_COL2 = "+str(TEXT_COL2)
#	print "TEXT_LIMI = "+str(TEXT_LIMI)	
#	print "TEXT_DATA = "+str(TEXT_DATA)
#	print "-----------------------------"
	
	if(len(TEXT_DATA) < TEXT_LIMI):
		n = TEXT_LIMI - len(TEXT_DATA)
		TEXT_DATA = TEXT_DATA + (" " * n)
	
	if   TEXT_FONT == "ARN":
		ILI9341.ARN( TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "ARB":
		ILI9341.ARB( TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "16B":
		ILI9341.Text_16B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "24B":
		ILI9341.Text_24B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)	
	elif TEXT_FONT == "32B":
		ILI9341.Text_32B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)	




















