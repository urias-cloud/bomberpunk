import pygame
from modelo.jugador import Jugador
from vista.jugador_vista import JugadorVista

class Juego:
    """Clase principal del juego que combina modelo, vista, y controlador"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Bomberpunk")
        self.clock = pygame.time.Clock()
        self.running = True

        self.jugador = Jugador(100, 100)
        self.jugador_vista = JugadorVista(self.jugador)

    def iniciar(self):
        while self.running:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(60)
        pygame.quit()
    def manejar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jugador.colocar_pocion()
            
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.jugador.mover_izquierda
        if teclas[pygame.K_RIGHT]:
            self.jugador.mover_derecha
        if teclas[pygame.K_UP]:
            self.jugador.mover_arriba
        if teclas[pygame.K_DOWN]:
            self.jugador.mover_abajo
    def actualizar(self):
        for pocion in self.jugador.pociones:
            pocion.actualizar()
