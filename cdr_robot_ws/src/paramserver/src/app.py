#!/usr/bin/env python
import rospy 
from PID.msg import IntArr
from std_msgs.msg import Bool

def reality_callback(msg):
    global Error,parcoursTarget,nextstep
    Error+=parcoursTarget-msg.ticks
    if(msg.cycles==0):
        nextstep=True
    

if __name__ == '__main__':
    global parcours,nextstep
    nextstep = True
    parcours = [100,200,300,100,500]
    rospy.init_node("param")
    realitysub = rospy.Subscriber("/right/reality",IntArr,reality_callback)
    targetpub = rospy.Publisher("/right/target",IntArr,queue_size=1)
    resetpub = rospy.Publisher("/breakServo",Bool,queue_size=1)
    global Error,parcoursTarget
    Error=0
    newvalues = [1,0,0]
    while True:
        Error=0
        #newvalues = newPID()
        rospy.set_param('rpid', newvalues)
        #publish on motorbreak
        resetpub.publish(False)
        for i in range(len(parcours)):
            nextstep = False
            msg = IntArr()
            msg.cycles =100
            msg.ticks = parcours[i]
            targetpub.publish(msg)
            while(not nextstep):
                pass
        resetpub.publish(True)
        rospy.loginfo(Error)  
    #rospy.set_param('lpid', [int(1),int(0),int(0)])


def newPID():
    return [10,1,1]