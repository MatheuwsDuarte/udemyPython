import math #importar biblioteca matemática

print(math.sqrt(16)) #usar função da biblioteca

def saudacao(nome, idade):#definir uma função
    return print(f'Olá, {nome}! Seja bem-vindo ao curso de Python! Você tem {idade} anos. ')

#xargs
def soma(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

def calcular_Desconto(preco, desconto):
    return preco - ((desconto / 100) * preco)

#varios argumentos nomeados
def agencia(**carro):
    return f'Carro alugado: {carro["marca"]}, Cor: {carro["cor"]}, Placa: {carro["placa"]}'

print(agencia(marca='BMW', cor='Branca', placa='1.0'))