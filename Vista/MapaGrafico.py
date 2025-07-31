import pygame
from .ParedGrafica import ParedGrafica
from .EnemigoGrafico import EnemigoGrafico
import os
import random

class MapaGrafico:
    def __init__(self, modelo_mapa,lista_enemigos, tamano_celda):
        """metodo constructor recibe mapa logico, lista de enemigos logicsos(para cargarlos y dibujarlos en mapa grafico, y tamaño de celda"""
        self.columnas = 27  # o el valor que estés usando
        self.filas = 20
        self.modelo = modelo_mapa#mapa logico lista de enemigos logicos
        self.tamano_celda= tamano_celda
        self.enemigos=[]#lista donde se cargan los enemigos graficos
        self.paredes_graficas = []# lista para cargar paredes graficas
        # metodo para crear las paredes graficas
        self.crear_enemigos(lista_enemigos)# metodo para crear enemigos graficos

        imagen_piso = os.path.join("assets","fondo_mapa.png")
        self.imagen_piso = pygame.image.load(imagen_piso).convert()#el convert convierte la imagen al mismo formato de la pantalla
        ancho = self.modelo.num_columnas * self.tamano_celda    #recibe el num de columnas y de filas de la clase mapa
        alto = self.modelo.num_filas * self.tamano_celda
        self.imagen_piso = pygame.transform.scale(self.imagen_piso, (ancho, alto))

        self.inicializar_paredes_graficas()
    def inicializar_paredes_graficas(self):
        """Metodo que inicializa las paredes"""
        for pared_logica in self.modelo.paredes_logicas:
            self.paredes_graficas.append(ParedGrafica(
                pared_logica.pos_x,
                pared_logica.pos_y,
                pared_logica,
                self.tamano_celda
            ))

    def crear_enemigos(self, lista_enemigos):
        """metodo para crear enemigos graficos asi se dibujan en el mapa. con un for recorre la lista de enemigos(enemigos logicos)
        por cada enemigo losgico q encuentra en la tabla crea un enemigo grafico y lo agrega a la lista de enemigos graficos"""
        for enemigo_logico in lista_enemigos:
            print(f"Creando enemigo en {enemigo_logico.get_posicion()}")
            enemigo_grafico = EnemigoGrafico(enemigo_logico, self.tamano_celda)
            self.enemigos.append(enemigo_grafico)
                      
                       
    def dibujar(self, pantalla):
        """Metodo para dibujar el piso y las paredes"""
        if self.imagen_piso:
            pantalla.blit(self.imagen_piso, (0, 0))  # Dibuja el fondo completo

        
        for pared in self.paredes_graficas:
            pared.dibujar(pantalla)
        for enemigo in self.enemigos :
           if enemigo.modelo.esta_vivo():
            enemigo.dibujar(pantalla)

    def obtener_paredes_graficas_activas(self):
        """metodo que comprueba si cada pared cargada en la lista  de paredes graficas se encuentra destruida o no... la usaremos
        para las colisiones, movientos """
        return [p for p in self.paredes_graficas if not p.modelo.esta_destruida()]
