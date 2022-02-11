class Carro:
    def __init__(self,modelo,cor,motor,tanque):
        self.modelo = modelo
        self.cor = cor
        self.motor = motor
        self.tanque  = tanque
    def exibe(self):
        print("O modelo do carro é {0}, sua cor é {1} e o seu motor funciona à {2} e tem {3} litros no tanque \n".format(self.modelo,self.cor,self.motor,self.tanque))
    def mudaCor(self,cor):
        self.cor = cor
        print("O carro {0} agora é da cor {1}".format(self.modelo,self.cor)) 
    def encherTanque(self,valor):
        self.tanque += valor
        print("Você abasteceu e agora o carro {0} está com {1} litros no tanque \n".format(self.modelo,self.tanque))
    def rodar(self,valor):
        self.tanque -= valor
        print("Você rodou {0} kms em seu {1} agora o carro tem {2} litros".format(valor,self.modelo,self.tanque))
        if self.tanque<=4:
            print("Sua gasolina está baixa, considere encher o tanque \n")
            ####Programa####
onix = Carro("Ônix","prata","diesel",10)
onix.exibe()

hb20 = Carro("HB20","Preto", "Gasolina", 4)
hb20.rodar(2)
hb20.encherTanque(10)

wrx2005 = Carro("WRX 2005", "Azul", "gasolina", 7)
wrx2005.exibe()
wrx2005.mudaCor("roxo")