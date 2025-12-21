
temperatura = float(input("Digite a temperatura da carne em °C: "))

if temperatura < 48:
    print('Cozinhar mais a carne.')
elif temperatura >= 48 and temperatura <54:
    ponto = "Selada"
elif temperatura in range(54, 59):
    ponto = "Ao Ponto para o mal"
elif temperatura >= 60 and temperatura <65:
    ponto = "Ao ponto"
elif temperatura >= 65 and temperatura <71:
    ponto = "Ao ponto para o bem"
elif temperatura >= 71:
    ponto = "Bem Passada"

    
print(f"O ponto da carne é: {ponto}")