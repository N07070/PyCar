# The code for the Raspberry Pi - powered car.
# Copyright (C) 2015  N07070
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import readchar
import RPi.GPIO as gpio
import time

def get_key_stroke():
    return readchar.readkey()

def initiate_motors():
    gpio.setmode(gpio.BOARD)

    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def go_strait():
    # Make all the motors go foward.
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)


def go_back():
    #Make all the motors go backwards.
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

def go_left():
    # Make all the right motors go forward.
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)

def go_right():
    # Make all the left motors go forward.
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

def stop():
    gpio.cleanup()

while True:
    key = get_key_stroke()
    initiate_motors()
    if key == "z":
        print("Go strait !")
    elif key == "s":
        print("Go back !")
    elif key == "q":
        print("Go left")
    elif key == "d":
        print("Go right")
    elif key == "p": # Always add a way to break, cause CRTL-C doesn't work...
        stop()
        break
    else:
        prin("Won't do anything to type this.")
