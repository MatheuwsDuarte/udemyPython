#classes aninhadas em Python uma classe dentro da outra

class Computador:
    def __init__(self, marca, modelo, processador, memoria, gpu, armazenamento):
        self.marca = marca
        self.modelo = modelo
        self.processador = self.Processador(processador.fabricante, processador.modelo, processador.frequencia)
        self.memoria = self.Memoria(memoria.capacidade, memoria.tipo)
        self.gpu = self.GPU(gpu.fabricante, gpu.modelo, gpu.memoria)
        self.armazenamento = self.Armazenamento(armazenamento.capacidade, armazenamento.tipo)
        
    class Processador:
        def __init__(self, fabricante, modelo, frequencia):
            self.fabricante = fabricante
            self.modelo = modelo
            self.frequencia = frequencia
        
        def detalhes(self):
            return f"Processador: {self.fabricante} {self.modelo} @ {self.frequencia}GHz"
    
    class Memoria:
        def __init__(self, capacidade, tipo):
            self.capacidade = capacidade
            self.tipo = tipo
        
        def detalhes(self):
            return f"Memória RAM: {self.capacidade}GB {self.tipo}"
        
    class GPU:
        def __init__(self, fabricante, modelo, memoria):
            self.fabricante = fabricante
            self.modelo = modelo
            self.memoria = memoria
        
        def detalhes(self):
            return f"GPU: {self.fabricante} {self.modelo} com {self.memoria}GB"
        
    class Armazenamento:
        def __init__(self, capacidade, tipo):
            self.capacidade = capacidade
            self.tipo = tipo
        
        def detalhes(self):
            return f"Armazenamento: {self.capacidade}GB {self.tipo}"
        
    def detalhes_computador(self):
        return f"{self.marca} {self.modelo}\n{self.processador.detalhes()}\n{self.memoria.detalhes()}\n{self.gpu.detalhes()}\n{self.armazenamento.detalhes()}"
    
#criando objetos das classes aninhadas
processador = Computador.Processador("Intel", "i7-10700K", 3.8)
memoria = Computador.Memoria(16, "DDR4")
gpu = Computador.GPU("NVIDIA", "RTX 3080", 10)
armazenamento = Computador.Armazenamento(512, "SSD")
computador = Computador("Dell", "Inspiron", processador, memoria, gpu, armazenamento)

#exibindo detalhes do computador
print(computador.detalhes_computador())