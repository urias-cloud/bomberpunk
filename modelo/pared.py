import pygame

class Pared:
    def __init__(self, x, y, tipo="fija"):
        """Metodo constructor de una pared"""
        self.rectangulo = pygame.Rect(x, y, 32, 32)
        self.tipo = tipo #puede ser fija(no se puede destruir) o debil(se puede destruir)
        self.visible = True

        if tipo == "fija":
            self.color = (100, 100, 100) #si es irrompible la hacemos gris
        elif tipo == "debil":
            self.color = (150, 75, 0) #si es rompible la hacemos marron

    def destruir(self):
        """Metodo que oculta la parde cuando una pocion explote(futuro desarrollo)"""
        if self.tipo == "debil":
            self.visible = False

    def dibujar(self, pantalla):
        """Metodo que dibuja las paredes"""
        if self.visible:
            pygame.draw.rect(pantalla, self.color, self.rectangulo)
