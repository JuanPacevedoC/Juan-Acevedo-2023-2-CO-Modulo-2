import pygame
import random

from dino_runner.components.obstacles.captus import Cactus
from dino_runner.components.obstacles.largeCaptus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    # def generate_obstacle(self):
    #     obstacle = Cactus(SMALL_CACTUS)
    #     return obstacle    

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("collision")
                pygame.time.delay(1000)
                game.playing = False
                break                 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)   