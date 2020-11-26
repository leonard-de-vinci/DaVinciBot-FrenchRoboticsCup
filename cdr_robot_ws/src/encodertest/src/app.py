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


def leftcallback(msg):
    global lcount, leftpub, ltarget, ddir
    lcount += msg.ticks


def rightcallback(msg):
    global rcount, rightpub, rtarget, ddir
    rcount += msg.ticks


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global rightpub, leftpub, lcount, rcount, ltarget, rtarget, ddir
    ddir = True
    lcount = 0
    rcount = 0
    rtarget = 0
    ltarget = 0
    rospy.init_node("tickviewer", anonymous=False)
    breakpub = rospy.Publisher("/breakServo", Bool, queue_size=1)
    rightpub = rospy.Publisher("/N1/target", speed, queue_size=1)
    leftpub = rospy.Publisher("/N2/target", speed, queue_size=1)
    leftsub = rospy.Subscriber("/N2/reality", speed, leftcallback)
    rightsub = rospy.Subscriber("/N1/reality", speed, rightcallback)
    print("waiting for full init")
    time.sleep(5)
    N = 1024
    msg = speed()
    msg.ticks = 0
    msg.dir = ddir
    rightpub.publish(msg)
    msg.ticks = 0
    leftpub.publish(msg)
    bmsg = Bool()

    bmsg.data = True
    breakpub.publish(bmsg)
    print("ON TEST BENCH")
    print("test for encoder connectivity")
    print("when ready press enter:")
    raw_input("...")
    msg.ticks = 30
    rightpub.publish(msg)
    msg.ticks = 30
    leftpub.publish(msg)
    bmsg = True
    breakpub.publish(bmsg)
    rtarget = 30
    ltarget = 30
    lcount = 0
    rcount = 0
    print("--------------------------------------------")
    print("please rotate the LEFT encoder 10 times:")
    print("in any direction")
    print("when finished press enter ...")
    raw_input("...")
    res = lcount/(N)
    print("rots = ", res)
    print("diff = ", lcount - (N*10))
    print("enter for next")
    raw_input("...")
    msg.ticks = 30
    rightpub.publish(msg)
    msg.ticks = 30
    leftpub.publish(msg)
    bmsg = True
    breakpub.publish(bmsg)
    rtarget = 30
    ltarget = 30
    lcount = 0
    rcount = 0
    print("--------------------------------------------")
    print("please rotate the RIGHT encoder 10 times:")
    print("in any direction")
    print("when finished press enter ...")
    raw_input("...")
    res = rcount/(N)
    print("rots = ", res)
    print("diff = ", rcount - (N*10))
    raw_input("...")
    msg.dir = False
    msg.ticks = 30
    rightpub.publish(msg)
    msg.ticks = 30
    leftpub.publish(msg)
    bmsg = True
    breakpub.publish(bmsg)
    rtarget = 30
    ltarget = 30
    lcount = 0
    rcount = 0
    print("--------------------------------------------")
    print("please rotate the LEFT encoder 10 times:")
    print("in any direction")
    print("when finished press enter ...")
    raw_input("...")
    res = lcount/(N)
    print("rots = ", res)
    print("diff = ", lcount - (N*10))
    print("enter for next")
    raw_input("...")
    msg.dir = False
    msg.ticks = 30
    rightpub.publish(msg)
    msg.ticks = 30
    leftpub.publish(msg)
    bmsg = True
    breakpub.publish(bmsg)
    rtarget = 30
    ltarget = 30
    lcount = 0
    rcount = 0
    print("--------------------------------------------")
    print("please rotate the RIGHT encoder 10 times:")
    print("in any direction")
    print("when finished press enter ...")
    raw_input("...")
    res = rcount/(N)
    print("rots = ", res)
    print("diff = ", rcount - (N*10))
    raw_input("...")
    print("                                                            __......_ ")
    print("                             .---.       _________    _.---`.-----_.'| ")
    print("                            ;     `.   (_   (_  _('\.' .--``   _.'   | ")
    print("                            `._//_.'    |   |   |   |.'     .-`     .' ")
    print("                  ,-. ,-.     //  (| _.' _.'_..-`   |..___.'        | ")
    print("         _       (O)_(O)_)_  //    ;(..(..(        .'     |        .' ")
    print("      ,-'"'--------` -| |-.\//     :|     |       /     \'=|        | "')
    print("    ,'|`.            `---` \\      |/___ /_......'        '-.....-`/ ")
    print("    |I|II\________ .---.____|| __..'    /       |        /   ____  | ")
    print("  .'|I|II|        `----._`-.  `-..____.'        |____...`.-``    ```-.. ")
    print(" /  |I|II|   .-````````-.`-.`.                         .'' .-``````-. ``. ")
    print(".  /`.|II|  ' .-``````-. `  \ `.                      / / / \\ || // \ \ \ ")
    print("' .---.`.| / / \\ || // \ \  \  \--------------------; : .   \\||//   . : \ ")
    print("; '   //  : .   \\||//   . :  \  \__________________:  | :----````----; ' | ")
    print(" \ './/   . :----````----; '   | |==================|  ; ;----.__,----: : \ ")
    print("  `. `-...' ;----.__,----: :`--|_| .-. \ '.// || \\.'-.| '   //||\\   ' ;-` ")
    print("    `-....; '   //||\\   ' ;            `. `-....-` .'  \ '.// || \\.' / ")
    print("   LGB     \ '.// || \\.' /  .-.          `-......-' _.-.`. `-....-` .' ")
    print("       .-._ `. `-....-` .'  1904 Buick    .-.              `-......-'  -. ")
    print("   .-._       `-......-'    .-._                   _.-.        .-._ ")
