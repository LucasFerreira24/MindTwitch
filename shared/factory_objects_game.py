import pygame
from shared.rezise_objects import rezise_objects


class FactoryObjectsGame:
    def __init__(self, screen, image: str, rect: list, name: str = None):
        self.name: str = name
        self.screen = screen

        self.rect = pygame.Rect(rect)

        self.image = pygame.image.load(image)
        self.image.set_alpha(255)
        self.image = rezise_objects(
            image=self.image, 
            screen_size=self.screen.size, 
            screen_reference=self.screen.reference, 
            image_size=(self.rect.width, self.rect.height)
        )

    def activate_blink(self):
        for index, object in enumerate(self.screen.objects_screen):
            object_surface = object[0]
            object_pos = object[1]

            object_rect = object_surface.get_rect(topleft=object_pos)

            if self.rect == object_rect:
                self.screen.change_alpha_object(object_pos=index, alpha=125)

    def disable_blink(self):
        for index, object in enumerate(self.screen.objects_screen):
            object_surface = object[0]
            object_pos = object[1]

            object_rect = object_surface.get_rect(topleft=object_pos)

            if self.rect == object_rect:
                self.screen.change_alpha_object(object_pos=index, alpha=255)
