import pygame
from munition import Munition

class Tank(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.vie = 50
        self.vie_max = 50
        self.attaque = 20
        self.vitesse = 7
        self.image = pygame.image.load("space-invaders.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.all_munitions = pygame.sprite.Group()
        self.rect.x = 950
        self.rect.y = 300
        self.origin_image = self.image
        self.angle = 0


    def update_vie_bar(self, surface):
        # afficher la bar de vie
        pygame.draw.rect(surface, (178, 193, 190), [self.rect.x + 30, self.rect.y - 15, self.vie_max, 7])
        pygame.draw.rect(surface, (55, 227, 21), [self.rect.x + 30, self.rect.y - 15, self.vie, 7])

    def launch_projectile(self):
        if self.jeu.is_playing:
            self.jeu.son.play("tir")
            self.all_munitions.add(Munition(self))

    def degats(self,dommages):
        self.vie -= dommages

    def move_up(self):
        self.rect.y -= self.vitesse


    def move_down(self):
        self.rect.y += self.vitesse


    def move_right(self):
        self.rect.x += self.vitesse


    def move_left(self):
        if not self.jeu.check_collision(self, self.jeu.all_monstres):
            self.rect.x -= self.vitesse



