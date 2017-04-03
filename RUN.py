##############################################
# v0.01			export PS1='> '
##############################################
import commands
import os 
import re
import time
##############################################
DevList = [""]*32
Data    = [""]*2
##############################################
DevList[0]="0,OP_ILI9341"
DevList[1]="0,OP_8229BSF"
##############################################
Path = os.path.dirname(os.path.realpath(__file__))
#print Path
##############################################
cou = 0
while 1:
	cou = cou + 1
	print "cou:"+str(cou)
	time.sleep(1)
	screen = commands.getoutput('screen -ls')
	for i in range(len(DevList)):
		if(len(DevList[i])>0):
			Data = re.split(',+',DevList[i])
			if(len(Data)==2):
				#print Data
				screen_comm = str(Data[0])
				screen_name = str(Data[1])
				vel = screen.find(screen_name)
				if(vel > 0):
					screen_stat = "1"
				else:
					screen_stat = "0"
				#print "screen_comm:"+screen_comm
				#print "screen_name:"+screen_name	
				#print "screen_stat:"+screen_stat
				if(screen_comm!=screen_stat):
					if(screen_comm=="1"):
						print "Need to start : "+screen_name
						comm = "screen -dmS "+screen_name+" bash -c 'cd "+Path+"/"+screen_name+"/ && python RUN.py'"
						print comm
						ddd = commands.getoutput(comm)
						#print ddd
					if(screen_comm=="0"):
						print "Need to stop  : "+screen_name				
						commands.getoutput("screen -S "+screen_name+" -X quit")







