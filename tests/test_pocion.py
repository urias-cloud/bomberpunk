import time
from modelos.Bomba import Bomba

class TestPocion(unittest.TestCase):
    def test_explosion_despues_tiempo(self):
        bomba = Bomba(0, 0, timer=1) #creamos la pocion para que explote en 1 segundo
        bomba.tiempo_inicial -= 1.5 #le restamos a tiempo inicial(cuando se coloco) mas de 1 segundo
        bomba.actualizar() #al llamar la funcion actualizar, la bomba ya exploto
        self.assertTrue(bomba.explotada)

    def test_bomba_no_exploto(self):
        bomba = Bomba(0,0, timer = 5) #creamos la pocion con un tiempo de 5
        bomba.tiempo_inicial -= 4 #le restamos cuatro osea que queda en uno
        bomba.actualizar() #como esta en uno llamamos al metodo actualizar y tendria que salir falso
        self.assertFalse(bomba.explotada)