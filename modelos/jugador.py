import pygame 
from modelos.pocion import Pocion

AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

class Jugador:
    def __init__(self, x, y):
        
        self.rect = pygame.Rect(x, y, 32, 32)
        self.color = AZUL
        self.velocidad = 2 #esta es la velocidad del jugador
        self.pociones = [] #este vendria a ser el inventario/mochila donde se guarda la cantidad de bombas

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad
    def colocar_pocion(self):
        pocion = Pocion(self.rect.x, self.rect.y)
        self.pociones.append(pocion)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)


