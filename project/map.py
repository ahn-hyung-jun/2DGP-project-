import random
import json
import os

from pico2d import *

import game_framework

class Map:
    def __init__(self, i = 0, j = 0):
        self.x_pos, self.y_pos = 10 + 10*i, 10+10*j
        self.state = 0
        self.size = 10


    def draw(self):
        pass