import unittest
from Modelos.Mapa import Mapa

class TestMapa(unittest.TestCase):
    def setUp(self):
        self.mapa = Mapa(tamano_celda=30)

    def test_celda_ocupada_devuelve_true_para_pared(self):
        """"""
        for pared in self.mapa.paredes_logicas:
            fila = pared.pos_y // 30
            columna = pared.pos_x // 30
            self.assertTrue(self.mapa.celda_ocupada(fila, columna))
