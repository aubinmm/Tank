
import pygame
from boss import Boss
from monstre import *



class Level:
    def __init__(self, jeu):
        self.jeu = jeu
        self.number = 0
        self.percent = 0
        self.percent_speed = 15

        self.level_mode = "Monster"  #Monster ou Boss

    def update_level_advance(self, surface):
        self.percent += self.percent_speed / 100
        pygame.draw.rect(surface, (0, 0, 0), (0, surface.get_height() - 20, surface.get_width(), 10))
        pygame.draw.rect(surface, (53, 234, 64), (0, surface.get_height() - 20,surface.get_width() / 100 * self.percent, 10))


        if self.level_mode == "Monster":
            if not self.is_full_loaded():
                while len(self.jeu.all_monstres) < self.max_monstres("Tous"):
                    nb_f = 0
                    for f in self.jeu.all_monstres:
                        if f.type == "Fantomes":
                            nb_f +=1
                    if nb_f < self.max_monstres("Fantome"):
                        self.jeu.monstre(Fantome)
                    nb_gf = 0
                    for gf in self.jeu.all_monstres:
                        if gf.type == "Grand_Fantomes":
                            nb_gf += 1
                    if nb_gf < self.max_monstres("Grand_Fantome"):
                        self.jeu.monstre(Grand_Fantome)
                    nb_bf = 0
                    for bf in self.jeu.all_monstres:
                        if bf.type == "Big_Fantomes":
                            nb_bf += 1
                    if nb_bf < self.max_monstres("Big_Fantome"):
                        self.jeu.monstre(Big_Fantome)

                    #print(self.jeu.all_monstres)
        if self.level_mode == "Init_Boss":
            while len(self.jeu.all_boss) < self.max_boss():
                self.jeu.all_boss.add(Boss(self.jeu))
            self.level_mode = "Boss"


        if self.level_mode == "Boss" and len(self.jeu.all_boss) == 0:
            self.level_mode = "Monster"
            self.start()
        if self.is_full_loaded() and self.level_mode == "Monster" and len(self.jeu.all_monstres) == 0:
                self.level_mode = "Init_Boss"
        #print(self.level_mode,len(self.jeu.all_monstres), len(self.jeu.all_boss))


        #Création des monstres


    def is_full_loaded(self):
        return self.percent >= 100

    def max_monstres(self,type_de_monstre):
        if type_de_monstre == "Tous":
            return self.max_monstres("Fantome") + self.max_monstres("Grand_Fantome") + self.max_monstres("Big_Fantome")
        if type_de_monstre == "Fantome":
            if self.number < 3:
                return 3
            if self.number < 5:
                return 5
        if type_de_monstre == "Grand_Fantome":
            if self.number < 3:
                return 0
            if self.number < 4:
                return 1
        if type_de_monstre == "Big_Fantome":
            if self.number < 5:
                return 0
            if self.number > 5:
                return 1

    def max_boss(self):
        if self.number < 3:
            return 3
        if self.number < 5:
            return 5

    def start(self):
        self.percent = 0
        self.number += 1
        if self.number > 1:
            self.jeu.score += 20
        self.level_mode = "Monster"

    def pour_commenter(self):
        if not self.number == 10:
            self.jeu.monstre(Fantome)
            self.jeu.monstre(Fantome)
            self.jeu.monstre(Fantome)
            if self.number >= 3:
                self.jeu.monstre(Fantome)
                self.jeu.monstre(Fantome)
                self.jeu.monstre(Fantome)
            if self.number >= 5:
                self.jeu.monstre(Grand_Fantome)
        else:
            self.jeu.monstre(Big_Fantome)


