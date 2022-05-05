
from tkinter import Tk,Canvas,StringVar,Button,Label
import time, threading


class VisualCanvas():
    _janela_ = None
    _status_ = None
    _buttonNovaJanela_ = None
    _buttonIniciaProcesso_ = None
    _logProcesso_ = None
    _textoLog_  = None
    _canvas_ = None
    _novaJanela_ = None
    _nrJanela_ = 0
    _linhaAtual_ = 0
    def __init__(self,nr):
        self._nrJanela_ = nr + 1
        self._janela_ = Tk()
        print("Aqui deveria criara outra variavel")
        self._status_ = Label(master=self._janela_)
        self._buttonNovaJanela_ = Button(master=self._janela_, text="Nova Janela", command=self.novaJanela)
        self._buttonIniciaProcesso_ = Button(master=self._janela_, text="Inicia Processo",  command=self.iniciaProcesso)
        self._textoLog_ = StringVar()
        self._textoLog_.set("RELATORIO: \n")
        self._logProcesso_   = Label(master=self._janela_, textvariable=self._textoLog_)
        self._canvas_ = Canvas(master=self._janela_, height=500, width=500, bg="yellow")
        self._buttonNovaJanela_.pack()
        self._buttonIniciaProcesso_.pack()
        self._status_.pack()
        self._logProcesso_.pack()
        self._canvas_.pack()


    def escreveLinha(self,texto):
        self._canvas_.create_text(100, 10 + (20 * self._linhaAtual_),text=texto,anchor='nw',font=('courier', 14))
        self._linhaAtual_ +=1

    def iniciaProcesso(self):
        inicio = time.perf_counter()
        self.escreveLinha("Rodando... INICIO: " + str(round(inicio,2)))
        t1 = threading.Thread(target=self.executarProcesso)
        t1.start()
        fim = time.perf_counter()
        self.escreveLinha("Rodando... FIM:    " + str(round(fim,2)))
        self.escreveLinha("Tempo decorrido:  " + str(round(fim-inicio,2)))

    def novaJanela(self):
        self._novaJanela_ = VisualCanvas(self._nrJanela_)
        self._novaJanela_.iniciar()
    def iniciar(self):
        self._janela_.mainloop()

    def executarProcesso(self):
        for i in range(10):
            self.escreveLinha("Rodando... ")
            time.sleep(1)

