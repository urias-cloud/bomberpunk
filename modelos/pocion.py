import pygame
import time 

class Pocion:
    def __init__(self, x, y, timer = 3):
        self.rectangulo = pygame.Rect(x, y, 32, 32) #dibuja el rectangulo
        self.timer = timer #tiempo que tarda en explotar la pocion
        self.tiempo_inicial = time.time() #esto guarda el tiempo en el que se coloco la pocion
        self.color = (0, 255, 0) #color verde
        self.explotada = False #esto es para saber si la pocion exploto o no
        self.radio = 32 #este es el radio de la explosion

    def actualizar(self):
        """Metodo que verificica cuanto tiempo paso desde que se puso la bomba, este metodo se ejecuta todo el tiempo"""
        if not self.explotada and time.time() - self.tiempo_inicial >= self.timer: #el time.time nos da el tiempo actual, el tiempo inicial es el tiempo en el que se creo la pocion al hacer la resta se obtiene cuantos segundos paso desde que se coloco
            self.explotar()

    def explotar(self):
        """Metodo que hace que una bomba explote"""
        self.explotada = True
        print("Pocion Exploto")

    def dibujar(self, pantalla):
        """La idea con este metodo seria dibujar la bomba"""
        if not self.explotada:
            pygame.draw.rect(pantalla, self.color, self.rectangulo)