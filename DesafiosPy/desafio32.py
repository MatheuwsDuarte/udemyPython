lambda_quadrado = lambda n: n**2

numeros = [1, 2, 3, 4, 5]
resultados = []

for i in numeros:
    resultados.append(lambda_quadrado(i))
  
print(f'Os quadrados dos numeros {numeros} são {resultados}')