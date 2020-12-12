import pygame
import sys


class screen:
    # Creates a new class of the screen object
    def __init__(self, width, height, name, back):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        pygame.init()
        self.screen.fill(back)
        self.back = back

    @staticmethod
    def check_quit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
