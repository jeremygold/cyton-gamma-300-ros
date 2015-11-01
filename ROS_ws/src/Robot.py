import rospy
from Motor import Motor
from PyQt4 import QtGui
import time

class Robot:
    def __init__(self):
        self.initRospy()

    def initRospy(self):
        rospy.init_node('cyton_controller_manager', anonymous=True)

        self.shoulderRollMotor = Motor("Shoulder Roll", "shoulder_roll_position_controller", -3.8, 1.5)
        self.shoulderPitchMotor = Motor("Shoulder Pitch", "shoulder_pitch_position_controller", -3.0, 0.6)
        self.shoulderYawMotor = Motor("Shoulder Yaw", "shoulder_yaw_position_controller", -3.0, 1.5)
        self.elbowYawMotor = Motor("Elbow Yaw", "elbow_yaw_position_controller", -3.0, 0.6)
        self.elbowPitchMotor = Motor("Elbow Pitch", "elbow_pitch_position_controller", -3.0, 0.6)
        self.wristPitchMotor = Motor("Wrist Pitch", "wrist_pitch_position_controller", -3.0, 0.6)
        self.wristRollMotor = Motor("Wrist Roll", "wrist_roll_position_controller", -3.0, 1.5)
        self.gripperMotor = Motor("Gripper", "gripper_position_controller", -2.5, 0.0)

    def savePos(self):
        text_file = open("SavePos.csv", "a")
        text_file.write("{0},{1},{2},{3},{4},{5},{6}\n".format(
            self.shoulderRollMotor.getMotorState(), \
            self.shoulderPitchMotor.getMotorState(), \
            self.shoulderYawMotor.getMotorState(), \
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
            self.shoulderPitchMotor.setRawPos(float(positions[1]))
            self.shoulderYawMotor.setRawPos(float(positions[2]))
            self.elbowYawMotor.setRawPos(float(positions[3]))
            self.elbowPitchMotor.setRawPos(float(positions[4]))
            self.wristPitchMotor.setRawPos(float(positions[5]))
            self.wristRollMotor.setRawPos(float(positions[6]))
            for i in range(1,5):
                QtGui.QApplication.processEvents()
                time.sleep(0.1)

    def resetPos(self):
        self.shoulderRollMotor.setPercentPos(50)
        self.shoulderPitchMotor.setPercentPos(50)
        self.shoulderYawMotor.setPercentPos(50)
        self.elbowYawMotor.setPercentPos(50)
        self.elbowPitchMotor.setPercentPos(50)
        self.wristPitchMotor.setPercentPos(50)
        self.wristRollMotor.setPercentPos(50)

