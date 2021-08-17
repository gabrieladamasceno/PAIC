import sys
import pygame
import math
from random import randrange, choice, uniform
from classe_disco import Disco
from scipy.stats import maxwell
import matplotlib.pyplot as plt
import numpy as np


'''Quantidade partículas'''

print("Bem-vindo a simulação!")
num = int(input("Número de partículas entre 10 e 200: "))
if 9 < num < 201:
    print("\nPara analisar o gráfico de Histogramas pressione F1 \nPara analisar o gráfico de Dispersão pressione F2")
    print("\nPara alterar o potencial gravitacional tecle: \n[F4] para dobrar \n[F5] para quadruplicar \n[F6] para dividir por 1/2 \n[F7] para dividir por 1/4")

    '''Resolução da Tela'''
    resolution = [1200, 800]
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption('Simulação Discos Rígidos')

    '''Cores'''
    BLACK = [0, 0, 0]
    WHITE = [255, 255, 255]
    GREEN = [0, 255, 0]
    RED = [255, 0, 0]
    BROWN = [128, 0, 0]

    '''Classe Game'''
    class Game:

        gravidade = 1
        def __init__(self):
            pygame.init()

            self.screen = pygame.display.set_mode(resolution)
            self.clock = pygame.time.Clock()
            self.gameObjects = []

        def operacao(self, g, m):
            gr = g*m
            #print(gr)
            if 0 < gr < 16:
                return gr
            else:
                print("Limite gravitacional alcançado, faça outra operação!")
                return g


        def load(self):
            matriz = []
            overlapping = False
            i = 0
            protecao = 0
            while len(matriz) < num:
                rad = 5
                mass = 1
                disco = Disco(choice([BLACK, GREEN, RED, BROWN]), randrange(rad, (resolution[0] - rad)), randrange(rad, (resolution[1] - rad)), 0.1, 0.1, rad, mass, self.gravidade)

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
                    self.histograma()
                    self.dispersao()
                    self.altura()
                    sys.exit(0)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_F1]:
                    self.histograma()

                if keys[pygame.K_F2]:
                    self.dispersao()

                if keys[pygame.K_F4]:
                    self.gravidade = self.operacao(self.gravidade, 2)
                    print(f"A gravidade agora é {self.gravidade} vezes a inicial e o dobro da anterior!")

                if keys[pygame.K_F5]:
                    self.gravidade = self.operacao(self.gravidade, 4)
                    print(f"A gravidade agora é {self.gravidade} vezes a inicial e o quádruplo da anterior!")

                if keys[pygame.K_F6]:
                    self.gravidade = self.operacao(self.gravidade, 0.5)
                    print(f"A gravidade agora é {self.gravidade} vezes a inicial e a metade da anterior!")

                if keys[pygame.K_F7]:
                    self.gravidade = self.operacao(self.gravidade, 0.25)
                    print(f"A gravidade agora é {self.gravidade} vezes a inicial e um quarto da anterior!")

                if keys[pygame.K_F8]:
                    self.altura()

        def run(self):
            while True:
                self.handleEvents()
                self.screen.fill(WHITE)

                for gameObj in self.gameObjects:
                    gameObj.draw(self.screen)
                    gameObj.update(self.gameObjects, self.gravidade)
                self.clock.tick(30)
                pygame.display.flip()


        def histograma(self):
            fig, ax = plt.subplots(1, 1)

            # Parâmetros
            x = np.linspace(maxwell.ppf(0.01), maxwell.ppf(0.99), num)
            ax.plot(x, maxwell.pdf(x), 'g-', lw=5, alpha=0.6, label='Curva de Maxwell-Boltzman')
            y = maxwell.pdf(x)

            # Parametros Histograma
            r = maxwell.rvs(size=1000)
            ax.hist(r, density=True, histtype='stepfilled', alpha=0.2, color=None, label= f"Histograma com {num} partículas")

            # Plotar Gráfico
            ax.legend(loc='upper right', frameon= True)
            '''print("Percentual de pontos de função: ")
            print(x)
            print("--------------------------------------------------------------------")
            print("Probabilidade de densidade de função: ")
            print(y)'''
            plt.xlabel("Velocidade (km/s)", size=10)
            plt.ylabel("Densidade de Probabilidade (s/km)", size=10)
            plt.show()

        def dispersao(self):
            posY = []
            X = []

            for disco in self.gameObjects:
                posY.append(disco.y)
                X.append(disco.x)

            #Inversão do eixo Y
            lista = [resolution[1]]*num
            a = np.array(posY)
            b = np.array(lista)
            Y = -1*(a - b)

            '''print("---------------------------------------------------------")
            print(f"Posição Y {Y}")
            print(f"Posição X {X}")'''

            fig, ax = plt.subplots(1, 1)
            colors = np.random.rand(num)
            plt.scatter(X, Y, c=colors, label= f"{num} partículas e {self.gravidade} vezes o potencial inicial")
            ax.legend(loc = 'best', borderpad = 1)
            plt.xlabel("Posição X", size=9)
            plt.ylabel("\nPosição Y", size=9)
            plt.show()

        def altura(self):
            pass



else:
    print("Digite um número de partículas válido!")