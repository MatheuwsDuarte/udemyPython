class Personagem:
    def atacar(self):
        return "O personagem ataca!"

class Guerreiro(Personagem):
    def atacar(self):
        return "O guerreiro ataca com uma espada!"
    
class Mago(Personagem):
    def atacar(self):
        return "O mago lança uma bola de fogo!"

class Arqueiro(Personagem):
    def atacar(self):
        return "O arqueiro dispara uma flecha!"
    
#criar objetos

guerreiro = Guerreiro()
mago = Mago()
arqueiro = Arqueiro()

personagens = [guerreiro, mago, arqueiro]

for p in personagens:
    print(p.atacar())
    
#sem herança

class Cachorro:
    def som(self):
        return "O cachorro late!"
    
class Gato:
    def som(self):
        return "O gato mia!"
    
cachorro = Cachorro()
gato = Gato()

animais = [cachorro, gato]

for a in  animais:
    print(a.som())