def fatorial(numero):
    if numero == 0 or numero ==1:
        return 1
    else:
        return numero * fatorial(numero-1)

    
numero = int(input('digite um numero:'))
resultado = fatorial(numero)

print(f' O fatorial de {numero} e: {resultado}')