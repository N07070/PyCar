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

import RPi.GPIO as gpio
import time

time.sleep(1.4)
gpio.cleanup()


class Motors(object):
    """docstring for Motors"""

    def initiate_motors(self):
        gpio.setmode(gpio.BOARD)

        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)

    def go_strait(self, time_roll):
        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, True)
        gpio.output(15, False)

        time.sleep(time_roll)

        gpio.output(7, False)
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, False)


    def go_back(self):
        pass

    def go_left(self):
        pass

    def go_right(self):
        pass
