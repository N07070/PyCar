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


class Motors(object):
    """docstring for Motors"""

    def __init__(self, arg):
        super(Motors, self).__init__()
        self.arg = arg

    def go_strait(self):
        pass

    def go_back(self):
        pass

    def go_left(self):
        pass

    def go_right(self):
        pass
