print('='*40)
print('{:^40}'.format('DESENHE UM X!'))
print('='*40)
dim = int(input('Insira a Dimensão: '))
ch = input('Digite o Caractere: ')
print()
for l in range(1,dim+1,1):
	for c in range(1,dim+1,1):
		if c == l:
			print(ch, end = ' ')
		elif l + c == (dim + 1):
			print(ch, end = ' ')
		else:
			print(' ', end = ' ')
	print()