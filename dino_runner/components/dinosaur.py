import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING

class Dinosaur(Sprite):

    X_pos = 80
    Y_pos = 310
    Jump_speed = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.Jump_speed

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()


        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True

        if self.step_index >= 10:
            self.step_index = 0

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
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))