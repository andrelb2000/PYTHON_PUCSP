class Pessoa():
    _nome_ = ""
    _idade_ = 0
    _salario_ = 0
    def __init__(self,n,i):
        self._nome_ = n
        self._idade_ = i
    def processaSalario(self):
        self._salario_ = int(self._idade_) * 500
    def modoApresentacao(self):
        return "NOME: " + str(self._nome_) + "\n" + \
               "Tem idade igual a " + str(self._idade_) + " anos \n" + \
               " E tem salario = " + str(self._salario_)
