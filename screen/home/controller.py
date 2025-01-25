import pygame
from .model import Model

class Controller:
    def __init__(self, screen, game):
        self.screen = screen
        self.model = Model(screen=self.screen)
    
    def run(self, *args, **kwargs):
        pass