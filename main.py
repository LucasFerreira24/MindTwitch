import sys
import importlib
import pygame
from config.screen import Screen
from config.game import Game
from screen import *


def load_class(state_game, screen, game, name_class, filename):
    module_class = importlib.import_module(f'{state_game}.{filename}')
    class_name = getattr(module_class, name_class)
    return class_name(screen, game)

pygame.init()

screen = Screen()
game = Game(screen=screen)

screen.set_mode()
screen.set_caption()

screen.set_state(state='screen.logo_presentation')
old_screen_state = screen.state

controller = load_class(state_game=screen.state, screen=screen, game=game, name_class='Controller', filename='controller')
view = load_class(state_game=screen.state, screen=screen, game=game, name_class='View', filename='view')

fps = 60

running = True

while running:
    if screen.state == 'screen.endgame':
        running = False

    for image_object in screen.objects_screen:
        if isinstance(image_object[0], pygame.Surface):
            screen.surface.blit(image_object[0], image_object[1])
        else:
            screen.surface.fill(image_object[0], image_object[1])

    if old_screen_state != screen.state:
        screen.rm_objects_screen(objects_screen=screen.objects_screen)
        
        controller = load_class(state_game=screen.state, screen=screen, game=game, name_class='Controller', filename='controller')
        view = load_class(state_game=screen.state, screen=screen, game=game, name_class='View', filename='view')
        
        old_screen_state = screen.state

    controller.run(event=pygame.event)
    view.run()

    pygame.display.flip()

    pygame.time.Clock().tick(fps)

pygame.quit()
sys.exit()
