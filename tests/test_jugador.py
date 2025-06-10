import unittest
import pygame
from modelos.jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_posicion_inicial(self):
        """Testeamos que el metodo crear jugador funcione correctamente"""
        jugador = Jugador(50,75)#creamos un jugador en esta posicion
        self.assertEqual(jugador.rect.x, 50)
        self.assertEqual(jugador.rect.y, 75)
    def test_colocar_pocion(self):
        """Testeamos el metodo colocar pocion funcione correctamente"""
        jugador = Jugador(32,32)
        self.assertEqual(len(jugador.pociones),0)
        jugador.colocar_pocion()#cuando colocamos una pocion en teoria estariamos sumando una al arreglo de las pociones
        self.assertEqual(len(jugador.pociones),1)