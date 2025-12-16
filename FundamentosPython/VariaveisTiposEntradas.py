nome = 'matheus' #string
altura = float(1.72)  #float
mensagem = 'Bom Dia' #string
professor = True    #booleanod


print(mensagem,' ',nome)
sobrenome = input('Digite seu sobrenome: ')
print(nome + ' ' + sobrenome)  
idade = int(input('Digite sua idade: '))
print(type(altura))
print(type(idade))


#F-String
print(f'Seu nome completo e: {nome} {sobrenome} e voce tem {int(idade)} anos.')
print(f'Sua idade daqui 2 anos sera: {idade + 2}')