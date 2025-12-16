for i in range(0, 6, 2): # 0 ate 6, de 2 em 2
    print(i)
    
i=0
while i < 5:
    print(f'Valor de i = {i}')
    i +=1
    
senha = ''
while senha != '123':
    senha = input('Digite a senha: ')
print('Senha Correta! Acesso Permitido.')