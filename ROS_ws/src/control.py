#!/usr/bin/env python 

import sys
from PyQt4 import QtGui, QtCore
import rospy
import time
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
        self.elbowPitchMotor = Motor("Elbow Pitch", "elbow_pitch_position_controller", -3.0, 0.6)
        self.wristPitchMotor = Motor("Wrist Pitch", "wrist_pitch_position_controller", -3.0, 0.6)
        self.wristRollMotor = Motor("Wrist Roll", "wrist_roll_position_controller", -3.0, 1.5)
        self.gripperMotor = Motor("Gripper", "gripper_position_controller", -20.0, 10.0)

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

    def makeControlTitle(self, x, name):
        newLabel = QtGui.QLabel(self)
        newLabel.setText(name)
        newLabel.setGeometry(x, 5, 100, 30)

    def initUI(self):      
        self.makeControlTitle(90, "Shoulder")
        self.makeControlSlider(30, "Roll", self.shoulderRollMotor)
        self.makeControlSlider(100, "Pitch", self.shoulderPitchMotor)
        self.makeControlSlider(170, "Yaw", self.shoulderYawMotor)

        self.makeControlTitle(270, "Elbow")
        self.makeControlSlider(240, "Pitch", self.elbowPitchMotor)
        self.makeControlSlider(310, "Yaw", self.elbowYawMotor)

        self.makeControlTitle(420, "Wrist")
        self.makeControlSlider(380, "Pitch", self.wristPitchMotor)
        self.makeControlSlider(450, "Roll", self.wristRollMotor)

        self.makeControlSlider(520, "Grip", self.gripperMotor)

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

    def savePos(self):
        text_file = open("SavePos.csv", "a")
        text_file.write("{0},{1},{2},{3},{4},{5},{6}\n".format(
            self.shoulderRollMotor.getMotorState(), \
            self.shoulderYawMotor.getMotorState(), \
            self.shoulderPitchMotor.getMotorState(), \
            self.elbowYawMotor.getMotorState(), \
            self.elbowPitchMotor.getMotorState(), \
            self.wristPitchMotor.getMotorState(), \
            self.wristRollMotor.getMotorState()))
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
            self.elbowPitchMotor.setRawPos(float(positions[4]))
            self.wristPitchMotor.setRawPos(float(positions[5]))
            self.wristRollMotor.setRawPos(float(positions[6]))
            for i in range(1,20):
                QtGui.QApplication.processEvents()
                time.sleep(0.1)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

