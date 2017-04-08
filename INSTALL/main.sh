#!/bin/bash


############################################################
if [ $(id -u) != "0" ]; then
	whiptail --title "Error" --msgbox "You must be root to run this script." 8 78	
	exit 1
fi
############################################################
choice=$(whiptail --title "MAXIOT" --menu "Make a choice :" 14 48 3 \
        "1" "MAXIOT System ( Update  ) " \
        "2" "MAXIOT System ( Install ) " 3>&2 2>&1 1>&3) 

option=$(echo $choice | tr '[:upper:]' '[:lower:]' | sed 's/ //g')
case "${option}" in
    1) 
        chmod +x Scripts/update/update.sh
        Scripts/update/update.sh
    ;;
    2)
    	chmod +x Scripts/install/install.sh
        Scripts/install/install.sh
    ;;
    *)
        exit
    ;;
esac
############################################################






			