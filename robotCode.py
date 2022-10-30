#Imports
import grovepi
import time
import brickpi3 

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division 

#Notes:
#Right side line following  (probably will change)

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
#Sensor & Motor Ports
driveLeft = BP.PORT_A
driveRight = BP.PORT_B
color_sensor = BP.PORT_1

def driveForward(speed):
    BP.set_motor_power(driveLeft + driveRight,  speed)

def driveBackward(speed):
    BP.set_motor_power(driveLeft + driveRight,  -speed)

def turnInPlaceRight(speed):
    BP.set_motor_power(driveLeft, speed)
    BP.set_motor_power(driveRight, -speed)
def turnInPlaceLeft(speed):
    BP.set_motor_power(driveRight, speed)
    BP.set_motor_power(driveLeft, -speed)
def arcTurnLeft(speed):
    BP.set_motor_power(driveLeft, p * speed)
    BP.set_motor_power(driveRight, speed)

def arcTurnRight(speed):
    BP.set_motor_power(driveLeft, speed)
    BP.set_motor_power(driveRight, p * speed)
#Determine whether accuracy is in acceptable range
def inRange(value, targetValue, bound):
    if(value < (targetValue + bound) and value > (targetValue - bound)):
        return 1
    return 0
#Line following path correction
def correctPath(lightValue, targetValue, speed):
    if(inRange(lightValue, targetValue, line_bound)):
        pass
    elif(lightValue > targetValue):
        while(not(inRange(lightValue, targetValue, line_bound))):
            arcTurnLeft(speed)
    elif(lightValue < targetValue):
        while(not(inRange(lightValue, targetValue, line_bound))):
            arcTurnRight(speed)

def addColorSensor(port):
    BP.set_sensor_type(port, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)


def readColorSensor():
    BP.get_sensor retrieves a sensor value.

#==========
#MAIN LOOP
#==========



#Error Bounds
line_bound = 2
#Control Gains
p = 0.8 

try:
    while True:
        



