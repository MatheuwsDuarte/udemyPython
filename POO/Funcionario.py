from Pessoas import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade) #chama o construtor da classe pai Pessoa
        self.cargo = cargo
    
    def trabalhar(self):
        return f"{self.nome} está trabalhando como {self.cargo}."

funcionario1 = Funcionario("Ana", 30, "Engenheira Jr")
print(funcionario1.trabalhar())