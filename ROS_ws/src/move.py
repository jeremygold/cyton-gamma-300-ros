#!/usr/bin/env python

import rospy
import std_msgs
import time

rospy.init_node('cyton_controller_manager', anonymous=True)
shoulder_roll = rospy.Publisher('/shoulder_roll_position_controller/command', std_msgs.msg.Float64, queue_size=10)
shoulder_yaw = rospy.Publisher('/shoulder_yaw_position_controller/command', std_msgs.msg.Float64, queue_size=10)
shoulder_pitch = rospy.Publisher('/shoulder_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)
wrist_pitch = rospy.Publisher('/wrist_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)
# gripper_position = rospy.Publisher('/gripper_position_controller/command', std_msgs.msg.Float64, queue_size=10)

 # * /wrist_pitch_position_controller/command [unknown type]
 # * /elbow_yaw_position_controller/command [unknown type]
 # * /cyton_joint_trajectory_action_controller/follow_joint_trajectory/cancel [unknown type]
 # * /elbow_pitch_position_controller/command [unknown type]
 # * /wrist_roll_position_controller/command [unknown type]
 # * /shoulder_pitch_position_controller/command [unknown type]
 # * /shoulder_yaw_position_controller/command [unknown type]
 # * /shoulder_roll_position_controller/command [unknown type]
 # * /cyton_joint_trajectory_action_controller/command [unknown type]
 # * /gripper_position_controller/command [unknown type]

for i in range (1,4):
	shoulder_roll.publish(-1.0)
	# shoulder_yaw.publish(-0.3)
	shoulder_pitch.publish(-1.1)
	wrist_pitch.publish(-1.0)

	# gripper_position.publish(15.0)
	time.sleep(1)

	shoulder_roll.publish(1.0)
	# shoulder_yaw.publish(0.3)
	shoulder_pitch.publish(-1.3)
	wrist_pitch.publish(-0.5)
	# gripper_position.publish(10.0)
	time.sleep(1)



