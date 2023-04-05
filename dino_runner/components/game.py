import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacleManager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.score import Score

class Game:
    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('Press any key to start....', self.screen)
        self.running = False
        self.death_count = 0
        self.score = Score()
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()        

    def reset(self):
        self.obstacle_manager.reset_obstacle()
        self.player.reset_dinosaur()
        self.score.reset_score()
        self.game_speed = self.GAME_SPEED

    def run(self):
        self.reset()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update_score(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw_score(self.screen)
        self.draw_background()
        pygame.display.update()
        pygame.display.flip()
        
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
        HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message('Game Over, Press any key to start')
            self.score.show_score(self.screen)
            self.score.show_highest_score(self.screen)
            self.obstacle_manager.show_death_count(self, self.screen)
            self.menu.draw(self.screen)    

        self.screen.blit(ICON, (HALF_SCREEN_WIDTH -50, HALF_SCREEN_HEIGHT -140))
        self.menu.update(self)


