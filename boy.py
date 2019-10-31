from pico2d import *


import game_world

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, UP_UP, DOWN_DOWN, DOWN_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == UP_DOWN:
            boy.velocity2 += 1
        elif event == DOWN_DOWN:
            boy.velocity2 -= 1
        elif event == UP_UP:
            boy.velocity2 -= 1
        elif event == DOWN_UP:
            boy.velocity2 += 1
        boy.timer = 300

    @staticmethod
    def exit(boy, event):
        # fill here
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        # fill here

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(0, 0, 50, 50, boy.x, boy.y)
        else:
            boy.image.clip_draw(0, 0, 50, 50, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == UP_DOWN:
            boy.velocity2 += 1
        elif event == DOWN_DOWN:
            boy.velocity2 -= 1
        elif event == UP_UP:
            boy.velocity2 -= 1
        elif event == DOWN_UP:
            boy.velocity2 += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        # fill here
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)
        boy.y += boy.velocity2

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(0, 0, 50, 50, boy.x, boy.y)
        else:
            boy.image.clip_draw(0, 0, 50, 50, boy.x, boy.y)


class SleepState:
    # fill here
    pass





next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, UP_UP: RunState, DOWN_DOWN: RunState, DOWN_UP: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,UP_DOWN: IdleState, UP_UP: IdleState, DOWN_DOWN: IdleState, DOWN_UP: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 80, 300
        self.image = load_image('main_character1.png')
        self.dir = 1
        self.velocity = 0
        self.velocity2 = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        # fill here
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

