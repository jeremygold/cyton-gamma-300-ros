#!/usr/bin/env python 

import sys
from PyQt4 import QtGui, QtCore
from Robot import Robot

sliderHeight = 300

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()

        self.robot = Robot()
        self.initUI()

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
        self.makeControlSlider(30, "Roll", self.robot.shoulderRollMotor)
        self.makeControlSlider(100, "Pitch", self.robot.shoulderPitchMotor)
        self.makeControlSlider(170, "Yaw", self.robot.shoulderYawMotor)

        self.makeControlTitle(270, "Elbow")
        self.makeControlSlider(240, "Pitch", self.robot.elbowPitchMotor)
        self.makeControlSlider(310, "Yaw", self.robot.elbowYawMotor)

        self.makeControlTitle(420, "Wrist")
        self.makeControlSlider(380, "Pitch", self.robot.wristPitchMotor)
        self.makeControlSlider(450, "Roll", self.robot.wristRollMotor)

        self.makeControlSlider(520, "Grip", self.robot.gripperMotor)

        savePosButton = QtGui.QPushButton(self)
        savePosButton.setText("Save pos")
        savePosButton.setGeometry(380, sliderHeight + 40, 100, 30)
        savePosButton.clicked.connect(self.robot.savePos)

        loadPosButton = QtGui.QPushButton(self)
        loadPosButton.setText("Load pos")
        loadPosButton.setGeometry(500, sliderHeight + 40, 100, 30)
        loadPosButton.clicked.connect(self.robot.loadPos)

        self.setGeometry(300, 300, 740, 480)
        self.setWindowTitle('Cyton Gamma 300 Control')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

