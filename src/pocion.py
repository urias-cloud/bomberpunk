import pygame
import time 

class Pocion:
    def __init__(self, x, y, timer = 3):
        self.rectangulo = pygame.Rect(x, y, 32, 32)
        self.timer = timer
        self.tiempo_inicial = time.time()
        self.color = (0, 255, 255)
        self.explotada = False

    def actualizar(self):
        if not self.explotada and time.time - self.tiempo_inicial >= self.timer:
            self.explotar()

    def explotar(self):
        self.explotada = True
        print("Pocion Exploto")

    def dibujar(self, pantalla):
        if not self.explotada:
            pygame.draw.rect(pantalla, self.color, self.rectangulo)