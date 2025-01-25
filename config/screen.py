import pygame
from shared.rezise_objects import rezise_objects


class Screen:
    def __init__(self, title: str = 'SimonGame'):
        self.__display_info = pygame.display.Info()

        self.objects_screen: list = []

        self.width: int = self.__display_info.current_w
        self.height: int = self.__display_info.current_h
        self.size: tuple = (self.width, self.height)
        self.reference: tuple = (1920, 1080) # screen size for which the game was created

        self.title: str = title

        self.surface = None
        self.state: str = ''

        self.font_title = pygame.font.Font(None, 75)

    def set_mode(self) -> None:
        self.surface = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN, pygame.NOFRAME)

    def set_caption(self) -> None:
        pygame.display.set_caption(self.title)

    def set_state(self, state) -> None:
        self.state = state
    
    def add_objects_screen(self, objects_screen: list) -> None:
        for object in objects_screen:
            if isinstance(object[0], str):
                object[0] = pygame.image.load(object[0]).convert_alpha()
            elif isinstance(object[0], tuple):
                object[0] = pygame.Color(object[0])
            elif isinstance(object[0], pygame.Surface):
                pass
            else:
                raise ValueError("Tipo não suportado para object[0]. Deve ser uma string (caminho de imagem), Surface ou tuple (cor).")
            
            if object[2]:
               object[0] = rezise_objects(image=object[0], screen_size=self.size, screen_reference=self.reference)
            
            self.objects_screen.append(object)

    def rm_objects_screen(self, objects_screen: list) -> None:
        self.objects_screen = [obj for obj in self.objects_screen if obj not in objects_screen]


    def change_alpha_object(self, object_pos: int, alpha: float) -> None:
        if 0 <= object_pos <= len(self.objects_screen):
            self.objects_screen[object_pos][0].set_alpha(alpha)

    def rezise_object(self, object_pos: int, size: tuple) -> None:
        if 0 <= object_pos <= len(self.objects_screen):
            self.objects_screen[object_pos][0] = rezise_objects(image=self.objects_screen[object_pos][0], screen_size=self.size, screen_reference=self.reference, image_size=size)
