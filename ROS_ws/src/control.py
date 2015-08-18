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
        sld.valueChanged[int].connect(self.changeValue)
        
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QtGui.QSlider')
        self.show()
        
    def changeValue(self, value):
	pos = (float(value) / 100.0) * 2.0 - 1.0
	shoulder_roll.publish(pos)
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

