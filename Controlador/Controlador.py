import pygame
import sys
import random
from Modelos.Bomba import Bomba
from Vista.BombaGrafica import BombaGrafica



class Controlador:
    """ clase controlador , encargada de gestionar los eventos (colisones ,teclas presionadas,comportamiento de jugador  y enemigos ) y dibujar los objetosen la pantalla"""
    
    def __init__(self, jugador_grafico, mapa_grafico, ancho_pantalla, alto_pantalla, tamano_celda):
        """constructor de la clase recibe el jugador grafico , mapa grafico , las medidas de la pantalla y el tamaño de las celdas"""
        self.jugador_grafico = jugador_grafico
        self.mapa_grafico = mapa_grafico
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
        self.tamano_celda = tamano_celda
        self.bombas_activas_logicas = []#lista para almacerans las bombas logicas qestan activas(no explotadas)
        self.bombas_activas_graficas = []#lista para almacerans las bombas graficas qestan activas
        self.ultimo_danio_jugador = 0 # atributo para saber cuando tubo el utlomo daño recibido
        self.cooldown_invulnerabilidad = 1000 #  el cooldown  sirve para cuando jugador recibe daño lo haga cada un segundo sino en cada freim (60 por segundo) le descontaba vida y lo mataba enseguida

        

    def manejo_de_eventos(self):
        """metodo que maneja los eventos al precionar teclas colisones daños de bombas movimientos de los enemigos y jugadores"""
        tiempo_actual = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # si se presiona la barra coloca una bomba en la posicion del jugador
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bomba = self.jugador_grafico.modelo.atacar(tiempo_actual)#aca se ve que gracias a la compopsion puede acceder al metodo atacar del jugador logico pero mediante el jugador grafico
                    if bomba:
                        bomba_grafica = BombaGrafica(
                            bomba.pos_x, bomba.pos_y, (255, 0, 0), bomba, self.tamano_celda
                        )
                        self.bombas_activas_logicas.append(bomba)#agrega las bombas logica y graficas a sus respectivas listas
                        self.bombas_activas_graficas.append(bomba_grafica)

        teclas = pygame.key.get_pressed()
        x = self.jugador_grafico.modelo.pos_x
        y = self.jugador_grafico.modelo.pos_y
        velocidad = 5

        if teclas[pygame.K_UP]:
            y -= velocidad
        if teclas[pygame.K_DOWN]:
            y += velocidad
        if teclas[pygame.K_LEFT]:
            x -= velocidad
        if teclas[pygame.K_RIGHT]:
            x += velocidad

        rect_prueba = pygame.Rect(x, y, self.tamano_celda, self.tamano_celda)#se crea un rectangulo de prueva de la clkase Rect para comprobar si colisiona con una pared
        puede_mover = True#iniicaliza con la condicion para moverse en true
        for pared in self.mapa_grafico.obtener_paredes_graficas_activas():#recorre el mapa logico atraves del mapa grafico en su arreglo de pares activas(no destruidas)
            if rect_prueba.colliderect(pared.rect):#si colisiona con una pared , su condicion para moverse cambia a false 
                puede_mover = False
                break
        #si se puede mover:a jugador logico lo mueve y tambien actualiza la posion de jugador grafico
        if puede_mover:
                self.jugador_grafico.modelo.mover(x, y)
                self.jugador_grafico.actualizar_posicion()

        # movimiento y colisiones de enemigos
        enemigos_graficos_a_eliminar = []#lista para almacenar los enemigos graficos que fueron eliminados, asi tambien los elimina de la lista logica
        #de esta forma si muere no los dinuja pero tambien los elimina logicamente y no quedan "zombies" por mas q no se dibujen

        for enemigo_grafico_individual in self.mapa_grafico.enemigos:#aca le decimos q por cada enemigo grafico de la lista de enemigos del mapa grafico calcularemos su posicon tentativa para moverse
            if enemigo_grafico_individual.modelo.esta_vivo():
        
                # mover_ia devuelve la (nueva_x, nueva_y) deseada por la ia
                posicion_tentativa_x, posicion_tentativa_y = enemigo_grafico_individual.modelo.mover_ia(tiempo_actual)
                
                # se crea un rectangulo  de prueba para colision con paredes
                rect_enemigo_prueba = pygame.Rect(posicion_tentativa_x, posicion_tentativa_y, self.tamano_celda, self.tamano_celda)

                colisiona_con_pared = False#estado de colision con la pared comienza en false
                for pared in self.mapa_grafico.obtener_paredes_graficas_activas():# para cada pared en las paredes graficas activas (no destruidas) vemos si el rectangulo de prueba colisiona con pared 
                    if rect_enemigo_prueba.colliderect(pared.rect):
                        colisiona_con_pared = True#si colisiona cambia condicon a true
                        enemigo_grafico_individual.modelo.cambiar_direccion()
                        break

                colisiona_con_otro_enemigo = False#aca al igual que con la pared comprova,os si colisiona con enemigo , asi cambia su direcion
                if not colisiona_con_pared: 
                    for otro_enemigo_grafico in self.mapa_grafico.enemigos:# itera sobre  los enemigos para ver si colisiona con otro enemigo
                        # comprobamos de que no es el mismo enemigo y que el otro enemigo estevivo
                        if otro_enemigo_grafico != enemigo_grafico_individual and otro_enemigo_grafico.modelo.esta_vivo():
                            rect_otro_enemigo = pygame.Rect(
                                otro_enemigo_grafico.modelo.pos_x,
                                otro_enemigo_grafico.modelo.pos_y,
                                self.tamano_celda,
                                self.tamano_celda
                            )
                            if rect_enemigo_prueba.colliderect(rect_otro_enemigo):# si colisiona con otro enemigo cambia de dirección (aleatoreamente)
                                colisiona_con_otro_enemigo = True#cambia la condicion
                                enemigo_grafico_individual.modelo.cambiar_direccion() # enemigo actual cambia de direccion
                                otro_enemigo_grafico.modelo.cambiar_direccion() # el otro enemigo tambien cambia diorecion
                                break #corta porque no se necesita revisar otros enemigos

                # si no colisiona con una pared Y  otro enemigo se mueve
                if not colisiona_con_pared and not colisiona_con_otro_enemigo:
                    enemigo_grafico_individual.modelo.mover(posicion_tentativa_x, posicion_tentativa_y)#recibe las posiones tentativas de parametro
                
                # actualiza la posicion enemigo grafico para que coincida con el enemigo logico (si se movió o no)
                enemigo_grafico_individual.actualizar_posicion() # siempre hay q actualizar los graficos

                # colisione de jugador con enemigos, creando rectangulos para detectar las coliciones(rect_jugador y rect_enemigo):
                if self.jugador_grafico.modelo.esta_vivo() and enemigo_grafico_individual.modelo.esta_vivo():#si jugador logico y grafico estan vivos
                    rect_jugador = pygame.Rect(self.jugador_grafico.modelo.pos_x, self.jugador_grafico.modelo.pos_y, self.tamano_celda, self.tamano_celda)
                    rect_enemigo = pygame.Rect(enemigo_grafico_individual.modelo.pos_x, enemigo_grafico_individual.modelo.pos_y, self.tamano_celda, self.tamano_celda)

                    if rect_jugador.colliderect(rect_enemigo):#si colisona jugador recibe daño,pero usa cooldown para controlar que no muera enseguida
                       if tiempo_actual - self.ultimo_danio_jugador > self.cooldown_invulnerabilidad:
                            self.jugador_grafico.modelo.recibir_danio(enemigo_grafico_individual.modelo.calcular_danio())
                            self.ultimo_danio_jugador = tiempo_actual # actualiza el tiempo del daño para calcular posteriormente en futura colision
            # si enemigo logico murio , agrega enemigo grafico a la lista de enemigos graficos a eliminar
            if not enemigo_grafico_individual.modelo.esta_vivo():
                enemigos_graficos_a_eliminar.append(enemigo_grafico_individual)

        # elimina los enemigos muertos de la lista del mapa grafico
        for enemigo_muerto_grafico in enemigos_graficos_a_eliminar:
            self.mapa_grafico.enemigos.remove(enemigo_muerto_grafico)

        # bombas y explosiones:
        bombas_a_eliminar = []
        bombas_graficas_a_eliminar = []

        for i, bomba in enumerate(self.bombas_activas_logicas):
            if bomba.estado_bomba(tiempo_actual): #si la bomba  logica exploto
                explosion = pygame.Rect(
                    bomba.pos_x - bomba.alcance, bomba.pos_y - bomba.alcance,
                    self.tamano_celda + 2 * bomba.alcance,
                    self.tamano_celda + 2 * bomba.alcance
                )

                # colision de explosion a jugador,siempre y cuando esl jugador logico este vivo y explosion colisiono con jugador le aplica daño al jugador
                if self.jugador_grafico.modelo.esta_vivo() and explosion.colliderect(pygame.Rect(self.jugador_grafico.modelo.pos_x, self.jugador_grafico.modelo.pos_y, self.tamano_celda, self.tamano_celda)):
                    self.jugador_grafico.modelo.recibir_danio(bomba.calcular_danio())

                # colision de  explocion a enemigos
                enemigos_afectados_por_explosion = []#alkmacena los enemigos alcanzados por la explocion
                for enemigo_grafico_individual in self.mapa_grafico.enemigos:
                    if enemigo_grafico_individual.modelo.esta_vivo():
                        rect_enemigo = pygame.Rect(enemigo_grafico_individual.modelo.pos_x, enemigo_grafico_individual.modelo.pos_y, self.tamano_celda, self.tamano_celda)
                        if explosion.colliderect(rect_enemigo):
                            enemigo_grafico_individual.modelo.recibir_danio(bomba.calcular_danio())
                            if not enemigo_grafico_individual.modelo.esta_vivo():
                                enemigos_afectados_por_explosion.append(enemigo_grafico_individual)

                # elimninamos enemigos que murieron por la explosion (se limpian al final del bucle de enemigos)
                for enemigo_muerto_por_bomba in enemigos_afectados_por_explosion:
                    if enemigo_muerto_por_bomba not in enemigos_graficos_a_eliminar: # evita que haya duplicados si ya estaban marcados
                        enemigos_graficos_a_eliminar.append(enemigo_muerto_por_bomba)

                # destruir paredes que puedesn destruirse("destruibles")
                paredes_logicas_a_eliminar = [] # no elimina  pared grafica, su modelo logico se actualiza
                for pared_logica in self.mapa_grafico.modelo.obtener_paredes_activas():
                    rect_pared = pygame.Rect(pared_logica.pos_x, pared_logica.pos_y, self.tamano_celda, self.tamano_celda)
                    if explosion.colliderect(rect_pared) and pared_logica.tipo == "destruible":
                        if pared_logica.destruir(): # destruyela pared logica ,si lo hace:deja de dibujar pared grafic
                            pass 

                bombas_a_eliminar.append(bomba)
                bombas_graficas_a_eliminar.append(self.bombas_activas_graficas[i])

                if self.jugador_grafico.modelo.bomba_activa == bomba:
                    self.jugador_grafico.modelo.bomba_activa = None
        #se eliminan bombas logicas y graficas ya explotadas
        for b in bombas_a_eliminar:
            self.bombas_activas_logicas.remove(b)
        for g in bombas_graficas_a_eliminar:
            self.bombas_activas_graficas.remove(g)

        