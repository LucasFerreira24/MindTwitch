from pygame import image, time
from .model import Model
from shared.calc_pos_objects import calc_pos_objects


class View:
    def __init__(self, screen, game):
        self.screen = screen
        self.model = Model(screen=self.screen)

        self._objects_scene_base = [
            ['asset/img/backgrond_home.png', (0,0), False],
            ['asset/img/logo.png', calc_pos_objects(reference_pos=(720,150), screen_size=screen.size, screen_reference=screen.reference), True],
        ]

    def run(self):
        if not self.screen.add_objects_base:
            self.screen.add_objects_screen(self._objects_scene_base)
            self.screen.add_objects_base = True
        
