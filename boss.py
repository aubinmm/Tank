import pygame
import random

class Boss(pygame.sprite.Sprite):

    def __init__(self, event_boss):
        super().__init__()
        self.boss_event = event_boss
        self.image = pygame.image.load("munition_méchant.png")
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        self.rect.x = - random.randint(200, 1000)
        self.rect.y = random.randint(-200, 400)
        self.vitesse = random.randint(10, 12)

    def remove(self):
        self.boss_event.jeu.son.play("boss")
        self.boss_event.boss.remove(self)

        if len(self.boss_event.boss) == 0:
            self.boss_event.reset_percent()
            self.boss_event.jeu.start()
            self.boss_event.jeu.score += 20

    def move(self):
        self.rect.x += self.vitesse
        if self.rect.x >= 1000:
            self.remove()
        if self.boss_event.jeu.check_collision(self, self.boss_event.jeu.all_joueurs):
            self.boss_event.jeu.joueur.vie -= 20
            self.remove()

