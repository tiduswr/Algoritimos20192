ordem = 5
matriz = []

for i in range(ordem):
    matriz.append([0] * ordem)

print('=' * 51)
print('{:^51}'.format('Matriz 10 x 10! '))
print('=' * 51)

for i in range(ordem):
    for j in range(ordem):
        if i < j:
            matriz[i][j] = 2*i + 7*j - 2
        if i == j:
            matriz[i][j] = (3*i)**2 - 1
        if i > j:
            matriz[i][j] = (4*i)**3 - (5*j)**2 + 1

for i in range(ordem):
    print('|', end = ' ')
    for j in range(ordem):
        print('{:^7.0f}'.format(matriz[i][j]), end = ' | ')
    print()
print('=' * 51)