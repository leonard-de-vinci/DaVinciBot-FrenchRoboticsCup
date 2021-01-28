#!/bin/bash
checkWifi(){
	#check if hotspot is active
	hotspotState=$(curl -s -u pi:10.0.0.2 localhost | grep "span> Hotspot")
	if [[ $hotspotState == *"active"* ]]; then
		echo "hotspot active"
		checkRaspLidar
	else
		echo "hotspot non-active"
		echo "retry in 5s"
		sleep 5
		checkWifi
	fi
}

checkRaspLidar(){
	dhcpList=$(iw dev wlan0 station dump)
	if [[ $dhcpList == *"dc:a6:32:d7:08:e4"* ]]; then
		echo "Lidar Raspberry is connected"
		echo "checking if Lidar Raspberry is accessible :"
		((count = 100))
		while [[ $count -ne 0 ]]; do
			ping -c 1 10.3.141.60
			rc=$?
			if [[ $rc -eq 0 ]]; then
				((count = 1))
			fi
			((count = count - 1))
		done
		if [[ $rc -eq 0 ]]; then
			echo "Lidar Raspberry is accessible on 10.3.141.60"
		else
			echo "ping Lidar Raspberry timed out"
			exit 1
		fi
		checkEnvVarMaster
	else
		echo "can't find lidar' raspberry on the network, retry in 5s"
		sleep 5
		checkRaspLidar
	fi		
}

checkEnvVarMaster(){
	echo "checking environment variables on MASTER :"
	if [ -z "$ROS_MASTER_URI" ]; then
		echo "environment variable ROS_MASTER_URI isn't defined"
		exit 1
	elif [ -z "$ROS_IP" ]; then
		echo "environment variable ROS_IP isn't defined"
		exit 1
	elif [ "$ROS_MASTER_URI" != "http://10.3.141.1:11311" ]; then
		echo "environment variable ROS_MASTER_URI is currently equal to ${ROS_MASTER_URI} but should be equal to http://10.3.141.1:11311"
		exit 1
	elif [ "$ROS_IP" != "10.3.141.1" ]; then
		echo "environment variable ROS_IP is currently equal to ${ROS_IP} but should be equal to 10.3.141.1"	
		exit 1
	fi
	echo "environment variables on MASTER are OK"
	checkEnvVarLidar
}

checkEnvVarLidar(){
	echo "checking environment variables on LIDAR :"
	LIDAR_ROS_MASTER_URI=$(ssh ubuntu@10.3.141.60 "echo $ROS_MASTER_URI")
	LIDAR_ROS_IP=$(ssh ubuntu@10.3.141.60 "echo $ROS_IP")
	if [ -z "$LIDAR_ROS_MASTER_URI" ]; then
		echo "environment variable ROS_MASTER_URI isn't defined"
		exit 1
	elif [ -z "$LIDAR_ROS_IP" ]; then
		echo "environment variable ROS_IP isn't defined"
		exit 1
	elif [ "$LIDAR_ROS_MASTER_URI" != "http://10.3.141.1:11311" ]; then
		echo "environment variable ROS_MASTER_URI is currently equal to ${LIDAR_ROS_MASTER_URI} but should be equal to http://10.3.141.1:11311"
		exit 1
	elif [ "$LIDAR_ROS_IP" != "10.3.141.60" ]; then
		echo "environment variable ROS_IP is currently equal to ${LIDAR_ROS_IP} but should be equal to 10.3.141.60"	
		exit 1
	fi
	echo "environment variables on LIDAR are OK"
	
}

checkWifi
