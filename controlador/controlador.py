import pygame
import sys
from Modelos.Bomba import Bomba
from Vista.BombaGrafica import BombaGrafica

class Controlador:
    def __init__(self, jugador1_grafico, enemigo_grafico, modelo_mapa, mapa_grafico, ancho_pantalla, alto_pantalla, tamano_celda):
        self.jugador1_grafico = jugador1_grafico
        self.enemigo_grafico = enemigo_grafico
        self.jugador1_logico = jugador1_grafico.modelo
        self.enemigo_logico = enemigo_grafico.modelo
        self.modelo_mapa = modelo_mapa
        self.mapa_grafico = mapa_grafico
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
        self.tamano_celda = tamano_celda
        self.bombas_activas_logicas = []
        self.bombas_activas_graficas = []

    def manejo_de_eventos(self):
        tiempo_actual = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bomba = self.jugador1_logico.atacar(tiempo_actual)
                    if bomba:
                        bomba_grafica = BombaGrafica(
                            bomba.pos_x, bomba.pos_y, (255, 0, 0), bomba, self.tamano_celda
                        )
                        self.bombas_activas_logicas.append(bomba)
                        self.bombas_activas_graficas.append(bomba_grafica)

        teclas = pygame.key.get_pressed()
        nueva_x = self.jugador1_logico.pos_x
        nueva_y = self.jugador1_logico.pos_y
        velocidad = self.jugador1_logico.velocidad

        if teclas[pygame.K_UP]:
            nueva_y -= velocidad
        if teclas[pygame.K_DOWN]:
            nueva_y += velocidad
        if teclas[pygame.K_LEFT]:
            nueva_x -= velocidad
        if teclas[pygame.K_RIGHT]:
            nueva_x += velocidad

        rect_prueba = pygame.Rect(nueva_x, nueva_y, self.tamano_celda, self.tamano_celda)
        puede_mover = True
        for pared in self.mapa_grafico.obtener_paredes_graficas_activas():
            if rect_prueba.colliderect(pared.rect):
                puede_mover = False
                break

        if puede_mover:
            self.jugador1_logico.mover(nueva_x, nueva_y)
            self.jugador1_grafico.actualizar_posicion()

        nueva_ex, nueva_ey = self.enemigo_logico.mover_ia(tiempo_actual)
        rect_enemigo_prueba = pygame.Rect(nueva_ex, nueva_ey, self.tamano_celda, self.tamano_celda)
        colisiona = any(rect_enemigo_prueba.colliderect(p.rect) for p in self.mapa_grafico.obtener_paredes_graficas_activas())

        if not colisiona:
            self.enemigo_logico.mover(nueva_ex, nueva_ey)
            self.enemigo_grafico.actualizar_posicion()

        rect_jugador = pygame.Rect(self.jugador1_logico.pos_x, self.jugador1_logico.pos_y, self.tamano_celda, self.tamano_celda)
        rect_enemigo = pygame.Rect(self.enemigo_logico.pos_x, self.enemigo_logico.pos_y, self.tamano_celda, self.tamano_celda)

        if rect_jugador.colliderect(rect_enemigo):
            self.enemigo_logico.atacar(self.jugador1_logico, tiempo_actual)

        bombas_a_eliminar = []
        graficas_a_eliminar = []

        for i, bomba in enumerate(self.bombas_activas_logicas):
            if bomba.estado_bomba(tiempo_actual):
                explosion = pygame.Rect(
                    bomba.pos_x - bomba.alcance, bomba.pos_y - bomba.alcance,
                    self.tamano_celda + 2 * bomba.alcance,
                    self.tamano_celda + 2 * bomba.alcance
                )
                if explosion.colliderect(rect_jugador):
                    self.jugador1_logico.recibir_danio(bomba.calcular_danio())
                if explosion.colliderect(rect_enemigo):
                    self.enemigo_logico.recibir_danio(bomba.calcular_danio())

                    # Destruir paredes si son destruibles
                for pared in self.modelo_grafico.modelo_mapa.obtener_paredes_activas():
                    rect_pared = pygame.Rect(pared.pos_x, pared.pos_y, self.tamano_celda, self.tamano_celda)
                    if explosion.colliderect(rect_pared):
                        pared.destruir()
                

                bombas_a_eliminar.append(bomba)
                graficas_a_eliminar.append(self.bombas_activas_graficas[i])

                if self.jugador1_logico.bomba_activa == bomba:
                    self.jugador1_logico.bomba_activa = None

        for b in bombas_a_eliminar:
            self.bombas_activas_logicas.remove(b)
        for g in graficas_a_eliminar:
            self.bombas_activas_graficas.remove(g)
