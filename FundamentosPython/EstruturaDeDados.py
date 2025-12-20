import array  # Importa a biblioteca array para trabalhar com arrays
from sys import getsizeof  # Importa a função getsizeof para verificar o tamanho em bytes de um objeto
#Listas em Python

frutas = ['maçã', 'banana', 'laranja']
numeros = [[1, 2], [3, 4, 5]] #funciona como uma matriz (2D)


fruta1, *outros = frutas

print(numeros[1][2])  # Acessa o elemento '5' na lista 'numeros'
print(frutas + numeros)  # Concatena duas listas
print(frutas.extend(numeros))  # Adiciona os elementos de 'numeros' à lista 'frutas'
print(frutas)       # Imprime a lista completa
print(frutas[0])  # Acessa o primeiro elemento da lista

frutas.append('uva')  # Adiciona um elemento ao final da lista
frutas.append('abacate')  # Adiciona um elemento ao final da lista
frutas.remove('banana')  # Remove um elemento específico da lista
frutas.insert(1, 'morango')  # Insere um elemento na posição 1
frutas.sort()  # Ordena a lista em ordem alfabética
frutas.reverse()  # Inverte a ordem da lista
frutas.pop()  # Remove o último elemento da lista

print(len(frutas))  # Imprime o tamanho da lista
print(frutas)

tarefas = []  # Cria uma lista vazia para armazenar tarefas
tarefas.append('Estudar Python')  # Adiciona uma tarefa à lista
tarefas.append('Fazer exercícios')  # Adiciona outra tarefa à lista
tarefas.append('Ler documentação')  # Adiciona mais uma tarefa à lista
print(tarefas)  # Imprime a lista de tarefas

print('Minhas Tarefas:')
i=0
while i < len(tarefas):
    print(f'Tarefa {i+1}: {tarefas[i]}')
    i += 1
    
cor_cliente = input('Digite a cor favorita do cliente: ')
cores = ['vermelho', 'azul', 'verde', 'amarelo']
valores = [10, 20, 30, 40, 50]

if cor_cliente.lower() in cores:
    print('Cor disponível!')
else:
    print('Cor não disponível.')
    
duas_listas = zip(cores, valores)  # Combina duas listas em pares de tuplas

print(list(duas_listas))  # Imprime a lista de tuplas combinada

frutas_usuario = input('Digite uma lista de frutas separadas por vírgula: ')
frutas_lista = frutas_usuario.split(', ')  # Divide a string em uma lista com base na vírgula    
print(frutas_lista)  # Imprime a lista de frutas fornecida pelo usuário

#Tuplas em Python, são imutaveis (os valores não mudam)
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses) # Imprime a tupla completa

#ARRAYS USAR QUANDO TIVER UMA LISTA MUITO GRANDE

letras = array('u', ['a', 'b', 'c', 'd', 'e'])  # Cria um array de caracteres
numeros_inteiros = array('i', [1, 2, 3, 4, 5])  # Cria um array de inteiros
numeros_float = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])  # Cria um array de floats


#Set Listas em Python, são estruturas de dados que não permitem valores duplicados
lista1 = [1, 2, 2, 3, 4, 4, 5]
lista2 = [1, 2, 3, 6, 7, 8] 
s1 = {1, 2, 2, 3, 4, 4, 5}  # Cria um set com valores duplicados

s1.discard(2)  # Remove o valor '2' do set e não dá erro se o valor não existir

conjunto1 = set(lista1)  # Converte a lista em um conjunto para remover duplicatas
conjunto2 = set(lista2)  # Converte a segunda lista em um conjunto

lista3 = lista1.diference(lista2)  # Obtém os elementos que estão em lista1 mas não em lista2
lista3 = lista1.union(lista2)  # Obtém a união dos elementos das duas listas
lista3 = lista1.intersection(lista2)  # Obtém os elementos comuns entre as
lista3 = lista1.symmetric_difference(lista2)  # Obtém os elementos que estão em uma lista ou na outra, mas não em ambas

print(conjunto1 | conjunto2)  # União dos dois conjuntos
print(conjunto1 & conjunto2)  # Interseção dos dois conjuntos
print(conjunto1 - conjunto2)  # Diferença entre os dois conjuntos
print(conjunto1 ^ conjunto2)  # Diferença simétrica entre os dois conjuntos

#Dicionarios em Python, são estruturas de chave e valor como uma tabela

aluno = {
    'nome': 'Matheus',      
    'idade': 23,
    'curso': ['Engenharia de Computação', 'Ciência de Dados'],
    'aprovado': True
}

del aluno['curso']  # Remove o par chave-valor com a chave 'curso'

aluno.update({'cidade': 'São Paulo'})  # Adiciona um novo par chave-valor ao dicionário
aluno.pop('aprovado')  # Remove o par chave-valor com a chave 'aprovado'
aluno.popitem()  # Remove o último par chave-valor adicionado ao dicionário
aluno.clear()  # Limpa todos os itens do dicionário


print(aluno.get('endereco', 'Endereço não cadastrado'))  # Imprime o valor associado à chave 'endereco' ou uma mensagem padrão se a chave não existir


print(aluno)  # Imprime o dicionário completo

aluno['idade'] = 24  # Atualiza a idade do aluno
aluno['email'] = 'matheus@exemplo.com'
print(aluno['nome'])  # Imprime o nome do aluno
print(aluno['idade'])  # Imprime a idade do aluno
print(aluno['curso'])  # Imprime o curso do aluno
print(aluno['email'])  # Imprime o email do aluno

usuario = {
    'username': input('Digite o nome do usuario: '),
    'password': input('Digite a senha: '),
    'email': input('Digite o email: ')
}

print(f'Usuario: {usuario["username"]}, Email: {usuario["email"]}')

for keys, values in usuario.items():
    print(f'{keys}: {values}')
    
    
#Lambda
lambda_soma = lambda a, b: a + b # Função lambda que soma dois números
print(lambda_soma(10, 20))

def somar(x):
    resultado = lambda x: x + 10
    return resultado(x) * 4

#map função que aplica uma função a todos os itens de um iterável (lista, tupla, etc.)

numeros = [1, 2, 3, 4, 5]

def multi(x):
    return x * 2

numeros_dobrados = map(multi, numeros)  # Aplica a função 'multi' a cada elemento da lista 'numeros'
print(list(numeros_dobrados))  # Converte o resultado para uma lista e imprime

lambda_numeros_dobrados = map(lambda x: x * 2, numeros)  # Usa uma função lambda para dobrar os números
print(list(lambda_numeros_dobrados))  # Converte o resultado para uma lista


#função filter

numeros_pares = filter(lambda x: x % 2 == 0, numeros)  # Filtra os números pares da lista 'numeros'
print(list(numeros_pares))  # Converte o resultado para uma lista e imprime

#list comprehension [expressão for item in iterable if condição]

quadrados = [x ** 2 for x in range(10)]  # Cria uma lista com os quadrados dos números de 0 a 9
print(quadrados)  # Imprime a lista de quadrados

frutas_comprehension = [item for item in frutas if 'a' in item]  # Cria uma lista com frutas que contêm a letra 'a'
print(list(frutas_comprehension))  # Imprime a lista de frutas filtradas

#Generators Expressions 

numeros_gerados = [x ** 2 for x in range(10)]  # Cria uma lista que gera os quadrados dos números de 0 a 9
print(getsizeof(numeros_gerados))  # Imprime o tamanho em bytes do generator

numeros_gerados2 = (x ** 2 for x in range(10))  # Cria um generator que gera os quadrados dos números de 0 a 9
print(getsizeof(numeros_gerados2))  # Imprime o tamanho em bytes do generator