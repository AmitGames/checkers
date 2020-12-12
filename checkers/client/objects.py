import pygame


def text(font, size, text, x, y, screen, color=(0, 0, 0), back=(255, 255, 255)):
    font = pygame.font.SysFont(font, size)
    t = font.render(text, True, color, back)
    textRect = t.get_rect()
    textRect.center = (x, y)
    screen.blit(t, textRect)
