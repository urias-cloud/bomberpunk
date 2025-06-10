import pygame

ROJO = (255, 0, 0) #creamos el color rojo para usarlo en el enemigo

class Enemigo:
    """Metodo constructor del enemigo"""
    def _init_(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.color = ROJO
        self.velocidad = 1.5  # velocidad del enemigo, puede ser distinta al jugador

    def mover(self):
        """Metodo que le aplica movimiento al enemigo"""
        # Movimiento simple: por ejemplo, moverse hacia la derecha constantemente
        self.rect.x += self.velocidad

    def dibujar(self, pantalla):
        """Metodo que dibuja al enemigo"""
        pygame.draw.rect(pantalla, self.color, self.rect)