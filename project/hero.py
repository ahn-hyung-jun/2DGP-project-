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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, DOWN_1, DOWN_2, DOWN_3, M_LEFT_DOWN = range(12)

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
    (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): M_LEFT_DOWN
}


# Boy States

class IdleState:

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
        if event == DOWN_2:
            hero.state = 2
        if event == DOWN_3:
            hero.state = 3

    @staticmethod
    def exit(hero, event):
        if event == M_LEFT_DOWN:
            hero.fire_bullet()
            print(hero.dir)

        pass

    @staticmethod
    def do(hero):
        hero.dir = math.atan2(mouse_y - hero.y, mouse_x - hero.x) - math.pi/2
        # fill here

    @staticmethod
    def draw(hero):
        if(hero.state == 1):
            hero.image.clip_composite_draw(0,800,200,200,hero.dir,'',hero.x,hero.y,100,100)
        elif(hero.state == 2):
            hero.image.clip_composite_draw(0, 600, 200, 200, hero.dir, '', hero.x, hero.y, 100, 100)
        elif(hero.state == 3):
            hero.image.clip_composite_draw(0, 400, 200, 200, hero.dir, '', hero.x, hero.y, 100, 100)

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
        if event == DOWN_2:
            hero.state = 2
        if event == DOWN_3:
            hero.state = 3

    @staticmethod
    def exit(hero, event):
        if event == M_LEFT_DOWN:
            hero.fire_bullet()
        pass

    @staticmethod
    def do(hero):
        hero.dir = math.atan2(mouse_y - hero.y, mouse_x - hero.x) - math.pi/2
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
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP: RunState, DOWN_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,
                DOWN_1 : IdleState, DOWN_2: IdleState, DOWN_3: IdleState,M_LEFT_DOWN:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP:IdleState, DOWN_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState,
               DOWN_1: RunState, DOWN_2: RunState, DOWN_3: RunState, M_LEFT_DOWN: RunState}
}

class Hero:

    def __init__(self):
        self.x, self.y = 800 / 2, 600/2
        self.image = load_image('hero_sprite.png')
        self.state = 1
        self.hor_speed = 0
        self.ver_speed = 0
        self.dir=0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_bullet(self):
        bullet = Bullet(self.x, self.y, mouse_x, mouse_y)
        game_world.add_object(bullet, 1)
        pass



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


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        elif (event.type, event.button) in key_event_table:
            key_event = key_event_table[(event.type, event.button)]
            self.add_event(key_event)
        elif event.type == SDL_MOUSEMOTION:
            global mouse_x, mouse_y
            mouse_x, mouse_y = event.x, 600 - 1 - event.y





