print('='*40)
print('{:^40}'.format('DESENHE UM QUADRADO!'))
print('='*40)
dim = int(input('Digite a Dimensão do quadrado: '))
ch = input('Digite o Caractere: ')
print()
for l in range(dim):
	print(('{} '.format(ch))*dim)