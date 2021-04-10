import pygame
import math

'''Resolução da Tela'''
resolution = [2000, 1000]
'''Classe Disco'''
class Disco:
    def __init__(self, cor, xpos, ypos, xvel, yvel, rad, m, yacc):
        self.cor = cor
        self.x = xpos
        self.y = ypos
        self.dx = xvel
        self.dy = yvel
        self.radius = rad
        self.ay = yacc
        self.mass = m
        self.type = "disco"

    def velo_module(self):
        norma = math.sqrt((self.dx ** 2) + (self.dy ** 2))
        return norma

    def pressao(self):
        p = (self.mass * self.ay)/(resolution[0]*resolution[1])
        return p
        pass

    def velo_media(self, gameObjects):
        velox = 0
        veloy = 0
        for i in range(len(gameObjects)):
            if self.dx > velox:
                velox = self.dx
            if self.dy > veloy:
                veloy = self.dx
        print(f"Velox {velox}")
        print(f"Velox {veloy}")


    def debug(self, disco):
        dx = (self.x - disco.x)
        dy = (self.y - disco.y)
        distancia = math.sqrt(dx * dx + dy * dy)
        diametro = (self.radius + disco.radius)
        energy_self = 0.5* (self.mass) * (self.velo_module())
        energy_disco = 0.5* (disco.mass) * (disco.velo_module())
        print(f"Self: Posição X = {self.x} Posição Y = {self.y}")
        print(f"VelX = {self.dx} VelY = {self.dy} raio = {self.radius}")
        print(f"Disco: Posição X = {disco.x} Posição Y = {disco.y}")
        print(f"VelX = {disco.dx} VelY = {disco.dy} raio = {disco.radius}")
        print(f"Energia Self = {energy_self} e Energia_disco = {energy_disco} ")


    def colision(self, disco):
        dx = (self.x - disco.x)
        dy = (self.y - disco.y)
        distancia = math.sqrt(dx*dx + dy*dy)
        diametro = (self.radius + disco.radius)
        if distancia <= diametro:
            print("****ANTES DA COLISÃO****")
            self.debug(disco)
            self.dx *= -1
            self.dy *= -1
            disco.dx *= -1
            disco.dy *= -1
            print("\n****DEPOIS DA COLISÃO****")
            self.debug(disco)
            print("-------------------------------------------")



    def draw(self, screen):
        pygame.draw.circle(screen, self.cor, (int(self.x), int(self.y)), self.radius)

    def update(self, gameObjects):
        for disco in gameObjects:
            self.dy += (1/60)*self.ay
            self.x += self.dx
            self.y += self.dy*(1/60)

            if self.x - self.radius <= 0 or self.x + self.radius >= resolution[0]:
                self.dx *= -1
            if self.y - self.radius <= 0 or self.y + self.radius >= resolution[1]:
                self.dy *= -1

            for disc in gameObjects:
                if self != disc:
                    self.colision(disc)

        tecla = pygame.key.get_pressed()
        if tecla[13] == 1:
            self.velo_media()
