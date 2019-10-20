print('='*50)
print('{:^50}'.format("Valores Pares e Inpares"))
print('='*50)
print()
N = int(input('Qual o Tamanho da lista?(Valor Inteiro): '))
Par = N // 2
Inpar = N // 2 + (N % 2)
listA = [' ']*N
listPar = [' ']*N
listInpar = [' ']*N
for i in range(N):
	listA[i] = int(input('Valor {} da lista:  '.format(i+1)))
for i in range(N):
	if listA[i] % 2 == 0:
		listPar[i] = listA[i]
	if listA[i] % 2 != 0:
		listInpar[i] = listA[i]
cond = 0
for i in range(N):
		if listPar[i] != ' ':
			cond = True
for i in range(N):
		if listPar[i] != ' ':
			if cond == True:
				print('\nLista de Valores Par:\n')
				cond = False
			print(listPar[i], end = ' ')
for i in range(N):
		if listInpar[i] != ' ':
			cond = True
for i in range(N):
		if listInpar[i] != ' ':
			if cond == True:
				print('\nLista de Valores Inpar:\n')
				cond = False
			print(listInpar[i], end = ' ')