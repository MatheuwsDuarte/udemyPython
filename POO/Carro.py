class Carro:
    def __init__(self, ano, cor):
        self.ano = ano
        self.cor = cor
        self.ligado = True
        self.seta = None #vazio no início
        
    def informacoes(self):
        return f"Carro do ano {self.ano} e cor {self.cor}"
    
    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            return "Carro ligado"
        else:
            return "O carro já está ligado"
        
    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            return "Carro desligado"
        else:
            return "O carro já está desligado"
        
    def setar(self, direcao):
        if direcao not in ["esquerda", "direita"]:
            return "Direção inválida. Use 'esquerda' ou 'direita'."
        if self.ligado == False:
            return "O carro está desligado. Não é possível acionar a seta."
        self.seta = direcao
        return f"Seta para {self.seta} acionada"
    
carro1 = Carro(2020, "vermelho")
print(carro1.informacoes())
print(carro1.ligar())
print(carro1.desligar())
print(carro1.setar("esquerda"))