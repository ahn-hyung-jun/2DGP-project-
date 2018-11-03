import random
import json
import os

from pico2d import *

import game_framework

class Map:
    def __init__(self, i, j):
        self.x_pos, self.y_pos = 10 + 10*i, 10+10*j
        self.state = 0
        self.size = 10
        self.image = load_image('test_map.png')



    def draw(self):
        #self.image.draw(800/2, 600/2)
        pass