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
wrist_pitch = rospy.Publisher('/wrist_pitch_position_controller/command', std_msgs.msg.Float64, queue_size=10)

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeShoulderRoll)
	sld.setSliderPosition(50)
        
        self.label = QtGui.QLabel(self)
        self.label.setText("Shoulder Roll")
        self.label.setGeometry(30, 20, 100, 30)

	sld2 = QtGui.QSlider(QtCore.Qt.Vertical, self)
        sld2.setFocusPolicy(QtCore.Qt.NoFocus)
        sld2.setGeometry(140, 40, 30, 100)
        sld2.valueChanged[int].connect(self.changeShoulderPitch)
	sld2.setSliderPosition(50)

	label2 = QtGui.QLabel(self)
	label2.setText("Shoulder Pitch")
        label2.setGeometry(140, 20, 100, 30)
        
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

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

