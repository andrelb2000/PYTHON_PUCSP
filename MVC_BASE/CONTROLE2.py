from VISUAL2 import *


class Controle2:
    _componenteVisual2_ = None
    def __init__(self):
        self._componenteVisual2_ = Visual2(self.processaPessoa)
    def processaPessoa(self):
        p = self._componenteVisual2_.lePessoa()
        p.processaSalario()
        self._componenteVisual2_.mostrePessoa(p)
    def executar(self):
        self._componenteVisual2_.iniciar()
