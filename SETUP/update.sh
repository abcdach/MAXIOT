#!/bin/bash

#####################################
if [ $(id -u) != "0" ]; then
	whiptail --title "Error" --msgbox "You must be root to run this script." 8 78	
	exit 1
fi
#####################################

whiptail --title "MAXIOT Update" --checklist  --separate-output "Press SPACE to select:" 20 60 11 \
"0"  "Update &  Upgrade Linux   " off \
"1"  "Update MAXIOT STUDIO" off \
"2"  "Update MAXIOT SERVER" off 2>results

clear
while read choice
do
	case $choice in
		0)
			echo "$(tput setaf 2)";
			echo $'\n*** update***\n';
			echo "$(tput sgr 0)";
			apt-get --yes update;
			echo "$(tput setaf 2)";
			echo $'\n*** upgrade ***\n';
			echo "$(tput sgr 0)";
			apt-get --yes upgrade;
		;;
		1)
			echo "$(tput setaf 2)";
			echo $'*** Update MAXIOT STUDIO ***';
			echo "$(tput sgr 0)";
			rm -rf MAXIOT_STUDIO;
			git clone https://github.com/abcdach/MAXIOT_STUDIO;
			if [ $? -eq 0 ]; then
				###########################################################
				ls  /var/www/html/IOT;
				if [ $? -ne 0 ]; then			    	
				    #######################################################
				    echo "$(tput setaf 1)";
				    echo $'You have to install MAXIOT STUDIO !!!!';
				    echo $'ERROR';
				    echo "$(tput sgr 0)"; 
				    #######################################################
				    rm -rf MAXIOT_STUDIO;
				    exit 1
			    fi
			    ###########################################################
				ls  /var/www/html/IOT/Config;
				if [ $? -ne 0 ]; then			    	
				    #######################################################
				    echo "$(tput setaf 1)";
				    echo $'You have to install MAXIOT STUDIO !!!!';
				    echo $'ERROR';
				    echo "$(tput sgr 0)";
				    #######################################################
				    rm -rf MAXIOT_STUDIO;
				    exit 1;			    	
			    fi			    
			    ###########################################################
			    rm -rf /var/www/html/IOT_TEMP;
			    mkdir  /var/www/html/IOT_TEMP;
			    cp -rf /var/www/html/IOT/Config /var/www/html/IOT_TEMP;
			    ###########################################################
			    rm -rf /var/www/html/IOT;
			    cp -rf MAXIOT_STUDIO/IOT /var/www/html/;
			    rm -rf /var/www/html/IOT/Config;
			    cp -rf /var/www/html/IOT_TEMP/Config /var/www/html/IOT/; 
			    rm -rf /var/www/html/IOT_TEMP;
			    ###########################################################
			    echo "$(tput setaf 2)";
				echo $'\nOK';
				echo "$(tput sgr 0)";
			    rm -rf MAXIOT_STUDIO;	    
			else
				echo "$(tput setaf 1)FAIL$(tput sgr 0)";
			fi
		;;
		2)
			echo "$(tput setaf 2)";
			echo $'*** Update MAXIOT SERVER ***';
			echo "$(tput sgr 0)";
			rm -rf MAXIOT_SERVER;
			git clone https://github.com/abcdach/MAXIOT_SERVER;
			if [ $? -eq 0 ]; then
				###########################################################
				ls  /etc/MAXIOT;
				if [ $? -ne 0 ]; then			    	
				    #######################################################
				    echo "$(tput setaf 1)";
				    echo $'You have to install MAXIOT SERVER !!!!';
				    echo $'ERROR';
				    echo "$(tput sgr 0)"; 
				    #######################################################
				    rm -rf MAXIOT_SERVER;
				    exit 1;
			    fi
			    ###########################################################
				rm -rf /etc/MAXIOT/MAXIOT_SERVER;
				cp -rf MAXIOT_SERVER/MAXIOT_SERVER /etc/MAXIOT/;
				
				
				####################################
				uname -a | grep x86 > /dev/null 2>&1
				if [ $? -eq 0 ]; then
					echo "Architecture : x86"
					cp -rf MAXIOT_SERVER/MAXIOT_SERVER_x86 /etc/MAXIOT/MAXIOT_SERVER
				fi
				uname -a | grep arm > /dev/null 2>&1
				if [ $? -eq 0 ]; then
					echo "Architecture : arm"
					cp -rf MAXIOT_SERVER/MAXIOT_SERVER_ARM /etc/MAXIOT/MAXIOT_SERVER
				fi

				
				
				chmod +x /etc/MAXIOT/MAXIOT_SERVER;
				###########################################################
				/etc/init.d/MAXIOT_Daemon stop;
				sleep 1;
				/etc/init.d/MAXIOT_Daemon start;
				###########################################################
			 	echo "$(tput setaf 2)";
				echo $'\nOK';
				echo "$(tput sgr 0)";
				rm -rf MAXIOT_SERVER;
				####################################										    
			else
				echo "$(tput setaf 1)FAIL$(tput sgr 0)";
			fi
		;;
		*)
		;;
	esac
done < results
		
			
			
			
			
			
			
			
			
			