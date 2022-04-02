import pygame

class Munition(pygame.sprite.Sprite):

    def __init__(self, Joueur):
        super().__init__()
        self.vitesse = 15
        self.image = pygame.image.load("munition.png")
        self.image = pygame.transform.scale(self.image, (25, 5))
        self.rect = self.image.get_rect()
        self.rect.x = Joueur.rect.x
        self.rect.y = Joueur.rect.y + 35
        self.origin_image = self.image
        self.angle = 0

    def move(self, Jeu):
        self.rect.x -= self.vitesse
        for monstre in Jeu.check_collision(self, Jeu.all_monstres):
            self.remove(Jeu.joueur.all_munitions)
            monstre.degats(Jeu.joueur.attaque)

        if self.rect.x < -100:
            self.remove(Jeu.joueur.all_munitions)

