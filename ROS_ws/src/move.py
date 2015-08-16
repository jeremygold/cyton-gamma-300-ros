#!/usr/bin/env python

import rospy
import std_msgs
import time

rospy.init_node('cyton_controller_manager', anonymous=True)
shoulder_roll = rospy.Publisher('/shoulder_roll_position_controller/command', std_msgs.msg.Float64, queue_size=10)
wrist_pitch = rospy.Publisher('/wrist_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)

for i in range (1,5):
	shoulder_roll.publish(-1.0)
	wrist_pitch.publish(-1.0)
	time.sleep(1)
	shoulder_roll.publish(1.0)
	wrist_pitch.publish(-0.5)
	time.sleep(1)


