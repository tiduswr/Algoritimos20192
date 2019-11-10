lin = 3
col = 6
matriz = []
somaimpar = 0
media2_4 = 0

print('=' * 50)
print('{:^50}'.format('Questão 08 Lista 06!'))
print('=' * 50)

for i in range(lin):
    matriz.append([0] * col)

for i in range(lin):
    for j in range(col):
        matriz[i][j] = float(input('Matriz[{}][{}]: '.format(i+1, j+1)))


for i in range(lin):
    for j in range(col):
        if ((j + 1) % 2) > 0:
            somaimpar = somaimpar + matriz[i][j]
        if (j + 1) == 2 or (j + 1) == 4:
            media2_4 = media2_4 + matriz[i][j]
        if (j + 1) == 6:
            matriz[i][j] = matriz[i][0] + matriz[i][1]

print('=' * 50)
print('{:^50}'.format('RESULTADOS'))
print('=' * 50)

print('\n* A soma de todos os elementos das colunas Impares\né igual a: {:.2f}'.format(somaimpar))
print('* A media de todos os elementos da Segunda e Quarta\ncoluna é igual a: {:.2f}\n'.format(media2_4/(lin*2)))
print('Matriz Modificada:\n')

for j in range(col):
    print('|','{:^8}'.format('Coluna_'+str(j+1)), end = ' ')
    if (j + 1) == col:
        print('|', end = '')
print()

for i in range(lin):
    for j in range(col):
        print('|', '{:^8.2f}'.format(matriz[i][j]), end = ' ')
        if (j + 1) == col:
            print('|', end = '')
    print()