import sys
import pygame
import math
from random import randrange, random, choice


num = int(input("Número de discos: "))
resolution = [600, 600]

#Cores
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
BROWN = [128, 0, 0]

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('CAIXA')



class Disco:
    def __init__(self, cor, xPos, yPos, xVel, yVel, rad):
        self.cor = cor
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        #self.ax = xAcc
        #self.ay = yAcc
        #self.mass = m
        self.type = "disco"

    def debug(self, disco):
        dx = (self.x - disco.x)
        dy = (self.y - disco.y)
        distancia = math.sqrt(dx * dx + dy * dy)
        diametro = (self.radius + disco.radius)
        print(f"Self: Posição X = {self.x} Posição Y = {self.y} VelX = {self.dx} VelY = {self.y} raio = {self.radius}")
        print(f"Disco: Posição X = {disco.x} Posição Y = {disco.y} VelX = {disco.dx} VelY = {disco.y} raio = {disco.radius}")
        print(f"Distancia = {distancia} Diâmetro = {diametro}")

    def colision(self, disco):
        dx = (self.x - disco.x)
        dy = (self.y - disco.y)
        distancia = math.sqrt(dx*dx + dy*dy)
        diametro = (self.radius + disco.radius)
        if distancia <= diametro:
            self.debug(disco)
            self.dx *= -1
            self.dy *= -1
            disco.dx *= -1
            disco.dy *= -1


    #def force(self):
        #fx = self.ax/self.mass
        #fy = self.ay/self.mass

    def draw(self, screen):
        pygame.draw.circle(screen, self.cor, (int(self.x), int(self.y)), self.radius)

    def update(self, gameObjects):
            self.x += self.dx
            self.y += self.dy

            for disc in gameObjects:
                if disc != self:
                    self.colision(disc)


            if (self.x - self.radius <= 0 or self.x + self.radius  >= resolution[0]):
                self.dx *= -1
            if (self.y - self.radius  <= 0 or self.y + self.radius  >= resolution[1]):
                self.dy *= -1


class Game():
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
            rad = randrange(20, 50)
            disco = Disco(choice([BLACK, WHITE, RED, BROWN]), randrange(rad, (resolution[0] - rad)), randrange(rad, (resolution[1] - rad)), 1, 1, rad)

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
            if protecao > 10000:
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
                gameObj.update(self.gameObjects)


            self.clock.tick(30)
            pygame.display.flip()



game = Game()
game.load()
game.run()


