from pico2d import *
import math
import game_world
import game_framework

# Bullet Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm

class Explosion:
    image = None

    def __init__(self, x = 400, y = 300):
        if Explosion.image == None:
            self.image = load_image('hero_sprite.png')
        self.frame = 1
        self.x = x
        self.y = y

    def draw(self):
        if self. state == 0 or self.state == 1 or self.state == 2:
            self.image.clip_composite_draw(980-20, 980-20, 40, 40, self.dir, '', self.x, self.y, 40, 40)
        elif self.state == 3:
            self.image.clip_composite_draw(900-50, 965-50, 100, 100, self.dir, '', self.x, self.y, 40, 40)

    def update(self):
        self.x += self.velocity_x*self.bullet_speed * game_framework.frame_time
        self.y += self.velocity_y*self.bullet_speed * game_framework.frame_time

        if self.x < 0 or self.x > 1280 or self.y < 0 or self.y > 1024:
            game_world.remove_object(self)

        if self.state == 0:
            pass


