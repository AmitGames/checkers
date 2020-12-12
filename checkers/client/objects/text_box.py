import pygame


class text_box:
    def __init__(self, x, y, width, height, font, text="", color_inactive=pygame.Color("lightskyblue3"), color_active=pygame.Color("dodgerblue2")):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
