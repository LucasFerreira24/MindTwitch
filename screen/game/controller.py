import pygame
from .model import Model

class Controller:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.model = Model(screen=self.screen)
    
    def run(self, *args, **kwargs):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index_object in range(len(self.screen.objects_screen)):
                    object_surface = self.screen.objects_screen[index_object][0]
                    object_pos = self.screen.objects_screen[index_object][1]

                    object_rect = object_surface.get_rect(topleft=object_pos)

                    if object_rect.collidepoint(pygame.mouse.get_pos()):
                        if index_object == 3:
                            self.model.close_game()
                        elif index_object in [5,6,7,8]:
                            self.model.compare_sequence_game(game=self.game, object_rect=object_rect)

