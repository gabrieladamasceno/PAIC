import sys
import pygame
import math
from random import randrange, choice, uniform
from classe_disco import Disco

'''Quantidade partículas'''
num = int(input("Número de discos: "))

'''Resolução da Tela'''
resolution = [2000, 1000]
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('CAIXA')

'''Cores'''
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
BROWN = [128, 0, 0]

'''Classe Game'''
class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.gameObjects = []

    def load(self):
        matriz = []
        overlapping = False
        i = 0
        protecao = 0
        while len(matriz) < num:
            rad = randrange(20, 30)
            mass = 1
            disco = Disco(choice([BLACK, WHITE, RED, BROWN]), randrange(rad, (resolution[0] - rad)), randrange(rad, (resolution[1] - rad)), 0.15, 0.15, rad, mass, uniform(0.5, 2))

            overlapping = False
            for j in range(len(matriz)):
                outro = matriz[j]
                dx = (disco.x - outro.x)
                dy = (disco.y - outro.y)
                distancia = math.sqrt(dx*dx + dy*dy)
                if distancia < (disco.radius + outro.radius):
                    overlapping = True
                    break

            if overlapping == False:
                matriz.append(disco)
                self.gameObjects.append(disco)

            i = i + 1
            protecao = protecao + 1
            if protecao > 100000:
                break



    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


    def run(self):
        while True:
            self.handleEvents()
            self.screen.fill(GREEN)

            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

                tecla = pygame.key.get_pressed()
                if tecla[13] == 0:
                    gameObj.update(self.gameObjects)
                if tecla[13] == 1:
                    gameObj.velo_media(self.gameObjects)
            self.clock.tick(30)
            pygame.display.flip()
