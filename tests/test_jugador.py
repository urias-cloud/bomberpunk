import unittest
from Modelos.Jugador import Jugador

class TestJugador(unittest.TestCase):
    def setUp(self):
        self.jugador = Jugador("Player1", 100, 0, 0)

    def test_atacar_crea_bomba(self):
        """Verifica que el jugador realize correctamente el ataque(colocar bomba)"""
        bomba = self.jugador.atacar(tiempo_actual=1000)
        self.assertIsNotNone(bomba)
        self.assertEqual((bomba.pos_x, bomba.pos_y), (0, 0))

    def test_atacar_no_repite_si_hay_bomba(self):
        """Verifica que el jugador no ataque si ya hay una bomba activa"""
        self.jugador.atacar(1000)
        self.assertIsNone(self.jugador.atacar(2000))
