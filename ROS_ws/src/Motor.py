import rospy
import std_msgs
from dynamixel_msgs.msg import JointState

class Motor:
    def __init__(self, name, nodeName, min, max):
        self.name = name
        self.min = min
        self.max = max
        self.posDelta = self.max - self.min
        self.publisher = rospy.Publisher("/{}/command".format(nodeName), std_msgs.msg.Float64, queue_size=10)
        rospy.Subscriber("/{}/state".format(nodeName), JointState, self.onMotorState)

    def percentToRaw(self, percentPos):
        rawPos = (float(percentPos) / 100.0) * self.posDelta + self.min
        return rawPos

    def rawToPercent(self, rawPos):
        percentPos = int(100.0 * (rawPos - self.min) / self.posDelta)
        return percentPos

    def setPercentPos(self, percentPos):
        rawPos = self.percentToRaw(percentPos)
        print '{}: {} ({}%)'.format(self.name, rawPos, percentPos)
        self.publisher.publish(rawPos)

    def setRawPos(self, rawPos):
        percentPos = self.rawToPercent(rawPos)
        print '{}: {} ({}%)'.format(self.name, rawPos, percentPos)
        self.slider.setSliderPosition(percentPos)
        self.publisher.publish(rawPos)

    def onMotorState(self, data):
        self.motorState = float(data.current_pos)

    def getMotorState(self):
        return self.motorState

    def setSlider(self, slider):
        self.slider = slider
