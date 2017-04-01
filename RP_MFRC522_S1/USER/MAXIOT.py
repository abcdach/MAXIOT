import socket
import sys
import json
import time


def SEND_DATA_TO_IOT_SERVER(IOT_DATA):
	print "-------------------------------------------"
	Server_IP          = "127.0.0.1"
	Server_PORT        = 3004
	DEVICE_NAME        = "700"
	DEVICE_DESCRIPTION = "RFID SENSOR"
	
	data = ""
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (Server_IP, Server_PORT)
	sock.settimeout(15)
	try:
		sock.connect(server_address)
		data = sock.recv(1024)
		data_len = len( data )
		
		if(data_len==0):
			print data_len
			return None
		
		print >>sys.stderr, '--> SOCK %s' % data
	
		json_data = json.loads(data)
		N_VEL = int(json_data["N"])
	
		if(N_VEL==1):
			data = "{\"N\":\"1\",\"D\":\""+DEVICE_NAME+"\",\"V\":\""+DEVICE_DESCRIPTION+"\"}"
			sock.sendall(data)
			print("<-- SOCK "+data)
	
		data = sock.recv(1024)
		print >>sys.stderr, '--> SOCK %s' % data
		json_data = json.loads(data)
		N_VEL = int(json_data["N"])
		
		TSLP = 0.05
		
		if(N_VEL==2):
			data = "{\"N\":\"0\",\"S\":\"0\",\"T\":\"0\",\"V\":\""+str(IOT_DATA)+"\"}"
			sock.sendall(data)
			print("<-- SOCK "+data)

			time.sleep (TSLP);
			
			data = "{\"N\":\"5\"}"
			sock.sendall(data)
			print("<-- SOCK "+data)	
			
		#else:
			#sock.close()
			
	except socket.error as sock_err:
		print "MAXIOT server not found !!!!!"
				
	finally:
		#print >>sys.stderr, 'closing socket'
		sock.close()
		print "-------------------------------------------"
	




















