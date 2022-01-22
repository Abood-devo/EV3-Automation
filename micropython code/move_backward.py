#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.robotics import DriveBase

# Create your objects here.
ev3 = EV3Brick()
left_wheel = Motor(Port.B)
right_wheel = Motor(Port.C)
robot = DriveBase(left_wheel, right_wheel, wheel_diameter=56, axle_track=104)
gyro = GyroSensor(Port.S1)

# Write your program here.
while robot.distance() > -100:
    robot.drive(-500, 0)
robot.stop()
left_wheel.brake()
right_wheel.brake()
ev3.speaker.play_file('done.wav')
