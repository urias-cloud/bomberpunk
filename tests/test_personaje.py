import unittest
from Modelos.Personaje import Personaje

class TestPersonaje(unittest.TestCase):
    def test_mover(self):
        """Verifica que el personaje pueda moverse correctamente"""
        p = Personaje("Bomberman", 100, 0, 0)
        p.mover(50, 60)
        self.assertEqual(p.get_posicion(), (50, 60))

    def test_recibir_danio_y_muerte(self):
        """Verifica que el personaje reciba daño y se muera"""
        p = Personaje("Heroe", 100, 0, 0)
        p.recibir_danio(120)
        self.assertEqual(p.vida, 0)
        self.assertFalse(p.esta_vivo())
