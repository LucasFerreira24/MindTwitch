from .model import Model
from shared.calc_pos_objects import calc_pos_objects


class View:
    def __init__(self, screen, game):
        self.screen = screen
        self.model = Model(screen=self.screen)

        self._alpha: float = 0
        self._delta: float = 1.25

        self._objects_scene_base = [
            ['asset/img/backgrond_home.png', (0,0), False],
            ['asset/img/game/up.png', calc_pos_objects(reference_pos=(0,0), screen_size=screen.size, screen_reference=screen.reference), True],
            ['asset/img/game/bg.png', calc_pos_objects(reference_pos=(480,300), screen_size=screen.size, screen_reference=screen.reference), True],
            [self.screen.font_title.render('Você perdeu!', True, (0,0,0)), calc_pos_objects(reference_pos=(615,395), screen_size=screen.size, screen_reference=screen.reference), True]
        ]

        self.__add_objects_base = False

    def run(self):
        if not self.__add_objects_base:
            self.screen.add_objects_screen(objects_screen=self._objects_scene_base)

            self.screen.rezise_object(object_pos=1, size=(1920,100))
            self.screen.rezise_object(object_pos=2, size=(1000,500))
            self.screen.rezise_object(object_pos=3, size=(700,300))

            self.__add_objects_base = True
    
