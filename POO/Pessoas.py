class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos."

