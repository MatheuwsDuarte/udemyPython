capitais = {
    'Espanha': 'madri',
    'Franca': 'paris',
    'Italia': 'roma',
    'Inglaterra': 'londres',
    'Alemanha': 'berlim'
}

pais = input('Digite o pais: ')

if pais in capitais:
    print(f' A capital da {pais} é {capitais[pais]}')
else:
    print(f' nao esta')