import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):

    X_pos = 80
    Y_pos = 310
    Jump_speed = 8.5
    Y_pos_duck = 345

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.Jump_speed
        self.dino_duck = False

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()    

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN]:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False 
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_run = True     

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed * 4 #limite de altura
        self.jump_speed -= 0.8 #control hasta cuando deja de saltar

        if self.jump_speed < -self.Jump_speed:
            self.dino_rect.y = self.Y_pos
            self.dino_jump = False
            self.jump_speed = self.Jump_speed

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos_duck
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))