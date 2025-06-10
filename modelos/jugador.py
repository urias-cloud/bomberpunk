import pygame 
from modelos.pocion import Pocion

AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

class Jugador:
    """Metodo constructor de la clase Jugador"""
    def __init__(self, x, y):
        
        self.rect = pygame.Rect(x, y, 32, 32)
        self.color = AZUL
        self.velocidad = 2 #esta es la velocidad del jugador
        self.pociones = [] #este vendria a ser el inventario/mochila donde se guarda la cantidad de pociones

    def mover(self, teclas):
        """Metodo para que el jugador se pueda mover"""
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad
    def colocar_pocion(self):
        """Metodo que coloca una pocion y que la suma al inventario"""
        pocion = Pocion(self.rect.x, self.rect.y)
        self.pociones.append(pocion)

    def dibujar(self, pantalla):
        """Metodo para dibujar al jugador"""
        pygame.draw.rect(pantalla, self.color, self.rect)


