#!/usr/bin/env python 

import sys
from PyQt4 import QtGui, QtCore
import rospy
import std_msgs
import time
from dynamixel_msgs.msg import JointState
from Motor import Motor

sliderHeight = 300

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()

        self.initRospy()
        self.initUI()

    def initRospy(self):
        rospy.init_node('cyton_controller_manager', anonymous=True)

        self.shoulderRollMotor = Motor("Shoulder Roll", "shoulder_roll_position_controller", -3.8, 1.5)
        self.shoulderPitchMotor = Motor("Shoulder Pitch", "shoulder_pitch_position_controller", -3.0, 0.6)
        self.shoulderYawMotor = Motor("Shoulder Yaw", "shoulder_yaw_position_controller", -3.0, 1.5)
        self.elbowYawMotor = Motor("Elbow Yaw", "elbow_yaw_position_controller", -3.0, 0.6)

        self.elbow_pitch = rospy.Publisher('/elbow_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)
        rospy.Subscriber('/elbow_pitch_position_controller/state', JointState, self.onElbowPitch)

        self.wrist_pitch = rospy.Publisher('/wrist_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)
        rospy.Subscriber('/wrist_pitch_position_controller/state', JointState, self.onWristPitch)

        self.wrist_roll = rospy.Publisher('/wrist_roll_position_controller/command', std_msgs.msg.Float64, queue_size=10)
        rospy.Subscriber('/wrist_roll_position_controller/state', JointState, self.onWristRoll)

        self.gripper_position = rospy.Publisher('/gripper_position_controller/command', std_msgs.msg.Float64, queue_size=10)
        # TODO: Where is gripper state?

    def onElbowPitch(self, data):
        self.elbowPitchPos = float(data.current_pos)

    def onWristPitch(self, data):
        self.wristPitchPos = float(data.current_pos)

    def onWristRoll(self, data):
        self.wristRollPos = float(data.current_pos)

    def makeControlSlider(self, x, name, motor):
        newSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        newSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        newSlider.setGeometry(x, 40, 30, sliderHeight)
        newSlider.valueChanged[int].connect(motor.setPercentPos)
	newSlider.setSliderPosition(50)
        motor.setSlider(newSlider)
        
        newLabel = QtGui.QLabel(self)
        newLabel.setText(name)
        newLabel.setGeometry(x, 20, 100, 30)

    def initUI(self):      
        shoulderLabel = QtGui.QLabel(self)
        shoulderLabel.setText("Shoulder")
        shoulderLabel.setGeometry(90, 5, 100, 30)

        self.makeControlSlider(30, "Roll", self.shoulderRollMotor)
        self.makeControlSlider(100, "Pitch", self.shoulderPitchMotor)
        self.makeControlSlider(170, "Yaw", self.shoulderYawMotor)

        elbowLabel = QtGui.QLabel(self)
        elbowLabel.setText("Elbow")
        elbowLabel.setGeometry(270, 5, 100, 30)
        self.makeControlSlider(310, "Yaw", self.elbowYawMotor)
        
        elbowPitchSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        elbowPitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        elbowPitchSlider.setGeometry(240, 40, 30, sliderHeight)
        elbowPitchSlider.valueChanged[int].connect(self.changeElbowPitch)
	elbowPitchSlider.setSliderPosition(50)
        
        elbowPitchLabel = QtGui.QLabel(self)
        elbowPitchLabel.setText("Pitch")
        elbowPitchLabel.setGeometry(240, 20, 100, 30)

        wristLabel = QtGui.QLabel(self)
        wristLabel.setText("Wrist")
        wristLabel.setGeometry(420, 5, 100, 30)

        wristPitchSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        wristPitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        wristPitchSlider.setGeometry(380, 40, 30, sliderHeight)
        wristPitchSlider.valueChanged[int].connect(self.changeWristPitch)
	wristPitchSlider.setSliderPosition(50)

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

        savePosButton = QtGui.QPushButton(self)
        savePosButton.setText("Save pos")
        savePosButton.setGeometry(380, sliderHeight + 40, 100, 30)
        savePosButton.clicked.connect(self.savePos)

        loadPosButton = QtGui.QPushButton(self)
        loadPosButton.setText("Load pos")
        loadPosButton.setGeometry(500, sliderHeight + 40, 100, 30)
        loadPosButton.clicked.connect(self.loadPos)

        self.setGeometry(300, 300, 740, 480)
        self.setWindowTitle('Cyton Gamma 300 Control')
        self.show()
        


    def changeElbowPitch(self, value):
	elbowPitchMin = -3.0
	elbowPitchMax = 0.6
	elbowPitchDelta = elbowPitchMax - elbowPitchMin
	pos = (float(value) / 100.0) * elbowPitchDelta + elbowPitchMin
	print 'Elbow pitch {0}'.format(pos)
	self.elbow_pitch.publish(pos)


    def changeWristPitch(self, value):
	wristPitchMin = -3.0
	wristPitchMax = 0.6
	wristPitchDelta = wristPitchMax - wristPitchMin
	pos = (float(value) / 100.0) * wristPitchDelta + wristPitchMin
	print 'Wrist pitch {0}'.format(pos)
	self.wrist_pitch.publish(pos)

    def changeWristRoll(self, value):
	wristRollMin = -3.0
	wristRollMax = 1.5
	wristRollDelta = wristRollMax - wristRollMin
	pos = (float(value) / 100.0) * wristRollDelta + wristRollMin
	print 'Wrist roll {0}'.format(pos)
	self.wrist_roll.publish(pos)

    def changeGripPos(self, value):
	gripPosMin = -20.0
	gripPosMax = -10.0
	gripPosDelta = gripPosMax - gripPosMin
	pos = (float(value) / 100.0) * gripPosDelta + gripPosMin
	print 'Grip pos {0}'.format(pos)
	self.gripper_position.publish(pos)

    def savePos(self):
        text_file = open("SavePos.csv", "a")
        text_file.write("{0},{1},{2},{3},{4},{5},{6}\n".format(
            self.shoulderRollMotor.getMotorState(), \
            self.shoulderYawMotor.getMotorState(), \
            self.shoulderPitchMotor.getMotorState(), \
            self.elbowYawMotor.getMotorState(), \
            self.elbowPitchPos, \
            self.wristPitchPos, \
            self.wristRollPos))
        text_file.close()
        print "Saved..."

    def loadPos(self):
        text_file = open("SavePos.csv", "r")
        lines = text_file.readlines()
        text_file.close()

        for line in lines:
            print "Loading position: {0}".format(line)
            positions = line.split(',')
            self.shoulderRollMotor.setRawPos(float(positions[0]))
            self.shoulderYawMotor.setRawPos(float(positions[1]))
            self.shoulderPitchMotor.setRawPos(float(positions[2]))
            self.elbowYawMotor.setRawPos(float(positions[3]))
            self.elbow_pitch.publish(float(positions[4]))
            self.wrist_pitch.publish(float(positions[5]))
            self.wrist_roll.publish(float(positions[6]))
            for i in range(1,20):
                QtGui.QApplication.processEvents()
                time.sleep(0.1)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

