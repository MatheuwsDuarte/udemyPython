cidades = ('Sao Paulo', 'Rio', 'Salvador')

cidade = input('Digite a cidade: ')

if cidade in cidades:
    print(f' {cidade} esta na lista')
else:
    print(f'{cidade} nao esta na lista') 

print(cidades)