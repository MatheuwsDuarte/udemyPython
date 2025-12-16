from FuncoesExemplos import saudacao, soma, calcular_Desconto #importar funções de outro arquivo
#import FuncoesExemplos #importar o arquivo inteiro

saudacao('Ana', 30)

resultado_soma = soma(10, 15)
print(f'O resultado da soma é: {resultado_soma}')

preco_produto = float(input('Digite o valor do produto: '))
desconto_produto = float(input('Digite o valor do desconto (%): ')) 
preco_com_desconto = calcular_Desconto(preco_produto, desconto_produto)
print(f'Preço com desconto: R$ {preco_com_desconto:.2f}')