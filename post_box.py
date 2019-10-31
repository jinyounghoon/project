import game_framework
from pico2d import *

import main_state

name = "PauseState"
image = None
rand = 0




def enter():
   global image
   image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def draw():
    global rand

    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    rand += 1
    if (rand % 2) == 0:
        image.draw(400,300,200,200)
        delay(0.1)
    delay(0.1)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass




