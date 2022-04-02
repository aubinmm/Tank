import pygame
import math
from monstre import *
from event_boss import Event_Boss
from tank import Tank
from Son import Son

pygame.font.init()

clock = pygame.time.Clock()
FPS = 60
nouvelle_variable_test = " "

class Jeu:

    def __init__(self):
        self.son = Son()
        self.level = 0
        self.is_playing = False
        self.all_joueurs = pygame.sprite.Group()
        self.joueur = Tank(self)
        self.boss_event = Event_Boss(self)
        self.all_joueurs.add(self.joueur)
        self.all_monstres = pygame.sprite.Group()
        self.all_munition = pygame.sprite.Group()
        self.font = pygame.font.SysFont("Rubik", 16)
        self.score = 0
        self.presse = {}


    def start(self):
        self.is_playing = True
        self.boss_event.jeu.level += 1
        self.boss_event.percent = 0

        if not self.level == 10:
            self.monstre(Fantome)
            self.monstre(Fantome)
            self.monstre(Fantome)
            if self.level >= 3:
                self.monstre(Fantome)
                self.monstre(Fantome)
                self.monstre(Fantome)
            if self.level >= 5:
                self.monstre(Grand_Fantome)
        else:
            self.monstre(Big_Fantome)

    def game_over(self):
        print("game over")
        self.son.play("game_over")
        self.all_monstres = pygame.sprite.Group()
        self.boss_event.boss = pygame.sprite.Group()
        self.joueur.vie = self.joueur.vie_max
        self.is_playing = False
        self.score = 0
        self.level = 0

    def update(self):
        self.boss_event.add_percent()
        score_text = self.font.render(f"score : {self.score}", 1, (255, 255, 255))
        level_text = self.font.render(f"level : {self.level}", 1, (255, 255, 255))
        fenetre.blit(score_text, (20, 20))
        fenetre.blit(level_text, (20, 40))
        # montrer le joueur
        fenetre.blit(jeu.joueur.image, jeu.joueur.rect)
        # bar de vie du joueur
        jeu.joueur.update_vie_bar(fenetre)
        # munition
        jeu.joueur.all_munition.draw(fenetre)
        # monstre
        jeu.all_monstres.draw(fenetre)

        # diriger la munition
        for munition in jeu.joueur.all_munition:
            munition.move(jeu.joueur, jeu)
        for monstre in jeu.all_monstres:
            monstre.move()
            monstre.update_vie_bar(fenetre)

        for boss in self.boss_event.boss:
            boss.move()

        jeu.boss_event.boss.draw(fenetre)
        jeu.boss_event.update_bar(fenetre)

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
