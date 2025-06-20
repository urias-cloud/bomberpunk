from .personaje import Personaje
import pygame
import random

class Enemigo(Personaje):
    """metodo constructor: recibe los parametros de la superclase y se añade daño"""
    def __init__(self, nombre, vida, pos_x, pos_y, velocidad, danio):
        super().__init__(nombre, vida, pos_x, pos_y)
        self.velocidad = velocidad  #velocidad específica del enemigo(sirve para los distintos enemigos)
        self.danio = danio
        self.alcance = 40
        self.valorDanio = {
            "normal": 30,
            "oscuridad": 50,
            "voladores": 20,
            "infierno": 40
        }
        self.direccion_actual = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        self.ultimo_cambio_direccion = pygame.time.get_ticks()
        self.tiempo_cambio_direccion = 1500

    """metodo que retorna el daño causado por enemigo (segun su tipo)"""
    def calcular_danio(self):
        return self.valorDanio.get(self.danio)

    """metodo ataque: devuelve el daño calculado segun el tipo de enemigo y se lo resta a la vida del jugador"""
    def atacar(self, otro_personaje):
        if self.esta_vivo:
            danio_causado = self.calcular_danio()
            otro_personaje.recibir_danio(danio_causado)
            return danio_causado
        else:
            return 0

    """metodo para mover al enemigo automáticamente, evitando colisiones
    decidiendo movimientos y verificando colisiones con las paredes.(el sistema de mapa sera cuadricular, donde
    tama�o celda representa una celda de la cuadricula,permite que enemigo y persinaje se muevan en celdas ,
    luego personaje grafico lo movera en pixeles, peropara calcular los movimientos es mejor hacerlo en celdas , es mas controlado
    """
    def mover_enemigo(self, paredes_activas):
        if not self.esta_vivo:
            return 0

        tiempo_actual = pygame.time.get_ticks()#se obtiene el tiempo actual,para usarlo a continuacion

        if tiempo_actual - self.ultimo_cambio_direccion > self.tiempo_cambio_direccion: # en esta linea se decide cambiar de posicion dado determinado tiempo. A tiempo actual se le resta el ultimo cambio de direccion y si es mayor al intervalo de cambio :procede a cambiar aleatoriamente de posicion y por ultimo actualiza el ultimo cambio de direccion
            self.direccion_actual = random.choice(["arriba", "abajo", "izquierda", "derecha"])
            self.ultimo_cambio_direccion = tiempo_actual

        nueva_pos_x = self.pos_x
        nueva_pos_y = self.pos_y

        if self.direccion_actual == "arriba":
            nueva_pos_y -= self.velocidad
        elif self.direccion_actual == "abajo":
            nueva_pos_y += self.velocidad
        elif self.direccion_actual == "izquierda":
            nueva_pos_x -= self.velocidad
        elif self.direccion_actual == "derecha":
            nueva_pos_x += self.velocidad

        # aca procedemos a chequear si hay colision con paredes, creando un enemigo temporal , que ira comprobando si tiene paredes proximas a colisionar
        temporal_enemigo = pygame.Rect(nueva_pos_x, nueva_pos_y, tamano_celda, tamano_celda)
        puede_moverse = True #booleano que determina si enemigo puede moverse o no (dependiendo de las colisiones con las paredes)

        for pared in paredes_activas: #Iteramos sobre cada pared que esta activa en el juego,paredes activas es una lista que contendra las paredes que no fueron destruidas ,las "activas"
            if temporal_enemigo.colliderect(pared.rect):#comprueba si el enemigo temporal chocara con la pared , se utiliza las clase rect de pygame, si esto sucede puede_moverse pasa a falso y el enemigo no puede moverse en esa direccion
                puede_moverse = False
                self.ultimo_cambio_direccion = 0 #actualizamos el tiempo de ultimo cambio
                break
#limitamos los movimientos de enemigo dentro de los bordes de la pantalla,estableciendo minimos y maximos.min(..):hace que enemigo salga por la derecha o abajo manejandose entre los valores de nueva_pos y ancho pantalla -tamño celda y max(0, resultado_del_min): evita que enemigo salga por la izquierda o arriba,manejandose entre los valores 0 y y min(..)
        nueva_pos_x = max(0, min(nueva_pos_x, ancho_pantalla - tamano_celda))
        nueva_pos_y = max(0, min(nueva_pos_y, alto_pantalla - tamano_celda))

        if puede_moverse:
            #enemigo actualiza su propia posicion logica y llama a metodo mover de la superclase Personaje
            super().mover(nueva_pos_x, nueva_pos_y)
