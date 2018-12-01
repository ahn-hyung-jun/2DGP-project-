from pico2d import *
import math
import game_world
import game_framework
import hero
import main_state

# Bullet Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
GUN_SPEED_KMPH = 10.0  # Km / Hour
GUN_SPEED_MPM = (GUN_SPEED_KMPH * 1000.0 / 60.0)
GUN_SPEED_MPS = (GUN_SPEED_MPM / 60.0)
GUN_SPEED_PPS = (GUN_SPEED_MPS * PIXEL_PER_METER)

FRAMES_PER_ACTION = 60

def get_distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

class Boss_bullet:
    image = None

    def __init__(self, x = 400, y = 300, dir = 0, state = 1):
        if Boss_bullet.image == None:
            self.image = load_image('hero_sprite.png')
        self.x, self.y = x, y
        self.state = state
        self.bullet_speed = GUN_SPEED_PPS
        if self.state == 5:
            self.bullet_speed = GUN_SPEED_PPS // 2
        self.damage = 5
        self.dir = dir
        self.fire_time = 0
        self.degree = 0
        self.fire_speed = 1


    def draw(self):
        if(self.state == 1 or self.state == 4):
            self.image.clip_composite_draw(980, 920, 20, 20, 0, '', self.x, self.y, 40, 40)
        elif self.state == 0 or self.state == 3:
            self.image.clip_composite_draw(980, 900, 20, 20, 0, '', self.x, self.y, 40, 40)
        elif self.state == 2 or self.state == 5 or self.state == 6:
            self.image.clip_composite_draw(980, 880, 20, 20, 0, '', self.x, self.y, 40, 40)


    def update(self):
        self.fire_speed += game_framework.frame_time * FRAMES_PER_ACTION
        if self.fire_speed > 1:
            self.fire_speed = 0
            self.fire_time += 1
            self.degree += 1
        #self.fire_time += self.fire_speed* game_framework.frame_time*FRAMES_PER_ACTION
        #self.degree += 1* game_framework.frame_time*FRAMES_PER_ACTION
        self.x += math.cos(self.dir) *self.bullet_speed * game_framework.frame_time
        self.y += math.sin(self.dir) * self.bullet_speed * game_framework.frame_time


        if self.x < 0 or self.x > 1280 or self.y < 0 or self.y > 1024:
            game_world.remove_object(self)

        if self.state == 4:
            if self.fire_time % 30 == 0:
                bullet = Boss_bullet(self.x, self.y, math.atan2(hero.find_y() - self.y, hero.find_x() - self.x), 1)
                game_world.add_object(bullet, 3)

        if self.state == 3:
            if self.fire_time % 30 == 0:
                bullet = Boss_bullet(self.x, self.y, math.atan2(hero.find_y() - self.y, hero.find_x() - self.x), 0)
                game_world.add_object(bullet, 3)

        if self.state == 5:
            if int(self.fire_time) % 8 == 0:
                bullet1 = Boss_bullet(self.x, self.y, math.radians(self.degree), 2)
                game_world.add_object(bullet1, 3)
            elif int(self.fire_time) % 8 == 1:
                bullet2 = Boss_bullet(self.x, self.y, math.radians(self.degree) - math.pi / 2, 2)
                game_world.add_object(bullet2, 3)
            elif int(self.fire_time) % 8 == 2:
                bullet3 = Boss_bullet(self.x, self.y, math.radians(self.degree) - math.pi, 2)
                game_world.add_object(bullet3, 3)
            elif int(self.fire_time) % 8 == 3:
                bullet4 = Boss_bullet(self.x, self.y, math.radians(self.degree) + math.pi / 2, 2)
                game_world.add_object(bullet4, 3)

        if self.state == 6:
            if int(self.fire_time) % 30 == 0:
                self.dir += math.radians(60)



