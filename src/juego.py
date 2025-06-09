import pygame
from jugador import Jugador

class Juego:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Bomberpunk")
        self.clock = pygame.time.Clock()
        self.running = True
        self.jugador = Jugador(100, 100)

    def iniciar(self):
        while self.running:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jugador.colocar_pocion()
            
            self.jugador.mover(keys)

            self.screen.fill((20, 20, 20))  # fondo negro cyberpunk
            self.jugador.draw(self.screen)

            for pocion in self.jugador.pociones:
                pocion.actualizar()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
