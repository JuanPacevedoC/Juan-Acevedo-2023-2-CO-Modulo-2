import pygame
from pygame.sprite import Sprite


from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, JUMPING_SHIELD,DUCKING_SHIELD,HAMMER_TYPE, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER, HAMMER

RUN_IMG = {DEFAULT_TYPE : RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
JUM_IMG = {DEFAULT_TYPE : JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = {DEFAULT_TYPE : DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}

class Dinosaur(Sprite):

    X_pos = 80
    Y_pos = 310
    Jump_speed = 8.5
    Y_pos_duck = 345
    Hammer_image = HAMMER
    Cord_hammer = 0
    Speed_hammer = 5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.Jump_speed
        self.dino_duck = False
        self.has_power_up = False
        self.power_time_up = 0
        self.dino_fly = False

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()    
        elif self.dino_fly:
            self.fly()     

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_fly = False
        elif user_input[pygame.K_DOWN]:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
            self.dino_fly = False
        elif user_input[pygame.K_RIGHT]:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = False
            self.dino_fly = True     
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_run = True     

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index += 1

    def jump(self):
        self.image = JUM_IMG[self.type]
        self.dino_rect.y -= self.jump_speed * 4 #limite de altura
        self.jump_speed -= 0.8 #control hasta cuando deja de saltar

        if self.jump_speed < -self.Jump_speed:
            self.dino_rect.y = self.Y_pos
            self.dino_jump = False
            self.jump_speed = self.Jump_speed

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos_duck
        self.step_index += 1
        self.dino_duck = False

    def fly(self):
        if self.type == HAMMER_TYPE:
            if self.dino_fly == True:
                self.dino_rect.y = 100
            else:
                self.dino_rect.y = self.Y_pos  

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

                


    def reset_dinosaur(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.Jump_speed
        self.dino_duck = False
        self.has_power_up = False
        self.power_time_up = 0
        self.dino_throw = False   