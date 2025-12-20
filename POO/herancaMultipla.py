from Animal import Animal

#Classes pai
class Predador(Animal):
    def caçar(self):
        return f" O {self.name} está caçando..."

class Presa(Animal):
    def fugir(self):
        return f" O {self.name} está fugindo..."
    
#Classes filhas
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass

coelho1 = Coelho("Coelho Branco", "Branco", "Angorá")

print(coelho1.fugir())

tigre1 = Tigre("Tigre", "Laranja", "Curto")
print(tigre1.caçar())

golfinho1 = Golfinho("Golfinho", "Cinza", "Curto")
print(golfinho1.caçar())
print(golfinho1.fugir())