from DADOS import Pessoa
class Visual:
    def lePessoa(self):
        nome  = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        pessoa = Pessoa(nome,idade)
        return pessoa
    def mostrePessoa(self,p):
        print(p.modoApresentacao())