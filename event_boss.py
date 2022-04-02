
import pygame
from boss import Boss


class Event_Boss:
    def __init__(self, jeu):
        self.jeu = jeu
        self.percent = 0
        self.percent_speed = 15
        self.boss = pygame.sprite.Group()
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0, 0, 0), (0, surface.get_height() - 20, surface.get_width(), 10))
        # barre percent
        pygame.draw.rect(surface, (53, 234, 64), (0, surface.get_height() - 20,surface.get_width() / 100 * self.percent, 10))

    def is_full_loaded(self):
        return self.percent >= 100

    def boss_fall(self):
        for i in range(0, 7):
            self.boss.add(Boss(self))

    def reset_percent(self):
        self.percent = 0

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.jeu.all_monstres) == 0:
            self.boss_fall()
            self.fall_mode = True

