#!/bin/bash

start(){
	clear
	echo "###############"
	echo -e "# \e[1m\e[31m\e[5mROS CHECKUP\e[0m #"
	echo "###############"
	echo ""
	checkWifi
}

checkWifi(){
    #check if hotspot is active

	printf "\e[K\e[4m\e[1mSTEP \e[5m1\e[25m : Check wifi\e[0m :"
    hotspotState=$(curl -s -u pi:10.0.0.2 localhost | grep "span> Hotspot")
    if [[ $hotspotState == *"active"* ]]; then
        printf " hotspot \e[4m\e[1m\e[32mactive\e[0m\n"
        checkRaspLidar
    else
        printf "hotspot \e[4m\e[1m\e[31mnon-active\e[0m. retry in 5s..."
        sleep 5
        checkWifi
    fi
}

checkRaspLidar(){
	printf "\e[K\e[4m\e[1mSTEP \e[5m2\e[25m : Check LIDAR Raspberry connectivity\e[0m :"
    dhcpList=$(iw dev wlan0 station dump)
    if [[ $dhcpList == *"dc:a6:32:d7:08:e4"* ]]; then
        printf " \e[4m\e[1m\e[32mconnected\e[0m"
        ((count = 100))
        while [[ $count -ne 0 ]]; do
            ping -c 1 10.3.141.60 1> /dev/null
            rc=$?
            if [[ $rc -eq 0 ]]; then
                ((count = 1))
            fi
            ((count = count - 1))
        done
        if [[ $rc -eq 0 ]]; then
            printf " on \e[4m10.3.141.60\e[0m\n"
        else
            printf ", \e[4m\e[1m\e[31mbut ping Lidar Raspberry timed out\e[0m"
            exit 1
        fi
        checkEnvVarMaster
    else
        printf " \e[4m\e[1m\e[31mcan't find lidar' raspberry on the network\e[0m, retry in 5s..."
        sleep 5
        checkRaspLidar
    fi
}

checkEnvVarMaster(){
    printf "\e[K\e[4m\e[1mSTEP \e[5m3\e[25m : Check environment variables on \e[34mMASTER\e[0m :"
    if [ -z "$ROS_MASTER_URI" ]; then
        printf " environment variable \e[34mROS_MASTER_URI\e[0m \e[4m\e[1m\e[31misn't defined\e[0m"
        exit 1
        elif [ -z "$ROS_IP" ]; then
        printf " environment variable \e[34mROS_IP\e[0m \e[4m\e[1m\e[31misn't defined\e[0m"
        exit 1
        elif [ "$ROS_MASTER_URI" != "http://10.3.141.1:11311" ]; then
        echo " environment variable \e[34mROS_MASTER_URI\e[0m is currently equal to ${ROS_MASTER_URI} but should be equal to http://10.3.141.1:11311"
        exit 1
        elif [ "$ROS_IP" != "10.3.141.1" ]; then
        echo " environment variable \e[34mROS_IP\e[0m is currently equal to ${ROS_IP} but should be equal to 10.3.141.1"
        exit 1
    fi
	BASHRC=$(cat ~/.bashrc)
	if [[ $BASHRC != *"source /opt/ros/kinetic/setup.bash"* ]]; then
		printf " \e[31m\e[1m/!\\ \e[21m\e[39m/opt/ros/kinetic/setup.bash must be sourced in ~/.basrc"
	fi
    printf " \e[4m\e[1m\e[32mOK\e[0m\n"
    checkUSBMaster
}

checkUSBMaster(){
	printf "\e[K\e[4m\e[1mSTEP \e[5m4\e[25m : Check USB devices on \e[34mMASTER\e[0m :"
	USBS=$(usb-devices)
	if [[ $USBS != *"Bus=01 Lev=02 Prnt=02 Port=00"* ]]; then
		printf " \e[31m\e[1m/!\\ \e[21m\e[39mplease check that there is a device connected to the top \e[34mUSB 3 (blue)\e[39m port on the raspberry \e[34mMASTER\e[0m.\n"
		printRPI
		exit 1
	fi
	if [[ $USBS != *"Bus=01 Lev=02 Prnt=02 Port=01"* ]]; then
		printf " \e[31m\e[1m/!\\ \e[21m\e[39mplease check that there is a device connected to the bottom \e[34mUSB 3 (blue)\e[39m port on the raspberry \e[34mMASTER\e[0m.\n"
		printRPI
		exit 1
	fi
	LISTUSB=$(lsusb)
	COUNT_TEENSY=$(grep -o 'Teensyduino' <<<"$LISTUSB" | grep -c .)
	if [ $COUNT_TEENSY != "2" ]; then
		printf " \e[31m\e[1m/!\\ \e[21m\e[39mplease check that there are 2 teensy connected to the raspberry \e[34mMASTER\e[0m\n"
		printRPI
		exit 1
	fi
	printf " \e[4m\e[1m\e[32mOK\e[0m\n"

}

checkUSBLidar(){
	printf "\e[K\e[4m\e[1mSTEP \e[5m6\e[25m : Check USB devices on \e[34mLIDAR\e[0m :"
	USBS=$(ssh ubuntu@10.3.141.60 "usb-devices")
	if [[ $USBS != *"Bus=01 Lev=02 Prnt=02 Port=01"* ]]; then
		printf " \e[31m\e[1m/!\\ \e[21m\e[39mplease check that there is a device connected to the bottom \e[34mUSB 3 (blue)\e[39m port on the raspberry \e[34mLIDAR\e[0m.\n"
		printRPI
		exit 1
	fi
	if [[ $USBS != *"TIM3xx"* ]]; then
		printf " \e[31m\e[1m/!\\ \e[21m\e[39m please check that the device connected in USB is indeed the \e[34mLIDAR\e[0m\n"
		printRPI
		exit 1
	fi
	printf " \e[4m\e[1m\e[32mOK\e[0m\n"
}

printRPI(){
	echo -e "\e[42m,--------------------------------.\e[49m"
	echo -e "\e[42m| \e[49moooooooooooooooooooo\e[42m      \e[47m\e[30m+======\e[39m\e[49m"
	echo -e "\e[42m| \e[49moooooooooooooooooooo\e[42m      \e[47m\e[30m|   Net\e[39m\e[49m"
	echo -e "\e[42m|                        \e[49moo\e[42m \e[47m\e[30m+======\e[39m\e[49m"
	echo -e "\e[42m|                        \e[49moo\e[42m      |\e[49m"
	echo -e "\e[42m|        \e[47m\e[30m,----.\e[39m\e[42m               \e[47m\e[30m+====\e[39m\e[49m"
	echo -e "\e[42m|        \e[47m\e[30m|CPU |\e[39m\e[42m               \e[47m\e[30m|\e[34mUSB3\e[39m\e[49m <== Here"
	echo -e "\e[42m|        \e[47m\e[30m|    |\e[39m\e[42m               \e[47m\e[30m+====\e[39m\e[49m"
	echo -e "\e[42m|        \e[47m\e[30m'----'\e[39m\e[42m                  |\e[49m\e[39m\e[49m"
	echo -e "\e[42m|                             \e[47m\e[30m+====\e[39m\e[49m"
	echo -e "\e[42m|                             \e[47m\e[30m|USB2\e[39m\e[49m"
	echo -e "\e[42m| \e[47m\e[30mpwr\e[39m\e[42m   \e[47m\e[30m|HD|\e[39m\e[42m   \e[47m\e[30m|HD|\e[39m\e[42m \e[47m\e[30m|I||A|\e[39m\e[42m    \e[47m\e[30m+====\e[39m\e[49m"
	echo -e "\e[42m -\e[47m\e[30m| |\e[39m\e[42m---\e[47m\e[30m|MI|\e[39m\e[42m---\e[47m\e[30m|MI|\e[39m\e[42m----\e[47m\e[30m|V|\e[39m\e[42m------- \e[49m"
}



start