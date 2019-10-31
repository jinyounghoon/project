from pico2d import *


class Postbox:
    def __init__(self):
        self.image = load_image('post_box.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 100)




