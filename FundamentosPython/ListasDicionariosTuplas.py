#Listas em Python

frutas = ['maçã', 'banana', 'laranja']

print(frutas)       # Imprime a lista completa
print(frutas[0])  # Acessa o primeiro elemento da lista

frutas.append('uva')  # Adiciona um elemento ao final da lista
frutas.append('abacate')  # Adiciona um elemento ao final da lista
frutas.remove('banana')  # Remove um elemento específico da lista
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
    
#Tuplas em Python, são imutaveis (os valores não mudam)

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses) # Imprime a tupla completa

#Dicionarios em Python, são estruturas de chave e valor como uma tabela

aluno = {
    'nome': 'Matheus',      
    'idade': 23,
    'curso': 'Engenharia de Computação'
}

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