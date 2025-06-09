import time
from pocion import Pocion

def test_explosion_despues_tiempo():
    pocion = Pocion(0, 0, timer=1)
    time.sleep(1.1)
    pocion.actualizar()
    assert pocion.explotada == True
