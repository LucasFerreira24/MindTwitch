from shared.factory_objects_game import FactoryObjectsGame


class Game:
    def __init__(self, screen):
        self.__level: int = 1

        self.button_choice_1 = FactoryObjectsGame(screen=screen, image='asset/img/game/buttons/blue.png', rect=(625,475,300,150), name='obj1')
        self.button_choice_2 = FactoryObjectsGame(screen=screen, image='asset/img/game/buttons/green.png', rect=(1025,475,300,150), name='obj2')
        self.button_choice_3 = FactoryObjectsGame(screen=screen, image='asset/img/game/buttons/red.png', rect=(625,675,300,150), name='obj3')
        self.button_choice_4 = FactoryObjectsGame(screen=screen, image='asset/img/game/buttons/yellow.png', rect=(1025,675,300,150), name='obj4')

        self.objects_game_choices: list = [
            self.button_choice_1,
            self.button_choice_2,
            self.button_choice_3,
            self.button_choice_4
        ]

        self.order_choosing_game_objects = [] # list to store the order in which the person has to load the game
        self.current_sequence_index = 0
        
        self.is_next_level = True


    def next_level(self) -> None:
        self.__level += 1
        self.current_sequence_index = 0
        self.order_choosing_game_objects = []
        self.is_next_level = True

    def get_level(self) -> int:
        return self.__level
