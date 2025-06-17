import pygame

"""CLase que sirve para representar al jugador
en la pantalla, usa si o si pygame
"""
class JugadorVista:
    def __init__(self, jugador, color=(0,0,255)):
        self.jugador = jugador
        self.color = color
    
    def dibujar(self, pantalla):
        rect = pygame.Rect(
            self.jugador.x,
            self.jugador y,
            self.jugador.ancho,
            self.jugador.alto
        )
        pygame.draw.rect(pantalla, self.color, rect)