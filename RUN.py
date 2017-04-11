##############################################
# v0.01			export PS1='> '
##############################################
import commands
import os 
import re
import time
##############################################



 
MAX_SYS_PATH = os.path.dirname(os.path.realpath(__file__))
MAX_SYS_SUB_PATH = os.path.dirname(MAX_SYS_PATH)
MAX_SYS_CONFIG_PATH = MAX_SYS_SUB_PATH+"/MAX_CONFIG"
MAX_DIV_CONFIG_FILE_PATH = MAX_SYS_SUB_PATH+"/MAX_CONFIG/DIV_CONFIG"



#print MAX_SYS_PATH
#print MAX_SYS_SUB_PATH
#print MAX_SYS_CONFIG_PATH

#commands.getoutput("rm -rf "+MAX_SYS_CONFIG_PATH)
##############################################
MAX_SYS_CONFIG_NEW = 0
if not os.path.exists(MAX_SYS_CONFIG_PATH):
	os.makedirs(MAX_SYS_CONFIG_PATH)
	MAX_SYS_CONFIG_NEW = 1
	print "MAX_SYS_CONFIG : WAS CREATED !!!"
##############################################
#commands.getoutput("rm -rf "+MAX_DIV_CONFIG_FILE_PATH)
##############################################
#MAX_DIV_CONFIG_FILE_NEW = 0
#if not os.path.exists(MAX_DIV_CONFIG_FILE_PATH):
#	file(MAX_DIV_CONFIG_FILE_PATH, 'w').close()
#	MAX_DIV_CONFIG_FILE_NEW = 1
#	print "DIV_CONFIG_FILE : WAS CREATED !!!"
##############################################
import glob
import ntpath

MAX_DevList = ["","",""]*256
MAX_DevNum  = int(0)
##############################################
for Dev_Path in glob.glob(MAX_SYS_PATH+"/DEV/OP/*"):
	Dev_Name = ntpath.basename(Dev_Path)
	MAX_DevList[MAX_DevNum]=(Dev_Name[0],Dev_Name,Dev_Path+"/")
	MAX_DevNum=MAX_DevNum+1
##############################################
for Dev_Path in glob.glob(MAX_SYS_PATH+"/DEV/RP/*"):
	Dev_Name = ntpath.basename(Dev_Path)
	MAX_DevList[MAX_DevNum]=(Dev_Name[0],Dev_Name,Dev_Path+"/")
	MAX_DevNum=MAX_DevNum+1
##############################################
for Dev_Path in glob.glob(MAX_SYS_PATH+"/DEV/UN/*"):
	Dev_Name = ntpath.basename(Dev_Path)
	MAX_DevList[MAX_DevNum]=(Dev_Name[0],Dev_Name,Dev_Path+"/")
	MAX_DevNum=MAX_DevNum+1
##############################################
print
for i in xrange(MAX_DevNum):
	print MAX_DevList[i]
##############################################
MAX_DIV_CONFIG_FILE_NEW = 0
if not os.path.exists(MAX_DIV_CONFIG_FILE_PATH):
	file(MAX_DIV_CONFIG_FILE_PATH, 'w').close()
	MAX_DIV_CONFIG_FILE_NEW = 1
	print "DIV_CONFIG_FILE : WAS CREATED !!!"		
print		
if(MAX_DIV_CONFIG_FILE_NEW==1):
	print "CREATING : DEV_CONFIG FILE !!!"
	print "------------------------------"
	f = open(MAX_DIV_CONFIG_FILE_PATH,"a")
	f.write("1,MAXIOT,A,A,A,A,A,A,A,A,\n")
	ii = 9000
	for i in xrange(MAX_DevNum):	
		data = "0,"+MAX_DevList[i][1]
		xLen = len(MAX_DevList[i][1])
		if(xLen<20):
			xLen = 16 - xLen
			for iii in xrange(xLen):
				data = data + " "		
		data = data + "," + str(ii)
		######################################
		Def_DESCRIPTION_FILE = MAX_DevList[i][2]+"Def_DESCRIPTION"
		if not os.path.exists(Def_DESCRIPTION_FILE):
			Dev_DESCRIPTION = MAX_DevList[i][1]
		else:
			Dev_DESCRIPTION = MAX_DevList[i][1]
			with open(Def_DESCRIPTION_FILE) as ff:
				content = ff.readlines()
				if(len(content)!=0):
					Dev_DESCRIPTION = content[0].strip()		
		data = data + "," + Dev_DESCRIPTION
		data = data + ",127.0.0.1,3004,"
		######################################
		print data		
		f.write(data+"\n")
		ii = ii + 10
	f.close()
	print "------------------------------"		
##############################################	
def Finde_Dev(dev):
	for i in xrange(MAX_DevNum):
		if(dev==MAX_DevList[i][1]):
			_Type = MAX_DevList[i][0]
			_Name = MAX_DevList[i][1]
			_Path = MAX_DevList[i][2]
			return (_Type,_Path)
	return ("","")
##############################################
#exit(0)
#(_Dev_Type,_Dev_Path) = Finde_Dev("pOP_ILI9341")
#if(len(_Dev_Path)>0):
#	print _Dev_Type
#	print _Dev_Path

##############################################











#exit(0)






##############################################
DevList = [""]*256
Data    = [""]*2
##############################################
cou = 0
st_mtime_new = ""
st_mtime_old = ""
while 1:

	st_mtime_new = os.stat(MAX_DIV_CONFIG_FILE_PATH).st_mtime
	if(st_mtime_new != st_mtime_old):
		print "--------------------------"
		print "READ : DEV_CONFIG FILE !!!"
		print "--------------------------"
		st_mtime_old = st_mtime_new
		with open(MAX_DIV_CONFIG_FILE_PATH) as f:
			content = f.readlines()
		content = [x.strip() for x in content]
		data_cou = 0
		for data in content:
			DevList[data_cou]=data
			data_cou=data_cou+1
		for i in xrange(data_cou):
			print DevList[i]			
		print "--------------------------"



	cou = cou + 1
	print "cou:"+str(cou)
	time.sleep(1)
	screen = commands.getoutput('screen -ls')
	for i in range(data_cou):
		if(len(DevList[i])>0):
			Data = re.split(',+',DevList[i])
			if(len(Data)>2):
				#print Data
				screen_ENABLE = str(Data[0].strip())
				screen_DEVICE = str(Data[1].strip())
				screen_ID     = str(Data[2].strip())
				screen_DESCRI = str(Data[3].strip())
				screen_IP     = str(Data[4].strip())
				screen_PORT   = str(Data[5].strip())
				
				screen_NAME = "MAX_"+screen_ID
				screen_ARGS = screen_ID+" "+screen_DESCRI+" "+screen_IP+" "+screen_PORT
				
				#print "screen_DEVICE : "+screen_DEVICE
				#print "screen_NAME   : "+screen_NAME
				
				vel = screen.find(screen_NAME)
				if(vel > 0):
					screen_STATUS = "1"
				else:
					screen_STATUS = "0"
					
				#print "screen_ENABLE:"+screen_ENABLE
				#print "screen_DEVICE:"+screen_DEVICE	
				#print "screen_STATUS:"+screen_STATUS
				
				
				if(screen_ENABLE!=screen_STATUS):
					if(screen_ENABLE=="1"):
					
						(_Dev_Type,_Dev_Path) = Finde_Dev(screen_DEVICE)
						if(len(_Dev_Path)>0):
							if(_Dev_Type=="p"):#Python
								print "START : "+screen_NAME+" "+screen_ARGS
								comm = "screen -dmS "+screen_NAME+" bash -c 'cd "+_Dev_Path+" && python RUN.py "+screen_ARGS+"'"
								#print comm
								commands.getoutput(comm)
								time.sleep(1)
							if(_Dev_Type=="c"):#C
								print "START : "+screen_NAME+" "+screen_ID
								comm = "screen -dmS "+screen_NAME+" bash -c 'cd "+_Dev_Path+" && ./RUN "+screen_ARGS+"'"
								#print comm
								commands.getoutput(comm)
								time.sleep(1)
							if(_Dev_Type=="b"):#BASH
								print "START : "+screen_NAME+" "+screen_ID
								comm = "screen -dmS "+screen_NAME+" bash -c 'cd "+_Dev_Path+" && ./RUN.sh "+screen_ARGS+"'"
								#print comm
								commands.getoutput(comm)
								time.sleep(1)
							
							
							
						if(screen_DEVICE=="MAXIOT"):
							print "START : "+screen_NAME
							comm = "screen -dmS "+screen_NAME+" bash -c '/etc/MAXIOT/MAXIOT_SERVER'"
							print comm
							commands.getoutput(comm)
							time.sleep(7)							

					if(screen_ENABLE=="0"):
						print "STOP  : "+screen_NAME				
						commands.getoutput("screen -S "+screen_NAME+" -X quit")







