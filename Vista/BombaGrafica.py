import pygame
import os
class BombaGrafica:
    """clase bomba grafica , representa graficamente a la bomba logica"""
    def __init__(self, x, y, color, modelo, tamano_celda):
        """metodo constructor recibe coordenadas de la posicon su color , el modelo logico(bomba logica) para hacer la composicion y el tamaño de la celda"""
        self.rect = pygame.Rect(x, y, tamano_celda, tamano_celda) #crea el rectangulo q representa la bomba
        self.modelo = modelo
        #le asignamos la imagen a la bomba
        if modelo.tipo == "normal":
            ruta = os.path.join("assets", "bombados.png")#accedemos a la ruta de forma segura
        self.imagen_original = pygame.image.load(ruta).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen_original, (40,40))
    def dibujar(self, pantalla):
        """metodo que dinuja la bomba ,recibe la pantalla de parametro donde dibujara la bomba siempre cuando no este explotada"""
        if not self.modelo.explotada:
            imagen_rect = self.imagen.get_rect(center=self.rect.center)
            pantalla.blit(self.imagen, imagen_rect.topleft)
