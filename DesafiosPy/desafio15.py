frutas = []

for fruta in range(0, 3):
    frutas.append('Maca')

frutas.append('Banana')
frutas.append('Uva')
cont = 0


for fruta in frutas:
    if fruta == 'Maca':
        cont += 1
        
print(frutas)
print(f' maca aparece {cont} vezes')




