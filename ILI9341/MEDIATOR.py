import re
import MAXIOT
import ILI9341

def RX(_SLOT,_DATA):
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	print "--> S("+SLOT+") "+DATA
	
	if   SLOT == "0":
		Text(DATA)
	elif SLOT == "1":
		ILI9341.Text_16(0,16*1,DATA,ILI9341.GREEN,ILI9341.BLACK)
	elif SLOT == "2":
		ILI9341.Text_16(0,16*2,DATA,ILI9341.GREEN,ILI9341.BLACK)

def ToCOLOR(color):
	if   color == "RED":return ILI9341.RED
	elif color == "GREEN":return ILI9341.GREEN
	elif color == "BLUE":return ILI9341.BLUE
	elif color == "BLACK":return ILI9341.BLACK
	elif color == "YELLOW":return ILI9341.YELLOW
	elif color == "WHITE":return ILI9341.WHITE
	elif color == "CYAN":return ILI9341.CYAN
	elif color == "BRIGHT_RED":return ILI9341.BRIGHT_RED
	elif color == "GRAY1":return ILI9341.GRAY1
	elif color == "GRAY2":return ILI9341.GRAY2
	else:return ILI9341.WHITE


def Text(DATA):


	print "-----------------------------"
 	DAT = re.split(r',',DATA)
 	print str(DAT)
 	Array_len  = len(DAT)
 	print str(Array_len)
 	print "-----------------------------"
 	
 	TEXT_FONT = DAT[0]
 	TEXT_X    = int(DAT[1])
	TEXT_Y    = int(DAT[2])	
	TEXT_COL1 = ToCOLOR(DAT[3])	
	TEXT_COL2 = ToCOLOR(DAT[4])	
	TEXT_DATA = DAT[5]

	
	if   TEXT_FONT == "16L":
		ILI9341.Text_16( TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "16B":
		ILI9341.Text_16B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)
	elif TEXT_FONT == "24B":
		ILI9341.Text_24B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)	
	elif TEXT_FONT == "32B":
		ILI9341.Text_32B(TEXT_X,TEXT_Y,TEXT_DATA,TEXT_COL1,TEXT_COL2)	
		

	
	
def TX(_SLOT,_DATA):
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	print "<-- S("+SLOT+") "+DATA
	MAXIOT.SEND(SLOT,DATA)

















