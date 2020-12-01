#!/usr/bin/env python
import rospy 
import time
from PID.msg import speed
from bot_coordinates.msg import Coordinates
from PID.msg import FloatArr
from std_msgs.msg import Bool
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global rightpub, leftpub
    rospy.init_node("tster", anonymous=False)
    breakpub = rospy.Publisher("/breakServo", Bool, queue_size=1)
    rightpub = rospy.Publisher("/N1/target", speed, queue_size=2)
    leftpub = rospy.Publisher("/N2/target", speed, queue_size=2)
    print("waiting for full init")
    time.sleep(5)
    msg = speed()
    msg.dir = True
    msg.ticks = 0
    rightpub.publish(msg)
    msg.ticks = 0
    leftpub.publish(msg)
    bmsg = Bool()
    bmsg.data = True
    breakpub.publish(bmsg)
    print("ON TEST BENCH")
    print("test for motor connectivity")
    print("when ready press enter:")
    raw_input("...")
    msg.dir = True
    msg.ticks = 30
    rightpub.publish(msg)
    time.sleep(0.2)
    msg.ticks = 0
    leftpub.publish(msg)
    bmsg = False
    breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT FORWARD")
    print("LEFT 0")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    msg.ticks = 0
    rightpub.publish(msg)
    time.sleep(0.2)
    msg.ticks = 30
    leftpub.publish(msg)
    # bmsg = False
    # breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT 0")
    print("LEFT FORWARD")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    msg.ticks = 0
    rightpub.publish(msg)
    time.sleep(0.2)
    msg.dir = False
    msg.ticks = 30
    leftpub.publish(msg)
    # bmsg = False
    # breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT 0")
    print("LEFT BACKWARDS")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    msg.dir = False
    msg.ticks = -30
    rightpub.publish(msg)
    time.sleep(0.2)
    msg.ticks = 0
    leftpub.publish(msg)
    # bmsg = False
    # breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT BACKWARDS")
    print("LEFT 0")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    msg.ticks = 0
    rightpub.publish(msg)
    time.sleep(0.2)
    leftpub.publish(msg)
    # bmsg = False
    # breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT 0")
    print("LEFT 0")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    msg.dir = False
    msg.ticks = 30
    rightpub.publish(msg)
    time.sleep(0.2)
    leftpub.publish(msg)
    # bmsg = False
    # breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT BACKWARDS")
    print("LEFT BACKWARDS")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    msg.dir = True
    msg.ticks = 30
    rightpub.publish(msg)
    time.sleep(0.2)
    leftpub.publish(msg)
    # bmsg = False
    # breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT FORWARD")
    print("LEFT FORWARD")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    msg.ticks = 30
    rightpub.publish(msg)
    time.sleep(0.2)
    leftpub.publish(msg)
    bmsg = True
    breakpub.publish(bmsg)
    print("--------------------------------------------")
    print("RIGHT BREAK")
    print("LEFT BREAK")
    print("if directions do not match please fix motor connectivity")
    print("when ready press enter")
    raw_input("...")
    print("                                         |")
    print("                                         |")
    print("                                         |")
    print("                                         |")
    print("   _______                   ________    |")
    print("  |ooooooo|      ____       | __  __ |   |")
    print("  |[]+++[]|     [____]      |/  \/  \|   |")
    print("  |+ ___ +|     ]()()[      |\__/\__/|   |")
    print("  |:|   |:|   ___\__/___    |[][][][]|   |")
    print("  |:|___|:|  |__|    |__|   |++++++++|   |")
    print("  |[]===[]|   |_|_/\_|_|    | ______ |   |")
    print("_ ||||||||| _ | | __ | | __ ||______|| __|")
    print("  |_______|   |_|[::]|_|    |________|   \\")
    print("              \_|_||_|_/               jro\\")
    print("                |_||_|                     \\")
    print("               _|_||_|_                     \\")
    print("      ____    |___||___|                     \\")
    print("     /  __\          ____                     \\")
    print("     \( oo          (___ \                     \\")
    print("     _\_o/           oo~)/")
    print("    / \|/ \         _\-_/_")
    print("   / / __\ \___    / \|/  \\")
    print("   \ \|   |__/_)  / / .- \ \\")
    print("    \/_)  |       \ \ .  /_/")
    print("     ||___|        \/___(_/")
    print("     | | |          | |  |")
    print("     | | |          | |  |")
    print("     |_|_|          |_|__|")
    print("     [__)_)        (_(___] ")
