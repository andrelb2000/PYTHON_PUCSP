from VISUAL import *


class Controle:
    _componenteVisual2_ = None
    def __init__(self):
        self._componenteVisual_ = Visual()
    def processaPessoa(self,p):
        p.processaSalario()
    def executar(self):
        p = self._componenteVisual_.lePessoa()
        self.processaPessoa(p)
        self._componenteVisual_.mostrePessoa(p)
