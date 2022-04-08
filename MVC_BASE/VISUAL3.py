from DADOS import Pessoa
from tkinter import Tk,Label,Button,Entry,StringVar

class Visual2():
    _janelaPrincipal_ = Tk()
    _textoRotulo_  = None
    _rotulo1_      = None
    _entradaNome_  = None
    _entradaIdade_ = None
    _insereButton_ = None
    def lePessoa(self):
        nome  = self._entradaNome_.get()
        idade = self._entradaIdade_.get()
        pessoa = Pessoa(nome,idade)
        return pessoa
    def mostrePessoa(self, p):
        self._textoRotulo_.set(p.modoApresentacao())
    def __init__(self,comandoProcessa):
        super().__init__()
        self._textoRotulo_  = StringVar()
        self._textoRotulo_.set("Entre com Nome e Idade")
        self._rotulo1_      = Label(master=self._janelaPrincipal_, textvariable=self._textoRotulo_)
        self._entradaNome_  = Entry(master=self._janelaPrincipal_, width=10)
        self._entradaIdade_ = Entry(master=self._janelaPrincipal_, width=10)
        self._insereButton_ = Button(master=self._janelaPrincipal_, text="Processa", command=comandoProcessa)
        self._rotulo1_.pack()
        self._entradaNome_.pack()
        self._entradaIdade_.pack()
        self._insereButton_.pack()
    def iniciar(self):
        self._janelaPrincipal_.mainloop()


