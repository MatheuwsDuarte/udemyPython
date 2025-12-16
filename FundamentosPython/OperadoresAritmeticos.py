preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))  # porcentagem


print(f'Valor com Desconto = R$ {(preco - ((desconto / 100) * preco))}')