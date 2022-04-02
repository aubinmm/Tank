import pygame

class Munition(pygame.sprite.Sprite):

    def __init__(self, t):
        super().__init__()
        self.vitesse = 15
        self.image = pygame.image.load("munition.png")
        self.image = pygame.transform.scale(self.image, (25, 5))
        self.rect = self.image.get_rect()
        self.rect.x = t.rect.x
        self.rect.y = t.rect.y + 35
        self.origin_image = self.image
        self.angle = 0

    def remove(self, t):
        t.all_munition.remove(self)

    def move(self, t, j):
        self.rect.x -= self.vitesse
        for monstre in j.check_collision(self, j.all_monstres):
            self.remove(t)
            monstre.degats(t.attaque)

        if self.rect.x < -100:
            self.remove(t)
