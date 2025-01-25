from .model import Model
from shared.calc_pos_objects import calc_pos_objects


class View:
    def __init__(self, screen, game):
        self.screen = screen
        self.model = Model(screen=self.screen)

        self._alpha: float = 0
        self._delta: float = 1.25

        self._objects_scene_base: list = [
            [(0,0,0), (0,0, screen.width, screen.height), False],
            ['asset/img/logo.png', calc_pos_objects(reference_pos=(700,300), screen_size=screen.size, screen_reference=screen.reference), True],
        ]

        self.__add_objects_base = False

    def run(self):
        if not self.__add_objects_base:
            self.screen.add_objects_screen(objects_screen=self._objects_scene_base)
            self.__add_objects_base = True

        self._alpha += self._delta

        if self._alpha >= 255:
            self._alpha = 0
            self.model.advance_state_screen()
        
        self.screen.change_alpha_object(object_pos=1, alpha=self._alpha)
    
