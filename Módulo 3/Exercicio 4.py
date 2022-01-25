class Pessoa():
    def __init__(self,nome,idade, peso, altura):
        self.nome = nome
        self.idade  = idade
        self.peso = peso
        self.altura = altura

    def crescer(self,valor):
        self.altura += valor
        return self.altura

    def envelhecer(self,valor):
        self.idade+=valor
        if self.idade<21:
            self.crescer(valor*0.5)
        return self.idade

    def engordar(self,valor):
        self.peso += valor
        return self.peso

    def emagrecer(self,valor):
        self.peso -= valor
        return self.peso
    

a = Pessoa("Carlos",14,38,164)
envelheceu = a.envelhecer(5)
print("{0} Envelheceu e agora tem {1} anos, e tem {2}cm de altura".format(a.nome, a.idade, a.altura))
engordou = a.engordar(3)
print("{0} agora engordou e pesa {1}Kg".format(a.nome,engordou))
emagreceu = a.emagrecer(2)
print("{0} agora emagreceu e pesa {1}Kg".format(a.nome,emagreceu))
cresceu = a.crescer(3)
print("{0} agora cresceu e mede {1}cm".format(a.nome,cresceu))