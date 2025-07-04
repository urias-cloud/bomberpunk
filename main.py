import pygame
import sys
import random 
import os 


from Modelos.Jugador import Jugador
from Modelos.Enemigo import Enemigo
from Modelos.Mapa import Mapa


from Vista.JugadorGrafico import JugadorGrafico 
from Vista.EnemigoGrafico import EnemigoGrafico
from Vista.MapaGrafico import MapaGrafico


from Controlador.Controlador import Controlador
#IMPORTANTE
#La idea es seguir trabajando en este juego como un proyecto personal y ver hasta donde llega
#Queremos presentarlo en septiembre, por lo tanto esta version va a seguir siendo actualizada hasta ese momento para mejorarlo lo mas que podamos
#Le agregamos un mapa de fondo y le cambiamos la bomba
#METAS A FUTURO:
#Mejorar las fisicas para que el personaje puede desplazarle de una forma fluida sin chocarse tanto
#Que la bomba explote en direcciones(arriba,abajo,izq y der) y que tenga animacion.Agregar mas tipos de bombas  
# Agregar mas enemigos
# Cambiar el personaje y mejorar su animacion ya que el que esta no es uno oficial.


TAMANO_CELDA = 40 #El valor puesto aca puede ser cambiado a 30 para obtener la experiencia que fue presentada en la ultima clase
NUM_COLUMNAS = 27 
NUM_FILAS = 20    
ANCHO_PANTALLA = NUM_COLUMNAS * TAMANO_CELDA 
ALTO_PANTALLA = NUM_FILAS * TAMANO_CELDA    

# evalua constantemente el estado del jugador_logico y la lista mapa_grafico.enemigos para determinar #si hay un game over o si gana. cuando termina mostrar_pantalla_final captura el keydown si se reinicia, la funci�n reiniciar_juego recrea todas las instancias de modelos logicos y graficos, incluyendo el Controlador


class MapaTemp(Mapa):
    """clase temporal que hereda de Mapa se usa para proporcionar el metodo estatico celda_ocupada_estatica donde verifica si una celda
    tiene una pared basandose en los datos del mapa original incluso antes  de instancia mapa o mapa grafico haya sido inicializada
    """
    @staticmethod# crea como una funcion normal en una clase , pero no necesita de un objeto de esa clase para funcionar.se puede llamar directamente usando el nombre de la clase
    def celda_ocupada_estatica(fila, columna):
        if 0 <= fila < len(Mapa.datos_mapa) and 0 <= columna < len(Mapa.datos_mapa[0]):
            return Mapa.datos_mapa[fila][columna] in ['x', 'd']
        return False 

# logica de reinicio de juego
def reiniciar_juego():
    """ metodo que reiniica o estancia los componentes logicos y graficos del juego.permitiendo la opcion de volver a jugar espeues q el juego termine(game over o ganar),reseteando todo el estado del juego retornando las nuevas instancias logicas y graficas"""
    jugador_logico = Jugador("Bomberpunk", 100, TAMANO_CELDA, TAMANO_CELDA)# se crea nueva instancia jugador logico 
     # nuevas instancias de enemigos logicos
    enemigos_logicos = [] 
    cantidad_enemigos = 5
    posiciones_ocupadas_por_enemigos = [] 
    for i in range(cantidad_enemigos):
        x_enemigo = None
        y_enemigo = None
        intentos = 0
        max_intentos = 20 

        # bucle para encontrar posicion aleatorea validad para  enemigo
        while intentos < max_intentos:
            # Genera coordenadas de columna y fila aleatorias, evitando los bordes
            rand_col = random.randint(2, NUM_COLUMNAS - 2)
            rand_fila = random.randint(2, NUM_FILAS - 2)

            x_pos = rand_col * TAMANO_CELDA 
            y_pos = rand_fila * TAMANO_CELDA 

            # se usa el metodo estatico de mapatemp y  verifica si la celda est ocupada por una pared
            # verifica que  posicion no este  ocupada por otro enemigo.
            if not MapaTemp.celda_ocupada_estatica(rand_fila, rand_col):
                if (x_pos, y_pos) not in posiciones_ocupadas_por_enemigos:
                    x_enemigo, y_enemigo = x_pos, y_pos
                    posiciones_ocupadas_por_enemigos.append((x_enemigo, y_enemigo))
                    break 
            
            intentos += 1 
        
        # si encontro posicion, crea enemigo logico y lo agrega a la lista
        if x_enemigo is not None:
            enemigos_logicos.append(Enemigo(f"Enemigo_{i+1}", 30, x_enemigo, y_enemigo, 0.4, "normal")) 
        else:
       
            break 
    
    # nueva instancia del mapa logico asegurando ue las paredes destruibles vuelvan a aparecer al reiniciar
    
    mapa_logico = Mapa(TAMANO_CELDA)
    mapa_grafico = MapaGrafico(mapa_logico, enemigos_logicos, TAMANO_CELDA)
    #  nuevas instancias de los objetos graficos


    jugador_grafico = JugadorGrafico(jugador_logico, TAMANO_CELDA)
    
    # retorna todas las instancias creadas
    return jugador_logico, mapa_logico, enemigos_logicos, jugador_grafico, mapa_grafico

#  mostrar pantallas finales game over/ganar
def mostrar_pantalla_final(pantalla, mensaje):
    """metodo que muestra resultado final del juego en la ventana del juegorecibe el mensaje a mostrar como parametro y muestra las
    opciones:"reiniciar" si usuario presiona 'R'"salir" si presiona 'ESC' 
    """
    fuente_titulo = pygame.font.SysFont("Consolas", 60, bold=True)
    fuente_instruccion = pygame.font.SysFont("Verdana", 28)

    #pantalla.fill((0, 0, 0))  # Fondo negro


    texto_titulo = fuente_titulo.render(mensaje, True, (255, 80, 80))  # Rojo pastel
    texto_instruccion = fuente_instruccion.render("Presiona 'R' para reiniciar o 'ESC' para salir", True, (180, 180, 255))


    rect_titulo = texto_titulo.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 - 30))
    rect_instruccion = texto_instruccion.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 + 30))


    ancho_fondo = max(rect_titulo.width, rect_instruccion.width) + 60
    alto_fondo = rect_titulo.height + rect_instruccion.height + 60
    x_fondo = (ANCHO_PANTALLA - ancho_fondo) // 2
    y_fondo = (ALTO_PANTALLA - alto_fondo) // 2

    fondo_rect = pygame.Rect(x_fondo, y_fondo, ancho_fondo, alto_fondo)
    pygame.draw.rect(pantalla, (30, 30, 30), fondo_rect, border_radius=15)  # fondo oscuro
    pygame.draw.rect(pantalla, (200, 0, 0), fondo_rect, width=4, border_radius=15)  # borde rojo


    pantalla.blit(texto_titulo, rect_titulo)
    pantalla.blit(texto_instruccion, rect_instruccion)
    pygame.display.flip()


    esperando_respuesta = True 
    while esperando_respuesta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir" 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "reiniciar" #  presiona r si decide reiniciar
                if event.key == pygame.K_ESCAPE:
                    return "salir" # presiona esc si  decide salir
    return "salir" 

# funcion principal
def main():
    pygame.init() 
    
    
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("BOMBERPUNK") 
    
    reloj = pygame.time.Clock() 
    fuente = pygame.font.SysFont("Arial", 20) 
    
    # la primera vez que se ejecuta e llama a reiniciar_juego para obtener todas las instancias iniciales de los objetos
    
    jugador_logico, mapa_logico, enemigos_logicos, jugador_grafico, mapa_grafico = reiniciar_juego()
    
    # se crea la instancia controlador
    controlador = Controlador(
        jugador_grafico,
        mapa_grafico,
        ANCHO_PANTALLA,
        ALTO_PANTALLA,
        TAMANO_CELDA
    )

    corriendo = True 
    while corriendo:
        reloj.tick(60)
    
        controlador.manejo_de_eventos()

        if not jugador_logico.esta_vivo():
            # si el jugador esta muerto muestra la pantalla de game over
            decision = mostrar_pantalla_final(pantalla, "GAME OVER!")
            
            if decision == "reiniciar":# si usuario elige "reiniciar" llama de nuevo a reiniciar_juego
                jugador_logico, mapa_logico, enemigos_logicos, jugador_grafico, mapa_grafico = reiniciar_juego()                
                controlador = Controlador(
                    jugador_grafico,
                    mapa_grafico,
                    ANCHO_PANTALLA,
                    ALTO_PANTALLA,
                    TAMANO_CELDA
                )
                continue
            else: 
                corriendo = False 
                continue # salta el resto de este ciclo del bucle para que el juego se cierre limpiamente

        # si gana, es decir los enemigos han muerto y el jugador vive:
        elif not mapa_grafico.enemigos and jugador_logico.esta_vivo():
           
            decision = mostrar_pantalla_final(pantalla, "GANASTE!")
            
            if decision == "reiniciar":
                jugador_logico, mapa_logico, enemigos_logicos, jugador_grafico, mapa_grafico = reiniciar_juego()
                controlador = Controlador(
                    jugador_grafico,
                    mapa_grafico,
                    ANCHO_PANTALLA,
                    ALTO_PANTALLA,
                    TAMANO_CELDA
                )
                continue
            else: 
                break # salta el resto de este ciclo del bucle


        if corriendo: 
            pantalla.fill((0, 0, 0)) 

            mapa_grafico.dibujar(pantalla) # dibuja las paredes del mapa
            
            #dibuja al jugador si esta vivo
            if jugador_logico.esta_vivo():
                jugador_grafico.dibujar(pantalla)
            
            # dibuja tbombas activas en el juego
            for bomba_grafica in controlador.bombas_activas_graficas:
                bomba_grafica.dibujar(pantalla)

	        
            
            texto_vida = fuente.render(f"Vida: {jugador_logico.vida}", True, (255, 255, 255))
            pantalla.blit(texto_vida, (10, 10))
            pygame.display.flip() 
      
    pygame.quit() 
    sys.exit()    

if __name__ == "__main__":
    main()