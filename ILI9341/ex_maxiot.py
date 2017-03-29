#	export PS1='> '

import socket
import sys
import json
import time
import ILI9341


ILI9341.INIT()
ILI9341.CLS3()

#data1 = str(sys.argv[1])
#data2 = str(sys.argv[2])
#data3 = str(sys.argv[3])
#data4 = str(sys.argv[4])

data1 = 111
data2 = 222
data3 = 333
data4 = 444

print ( data1 )
print ( data2 )
print ( data3 )
print ( data4 )

Server_IP          = "10.0.0.20"
Server_PORT        = 3004
DEVICE_NAME        = "222"
DEVICE_DESCRIPTION = "LCD"

data = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (Server_IP, Server_PORT)
sock.settimeout(15)

while 1:
	print "... SOCK : connecting !!!"
	try:
		sock.connect(server_address)
		break
	except Exception as e: 
		print "... SOCK : "+str(e)
		sock.close()
		exit (0)
		
		
#sock.close()		
#print "close ..."		
#exit(0)		
		

try:
	while 1:
		data = sock.recv(1024)
		DATA_LEN = len(data)
		#print "... SOCK : DARA LEN : "+str(DATA_LEN)
		if(DATA_LEN==0): exit(0)

		print("--> SOCK "+data)
		
		json_data = json.loads(data)
		N_VEL = int(json_data["N"])

		if(N_VEL==9):
			exit(0)
		if(N_VEL==1):
			data = "{\"N\":\"1\",\"D\":\""+DEVICE_NAME+"\",\"V\":\""+DEVICE_DESCRIPTION+"\"}"
			sock.sendall(data)
			print("<-- SOCK "+data)
		if(N_VEL==0):
			V_VEL = str(json_data["V"])
			print str(V_VEL)
			ILI9341.Text_16(0,0,str(V_VEL),ILI9341.GREEN,ILI9341.BLACK)
			
			data = "{\"N\":\"8\",\"i\":\"PING\"}"
			sock.sendall(data)
			print("<-- SOCK "+data)		
		#if(N_VEL==7):
			#data = "{\"N\":\"8\",\"i\":\"PING\"}"
			#sock.sendall(data)
			#print("<-- SOCK "+data)
			
		if(N_VEL==2):
			data = "{\"N\":\"0\",\"S\":\"0\",\"T\":\"0\",\"V\":\""+str(data1)+"\"}"
			sock.sendall(data)
			print("<-- SOCK "+data)			
		 	
			

	#data = sock.recv(1024)
	#print >>sys.stderr, '--> SOCK %s' % data
	#json_data = json.loads(data)
	#N_VEL = int(json_data["N"])
	
	#TSLP = 0.05	# 0.02 sakmarisia
	#if(N_VEL==2):
		
		#data = "{\"N\":\"0\",\"S\":\"4\",\"T\":\"0\",\"V\":\"1\"}"
		#sock.sendall(data)
		#print("<-- SOCK "+data)	
		
		#time.sleep (TSLP);
		
		#data = "{\"N\":\"5\"}"
		#sock.sendall(data)
		#print("<-- SOCK "+data)	
		
			
	#else:
		#print("<-- SOCK "+"Error !!!")


finally:
    print "... SOCK : closing socket !!!"
    sock.close()
