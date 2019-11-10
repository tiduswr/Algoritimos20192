ordem = 0
matriz = []
soma = 0

print('=' * 50)
print('{:^50}'.format('Calculo dos Numeros acima da Diagonal Principal! '))
print('=' * 50)

ordem = int(input('Insira a Ordem da Matriz: '))

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = float(input('Matriz[{}][{}]: '.format(i+1, j+1)))

for i in range(ordem):
    for j in range(ordem):
        if j > i:
            soma = soma + matriz[i][j]

print('\n','A soma dos Numeros acima da diagonal principal é\nigual a',soma)
print('=' * 50)
print('{:^50}'.format('Fim do Programa!'))
print('=' * 50)