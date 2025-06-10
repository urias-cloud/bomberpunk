import time
from modelos.pocion import Pocion

class TestPocion(unittest.TestCase):
    def test_explosion_despues_tiempo(self):
        pocion = Pocion(0, 0, timer=1) #creamos la pocion para que explote en 1 segundo
        pocion.tiempo_inicial -= 1.5 #le restamos a tiempo inicial(cuando se coloco) mas de 1 segundo
        pocion.actualizar() #al llamar la funcion actualizar, la bomba ya exploto
        self.assertTrue(pocion.explotada)

    def test_bomba_no_exploto(self):
        pocion = Pocion(0,0, timer = 5) #creamos la pocion con un tiempo de 5
        pocion.tiempo_inicial -= 4 #le restamos cuatro osea que queda en uno
        pocion.actualizar() #como esta en uno llamamos al metodo actualizar y tendria que salir falso
        self.assertFalse(pocion.explotada)