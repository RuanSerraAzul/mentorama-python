from cgi import print_directory


class ContaCorrente():
    def __init__(self,numero_da_conta,nome_correntista,*saldo):
        self.numero_da_conta = numero_da_conta
        self.nome_correntista = nome_correntista
        self.saldo = 0

    def alterarNome(self,nome):
        self.nome_correntista = nome
        print("Nome do Correntista: {}".format(self.nome_correntista))

    def saque(self,valor):
        self.saldo -= valor
        print("Você sacou {} reais, você agora tem {} R$ em conta".format(valor,self.saldo))
        if self.saldo<0:
            print("Seu saldo está negativo. Entre em contato com sua agência para regularizarmos sua situação.")

    def deposito(self,valor):
        self.saldo += valor
        print("Você depositou {} reais, você agora tem {} R$ em conta".format(valor,self.saldo))



a = ContaCorrente("0123432","Carlos Souza")
a.deposito(100)
a.saque(50)
a.alterarNome("Mauricio Silvestre")