import pygame
import math
from monstre import *
from level import Level
from tank import Tank
from Son import Son

pygame.font.init()

clock = pygame.time.Clock()
FPS = 60


class Jeu:

    def __init__(self):
        self.son = Son()
        self.level = Level(self)
        self.is_playing = False
        self.all_joueurs = pygame.sprite.Group()
        self.joueur = Tank(self)
        self.all_joueurs.add(self.joueur)
        self.all_monstres = pygame.sprite.Group()
        self.all_munitions = pygame.sprite.Group()
        self.all_boss = pygame.sprite.Group()
        self.font = pygame.font.SysFont("Rubik", 16)
        self.score = 0
        self.presse = {}


    def start(self):
        self.all_monstres = pygame.sprite.Group()
        self.level.all_boss = pygame.sprite.Group()
        self.is_playing = True
        self.level.number = 0
        self.level.start()

    def game_over(self):
        print("game over")
        self.son.play("game_over")
        self.joueur.vie = self.joueur.vie_max
        self.is_playing = False
        self.score = 0
        self.level.number = 0

    def update(self):
        #Affichage des informations du jeu en haut à gauche
        score_text = self.font.render(f"score : {self.score}", 1, (255, 255, 255))
        level_text = self.font.render(f"level : {self.level.number}", 1, (255, 255, 255))
        fenetre.blit(score_text, (20, 20))
        fenetre.blit(level_text, (20, 40))
        # montrer le joueur et sa barre de vie
        fenetre.blit(self.joueur.image, self.joueur.rect)
        self.joueur.update_vie_bar(fenetre)
        # munition
        self.joueur.all_munitions.draw(fenetre)
        # monstre
        self.all_monstres.draw(fenetre)
        #Boss/missiles
        self.all_boss.draw(fenetre)

        # déplacements des objets autonomes
        for munition in self.joueur.all_munitions:
            munition.move(jeu)
        for monstre in self.all_monstres:
            monstre.move(fenetre)
        for boss in self.all_boss:
            boss.move()
        #Barre de défilement du niveau
        jeu.level.update_level_advance(fenetre)

        # diriger le joueur
        if jeu.presse.get(pygame.K_UP) and jeu.joueur.rect.y > 30:
            jeu.joueur.move_up()
        elif jeu.presse.get(pygame.K_DOWN) and jeu.joueur.rect.y < 600:
            jeu.joueur.move_down()
        elif jeu.presse.get(pygame.K_RIGHT) and jeu.joueur.rect.x < 1000:
            jeu.joueur.move_right()
        elif jeu.presse.get(pygame.K_LEFT) and jeu.joueur.rect.x > 30:
            jeu.joueur.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def monstre(self, monstre_nom):
        self.all_monstres.add(monstre_nom.__call__(self, self.joueur))

# fenêtre
pygame.display.set_caption("jeu vidéo")
fenetre = pygame.display.set_mode((1100, 700))
fond = pygame.image.load("DSCF0211.JPG")

banner = pygame.image.load("banner.png")
banner = pygame.transform.scale(banner, (600, 200))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(fenetre.get_width() / 4.5)

play_button = pygame.image.load("boutton_play.png")
play_button = pygame.transform.scale(play_button, (300, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(fenetre.get_width() / 2.75)
play_button_rect.y = math.ceil(fenetre.get_height() / 2.5)



jeu = Jeu()
running = True

while running:
    # arrière plan
    fenetre.blit(fond, (0, -200))
    # début du jeu
    if jeu.is_playing:
        jeu.update()
    else:
        fenetre.blit(banner, banner_rect)
        fenetre.blit(play_button, play_button_rect)

    # vérifier si le joueur est mort
    if jeu.joueur.vie <= 0:
        jeu.game_over()

    # mettre à jour l'écran
    pygame.display.flip()
    # fermeture de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            jeu.presse[event.key] = True

            if event.key == pygame.K_SPACE:
                jeu.joueur.launch_projectile()
        elif event.type == pygame.KEYUP:
            jeu.presse[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not jeu.is_playing:
                if play_button_rect.collidepoint(event.pos):
                    jeu.start()
                    jeu.son.play("click")
    clock.tick(FPS)
