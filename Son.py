import pygame

pygame.mixer.init()

class Son:

    def __init__(self):
        self.sons = {
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'boss': pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg"),
        }

    def play(self, nom):
        self.sons[nom].play()
