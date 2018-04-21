from core.utils.util import Util


def testeCalculaMediaFinal():
    assert(Util.calculaMediaFinal(10, 10) == 10)
    assert(Util.calculaMediaFinal(6, 12) == None)
    assert(Util.calculaMediaFinal(-4, 8) == None)
    assert(Util.calculaMediaFinal(4, 4) == 4)
    assert(Util.calculaMediaFinal(9, 9) == 9)
    assert(Util.calculaMediaFinal(5, 5) == 5)
    assert(Util.calculaMediaFinal(7, 7) == 7)

def testeCalculaMedia():
    notas = [8.0]
    assert(Util.calculaMedia(notas) == 8.0)

def testeDescontaNota():
    assert(Util.descontaNota(10, 10) == 9.0)

def testeVerificaCopia():
    assert(Util.verificaCopia('abc', 'abc') is True)
    assert(Util.verificaCopia('abc', 'xaf') is False)
