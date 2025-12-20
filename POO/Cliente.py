from Pessoas import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)  # chama o construtor da classe pai Pessoa
        self.saldo = saldo

    def informacoes(self):
        return f"{super().informacoes()} Saldo: R$ {self.saldo:.2f}." #chama o metodo informacoes da classe pai e adiciona o saldo
    
    def comprar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Compra de R$ {valor:.2f} realizada com sucesso! Novo saldo: R$ {self.saldo:.2f}."
        else:
            return "Saldo insuficiente para realizar a compra."

cliente1 = Cliente("Matheus", 30, 1000.0)
print(cliente1.informacoes())

valor = float(input('Digite o valor da compra: '))
print(cliente1.comprar(valor))