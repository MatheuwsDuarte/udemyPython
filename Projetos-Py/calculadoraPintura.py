rendimento = float(input("Digite o rendimento da tinta (m²/L): "))
Largura = float(input("Digite a largura da parede (m): "))
Comprimento = float(input("Digite o comprimento da parede (m): "))

def calcularArea():
    area = Largura * Comprimento
    return area / rendimento


print(f"Área da parede: {calcularArea()} m²")
