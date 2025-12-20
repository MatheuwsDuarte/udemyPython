try:
    indice = int(input("Digite um índice para acessar a lista: "))
    letras = ['a', 'b', 'c', 'd', 'e']  # Cria uma lista de caracteres
    print(f'Letra na posição {indice}: {letras[indice]}')
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("Execução do bloco try-except finalizada.")
