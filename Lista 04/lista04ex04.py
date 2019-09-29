print('='*40)
print('{:^40}'.format('DESENHE UM TRAÇADO DIAGONAL!'))
print('='*40)
dim = int(input('Insira a Dimensão: '))
ch = input('Digite o Caractere: ')
for l in range(dim):
	for c in range(dim):
		if c == l:
			print(ch, end = ' ')
		else:
			print(' ', end = ' ')
	print()