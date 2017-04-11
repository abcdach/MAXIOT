##############################################
# v0.02			export PS1='> '
##############################################
import threading
import socket
import sys
import json
import time
import re
import commands
##############################################
import MEDIATOR
##############################################
MAX_dbg = 1
##############################################
reconnect		   =  1
Server_IP          = "127.0.0.1"
Server_PORT        =  3004
DEVICE_ID          = "9999"
DEVICE_DESCRIPTION = "Device"
##############################################
data = ""
PING_STATUS = 0
CLIENT_STATUS  = 0
##############################################
class pingThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		if(MAX_dbg==1):print "###################################"
		if(MAX_dbg==1):print "... MAX : PING START   !!!"
		if(MAX_dbg==1):print "###################################"
		while 1:
			time.sleep(3)
			if(PING_STATUS==0):break
			data = "{\"N\":\"8\",\"i\":\"PING\"}"
			sock.sendall(data)
			if(MAX_dbg==1):print("<-- MAX "+data)
		if(MAX_dbg==1):print "###################################"
		if(MAX_dbg==1):print "... MAX : PING STOP !!!"
		if(MAX_dbg==1):print "###################################"
##############################################
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_address = (Server_IP, Server_PORT)
#sock.settimeout(15)
##############################################
class clientThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		global PING_STATUS
		global CLIENT_STATUS
		global sock	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (Server_IP, Server_PORT)
		sock.settimeout(15)
		if(MAX_dbg==1):print "###################################"
		if(MAX_dbg==1):print "... MAX : Server_IP   : "+str(Server_IP)
		if(MAX_dbg==1):print "... MAX : Server_PORT : "+str(Server_PORT)
		if(MAX_dbg==1):print "... MAX : DEVICE_ID   : "+str(DEVICE_ID)
		if(MAX_dbg==1):print "... MAX : DEVICE_DESC : "+str(DEVICE_DESCRIPTION)
		if(MAX_dbg==1):print "###################################"
		if(MAX_dbg==1):print "... MAX : CLIENT START !!!"
		if(MAX_dbg==1):print "###################################"
		if(MAX_dbg==1):print "... MAX : CONNECTING   !!!"
		try:
			sock.connect(server_address)
			if(MAX_dbg==1):print "... MAX : OK"
		except Exception as e: 
			if(MAX_dbg==1):print "... MAX : "+str(e)
			if(MAX_dbg==1):print "###################################"
			if(MAX_dbg==1):print "... MAX : CLIENT STOP !!!"
			if(MAX_dbg==1):print "###################################"
			CLIENT_STATUS = 0
			sock.close()
			exit (0)
		##############################################
		#if(MAX_dbg==1):print "CLIENT_STATUS:"+str(CLIENT_STATUS)	
		if(MAX_dbg==1):print "###################################"
		try:
			while 1:
				if(CLIENT_STATUS==0):break
				try:
					data = sock.recv(1024)
				except Exception as e:
					if(MAX_dbg==1):print "###################################"
					if(MAX_dbg==1):print "... MAX : "+str(e)
					if(MAX_dbg==1):print "###################################"
					CLIENT_STATUS = 0
					PING_STATUS   = 0
				if(CLIENT_STATUS==0):break
				DATA_LEN = len(data)
				#if(MAX_dbg==1):print "... MAX : DARA LEN : "+str(DATA_LEN)
				if(DATA_LEN==0): exit(0)
				#if(MAX_dbg==1):print("--> MAX : "+data)
				#-------------------------------
				data_split = re.split(r'}',data)
				#if(MAX_dbg==1):print(data_split)
				Array_len = len(data_split)
				#if(MAX_dbg==1):print str(Array_len)
				for x in range(Array_len):
					sub_data = data_split[x]
					if(len(sub_data)>5):
						sub_data = sub_data + "}"
						if(MAX_dbg==1):print("--> MAX : "+sub_data)
						#-------------------------------
						try:
							json_data = json.loads(sub_data)
							N_VEL = int(json_data["N"])
							#-------------------------------
							if(N_VEL==1):# mowyobiobis parametrebis gadacema
								data = "{\"N\":\"1\",\"D\":\""+DEVICE_ID+"\",\"V\":\""+DEVICE_DESCRIPTION+"\"}"
								sock.sendall(data)
								if(MAX_dbg==1):print("<-- MAX : "+data)
							#-------------------------------			
							if(N_VEL==0):# pirdapiri onacemebis migeba
								V_VEL = str(json_data["V"])
								S_VEL = str(json_data["S"])
								MEDIATOR.RX(S_VEL,V_VEL)
							#-------------------------------
							if(N_VEL==4):# damaxsovrebuli monacemebis migeba
								V_VEL = str(json_data["V"])
								S_VEL = str(json_data["S"])
								MEDIATOR.MEM_RX(S_VEL,V_VEL)
								if(MAX_dbg==1):print "MEM:"+str(V_VEL)
								if(MAX_dbg==1):print "MEM:"+str(S_VEL)
							#-------------------------------		
							if(N_VEL==2):# daregistrirebis dasturi
								PING_STATUS = 1
								PING = pingThread(1, "MAX_PING", 1)
								PING.start()
							#-------------------------------			
							#if(N_VEL==7):# pingi
								#data = "{\"N\":\"8\",\"i\":\"PING\"}"
								#sock.sendall(data)
								#if(MAX_dbg==1):print("<-- MAX : "+data)
							#-------------------------------			
							if(N_VEL==9):
								exit(0)	
							#-------------------------------
						except Exception as e: 
							if(MAX_dbg==1):print "... JSON : ERROR !!!"		
		finally:
			if(MAX_dbg==1):print "###################################"
			if(MAX_dbg==1):print "... MAX : CLIENT  STOP !!!"
			if(MAX_dbg==1):print "###################################"
			PING_STATUS = 0
			CLIENT_STATUS  = 0
			sock.close()
    
 
def START():
	global CLIENT_STATUS
	CLIENT_STATUS = 1
	CLIENT = clientThread(1, "MAX_CLIENT", 1)
	CLIENT.start()
 
def SEND(SLOT,DATA):
	global PING_STATUS
	if(PING_STATUS==1):
		data = "{\"N\":\"0\",\"S\":\""+str(SLOT)+"\",\"V\":\""+str(DATA)+"\"}"
		sock.sendall(data)
		if(MAX_dbg==1):print("<-- MAX : "+data)    
  

    
    
    
