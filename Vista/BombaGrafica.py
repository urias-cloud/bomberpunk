import pygame

class BombaGrafica:
    def __init__(self, x, y, color, modelo, tamano_celda):
        self.rect = pygame.Rect(x, y, tamano_celda, tamano_celda)
        self.color = color
        self.modelo = modelo

    def dibujar(self, pantalla):
        if not self.modelo.explotada:
            pygame.draw.circle(pantalla, self.color, self.rect.center, self.rect.width // 2)
