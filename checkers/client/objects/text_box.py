import pygame


class text_box:
    def __init__(self, text, font, size, x, y, screen, color=(0, 0, 0), back=(255, 255, 255)):
        self.text = text
        self.font = font
        self.color = color
        self.back = back
        self.size = size
        self.x = x
        self.y = y
        self.screen = screen
        self.render_text()

    def render_text(self):
        font = pygame.font.SysFont(self.font, self.size)
        t = font.render(self.text, True, self.color, self.back)
        textRect = t.get_rect()
        textRect.center = (self.x, self.y)
        self.screen.blit(t, textRect)
