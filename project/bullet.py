from pico2d import *
import math
import game_world

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity_x = 1, velocity_y = 1):
        if Bullet.image == None:
            Bullet.image = load_image('ball21x21.png')
        self.velocity_x = (velocity_x - x) / math.sqrt((velocity_x - x)**2 +(velocity_y-y)**2)
        self.velocity_y = (velocity_y - y) / math.sqrt((velocity_x - x)**2 +(velocity_y-y)**2)
        self.x, self.y = x + self.velocity_x*40, y + self.velocity_y*40

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity_x*3
        self.y += self.velocity_y*3

        if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600:
            game_world.remove_object(self)
