print('='*40)
print('{:^40}'.format('Triangulo Retângulo - Base para Baixo!'))
print('='*40)
dim = int(input('Insira a Dimensão: '))
ch = input('Digite o Caractere: ')
print()
for l in range(1,dim+1,1):
	for c in range(1,dim+1,1):
		if l >= c:
			print(ch, end = ' ')
		else:
			print(' ', end = ' ')
	print()