from pico2d import *
import math
import random

from bullet import Bullet
import game_world



# Hero Run Speed
PIXEL_PER_METER =  (1.0/0.3)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

# Hero Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, DOWN_1, DOWN_2, DOWN_3, M_LEFT_DOWN, M_LEFT_UP = range(13)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_w): UP_DOWN,
    (SDL_KEYDOWN, SDLK_s): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_1): DOWN_1,
    (SDL_KEYDOWN, SDLK_2): DOWN_2,
    (SDL_KEYDOWN, SDLK_3): DOWN_3,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYUP, SDLK_w): UP_UP,
    (SDL_KEYUP, SDLK_s): DOWN_UP,
    (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): M_LEFT_DOWN,
    (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT): M_LEFT_UP
}


# Boy States
class RunState:

    @staticmethod
    def enter(hero, event):
        if event == RIGHT_DOWN:
            hero.hor_speed += RUN_SPEED_PPS
        if event == LEFT_DOWN:
            hero.hor_speed -= RUN_SPEED_PPS
        if event == UP_DOWN:
            hero.ver_speed += RUN_SPEED_PPS
        if event == DOWN_DOWN:
            hero.ver_speed -= RUN_SPEED_PPS

        if event == RIGHT_UP:
            hero.hor_speed -= RUN_SPEED_PPS
        if event == LEFT_UP:
            hero.hor_speed += RUN_SPEED_PPS
        if event == UP_UP:
            hero.ver_speed -= RUN_SPEED_PPS
        if event == DOWN_UP:
            hero.ver_speed += RUN_SPEED_PPS

        if event == DOWN_1:
            hero.state = 1
            hero.fire_timer = 1000
            if hero.rifle_reloading == True:
                hero.rifle_reload_time = 100
        if event == DOWN_2:
            hero.state = 2
            hero.fire_timer = 1000
            if hero.shotgun_reloading == True:
                hero.shotgun_reload_time = 100
        if event == DOWN_3:
            hero.state = 3
            hero.fire_timer = 1000
            if hero.bazuka_reloading == True:
                hero.bazuka_reload_time = 100

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        hero.dir = math.atan2(mouse_y - hero.y, mouse_x - hero.x) - math.pi/2
        if hero.state == 1 and hero.rifle_reloading == True:
            hero.rifle_reload_time -= 1
            if hero.rifle_reload_time < 0:
                hero.rifle_reloading = False
                hero.rifle_reload_time = 100
                hero.rifle_ammo = 30

        elif hero.state == 2 and hero.shotgun_reloading == True:
            hero.shotgun_reload_time -= 1
            if hero.shotgun_reload_time < 0:
                hero.shotgun_reloading = False
                hero.shotgun_reload_time = 100
                hero.shotgun_ammo = 8

        elif hero.state == 3 and hero.bazuka_reloading == True:
            hero.bazuka_reload_time -= 1
            if hero.bazuka_reload_time < 0:
                hero.bazuka_reloading = False
                hero.bazuka_reload_time = 100
                hero.bazuka_ammo = 3

        if hero.auto_fire == True and hero.rifle_reloading == False and hero.state == 1:
                hero.fire_timer -= hero.rifle_fire_speed
        elif hero.auto_fire == True and hero.shotgun_reloading == False and hero.state == 2:
                hero.fire_timer -= hero.shotgun_fire_speed
        elif hero.auto_fire == True and hero.bazuka_reloading == False and hero.state == 3:
                hero.fire_timer -= hero.bazuka_fire_speed


        if hero.fire_timer < 0:
            hero.fire_timer = 1000
            hero.fire_bullet()

        hero.x += hero.hor_speed
        hero.y += hero.ver_speed

    @staticmethod
    def draw(hero):
        if (hero.state == 1):
            hero.image.clip_composite_draw(0, 800, 200, 200, hero.dir, '', hero.x, hero.y, 100, 100)
        elif (hero.state == 2):
            hero.image.clip_composite_draw(0, 600, 200, 200, hero.dir, '', hero.x, hero.y, 100, 100)
        elif (hero.state == 3):
            hero.image.clip_composite_draw(0, 400, 200, 200, hero.dir, '', hero.x, hero.y, 100, 100)


next_state_table = {

    RunState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP:RunState, DOWN_UP: RunState,
               LEFT_DOWN: RunState, RIGHT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,
               DOWN_1: RunState, DOWN_2: RunState, DOWN_3: RunState}
}

class Hero:
    def __init__(self):
        self.x, self.y = 800 / 2, 600/2
        self.image = load_image('hero_sprite.png')
        self.state = 1
        self.auto_fire = False
        self.fire_timer = 1000
        self.hor_speed = 0
        self.ver_speed = 0
        self.dir = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.font = load_font('ENCR10B.TTF', 16)

        self.rifle_ammo = 30
        self.rifle_reloading = False
        self.rifle_reload_time = 50
        self.rifle_fire_speed = 500

        self.shotgun_ammo = 8
        self.shotgun_reloading = False
        self.shotgun_reload_time = 50
        self.shotgun_fire_speed = 100

        self.bazuka_ammo = 3
        self.bazuka_reloading = False
        self.bazuka_reload_time = 50
        self.bazuka_fire_speed = 50




    def fire_bullet(self):
        if(self.state == 1):
            bullet = Bullet(self.x, self.y, mouse_x+random.randint(-20,20), mouse_y + random.randint(-20,20))
            game_world.add_object(bullet, 1)
            self.rifle_ammo -= 1
            if self.rifle_ammo == 0:
                self.rifle_reloading = True
        if (self.state == 2):
            for n in range(10):
                bullet = Bullet(self.x, self.y, mouse_x + random.randint(-20, 20), mouse_y + random.randint(-20, 20))
                game_world.add_object(bullet, 1)
            self.shotgun_ammo -= 1
            if self.shotgun_ammo == 0:
                self.shotgun_reloading = True
        if (self.state == 3):
            bullet = Bullet(self.x, self.y, mouse_x, mouse_y)
            game_world.add_object(bullet, 1)
            self.bazuka_ammo -= 1
            if self.bazuka_ammo == 0:
                self.bazuka_reloading = True




    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        if self.state == 1:
            if self.rifle_reloading == False:
                self.font.draw(self.x - 60, self.y + 50, '(R %3.2i / 30)' % self.rifle_ammo, (255, 255, 0))
            elif self.rifle_reloading == True:
                self.font.draw(self.x - 60, self.y + 50, '(R Reloading!)', (255, 255, 0))
        elif self.state == 2:
            if self.shotgun_reloading == False:
                self.font.draw(self.x - 60, self.y + 50, '(S %3.2i / 8)' % self.shotgun_ammo, (255, 255, 0))
            elif self.shotgun_reloading == True:
                self.font.draw(self.x - 60, self.y + 50, '(S Reloading!)', (255, 255, 0))
        elif self.state == 3:
            if self.bazuka_reloading == False:
                self.font.draw(self.x - 60, self.y + 50, '(B %3.2i / 3)' % self.bazuka_ammo, (255, 255, 0))
            elif self.bazuka_reloading == True:
                self.font.draw(self.x - 60, self.y + 50, '(B Reloading!)', (255, 255, 0))


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                self.auto_fire = True
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                self.auto_fire = False
        elif event.type == SDL_MOUSEMOTION:
            global mouse_x, mouse_y
            mouse_x, mouse_y = event.x, 600 - 1 - event.y





