class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Cargo: {self.cargo}."

    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        return f"{self.nome} foi promovido(a) para {self.cargo}."
    
    def aniversario(self):
        self.idade += 1
        return f"Feliz aniversário, {self.nome}! Parabéns pelos seus {self.idade} anos."


pessoa1 = Pessoa("Ana", 30, "Engenheira Jr")
pessoa2 = Pessoa("Bruno", 25, "Designer Jr")
print(pessoa1.promover("Engenheira Pleno"))   
print(pessoa2.aniversario())
print(pessoa1.informacoes())
print(pessoa2.informacoes())