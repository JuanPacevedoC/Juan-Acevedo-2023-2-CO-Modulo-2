import pygame
import random

from dino_runner.components.obstacles.captus import Cactus
from dino_runner.components.obstacles.largeCaptus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    Enemy = random.randint(0, 3)

    def update(self, game):
        if len(self.obstacles) == 0:
            if self.Enemy == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 3) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 3) == 2 or random.randint(0, 3) == 3:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("collision")
                pygame.time.delay(1000)
                game.death_count += 1
                game.playing = False
                break                 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 

    def reset_obstacle(self):
        self.obstacles = []        