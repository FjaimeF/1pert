import automatizacion

def test_suma_normal():
    assert automatizacion.sumar(2, 3) == 5

def test_suma_ceros():
    assert automatizacion.sumar(0, 0) == 0

def test_suma_negativos():
    assert automatizacion.sumar(-1, 1) == 0
