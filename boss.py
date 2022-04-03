import pygame
import random

class Boss(pygame.sprite.Sprite):

    def __init__(self, Jeu):
        super().__init__()
        self.jeu = Jeu
        self.image = pygame.image.load("munition_méchant.png")
        #self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        self.rect.x = - random.randint(200, 1000)
        self.rect.y = random.randint(50, 650)
        self.vitesse = random.randint(10, 12)

    def move(self):
        self.rect.x += self.vitesse
        if self.rect.x >= 1000:
            self.jeu.son.play("boss")
            self.remove(self.jeu.all_boss)
        if self.jeu.check_collision(self, self.jeu.all_joueurs):
            self.jeu.joueur.degats(20)
            self.remove(self.jeu.all_boss)

