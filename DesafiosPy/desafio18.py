estoque = ['BMW', 'AUDI', 'CAMARO']

carroDesejado = input('Digite o carro que você deseja: ')

if carroDesejado.lower() in estoque:
    print(f'{estoque} Disponivel')
else:
    print(f'Desculpe, {carroDesejado} não disponivel')