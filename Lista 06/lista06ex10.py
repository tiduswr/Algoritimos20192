print('=' * 56)
print('{:^56}'.format('TRIANGULO PASCAL'))
print('=' * 56)

tam = int(input('Insira o Tamanho do Triangulo: '))
pascal = []

for i in range(tam):
    pascal.append([])
    pascal[i].append(1)
    if i > 0:
        for j in range(1,i):
            pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
    if tam != 0:
        if i != 0:
            pascal[i].append(1)

for i in range(tam):
    for j in range(len(pascal[i])):
        print(pascal[i][j], end = ' ')
    print()

print('=' * 56)
print('{:^56}'.format('FIM'))
print('=' * 56)