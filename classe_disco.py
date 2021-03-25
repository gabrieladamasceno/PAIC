#Bibliotecas
import pygame
import math

#Resolução da Tela
resolution = [2000, 1000]

#Classe Disco
class Disco():
    def __init__(self, cor, xPos, yPos, xVel, yVel, rad, m,xAcc, yAcc):
        self.cor = cor
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.ax = xAcc
        self.ay = yAcc
        self.mass = m
        self.type = "disco"

    def debug(self, disco):
        dx = (self.x - disco.x)
        dy = (self.y - disco.y)
        distancia = math.sqrt(dx * dx + dy * dy)
        diametro = (self.radius + disco.radius)
        print(f"Self: Posição X = {self.x} Posição Y = {self.y} VelX = {self.dx} VelY = {self.dy} raio = {self.radius}")
        print(f"Disco: Posição X = {disco.x} Posição Y = {disco.y} VelX = {disco.dx} VelY = {disco.dy} raio = {disco.radius}")
        print(f"Distancia = {distancia} Diâmetro = {diametro}")

    def force(self):
        fx, fy = 1, 1
        self.ax = fx/self.mass
        self.ay = fy/self.mass

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




    #def new_velocity(self):



    def draw(self, screen):
        pygame.draw.circle(screen, self.cor, (int(self.x), int(self.y)), self.radius)


    def update(self, gameObjects):
        for disc in gameObjects:
            self.x += self.dx
            self.y += self.dy

            if (self.x - self.radius <= 0 or self.x + self.radius >= resolution[0]):
                self.dx *= -1
            if (self.y - self.radius <= 0 or self.y + self.radius >= resolution[1]):
                self.dy *= -1

            for disc in gameObjects:
                if self != disc:
                    self.colision(disc)
