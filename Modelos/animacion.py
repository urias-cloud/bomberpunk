import pygame
import os

class Animacion:
    def __init__(self,ancho, alto, ruta_idle,ruta_run):
        self.ancho = ancho
        self.alto = alto

        self.ruta_idle = ruta_idle
        self.ruta_run = ruta_run
        #animaciones
        self.izquierda_caminando = []
        self.derecha_caminando = []
        self.izquierda_quieto = []
        self.derecha_quieto = []


        # Estado inicial
        self.estado = "quieto"
        self.direccion = "derecha"
        self.contador_frame = 0
        self.indice_frame = 0
        self.velocidad_animacion = 10  # cambiar cada 10 ticks

        #self.estado = "derecha_quieto"
        self.cargar_imagenes()
        self.imagen_actual = self.derecha_quieto[0]
    def cargar_imagenes(self):
        idle_sheet = pygame.image.load(self.ruta_idle).convert_alpha()
        run_sheet = pygame.image.load(self.ruta_run).convert_alpha()


#idle(quieto)
        num_frames_idle = idle_sheet.get_width() // self.ancho
        for i in range(num_frames_idle):
            x = i * self.ancho
            y = 0
            recorte = idle_sheet.subsurface((x, y, self.ancho, self.alto))
            imagen = pygame.transform.scale(recorte, (36, 36))

            self.derecha_quieto.append(imagen)
            self.izquierda_quieto.append(pygame.transform.flip(imagen,True,False))
    #run(corriendo )
        num_frames_run = idle_sheet.get_width() // self.ancho
        for i in range(num_frames_run):
            x = i * self.ancho
            y = 0
            recorte = run_sheet.subsurface((x, y, self.ancho, self.alto))
            imagen = pygame.transform.scale(recorte, (36, 36))

            self.derecha_caminando.append(imagen)
            self.izquierda_caminando.append(pygame.transform.flip(imagen,True,False))


    def actualizar(self, direccion, caminando=True):
        """
        Actualiza la imagen actual según la dirección y si está caminando.
        - direccion: "arriba", "abajo", "izquierda", "derecha"
        - caminando: True si el personaje se está moviendo
        """
        self.estado = "caminando" if caminando else "quieto"
        self.direccion = direccion
        self.contador_frame += 1

        if self.estado == "quieto":
            lista = self.derecha_quieto if direccion == "derecha" else self.izquierda_quieto
        else:
            lista = self.derecha_caminando if direccion == "derecha" else self.izquierda_caminando

        #lista = getattr(self, self.estado)

        if self.contador_frame >= self.velocidad_animacion:
            self.indice_frame = (self.indice_frame + 1) % len(lista)
            self.contador_frame = 0

        self.imagen_actual = lista[self.indice_frame]