
from tkinter import Tk,Canvas,StringVar,Button,Label
import time, threading, random

class DepositoTexto():

    _listaPalavras_ = []
    _semaforo_ = None
    def __init__(self):
        random.Random()
        self._semaforo_ = threading.Semaphore()

    def armazenaAleatoria(self):
        self._semaforo_.acquire()
        palavra = "Palavra_" + str(random.randint(0,10000))
        self._listaPalavras_.append(palavra)

        time.sleep(1)
        self._semaforo_.release()
    def armazena(self,palavra):
        self._listaPalavras_.append(palavra)
    def obterPalavraAleatoria(self):
        self._semaforo_.acquire()
        n = random.randint(0,len(self._listaPalavras_)-1)
        time.sleep(1)
        self._semaforo_.release()
        return self._listaPalavras_[n]

class DepositoTextoSimples(DepositoTexto):

    def armazenaAleatoria(self):
        palavra = "Palavra_" + str(random.randint(0,10000))
        self._listaPalavras_.append(palavra)
        time.sleep(1)

    def obterPalavraAleatoria(self):
        n = random.randint(0,len(self._listaPalavras_)-1)
        time.sleep(1)
        return self._listaPalavras_[n]


class VisualCanvas():
    NUMERO_EXECUCOES = 8
    TAMANHO_TEXTO = 10

    _janela_ = None
    _buttonNovaJanela_ = None
    _buttonIniciaProcesso_ = None
    _buttonIniciaProcesso2_ = None
    _buttonIniciaProcesso3_ = None
    _buttonIniciaProcesso4_ = None

    _logProcesso_ = None
    _textoLog_  = None
    _canvas_ = None
    _novaJanela_ = None
    _nrJanela_ = 0
    _linhaAtual_ = 0
    _deposito_ = None
    _depositoLocal_ = None
    _depositoSemControle_ = None
    _depositoLocalSemControle_ = None
    _timePrimeiraExecucao_ = None

    def __init__(self,nr,deposito,deposito2):
        if deposito==None:
            self._deposito_ = DepositoTexto()
        else:
            self._deposito_ = deposito

        if deposito2==None:
            self._depositoSemControle_ = DepositoTextoSimples()
        else:
            self._depositoSemControle_ = deposito2

        #Correcao
        self._depositoLocal_ = DepositoTexto()
        self._depositoLocalSemControle_ = DepositoTextoSimples()

        self._nrJanela_ = nr + 1
        self._janela_ = Tk()
        print("Aqui deveria criara outra variavel")
        self._buttonNovaJanela_ = Button(master=self._janela_, text="Nova Janela", command=self.novaJanela)
        self._buttonIniciaProcesso_ = Button(master=self._janela_, text="Inicia Processo c/Semaforo e Compartilhado",  command=self.iniciaProcesso)
        self._buttonIniciaProcesso2_ = Button(master=self._janela_, text="Inicia Processo - c/Semaforo e Dep.Local", command=self.iniciaProcesso2)
        self._buttonIniciaProcesso3_ = Button(master=self._janela_, text="Inicia Processo - S/Semaforo e Compartilhado", command=self.iniciaProcesso3)
        self._buttonIniciaProcesso4_ = Button(master=self._janela_, text="Inicia Processo - S/Semaforo e Dep. Local", command=self.iniciaProcesso4)

        self._textoLog_ = StringVar()
        self._textoLog_.set("RELATORIO - Janela: " + str(self._nrJanela_))
        self._logProcesso_   = Label(master=self._janela_, textvariable=self._textoLog_)
        self._canvas_ = Canvas(master=self._janela_, height=540, width=300, bg="yellow")
        self._buttonNovaJanela_.pack()
        self._buttonIniciaProcesso_.pack()
        self._buttonIniciaProcesso2_.pack()
        self._buttonIniciaProcesso3_.pack()
        self._buttonIniciaProcesso4_.pack()
        self._logProcesso_.pack()
        self._canvas_.pack()


    def escreveLinha(self,texto):
        self._canvas_.create_text(5, self.TAMANHO_TEXTO +
                                     ((self.TAMANHO_TEXTO) * self._linhaAtual_),
                                      text=texto,anchor='nw',

      font=('courier', self.TAMANHO_TEXTO))
        self._linhaAtual_ +=1

    def iniciaProcesso(self):
        if self._timePrimeiraExecucao_ == None:
            self._timePrimeiraExecucao_ = time.perf_counter()
        inicio = time.perf_counter()
        self.escreveLinha("Rodando... INICIO da chamada: " + str(round(inicio,2)))
        t1 = threading.Thread(target=self.executarProcesso,args=[inicio])
        t1.start()
        fim = time.perf_counter()
        self.escreveLinha("Rodando... Volta da Chamada: " + str(round(fim,2)))
        self.escreveLinha("Tempo decorrido da chamada:  " + str(round(fim-inicio,2)))


    def iniciaProcesso2(self):
        if self._timePrimeiraExecucao_ == None:
            self._timePrimeiraExecucao_ = time.perf_counter()
        inicio = time.perf_counter()
        self.escreveLinha("Deposito Local... INICIO: " + str(round(inicio,2)))
        t1 = threading.Thread(target=self.executarProcesso2,args=[inicio])
        t1.start()
        fim = time.perf_counter()
        self.escreveLinha("Deposito Local... VOLTA: " + str(round(fim,2)))
        self.escreveLinha("Tempo decorrido da chamada:  " + str(round(fim-inicio,2)))

    def iniciaProcesso3(self):
        if self._timePrimeiraExecucao_ == None:
            self._timePrimeiraExecucao_ = time.perf_counter()
        inicio = time.perf_counter()
        self.escreveLinha("Deposito S/Semaforo - INICIO: " + str(round(inicio,2)))
        t1 = threading.Thread(target=self.executarProcesso3,args=[inicio])
        t1.start()
        fim = time.perf_counter()
        self.escreveLinha("Deposito S/Semaforo - VOLTA: " + str(round(fim,2)))
        self.escreveLinha("Tempo decorrido da chamada:  " + str(round(fim-inicio,2)))


    def iniciaProcesso4(self):
        if self._timePrimeiraExecucao_ == None:
            self._timePrimeiraExecucao_ = time.perf_counter()
        inicio = time.perf_counter()
        self.escreveLinha("Deposito Local S/Semaforo INICIO: " + str(round(inicio,2)))
        t1 = threading.Thread(target=self.executarProcesso4,args=[inicio])
        t1.start()
        fim = time.perf_counter()
        self.escreveLinha("Deposito Local S/Semaforo VOLTA: " + str(round(fim,2)))
        self.escreveLinha("Tempo decorrido da chamada:  " + str(round(fim-inicio,2)))



    def novaJanela(self):
        self._novaJanela_ = VisualCanvas(self._nrJanela_,self._deposito_,self._depositoSemControle_)
        self._novaJanela_.iniciar()
    def iniciar(self):
        self._janela_.mainloop()

    def processo(self):
        self._deposito_.armazenaAleatoria()
        palavra = self._deposito_.obterPalavraAleatoria()
        self.escreveLinha("Obtendo Palavra: "+palavra)


    def processo2(self):
        self._depositoLocal_.armazenaAleatoria()
        palavra = self._depositoLocal_.obterPalavraAleatoria()
        self.escreveLinha("Obtendo Palavra: "+palavra)

    def processo3(self):
        self._depositoSemControle_.armazenaAleatoria()
        palavra = self._depositoSemControle_.obterPalavraAleatoria()
        self.escreveLinha("Obtendo Palavra: "+palavra)

    def processo4(self):
        self._depositoLocalSemControle_.armazenaAleatoria()
        palavra = self._depositoLocalSemControle_.obterPalavraAleatoria()
        self.escreveLinha("Obtendo Palavra: "+palavra)


    def executarProcesso(self,disparado):

        for i in range(self.NUMERO_EXECUCOES):
            inicio = time.perf_counter()
            time.sleep(1)
            self.processo()
            fim = time.perf_counter()
            self.escreveLinha("(1)Rodando "+str(i)+ " Tempo: " + str(round(fim - inicio, 1)))
        self.escreveLinha("Tempo desde a chamada: " + str(round(fim - disparado, 3)))
        self.escreveLinha("Tempo total execucoes: " + str(round(fim - self._timePrimeiraExecucao_, 2)))
        self.escreveLinha("------------------------------")

    def executarProcesso2(self,disparado):
        for i in range(self.NUMERO_EXECUCOES):
            inicio = time.perf_counter()
            time.sleep(1)
            self.processo2()
            fim = time.perf_counter()
            self.escreveLinha("(2)Rodando "+str(i)+ " Tempo: " + str(round(fim - inicio, 1)))
        self.escreveLinha("Tempo desde a chamada: " + str(round(fim - disparado, 3)))
        self.escreveLinha("Tempo total execucoes: " + str(round(fim - self._timePrimeiraExecucao_, 2)))
        self.escreveLinha("------------------------------")


    def executarProcesso3(self,disparado):
        for i in range(self.NUMERO_EXECUCOES):
            inicio = time.perf_counter()
            time.sleep(1)
            self.processo3()
            fim = time.perf_counter()
            self.escreveLinha("(3)Rodando "+str(i)+ " Tempo: " + str(round(fim - inicio, 1)))
        self.escreveLinha("Tempo desde a chamada: " + str(round(fim - disparado, 3)))
        self.escreveLinha("Tempo total execucoes: " + str(round(fim - self._timePrimeiraExecucao_, 2)))
        self.escreveLinha("------------------------------")


    def executarProcesso4(self, disparado):
        for i in range(self.NUMERO_EXECUCOES):
            inicio = time.perf_counter()
            time.sleep(1)
            self.processo4()
            fim = time.perf_counter()
            self.escreveLinha("(4)Rodando " + str(i) + " Tempo: " + str(round(fim - inicio, 1)))
        self.escreveLinha("Tempo desde a chamada: " + str(round(fim - disparado, 3)))
        self.escreveLinha("Tempo total execucoes: " + str(round(fim - self._timePrimeiraExecucao_, 2)))
        self.escreveLinha("------------------------------")