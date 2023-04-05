import random
from dino_runner.components.obstacles.obstacles import Obstacle

class Bird(Obstacle):
    Bird_Hight = [200, 250, 310]

    def __init__(self, image):
        self.type = 0 
        super().__init__(image, self.type)
        self.rect.y = self.Bird_Hight[random.randint(0, 2)]  #posicion  del ave
        self.index = 0

    #cambio de imagen cada 5 veces, las primeras 5 veces se que se llama esta funcion draw se llama la primera imagen de bird para despues cambiar de imagen hasta resetear el self.index y volver a tener la misma animacion anterior
    def draw(self, screen):
        if self.index >= 9: 
            self.index = 0
        screen.blit(self.image[self.index//5], (self.rect.x, self.rect.y)) 
        self.index += 1    