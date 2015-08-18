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
wrist_roll = rospy.Publisher('/wrist_roll_position_controller/command', std_msgs.msg.Float64, queue_size=10)

gripper_position = rospy.Publisher('/gripper_position_controller/command', std_msgs.msg.Float64, queue_size=10)

sliderHeight = 300

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        shoulderLabel = QtGui.QLabel(self)
        shoulderLabel.setText("Shoulder")
        shoulderLabel.setGeometry(90, 5, 100, 30)

        shoulderRollSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        shoulderRollSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        shoulderRollSlider.setGeometry(30, 40, 30, sliderHeight)
        shoulderRollSlider.valueChanged[int].connect(self.changeShoulderRoll)
	shoulderRollSlider.setSliderPosition(50)
        
        shoulderRollLabel = QtGui.QLabel(self)
        shoulderRollLabel.setText("Roll")
        shoulderRollLabel.setGeometry(30, 20, 100, 30)

	shoulderPitchSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        shoulderPitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        shoulderPitchSlider.setGeometry(100, 40, 30, sliderHeight)
        shoulderPitchSlider.valueChanged[int].connect(self.changeShoulderPitch)
	shoulderPitchSlider.setSliderPosition(50)

	shoulderPitchLabel = QtGui.QLabel(self)
	shoulderPitchLabel.setText("Pitch")
        shoulderPitchLabel.setGeometry(100, 20, 100, 30)
        
        shoulderYawSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        shoulderYawSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        shoulderYawSlider.setGeometry(170, 40, 30, sliderHeight)
        shoulderYawSlider.valueChanged[int].connect(self.changeShoulderYaw)
	shoulderYawSlider.setSliderPosition(50)
        
        shoulderYawLabel = QtGui.QLabel(self)
        shoulderYawLabel.setText("Yaw")
        shoulderYawLabel.setGeometry(170, 20, 100, 30)

        elbowPitchSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        elbowPitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        elbowPitchSlider.setGeometry(240, 40, 30, sliderHeight)
        elbowPitchSlider.valueChanged[int].connect(self.changeElbowPitch)
	elbowPitchSlider.setSliderPosition(50)
        
        elbowLabel = QtGui.QLabel(self)
        elbowLabel.setText("Elbow")
        elbowLabel.setGeometry(270, 5, 100, 30)

        elbowPitchLabel = QtGui.QLabel(self)
        elbowPitchLabel.setText("Pitch")
        elbowPitchLabel.setGeometry(240, 20, 100, 30)

        elbowYawSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        elbowYawSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        elbowYawSlider.setGeometry(310, 40, 30, sliderHeight)
        elbowYawSlider.valueChanged[int].connect(self.changeElbowYaw)
	elbowYawSlider.setSliderPosition(50)
        
        elbowYawLabel = QtGui.QLabel(self)
        elbowYawLabel.setText("Yaw")
        elbowYawLabel.setGeometry(310, 20, 100, 30)

        wristPitchSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        wristPitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        wristPitchSlider.setGeometry(380, 40, 30, sliderHeight)
        wristPitchSlider.valueChanged[int].connect(self.changeWristPitch)
	wristPitchSlider.setSliderPosition(50)
        
        wristLabel = QtGui.QLabel(self)
        wristLabel.setText("Wrist")
        wristLabel.setGeometry(420, 5, 100, 30)

        wristPitchLabel = QtGui.QLabel(self)
        wristPitchLabel.setText("Pitch")
        wristPitchLabel.setGeometry(380, 20, 100, 30)

        wristRollSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        wristRollSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        wristRollSlider.setGeometry(450, 40, 30, sliderHeight)
        wristRollSlider.valueChanged[int].connect(self.changeWristRoll)
	wristRollSlider.setSliderPosition(50)
        
        wristRollLabel = QtGui.QLabel(self)
        wristRollLabel.setText("Roll")
        wristRollLabel.setGeometry(450, 20, 100, 30)

        gripPosSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        gripPosSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        gripPosSlider.setGeometry(520, 40, 30, sliderHeight)
        gripPosSlider.valueChanged[int].connect(self.changeGripPos)
	gripPosSlider.setSliderPosition(50)
        
        gripPosLabel = QtGui.QLabel(self)
        gripPosLabel.setText("Grip Pos")
        gripPosLabel.setGeometry(520, 20, 100, 30)

        self.setGeometry(300, 300, 740, 480)
        self.setWindowTitle('Cyton Gamma 300 Control')
        self.show()
        
    def changeShoulderRoll(self, value):
	shoulderRollMin = -3.8
	shoulderRollMax = 1.5
	shoulderRollDelta = shoulderRollMax - shoulderRollMin
	pos = (float(value) / 100.0) * shoulderRollDelta + shoulderRollMin
	print 'Shoulder roll {0}'.format(pos)
	shoulder_roll.publish(pos)
        
    def changeShoulderPitch(self, value):
	shoulderPitchMin = -3.0
	shoulderPitchMax = 0.6
	shoulderPitchDelta = shoulderPitchMax - shoulderPitchMin
	pos = (float(value) / 100.0) * shoulderPitchDelta + shoulderPitchMin
	print 'Shoulder pitch {0}'.format(pos)
	shoulder_pitch.publish(pos)

    def changeShoulderYaw(self, value):
	shoulderYawMin = -3.0
	shoulderYawMax = 1.5
	shoulderYawDelta = shoulderYawMax - shoulderYawMin
	pos = (float(value) / 100.0) * shoulderYawDelta + shoulderYawMin
	print 'Shoulder yaw {0}'.format(pos)
	shoulder_yaw.publish(pos)

    def changeElbowPitch(self, value):
	elbowPitchMin = -3.0
	elbowPitchMax = 0.6
	elbowPitchDelta = elbowPitchMax - elbowPitchMin
	pos = (float(value) / 100.0) * elbowPitchDelta + elbowPitchMin
	print 'Elbow pitch {0}'.format(pos)
	elbow_pitch.publish(pos)

    def changeElbowYaw(self, value):
	elbowYawMin = -3.0
	elbowYawMax = 0.6
	elbowYawDelta = elbowYawMax - elbowYawMin
	pos = (float(value) / 100.0) * elbowYawDelta + elbowYawMin
	print 'Elbow yaw {0}'.format(pos)
	elbow_yaw.publish(pos)

    def changeWristPitch(self, value):
	wristPitchMin = -3.0
	wristPitchMax = 0.6
	wristPitchDelta = wristPitchMax - wristPitchMin
	pos = (float(value) / 100.0) * wristPitchDelta + wristPitchMin
	print 'Wrist pitch {0}'.format(pos)
	wrist_pitch.publish(pos)

    def changeWristRoll(self, value):
	wristRollMin = -3.0
	wristRollMax = 1.5
	wristRollDelta = wristRollMax - wristRollMin
	pos = (float(value) / 100.0) * wristRollDelta + wristRollMin
	print 'Wrist roll {0}'.format(pos)
	wrist_roll.publish(pos)

    def changeGripPos(self, value):
	gripPosMin = -20.0
	gripPosMax = -10.0
	gripPosDelta = gripPosMax - gripPosMin
	pos = (float(value) / 100.0) * gripPosDelta + gripPosMin
	print 'Grip pos {0}'.format(pos)
	gripper_position.publish(pos)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

