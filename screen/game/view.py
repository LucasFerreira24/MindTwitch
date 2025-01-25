from random import randint
import time
from .model import Model
from shared.calc_pos_objects import calc_pos_objects


class View:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.model = Model(screen=self.screen)

        self._objects_scene_base = [
            ['asset/img/backgrond_home.png', (0,0), False],
            ['asset/img/game/table.png', calc_pos_objects(reference_pos=(800,0), screen_size=screen.size, screen_reference=screen.reference), True],
            ['asset/img/game/up.png', calc_pos_objects(reference_pos=(0,0), screen_size=screen.size, screen_reference=screen.reference), True],
            ['asset/img/buttons/close.png', calc_pos_objects(reference_pos=(10,0), screen_size=screen.size, screen_reference=screen.reference), True],
            [self.screen.font_title.render(f'SimonGame', True, (0,0,0)), calc_pos_objects(reference_pos=(820,175), screen_size=screen.size, screen_reference=screen.reference), True]
        ]

        self.last_object_show_time: float = time.time()
        self.object_show_interval: float = 2

        self.blinking_objects: list = None

        self.__add_objects_base: bool = False

    def run(self):
        if not self.__add_objects_base:
            self.screen.add_objects_screen(self._objects_scene_base)

            for object_game in self.game.objects_game_choices:
                self.screen.add_objects_screen([[object_game.image, calc_pos_objects(reference_pos=(object_game.rect.x, object_game.rect.y), screen_size=self.screen.size, screen_reference=self.screen.reference), True]])

            self.screen.rezise_object(object_pos=1, size=(350,350))
            self.screen.rezise_object(object_pos=2, size=(1920,100))
            self.screen.rezise_object(object_pos=3, size=(70,70))

            self.__add_objects_base = True

        if self.game.is_next_level:

            for level in range(0, self.game.get_level()):
                index_object: int = randint(0, len(self.game.objects_game_choices) - 1)
                self.game.order_choosing_game_objects.append(self.game.objects_game_choices[index_object])
            
            self.blinking_objects = self.game.order_choosing_game_objects.copy()

            self.game.is_next_level = False

        if self.blinking_objects:
            if time.time() - self.last_object_show_time <= self.object_show_interval:
                self.blinking_objects[0].activate_blink()
            else:
                self.blinking_objects[0].disable_blink()
                rm_blinking_object = self.blinking_objects.pop(0)
                self.last_object_show_time = time.time()
