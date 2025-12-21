
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))


def calculoIMC(peso, altura):
    return peso / (altura ** 2)

imc = float(calculoIMC(peso, altura))

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso normal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 35:
    print("Você está com Obesidade Grau I.")
elif imc >= 35 and imc < 40:
    print("Você está com Obesidade Grau II.")
elif imc >= 40:
    print("Você está com Obesidade Grau III.")
