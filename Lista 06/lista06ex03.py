ordem = 5
matriz = []
matriz2 = []
matrizfinal = []

for i in range(ordem):
    matriz.append([0] * ordem)
    matriz2.append([0] * ordem)
    matrizfinal.append([0] * ordem)

print('=' * 50)
print('{:^50}'.format('Solicitação de Matriz 01'))
print('=' * 50)
for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = float(input('Valor Matriz 1 - Linha{} | Coluna {}: '.format(i+1, j+1)))
print('=' * 50,'\n')

print('=' * 50)
print('{:^50}'.format('Solicitação de Matriz 02'))
print('=' * 50)
for i in range(ordem):
    for j in range(ordem):
        matriz2[i][j] = float(input('Valor Matriz 2 - Linha{} | Coluna {}: '.format(i+1, j+1)))
print('=' * 50,'\n')

for i in range(ordem):
    for j in range(ordem):
        if matriz[i][j] >= matriz2[i][j]:
            matrizfinal[i][j] = matriz[i][j]
        else:
            matrizfinal[i][j] = matriz2[i][j]
print('\nMATRIZ COM MAIORES VALORES COMPARADOS POR POSIÇÃO:\n')

for i in range(ordem):
    print('|', end = ' ')
    for j in range(ordem):
        print('{:^5.0f}'.format(matrizfinal[i][j]), end = ' | ')
    print()