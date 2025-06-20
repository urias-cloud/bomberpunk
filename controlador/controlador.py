import pygame
from modelos import Personaje
from modelos import Jugador 
from modelos import Enemigo  
from vista import PersonajeGrafico
from modelos import Pared#esta clase tiene que tener una lista con paredes activas


"""clase que controla y maneja los eventos"""
class Controlador:
	"""constructor de la clase ,recibe jugador1_grafico( jugador personajeGrafico)-jugador_grafico( enemigo personajeGrafico)-paredes_graficas_activas(lista de las paredes de personajeGrafico) """
	def __init__(self, jugador1_grafico, jugador2_grafico, paredes_graficas_activas, ancho_pantalla, alto_pantalla, tamano_celda):
            self.jugador1_grafico = jugador1_grafico
            #se guarda la referancia a los objetos/personajes graficos
            self.jugador2_grafico = jugador2_grafico
            self.jugador1_logico = jugador1_grafico.modelo
            #mediante los objetos graficos se accede a objetos logicos(de personaje grafico se accede a personaje logico)
            self.jugador2_logico = jugador2_grafico.modelo
            self.paredes_graficas_activas = paredes_graficas_activas  # lista que contiene las paredes de personajeGrafico
            self.ancho_pantalla = ancho_pantalla
            self.alto_pantalla = alto_pantalla
            self.tamano_celda = tamano_celda
 
"""metodo que actualiza la lista de paredes activas(no destruidas), el main tiene que llamarla cuando una pared sea destruida"""   
def actualizar_paredes_activas(self, nuevas_paredes_activas_graficas):
	    self.paredes_graficas_activas = nuevas_paredes_activas_graficas

def manejo_de_eventos(self):
        teclas = pygame.key.get_pressed()

        # movimientos del jugador, ya que los de enemigos se definieron en su clase y no el controlador porque: jugador lo maneja usuario , en cambios los movimientos de enemigo son automaticos y aleatorios , al no necesitar controlar sus movimientos se definio en su clase
       
        nueva_pos_x = self.jugador1_logico.pos_x  # nueva posicion de jugador logico
        nueva_pos_y = self.jugador1_logico.pos_y
        
        velocidad_jugador = 5 # en un futuro si velocidad de jugador va a cambiar como la de enemigo: la definimos en su clase y no aca

        if teclas[pygame.K_UP]:
            nueva_pos_y -= velocidad_jugador
        if teclas[pygame.K_DOWN]:
            nueva_pos_y += velocidad_jugador
        if teclas[pygame.K_LEFT]:
            nueva_pos_x -= velocidad_jugador
        if teclas[pygame.K_RIGHT]:
            nueva_pos_x += velocidad_jugador

        #  se crea un rectangulo temporal(jugador temporal) para la posicion tentativa del jugador, para saber si hay colisiones con paredes 
        temp_rect_jugador = pygame.Rect(nueva_pos_x, nueva_pos_y, self.tamano_celda, self.tamano_celda)
        
        puede_mover = True #esta variable se crea para saber siel jugador esta hablitido para moverse

        # for para determinar si hay colision con paredes , si la hay: cambia estado de puede_mover a false (ya que no puede avanzar)
        for pared_grafica in self.paredes_graficas_activas:
            if temp_rect_jugador.colliderect(pared_grafica.rect):
                puede_mover = False
                break
        
        # si enemigo logicamente esta vivo y jugador grafico esta a punto de colisionar con enemigo grafico, jugador no puede moverse a esa posicion"
        if self.jugador2_logico.esta_vivo() and temp_rect_jugador.colliderect(self.jugador2_grafico.rect):
            puede_mover = False

        # al igual que ne la clase enemigo, limitamos los movimientos de jugador a la pantalla
        nueva_pos_x = max(0, min(nueva_pos_x, self.ancho_pantalla - self.tamano_celda))
        nueva_pos_y = max(0, min(nueva_pos_y, self.alto_pantalla - self.tamano_celda))

        # si no hay colision actualiza la posicion logica del jugador(posicion de jugador logico)
        if puede_mover:
            # Llama al metodo 'mover' del MODELO L�GICO del jugador
            self.jugador1_logico.pos_x = nueva_pos_x
            self.jugador1_logico.pos_y = nueva_pos_y
        
        # actualiza posicion grafica del jugador para que coincida con el modelo
        self.jugador1_grafico.actualizar_posicion()

        # movimientos automaticos de enemigo,enemigo logico decide y actualiza su propia pos_x y pos_y
        if self.jugador2_logico.esta_vivo():
            self.jugador2_logico.mover_enemigo(self.paredes_graficas_activas)#se pasa pared grafica para que chequee colisi�n grafica
            self.jugador2_grafico.actualizar_posicion()


        # jugador coloca bomba
        if teclas[pygame.K_SPACE]:
            bomba_colocada_logica = self.jugador1_logico.atacar()# jugador logico intenta "atacar" (colocar una bomba)
            
            if isinstance(bomba_colocada_logica, Bomba):
                # sii el jugador coloco una nueva bomba,se añade a nuestras listas
                self.bombas_activas_logicas.append(bomba_colocada_logica)
                # Crear la contraparte grafica de la bomba
                bomba_grafica = BombaGrafica(bomba_colocada_logica.pos_x, bomba_colocada_logica.pos_y, (255, 0, 0), bomba_colocada_logica, self.tamano_celda)
                self.bombas_activas_graficas.append(bomba_grafica)
                print(f"Bomba colocada en: ({bomba_colocada_logica.pos_x}, {bomba_colocada_logica.pos_y})")

        #movimientos automaticos de enemigo
        if self.jugador2_logico.esta_vivo():
            # se llama a metodo mover_enemigo 
            self.jugador2_logico.mover_enemigo(self.paredes_graficas_activas, self.ancho_pantalla, self.alto_pantalla, self.tamano_celda)
            self.jugador2_grafico.actualizar_posicion()

        # bombas activas y explosiones 
        bombas_a_eliminar_logicas = []
        bombas_a_eliminar_graficas = []

        for i, bomba_logica in enumerate(self.bombas_activas_logicas):
            # bomba logica verifica si debe explotar
            if bomba_logica.estadoBomba(): # este metodo  marca la bomba como explotada internamente(objeto logico)
                danio_bomba = bomba_logica.calcular_danio()
               
                # aplicar daño a enemigo en el radio de la explosion 
                # la logica es q se asume un alcance simple: misma celda 
                if self.jugador2_logico.esta_vivo():
                    enemigo_cerca_bomba_x = abs(bomba_logica.pos_x - self.jugador2_logico.pos_x) < self.tamano_celda * 1.5 # Un poco m�s que 1 celda para ser flexible
                    enemigo_cerca_bomba_y = abs(bomba_logica.pos_y - self.jugador2_logico.pos_y) < self.tamano_celda * 1.5
                    
                    if enemigo_cerca_bomba_x and enemigo_cerca_bomba_y:
                        self.jugador2_logico.recibir_danio(danio_bomba)
                        if not self.jugador2_logico.esta_vivo():
                            self.jugador2_grafico.rect.x = -1000 # para eliminarlo lo saca temporalmente de la pantalla

                # daños a paredes q estan en el radio de explosion de la bomba
                paredes_a_destruir_logicas = []
                paredes_a_destruir_graficas = []
                
                # se itera sobre una copia para poder modificar la lista original si  se eliminama elementos
                for pared_grafica in list(self.paredes_graficas_activas): 
                    pared_logica = pared_grafica.modelo
                    
                    # chequea si la pared esta en el radio de la explosion
                    dist_x_pared = abs(bomba_logica.pos_x - pared_logica.pos_x)
                    dist_y_pared = abs(bomba_logica.pos_y - pared_logica.pos_y)

                    if dist_x_pared < self.tamano_celda * 1.5 and dist_y_pared < self.tamano_celda * 1.5:
                        if pared_logica.destruir(): #  destruir la pared logica
                            paredes_a_destruir_logicas.append(pared_logica)
                            paredes_a_destruir_graficas.append(pared_grafica)
                            
                # elimina las paredes graficas que fueron destruidas de la lista activa
                for pared_grafica_eliminar in paredes_a_destruir_graficas:
                    self.paredes_graficas_activas.remove(pared_grafica_eliminar)

                # elimina bomba de las listas de bombas activas
                bombas_a_eliminar_logicas.append(bomba_logica)
                bombas_a_eliminar_graficas.append(self.bombas_activas_graficas[i])#indice 'i' si las listas logica y gr�fica son paralelas, sino buscar otra forma de obtener bomba grafica

        # elimina  bombas explotadas de las listas de activas
        for bomba_logica_eliminar in bombas_a_eliminar_logicas:
            self.bombas_activas_logicas.remove(bomba_logica_eliminar)
        for bomba_grafica_eliminar in bombas_a_eliminar_graficas:
            self.bombas_activas_graficas.remove(bomba_grafica_eliminar)