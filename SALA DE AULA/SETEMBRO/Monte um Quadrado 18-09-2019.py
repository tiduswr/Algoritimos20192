dimensao = int(input('Dimensão: '))
caractere = input('Caractere: ')
for i in range(dimensao):
	if i == 0 or i == (dimensao - 1):
		for j in range(dimensao):
			print(caractere, end = ' ')
		print()
	else:
		for j in range(dimensao):
			if j == 0 or j == (dimensao - 1):
				print(caractere, end = ' ')
			else:
				print(' ', end = ' ')
		print()
			