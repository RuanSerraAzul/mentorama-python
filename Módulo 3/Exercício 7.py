class TV():
    def __init__(self,canal,volume):
        self.canal = canal
        self.volume = volume
        print("TV Ligada.")

    def mudarCanal(self,valor):
        self.canal = valor
        print("Canal selecionado: {}".format(valor))
        if self.canal>100 or self.canal<0:
            print("Canal inválido, o canal voltará para o canal padrão.")
            self.canal = 10
            
    
    def aumentarVolume(self):
        self.volume+=1
        if self.volume>100:
            print("Erro, volume não pode ser maior que 100")
            self.volume=100
        print("Volume atual: {}".format(self.volume))
        

    def diminuirVolume(self):
        self.volume-=1
        if self.volume<0:
            print("Erro, volume não pode ser menor que 0")
            self.volume=100
        print("Volume atual: {}".format(self.volume))
    

televisao = TV(10,0)
televisao.mudarCanal(12)
televisao.aumentarVolume()
televisao.aumentarVolume()
televisao.aumentarVolume()
televisao.aumentarVolume()
televisao.aumentarVolume()
