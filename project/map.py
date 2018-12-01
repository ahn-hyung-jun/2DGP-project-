import random
import json
import os
import main_state
from pico2d import *

import game_framework

class Map:
    def __init__(self, i = 0, j = 0):
        self.image = load_image('back_ground.png')
        self.x_pos, self.y_pos = 1280/2, 1024/2
        self.bgm = load_music('Bgm.mp3')
        self.bgm.set_volume(40)
        self.bgm.repeat_play()


    def update(self):
        pass


    def draw(self):
        self.image.draw(self.x_pos, self.y_pos)
