#!/bin/bash


############################################################
if [ $(id -u) != "0" ]; then
	whiptail --title "Error" --msgbox "You must be root to run this script." 8 78	
	exit 1
fi
############################################################
choice=$(whiptail --title "MAXIOT TOOLS" --menu "     " 14 48 3 \
        "1" "MAXIOT TOOLS " \
        "2" "Self update ..." 3>&2 2>&1 1>&3) 

option=$(echo $choice | tr '[:upper:]' '[:lower:]' | sed 's/ //g')
case "${option}" in
    1) 
        chmod +x main.sh
        ./main.sh
    ;;
    2)
    	echo "$(tput setaf 2)";
		echo $'*** Self update ... ***';
		echo "$(tput sgr 0)";
    	rm -rf MAXIOT_MANAGER
    	git clone https://github.com/abcdach/MAXIOT_MANAGER
    	rm -rf Scripts tools.sh
    	cp -rf MAXIOT_MANAGER/Scripts  .
    	chmod +x Scripts/main.sh
    	rm -rf MAXIOT_MANAGER
    	echo "$(tput setaf 2)";
		echo $'\nOK';
		echo "$(tput sgr 0)";
    ;;
    *)
        exit
    ;;
esac
############################################################






			