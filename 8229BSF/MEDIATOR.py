



import MAXIOT









def RX(_SLOT,_DATA):
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	print "--> S("+SLOT+") "+DATA

	
def TX(_SLOT,_DATA):
	SLOT = str(_SLOT)
	DATA = str(_DATA)
	print "<-- S("+SLOT+") "+DATA
	MAXIOT.SEND(SLOT,DATA)

















