class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia
    
class Carro(Motor):
    def __init__(self, marca="", potencia=0, modelo=""):
        super().__init__(marca, potencia)
        self.modelo = []
    
    def adicionar_motor(self, motor):
        self.modelo.append(motor) #adiciona motor ao carro na lista de modelos
        
    def listar_motores(self):
        for motor in self.modelo:
            print(f"Motor: {motor.marca}, Potência: {motor.potencia} HP")

#criando objetos motores

motor_v6 = Motor("Ford", 300)
motor_v8 = Motor("Chevrolet", 400)
motor_v12 = Motor("Ferrari", 700)

#criando objetos carros
carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8)
carro.adicionar_motor(motor_v12)

#Listar motores
carro.listar_motores()