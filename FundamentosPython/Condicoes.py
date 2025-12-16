nota_aluno = float(input('Digite a nota do aluno: '))

if(nota_aluno >= 7):
    print(' Aluno Aprovado!')
elif(nota_aluno >= 5 and nota_aluno < 7):
    print(' Aluno em Recuperacao!')
else:
    print(' Aluno Reprovado!')
    
usuario = input('Digite o nome do usuario: ')
senha = input('Digite a senha: ')

if(usuario == 'admin' and senha == '1234'):
    print(' Acesso Permitido!')
    print(' Carregando sistema...')
else:
    print(' Acesso Negado!')
    
idade = int(input('Digite sua idade: '))
autorizacao_pais = input('Voce tem autorizacao dos pais? (sim/nao): ')

if(idade >= 18):
    print(' Entrada Permitida!')
elif(idade >= 16 and autorizacao_pais.lower() == 'sim'):
    print(' Entrada Permitida com Autorizacao dos Pais!')
else:
    print(' Entrada Negada!')