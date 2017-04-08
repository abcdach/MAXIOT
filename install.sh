#!/bin/bash


#systemctl disable log2ram.service





#####################################
if [ $(id -u) != "0" ]; then
	whiptail --title "Error" --msgbox "You must be root to run this script." 8 78	
	exit 1
fi
#####################################
MySQL_ROOT_PASSWORD=$(whiptail --inputbox "What is MySQL Server root Password?" 8 78 dach --title "MySQL Configuration" 3>&1 1>&2 2>&3)
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "MySQL_ROOT_PASSWORD=" $MySQL_ROOT_PASSWORD
else
    MySQL_ROOT_PASSWORD="dach"
fi
#####################################
phpMyadmin_ROOT_PASSWORD=$(whiptail --inputbox "What is phpMyadmin root Password?" 8 78 dach --title "phpMyadmin Configuration" 3>&1 1>&2 2>&3)
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "phpMyadmin_ROOT_PASSWORD=" $phpMyadmin_ROOT_PASSWORD
else
    phpMyadmin_ROOT_PASSWORD="dach"
fi
#####################################
MAXIOT_MySQL_PASSWORD=$(whiptail --inputbox "What is MAXIOT Server to MySQL Server communication Password?" 8 78 dach --title "MAXIOT Configuration" 3>&1 1>&2 2>&3)
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "MAXIOT_MySQL_PASSWORD=" $MAXIOT_MySQL_PASSWORD
else
    MAXIOT_MySQL_PASSWORD="dach"
fi
#####################################
echo "MySQL_ROOT_PASSWORD      =" $MySQL_ROOT_PASSWORD
echo "phpMyadmin_ROOT_PASSWORD =" $phpMyadmin_ROOT_PASSWORD
echo "MAXIOT_MySQL_PASSWORD    =" $MAXIOT_MySQL_PASSWORD
echo "mysql-server mysql-server/root_password password "$MySQL_ROOT_PASSWORD

#####################################

whiptail --title "MAXIOT installer" --checklist  --separate-output "Press SPACE to select:" 20 60 11 \
"0"  "Update  Linux   " off \
"1"  "Upgrade Linux   " off \
"2"  "Install Apache2" off \
"3"  "Install MySQL" off \
"4"  "Install phpMyadmin" off \
"5"  "Install DEV" off \
"6"  "Install MAXIOT STUDIO " off \
"7"  "Install MAXIOT SERVER" off \
"8"  "Install Psutil" off \
"9"  "Install midori matchbox unclutter" off \
"_" "" off 2>results
clear
#####################################
# Orange pi
# systemctl disable log2ram.service
#####################################
while read choice
do
	case $choice in
		0)
			echo "$(tput setaf 2)";echo $'\n*** update***\n'; echo "$(tput sgr 0)"; sleep 2
			apt-get --yes update
		;;
		1)
			echo "$(tput setaf 2)";echo $'\n*** upgrade ***\n'; echo "$(tput sgr 0)"; sleep 2
			apt-get --yes upgrade
		;;
		2)
			echo "$(tput setaf 2)";echo $'\n*** install apache2 ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install apache2
			echo "$(tput setaf 2)";echo $'\n*** install apache2-doc ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install apache2-doc
			echo "$(tput setaf 2)";echo $'\n*** install apache2-utils ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install apache2-utils
			echo "$(tput setaf 2)";echo $'\n*** install libapache2-mod-php5 ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install libapache2-mod-php5
			echo "$(tput setaf 2)";echo $'\n*** install php5 ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install php5
			echo "$(tput setaf 2)";echo $'\n*** install php-pear ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install php-pear
			echo "$(tput setaf 2)";echo $'\n*** install php5-xcache ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install php5-xcache
			echo "$(tput setaf 2)";echo $'\n*** install php5-mysql ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install php5-mysql
		;;
		3)
			echo "$(tput setaf 2)";echo $'\n*** install mysql-server ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			echo "mysql-server mysql-server/root_password password "$MySQL_ROOT_PASSWORD | debconf-set-selections
			echo "mysql-server mysql-server/root_password_again password "$MySQL_ROOT_PASSWORD | debconf-set-selections
			apt-get --yes install mysql-server
			####################################
			echo "$(tput setaf 2)";echo $'\n*** install mysql-client ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install mysql-client
			####################################
			sleep 1
			/etc/init.d/mysqld restart
			sleep 4
			####################################
			echo "$(tput setaf 2)";echo $'*** Configure MySQL DB for MAXIOT SYSTEM ***'; echo "$(tput sgr 0)"; sleep 0.5
			EXPECTED_ARGS=3
			E_BADARGS=65
			MYSQL=`which mysql`
			  
			#Q1="CREATE DATABASE IF NOT EXISTS MAXIOT;"
			Q1=""
			Q2="GRANT USAGE ON *.* TO MAXIOT@localhost IDENTIFIED BY '$MAXIOT_MySQL_PASSWORD';"
			Q3="GRANT ALL PRIVILEGES ON MAXIOT.* TO MAXIOT@localhost;"
			Q4="FLUSH PRIVILEGES;"
			SQL="${Q1}${Q2}${Q3}${Q4}"
			$MYSQL --user="root" --password="$MySQL_ROOT_PASSWORD" -e "$SQL"
			echo "$(tput setaf 2)OK$(tput sgr 0)"	
		;;
		4)
			echo "$(tput setaf 2)";echo $'\n*** install phpmyadmin ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-set-selections
			echo "phpmyadmin phpmyadmin/app-password-confirm password "$MySQL_ROOT_PASSWORD | debconf-set-selections
			echo "phpmyadmin phpmyadmin/mysql/admin-pass password "$MySQL_ROOT_PASSWORD | debconf-set-selections
			echo "phpmyadmin phpmyadmin/mysql/app-pass password "$MySQL_ROOT_PASSWORD | debconf-set-selections
			echo "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2" | debconf-set-selections
			apt-get --yes install phpmyadmin

			echo "$(tput setaf 2)";echo $'\n*** Add to apache2.conf ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			xFile="/etc/apache2/apache2.conf"
			xText="Include /etc/phpmyadmin/apache.conf"

			if grep -q $xText $xFile
			then
			    echo "Text is found"
			else
			    echo "Text is not found !!!"
			    echo $'\n'  >> $xFile
			    echo $xText >> $xFile
			    echo $'\n'  >> $xFile
			fi

			/etc/init.d/apache2 restart
		;;
		5)
			echo "$(tput setaf 2)";echo $'\n*** install libmysqlclient-dev ***\n'; echo "$(tput sgr 0)";sleep 0.5
			apt-get --yes --force-yes install libmysqlclient-dev
			echo "$(tput setaf 2)";echo $'\n*** install python-dev ***\n'; echo "$(tput sgr 0)";sleep 0.5
			apt-get --yes --force-yes install python-dev
			echo "$(tput setaf 2)";echo $'\n*** install screen ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install screen
			echo "$(tput setaf 2)";echo $'*** install daemon ***'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install daemon
			echo "$(tput setaf 2)OK$(tput sgr 0)"
			echo "$(tput setaf 2)";echo $'*** install sysv-rc-conf ***'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install sysv-rc-conf
			echo "$(tput setaf 2)OK$(tput sgr 0)"		
		;;
		6)
			echo "$(tput setaf 2)";echo $'\n*** install MAXIOT STUDIO ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			rm -rf MAXIOT_STUDIO
			git clone https://github.com/abcdach/MAXIOT_STUDIO
			if [ $? -eq 0 ]; then
			    echo "$(tput setaf 2)OK$(tput sgr 0)"
				rm -rf /var/www/html/IOT
				cp -rf MAXIOT_STUDIO/IOT /var/www/html/
				rm -rf MAXIOT_STUDIO
				####################################	
				echo "$(tput setaf 2)";echo $'*** Configure  /var/www/html/IOT/Config/MySQL.php ***'; echo "$(tput sgr 0)"; sleep 0.5
				rm -rf /var/www/html/IOT/Config/MySQL.php				
				echo $'<?php'									>> /var/www/html/IOT/Config/MySQL.php
				echo $'   $mysql_host     = '"'"'localhost'"';"	>> /var/www/html/IOT/Config/MySQL.php
				echo $'   $mysql_user     = '"'"'MAXIOT'"';"    >> /var/www/html/IOT/Config/MySQL.php
				echo $'   $mysql_password = '"'"$MAXIOT_MySQL_PASSWORD"';" >> /var/www/html/IOT/Config/MySQL.php
				echo $'   $mysql_dbname   = '"'"'MAXIOT'"';"    >> /var/www/html/IOT/Config/MySQL.php
				echo $'?>\n'									>> /var/www/html/IOT/Config/MySQL.php
				cat  /var/www/html/IOT/Config/MySQL.php
				echo "$(tput setaf 2)OK$(tput sgr 0)"			
				####################################				    
			else
				echo "$(tput setaf 1)FAIL$(tput sgr 0)"
			fi
		;;
		7)
			echo "$(tput setaf 2)";echo $'\n*** Clone MAXIOT SERVER files ***'; echo "$(tput sgr 0)"; sleep 0.5
			rm -rf MAXIOT_SERVER
			git clone https://github.com/abcdach/MAXIOT_SERVER
			
			if [ $? -eq 0 ]; then
			    echo "$(tput setaf 2)OK$(tput sgr 0)"
			    ####################################
			    echo "$(tput setaf 2)";echo $'*** copy MAXIOT SERVER files to /etc/MAXIOT ***'; echo "$(tput sgr 0)"; sleep 0.5
				rm -rf /etc/MAXIOT
				mkdir /etc/MAXIOT
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
				chmod +x /etc/MAXIOT/MAXIOT_SERVER
				echo "$(tput setaf 2)OK$(tput sgr 0)"
				####################################
				echo "$(tput setaf 2)";echo $'*** Configure  /etc/MAXIOT/MySQL.cnf ***'; echo "$(tput sgr 0)"; sleep 0.5
				rm -rf /etc/MAXIOT/MySQL.cnf
				echo $'{'                        >> /etc/MAXIOT/MySQL.cnf
				echo $'   "SERVER":"localhost"'  >> /etc/MAXIOT/MySQL.cnf
				echo $'   "USER":"MAXIOT"'          >> /etc/MAXIOT/MySQL.cnf
				echo $'   "PASSWORD":"'$MAXIOT_MySQL_PASSWORD'"' >> /etc/MAXIOT/MySQL.cnf
				echo $'}\n'                      >> /etc/MAXIOT/MySQL.cnf
				cat  /etc/MAXIOT/MySQL.cnf
				echo "$(tput setaf 2)OK$(tput sgr 0)"			
				####################################
				#who -r
				#sudo service --status-all
				#sudo /etc/init.d/MAXIOT.d start
				#sudo /etc/init.d/MAXIOT.d stop
				#sudo ps -ef | grep MAXIOT.d
				#sudo ps -ef | grep MAXIOT_SERVER
				#sudo ps -ef | grep MAXIOT_WatchDog
				#sudo chkconfig --add MAXIOT_Daemon
				#find /etc -name "*MAXIOT_Daemon"
				#systemctl status MAXIOT_Daemon.service
				#systemctl status apache2.service
				####################################			
				#echo "$(tput setaf 2)";echo $'*** install daemon ***'; echo "$(tput sgr 0)"; sleep 0.5
				#apt-get --yes install daemon
				#echo "$(tput setaf 2)OK$(tput sgr 0)"
				#echo "$(tput setaf 2)";echo $'*** install sysv-rc-conf ***'; echo "$(tput sgr 0)"; sleep 0.5
				#apt-get --yes install sysv-rc-conf
				#echo "$(tput setaf 2)OK$(tput sgr 0)"
				
				
				
				
				
				####################################
				echo "$(tput setaf 2)";echo $'*** killing MAXIOT_SERVER ***'; echo "$(tput sgr 0)"; sleep 0.5
				/etc/init.d/MAXIOT_Daemon stop
				PID=`ps -eaf | grep MAXIOT_SERVER | grep -v grep | awk '{print $2}'`
				if [[ "" !=  "$PID" ]]; then
				  echo "killing $PID"
				  kill -9 $PID
				fi
				PID=`ps -eaf | grep MAXIOT_SERVER | grep -v grep | awk '{print $2}'`
				if [[ "" !=  "$PID" ]]; then
				  echo "killing $PID"
				  kill -9 $PID
				fi
				echo "$(tput setaf 2)OK$(tput sgr 0)"		
				####################################											
				echo "$(tput setaf 2)";echo $'*** copy MAXIOT_Daemon file to /etc/init.d/ ***'; echo "$(tput sgr 0)"; sleep 0.5				
				rm -rf /etc/init.d/MAXIOT_Daemon
				cp -rf MAXIOT_SERVER/MAXIOT_Daemon /etc/init.d/MAXIOT_Daemon
				chmod +x /etc/init.d/MAXIOT_Daemon
				echo "$(tput setaf 2)OK$(tput sgr 0)"			
				####################################
				echo "$(tput setaf 2)";echo $'*** copy MAXIOT_Daemon file to /etc/init.d/ ***'; echo "$(tput sgr 0)"; sleep 0.5			
				#chkconfig --add MAXIOT_Daemon
				sysv-rc-conf MAXIOT_Daemon on
				echo "$(tput setaf 2)OK$(tput sgr 0)"
				####################################
				echo "$(tput setaf 2)";echo $'*** MAXIOT_Daemon start ***'; echo "$(tput sgr 0)"; sleep 0.5	
				/etc/init.d/MAXIOT_Daemon start
				echo "$(tput setaf 2)OK$(tput sgr 0)"		
				####################################
				rm -rf MAXIOT_SERVER
				####################################										    
			else
				echo "$(tput setaf 1)FAIL$(tput sgr 0)"
			fi
		;;
		8)
			echo "$(tput setaf 2)";echo $'\n*** install psutil ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get install python-pip python-dev build-essential
			pip install --upgrade pip
			pip install --upgrade virtualenv

			wget https://bootstrap.pypa.io/get-pip.py
			python get-pip.py
			pip install psutil
			rm -rf get-pip.py
		;;
		9)

			
			echo "$(tput setaf 2)";echo $'\n*** install midori ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install midori midori			
			echo "$(tput setaf 2)";echo $'\n*** install matchbox ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install matchbox			
			echo "$(tput setaf 2)";echo $'\n*** install unclutter ***\n'; echo "$(tput sgr 0)"; sleep 0.5
			apt-get --yes install unclutter
						
		;;
		10)

		;;
		*)
		;;
	esac
done < results

#echo "mysql-server-5.5 mysql-server/root_password password dach" | debconf-set-selections
#echo "mysql-server-5.5 mysql-server/root_password_again password dach" | debconf-set-selections
			
			
			
			
			