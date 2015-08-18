#!/usr/bin/env python 

import sys
from PyQt4 import QtGui, QtCore
import rospy
import std_msgs
import time

rospy.init_node('cyton_controller_manager', anonymous=True)
shoulder_roll = rospy.Publisher('/shoulder_roll_position_controller/command', std_msgs.msg.Float64, queue_size=10)
shoulder_yaw = rospy.Publisher('/shoulder_yaw_position_controller/command', std_msgs.msg.Float64, queue_size=10)
shoulder_pitch = rospy.Publisher('/shoulder_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)
elbow_yaw = rospy.Publisher('/elbow_yaw_position_controller/command', std_msgs.msg.Float64, queue_size=10)
elbow_pitch = rospy.Publisher('/elbow_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)

wrist_pitch = rospy.Publisher('/wrist_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        shoulderRollSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        shoulderRollSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        shoulderRollSlider.setGeometry(30, 40, 100, 30)
        shoulderRollSlider.valueChanged[int].connect(self.changeShoulderRoll)
	shoulderRollSlider.setSliderPosition(50)
        
        shoulderRollLabel = QtGui.QLabel(self)
        shoulderRollLabel.setText("Shoulder Roll")
        shoulderRollLabel.setGeometry(30, 20, 100, 30)

	shoulderPitchSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        shoulderPitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        shoulderPitchSlider.setGeometry(140, 40, 30, 100)
        shoulderPitchSlider.valueChanged[int].connect(self.changeShoulderPitch)
	shoulderPitchSlider.setSliderPosition(50)

	shoulderPitchLabel = QtGui.QLabel(self)
	shoulderPitchLabel.setText("Shoulder Pitch")
        shoulderPitchLabel.setGeometry(140, 20, 100, 30)
        
        elbowYawSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        elbowYawSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        elbowYawSlider.setGeometry(250, 40, 30, 100)
        elbowYawSlider.valueChanged[int].connect(self.changeElbowYaw)
	elbowYawSlider.setSliderPosition(50)
        
        elbowYawLabel = QtGui.QLabel(self)
        elbowYawLabel.setText("Elbow Yaw")
        elbowYawLabel.setGeometry(360, 20, 100, 30)

        elbowPitchSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        elbowPitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        elbowPitchSlider.setGeometry(360, 40, 30, 100)
        elbowPitchSlider.valueChanged[int].connect(self.changeElbowPitch)
	elbowPitchSlider.setSliderPosition(50)
        
        elbowPitchLabel = QtGui.QLabel(self)
        elbowPitchLabel.setText("Elbow Pitch")
        elbowPitchLabel.setGeometry(250, 20, 100, 30)

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Cyton Gamma 300 Control')
        self.show()
        
    def changeShoulderRoll(self, value):
	shoulderRollMin = -1.0
	shoulderRollMax = 1.0
	shoulderRollDelta = shoulderRollMax - shoulderRollMin
	pos = (float(value) / 100.0) * shoulderRollDelta + shoulderRollMin
	print 'Shoulder roll {0}'.format(pos)
	shoulder_roll.publish(pos)
        
    def changeShoulderPitch(self, value):
	shoulderPitchMin = -2.0
	shoulderPitchMax = 0.0
	shoulderPitchDelta = shoulderPitchMax - shoulderPitchMin
	pos = (float(value) / 100.0) * shoulderPitchDelta + shoulderPitchMin
	print 'Shoulder pitch {0}'.format(pos)
	shoulder_pitch.publish(pos)

    def changeElbowYaw(self, value):
	elbowYawMin = -2.0
	elbowYawMax = 0.0
	elbowYawDelta = elbowYawMax - elbowYawMin
	pos = (float(value) / 100.0) * elbowYawDelta + elbowYawMin
	print 'Elbow yaw {0}'.format(pos)
	elbow_yaw.publish(pos)

    def changeElbowPitch(self, value):
	elbowPitchMin = -2.0
	elbowPitchMax = 0.0
	elbowPitchDelta = elbowPitchMax - elbowPitchMin
	pos = (float(value) / 100.0) * elbowPitchDelta + elbowPitchMin
	print 'Elbow pitch {0}'.format(pos)
	elbow_pitch.publish(pos)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

