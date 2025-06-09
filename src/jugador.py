import pygame 
from pocion import Pocion
class Jugador:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.color = (0, 0, 255)
        self.velocidad = 4
        self.pociones = []

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
        pygame.draw.rect(pantalla, self.color, self.rectangulo)


