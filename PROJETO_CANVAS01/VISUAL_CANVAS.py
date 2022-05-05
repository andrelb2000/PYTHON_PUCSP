
from tkinter import Tk,Canvas,StringVar,Button,Label


class VisualCanvas():
    _janela_ = None
    _status_ = None
    _buttonAtualiza_ = None
    _buttonNovaJanela_ = None
    _buttonNovaBola_ = None
    _canvas_ = None
    _novaJanela_ = None
    _nrJanela_ = 0
    def __init__(self,nr):
        self._nrJanela_ = nr + 1
        self._janela_ = Tk()
        print("Aqui deveria criara outra variavel")
        self._status_ = Label(master=self._janela_)
        self._buttonAtualiza_   = Button(master=self._janela_,text="Comceçar",command=self.alteraStatus)
        self._buttonNovaJanela_ = Button(master=self._janela_, text="Nova Janela", command=self.novaJanela)
        self._buttonNovaBola_ = Button(master=self._janela_, text="Nova Bola", command=self.novaBola)

        self._canvas_ = Canvas(master=self._janela_, height=500, width=500, bg="yellow")
        self._buttonAtualiza_.pack()
        self._buttonNovaJanela_.pack()
        self._buttonNovaBola_.pack()
        self._status_.pack()
        self._canvas_.pack()
    _bola_ = None
    _bola2_ = None
    _listaBola_ = []
    _posInicial_ = 0
    def moveBola(self):
        self._canvas_.move(self._bola_,5,0)
        #self._canvas_.update()
        self._canvas_.after(300,func=self.moveBola)

    def moveBola2(self):
        for o in self._listaBola_:
            self._canvas_.move(o[0],o[1],0)
        self._canvas_.after(600,func=self.moveBola2)

    def alteraStatus(self):
        print("executando status " + str(self._nrJanela_))
        self._status_.config(text="Iniciado")
        self._bola_ = self._canvas_.create_oval(50, 50, 70, 70, outline="black")
        self.moveBola()


    def novaBola(self):
        self._bola2_ = self._canvas_.create_oval(50, 300+self._posInicial_, 70, 320+self._posInicial_, outline="black", fill="blue")
        self._posInicial_ += 5
        self._listaBola_.append([self._bola2_,self._posInicial_])
        self.moveBola2()



    def novaJanela(self):
        self._novaJanela_ = VisualCanvas(self._nrJanela_)
        self._novaJanela_.iniciar()
    def iniciar(self):
        self._janela_.mainloop()

