import pygame

class ParedGrafica:
    def __init__(self, x, y, color, modelo, tamano_celda):
        self.rect = pygame.Rect(x, y, tamano_celda, tamano_celda)
        self.color = color
        self.modelo = modelo

    def dibujar(self, pantalla):
        if not self.modelo.esta_destruida():
            pygame.draw.rect(pantalla, self.color, self.rect)
