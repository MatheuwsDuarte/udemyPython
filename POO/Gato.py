from Animal import Animal

class Gato(Animal):  #heranca da classe Animal
    pass #aqui nao tem nada a mais, entao ele herda tudo da classe Animal

    def miar(self):
        return "Miau!"
    

gato1 = Gato("Mingau", "Branco", "Persa")
print(gato1.apresentar())
print(gato1.miar())