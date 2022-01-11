#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
import random

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
rand_int = random.randrange(0, 5, 1)

if rand_int == 0:
    ev3.speaker.play_file('are you happy guys.wav')

elif rand_int == 1:
    ev3.speaker.play_file('can you turn me off.wav')

elif rand_int == 2:
    ev3.speaker.play_file('hope you are having fun.wav')

elif rand_int == 3:
    ev3.speaker.play_file('you are asking too much.wav')

elif rand_int == 4:
    ev3.speaker.play_file("i'm hungry.wav")
