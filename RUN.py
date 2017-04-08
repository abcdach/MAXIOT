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
DevList[0]="1,SYS,MAXIOT,"
DevList[1]="1,GUI,RPb_WebGUI,"
DevList[2]="0,P,OPp_ILI9341,"
DevList[3]="0,P,OPp_8229BSF,"
DevList[4]="0,P,RPp_MFRC522_S0,"
DevList[5]="0,P,RPp_MFRC522_S1,"
DevList[6]="0,P,RPp_RELAY,"
DevList[7]="0,P,Up_Host_IP,"
DevList[8]="0,C,Uc_MIZ_1,"
##############################################
Path = os.path.dirname(os.path.realpath(__file__))
#print Path
##############################################
commands.getoutput("screen -S OPp_ILI9341    -X quit")
time.sleep(0.2)
commands.getoutput("screen -S OPp_8229BSF    -X quit")
time.sleep(0.2)
commands.getoutput("screen -S RPp_MFRC522_S0 -X quit")
time.sleep(0.2)
commands.getoutput("screen -S RPp_MFRC522_S1 -X quit")
time.sleep(0.2)
commands.getoutput("screen -S RPp_RELAY      -X quit")
time.sleep(0.2)
commands.getoutput("screen -S Up_Host_IP     -X quit")
time.sleep(0.2)
commands.getoutput("screen -S Uc_MIZ_1       -X quit")
time.sleep(1)
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
			if(len(Data)>2):
				#print Data
				screen_comm = str(Data[0])
				screen_type = str(Data[1])
				screen_name = str(Data[2])
				screen_argu = str(Data[3])
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
						if(screen_type=="P"):#Python
							print "START : "+screen_name+" "+screen_argu
							comm = "screen -dmS "+screen_name+" bash -c 'cd "+Path+"/"+screen_name+"/ && python RUN.py "+screen_argu+"'"
							#print comm
							ddd = commands.getoutput(comm)
							#print ddd
							time.sleep(1)
						if(screen_type=="C"):#C
							print "START : "+screen_name+" "+screen_argu
							comm = "screen -dmS "+screen_name+" bash -c 'cd "+Path+"/"+screen_name+"/ && ./RUN "+screen_argu+"'"
							#print comm
							ddd = commands.getoutput(comm)
							#print ddd
							time.sleep(1)
						if(screen_type=="GUI"):#C
							print "START : "+screen_name+" "+screen_argu
							comm = "screen -dmS "+screen_name+" bash -c 'cd "+Path+"/"+screen_name+"/ && ./RUN.sh "+screen_argu+"'"
							#print comm
							ddd = commands.getoutput(comm)
							#print ddd
							time.sleep(3)
						if(screen_type=="SYS"):#
							#print "START : "+screen_name+" "+screen_argu
							comm = "screen -dmS "+screen_name+" bash -c '/etc/MAXIOT/MAXIOT_SERVER "+screen_argu+"'"
							print comm
							ddd = commands.getoutput(comm)
							#print ddd
							time.sleep(7)							
							#/etc/MAXIOT/MAXIOT_SERVER
					if(screen_comm=="0"):
						print "STOP  : "+screen_name				
						commands.getoutput("screen -S "+screen_name+" -X quit")







