##############################################
#	export PS1='> '
##############################################
import threading
import socket
import sys
import json
import time
##############################################
#import ILI9341
##############################################
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
##############################################
Server_IP          = "10.0.0.13"
Server_PORT        =  3004
DEVICE_NAME        = "9001"
DEVICE_DESCRIPTION = "Capacitive Touch"
##############################################
data = ""
SATELIT_STATUS = 0
CLIENT_STATUS  = 0
##############################################
class pingThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "SATELIT Start !!!!!" 
		while 1:
			time.sleep(3)
			if(SATELIT_STATUS==0):break
			data = "{\"N\":\"8\",\"i\":\"PING\"}"
			sock.sendall(data)
			print("<-- SOCK "+data)
		print "SATELIT Exiting !!!!!"
##############################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (Server_IP, Server_PORT)
sock.settimeout(15)
##############################################
class clientThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		global SATELIT_STATUS
		global CLIENT_STATUS
		print "CLIENT Start !!!!!" 	
		while 1:
			print "... SOCK : connecting !!!"
			try:
				sock.connect(server_address)
				break
			except Exception as e: 
				print "... SOCK : "+str(e)
				#sock.close()
				exit (0)
		##############################################
		print "CLIENT_STATUS:"+str(CLIENT_STATUS)	
		try:
			while 1:
				if(CLIENT_STATUS==0):break
				data = sock.recv(1024)
				if(CLIENT_STATUS==0):break
				DATA_LEN = len(data)
				#print "... SOCK : DARA LEN : "+str(DATA_LEN)
				if(DATA_LEN==0): exit(0)
				print("--> SOCK "+data)
				#-------------------------------		
				json_data = json.loads(data)
				N_VEL = int(json_data["N"])
				#-------------------------------
				if(N_VEL==1):
					data = "{\"N\":\"1\",\"D\":\""+DEVICE_NAME+"\",\"V\":\""+DEVICE_DESCRIPTION+"\"}"
					sock.sendall(data)
					print("<-- SOCK "+data)
				#-------------------------------			
				if(N_VEL==0):
					V_VEL = str(json_data["V"])
					print str(V_VEL)
				#-------------------------------	
				if(N_VEL==2):
					SATELIT_STATUS = 1
					SATELIT = pingThread(1, "Thread-1", 1)
					SATELIT.start()
					print "xSATELIT_STATUS:"+str(SATELIT_STATUS)
				#-------------------------------			
				#if(N_VEL==7):
					#data = "{\"N\":\"8\",\"i\":\"PING\"}"
					#sock.sendall(data)
					#print("<-- SOCK "+data)
				#-------------------------------			
				if(N_VEL==9):
					exit(0)	
				#-------------------------------		
		finally:
		    print "CLIENT Exiting !!!!!"
		    SATELIT_STATUS = 0
		    sock.close()
    
 
def START():
	global CLIENT_STATUS
	CLIENT_STATUS = 1
	CLIENT = clientThread(1, "Thread-1", 1)
	CLIENT.start()
 
def SEND(DATA):
	global SATELIT_STATUS
	if(SATELIT_STATUS==1):
		data = "{\"N\":\"0\",\"S\":\"0\",\"T\":\"0\",\"V\":\""+str(DATA)+"\"}"
		sock.sendall(data)
		print("<-- SOCK "+data)    
  
    
    
    
    
    
    
    
    
    
    
    
