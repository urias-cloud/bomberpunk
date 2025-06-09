import pygame

class Pared:
    def __init__(self, x, y, tipo="fija"):
        self.rectangulo = pygame.Rect(x, y, 32, 32)
        self.tipo = tipo
        self.visible = True

        if tipo == "fija":
            self.color = (100, 100, 100)
        elif tipo == "debil":
            self.color = (150, 75, 0)

    def destruir(self):
        if self.tipo == "debil":
            self.visible = False

    def dibujar(self, pantalla):
        if self.visible:
            pygame.draw.rect(pantalla, self.color, self.rectangulo)
