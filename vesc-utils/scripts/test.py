from cmath import sin
from tokenize import Double
import rospy
import math
from std_msgs.msg import Float64
import signal
terminateProgram = False
import logging

def mySigintHandler(signum, frame):
    rospy.loginfo("stoping on Sig %s"%signum)
    terminateProgram = True

def testServo():
    pub = rospy.Publisher('/vesc/commands/servo/position', Float64, queue_size=1)
    stepPerSecond = 50
    rate = rospy.Rate(stepPerSecond)
    loopCount = 0
    while not (rospy.is_shutdown() or  terminateProgram):
        position = Float64(math.sin(loopCount)*0.35 +0.5)
        rospy.loginfo("Positon set to %s", position)
        pub.publish(position)
        rate.sleep()
        loopCount=(loopCount+ (2* math.pi/stepPerSecond))%(2*math.pi)
if __name__ == '__main__':
    signal.signal(signal.SIGINT, mySigintHandler)
    rospy.init_node('testServov', anonymous=True, log_level=rospy.ERROR)
    testServo()
