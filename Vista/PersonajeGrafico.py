import pygame

class PersonajeGrafico:
    def __init__(self, x, y, color, modelo, tamano=30):
        self.rect = pygame.Rect(x, y, tamano, tamano)
        self.color = color
        self.modelo = modelo

    def actualizar_posicion(self):
        self.rect.x = self.modelo.pos_x
        self.rect.y = self.modelo.pos_y

    def dibujar(self, pantalla):
        if self.modelo.esta_vivo():
            pygame.draw.rect(pantalla, self.color, self.rect)

    def colisiona_con(self, otro_rect):
        return self.rect.colliderect(otro_rect)
