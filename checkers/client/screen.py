import pygame
import sys


class screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.init()

    @staticmethod
    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
