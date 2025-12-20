class Animal:
    def __init__(self, name, cor, especies):
        self.name = name
        self.cor = cor
        self.especies = especies
        
    def apresentar(self):
        return f"Nome: {self.name}, Cor: {self.cor}, Espécie: {self.especies}"
    
