print('='*50)
print('{:^50}'.format("Questão 06 Lista V"))
print('='*50)
print('\nDigite apenas valores Inteiros\n')
listA = [' ']*20
listB = [' ']*20
listDif = [' ']*20
listSom = [' ']*20
listMul = [' ']*20
print('\nDigite a lista dos primeiros valores para realizar as operações:\n')
for i in range(20):
	listA[i] = int(input('Valor {} da lista A: '.format(i+1)))
print('\nDigite a lista dos segundos valores para realizar as operações\n')
for i in range(20):
	listB[i] = int(input('Valor {} Lista B: '.format(i+1)))
for i in range(20):
	listDif[i] = listA[i] - listB[i]
	listSom[i] = listA[i] + listB[i]
	listMul[i] = listA[i] * listB[i]
print('\nDiferença (Lista A - Lista B):\n',listDif)
print('\nSoma (Lista A + Lista B):\n', listSom)
print('\nMultiplicação (Lista A x Lista B):\n', listMul)