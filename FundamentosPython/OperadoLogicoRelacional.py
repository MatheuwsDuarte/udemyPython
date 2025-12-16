valorPorcao = float(input('Digite o valor da porção: '))
quantidade = int(input('Digite a quantidade consumida por dia: '))

print(f' Vai durar: {int(valorPorcao / quantidade)} dias')
print(f' Vai durar: {(valorPorcao / quantidade):.5f} dias')

idade = int(input('Digite sua idade: '))
carteira = True

#AND e um e outro
#OR ou um ou outro
#NOT não nenhum dos dois

if(idade >=18 and carteira == True):
    print(' Ja pode tirar a habilitacao!')
else:
    print(' Ainda nao pode tirar a habilitacao.')
