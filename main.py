import pygame
import sys

from Modelos.Jugador import Jugador
from Modelos.Enemigo import Enemigo
from Modelos.Mapa import Mapa

from Vista.PersonajeGrafico import PersonajeGrafico
from Vista.MapaGrafico import MapaGrafico
from Vista.BombaGrafica import BombaGrafica

from Controlador.Controlador import Controlador

TAMANO_CELDA = 30
NUM_COLUMNAS = 27
NUM_FILAS = 20
ANCHO_PANTALLA = NUM_COLUMNAS * TAMANO_CELDA
ALTO_PANTALLA = NUM_FILAS * TAMANO_CELDA


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Bomberman MVC")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Arial", 20)

    mapa_logico = Mapa(TAMANO_CELDA)
    mapa_grafico = MapaGrafico(mapa_logico, TAMANO_CELDA)

    jugador_logico = Jugador("Bomberman", 100, TAMANO_CELDA, TAMANO_CELDA)
    enemigo_logico = Enemigo("Enemigo", 100, 3*TAMANO_CELDA, 3*TAMANO_CELDA, 3, "normal")
    
    
    jugador_grafico = PersonajeGrafico(jugador_logico.pos_x, jugador_logico.pos_y, (0, 0, 255), jugador_logico, TAMANO_CELDA)
    enemigo_grafico = PersonajeGrafico(enemigo_logico.pos_x, enemigo_logico.pos_y, (255, 0, 0), enemigo_logico, TAMANO_CELDA)
    


    controlador = Controlador(
        jugador_grafico,
        enemigo_grafico,
        mapa_logico,
        mapa_grafico,
        ANCHO_PANTALLA,
        ALTO_PANTALLA,
        TAMANO_CELDA
    )

    ejecutando = True
    while ejecutando:
        controlador.manejo_de_eventos()

        pantalla.fill((0, 0, 0))

        mapa_grafico.dibujar(pantalla)

        if jugador_logico.esta_vivo():
            jugador_grafico.dibujar(pantalla)
        if enemigo_logico.esta_vivo():
            enemigo_grafico.dibujar(pantalla)

        for bomba in controlador.bombas_activas_graficas:
            bomba.dibujar(pantalla)

        texto_vida = fuente.render(f"Vida: {jugador_logico.vida}", True, (255, 255, 255))
        pantalla.blit(texto_vida, (10, 10))

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
