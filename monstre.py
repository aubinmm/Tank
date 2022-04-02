import pygame
import random


class Monstre(pygame.sprite.Sprite):

    def __init__(self, jeu, joueur, taille):
        super().__init__()
        self.attaque = 0.1
        self.jeu = jeu
        self.joueur = joueur
        self.point = 10
        self.vie = 50
        self.vie_max = 50
        self.vitesse = 5
        self.taille = taille
        self.image = pygame.image.load('ghost.png')
        self.image = pygame.transform.scale(self.image, (self.taille, self.taille))
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = random.randint(0, 500)

    def degats(self, nombre):
        self.vie -= nombre

    def tire(self, degat):
        self.jeu.joueur.vie -= degat


    def update_vie_bar(self, surface):
        # afficher la bar de vie
        pygame.draw.rect(surface, (178, 193, 190), [self.rect.x, self.rect.y - 15, self.vie_max, 5])
        pygame.draw.rect(surface, (236, 57, 22 ), [self.rect.x, self.rect.y - 15, self.vie, 5])


    def move(self):
        if not self.jeu.check_collision(self, self.jeu.all_joueurs):
            self.rect.x += self.vitesse
        else:
            self.tire(self.attaque)

        if self.vie <= 0:
            self.vie = self.vie_max
            self.rect.x = -100
            self.rect.y = random.randint(50, 500)
            self.jeu.score += self.point
            if self.jeu.boss_event.is_full_loaded():
                self.jeu.all_monstres.remove(self)
                self.jeu.boss_event.attempt_fall()



        if self.rect.x > 1300:
            self.vie = self.vie_max
            self.rect.x = -100
            self.rect.y = random.randint(50, 500)
            if self.jeu.boss_event.is_full_loaded():
                self.jeu.all_monstres.remove(self)
                self.jeu.boss_event.attempt_fall()



class Fantome(Monstre):

    def __init__(self, jeu, joueur):
        super().__init__(jeu, joueur, 50)
        self.vie = 50
        self.vie_max = 50
        self.vitesse = random.randint(5, 7)
        self.attaque = 0.2
        self.point = 20


class Grand_Fantome(Monstre):

    def __init__(self, jeu, joueur):
        super().__init__(jeu, joueur, 200)
        self.vie = 200
        self.vie_max = 200
        self.vitesse = 3
        self.attaque = 0.5
        self.point = 50


class Big_Fantome(Monstre):

    def __init__(self, jeu, joueur):
        super().__init__(jeu, joueur, 600)
        self.vie = 600
        self.vie_max = 600
        self.vitesse = 1
        self.attaque = 1
        self.point = 100
        self.rect.y = 50


