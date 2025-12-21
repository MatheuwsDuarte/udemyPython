funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

Lista1 = set(turno_noite) & set(tem_carro)
Lista2 = set(tem_carro).intersection(turno_dia)
Lista3 = set(funcionarios) - set(tem_carro)

print(Lista1)  # Imprime os funcionários que trabalham no turno da noite e têm carro
print(Lista2)  # Imprime os funcionários que trabalham no turno do dia e têm carro
print(Lista3)  # Imprime os funcionários que não têm carro