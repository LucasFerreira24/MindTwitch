import pygame
from .model import Model

class Controller:
    def __init__(self, screen, game):
        self.screen = screen
        self.model = Model(screen=self.screen)
    
    def run(self, *args, **kwargs):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.model.advance_state_screen()