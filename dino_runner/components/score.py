import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT , SCREEN_WIDTH

class Score:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2 
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    def __init__(self):
        self.score = 0
        self.highest_score = 0

    def update_score(self, game):
        self.score += 1
        if self.score % 200 == 0 and game.game_speed < 500:
            game.game_speed += 5

    def  draw_score(self, screen):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(f'score {self.score}', True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (1000, 50)
        screen.blit(self.text, self.text_rect)

    def reset_score(self):
        self.score = 0    
        
    def show_score(self, screen):
        self.text = self.font.render(f'Your Score: {self.score}', True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)
        screen.blit(self.text, self.text_rect)


    def show_highest_score(self, screen):
        if self.score > self.highest_score:
            self.highest_score = self.score

        self.text = self.font.render(f'Your highest Score: {self.highest_score}', True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 80)
        screen.blit(self.text, self.text_rect)  
