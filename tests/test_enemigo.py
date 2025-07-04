import unittest
from Modelos.Enemigo import Enemigo

class TestEnemigo(unittest.TestCase):
    def setUp(self):
        self.enemigo = Enemigo("Enemigo", 30, 0, 0, 2, "normal")

    def test_recibir_danio(self):
        """Verifica que el enemigo reciba daño correctamente"""
        self.enemigo.recibir_danio(10)
        self.assertEqual(self.enemigo.vida, 20)

    def test_muere_correctamente(self):
        """Verifica que el enemigo sea asesinado correctamente"""
        self.enemigo.recibir_danio(30)
        self.assertFalse(self.enemigo.esta_vivo())
