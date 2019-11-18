lin = int(input('Linhas: '))
col = int(input('Colunas: '))
M = []

for i in range(lin):
	M.append([0] * col)

print()

for i in range(lin):
	for j in range(col):
		M[i][j] = int(input('Matriz[{}][{}]: '.format(i+1,j+1)))

l1 = int(input('\nQuer trocar que linha? '))
l2 = int(input('\nPor qual linha? '))

for i in range(col):
	aux = M[l1-1][i]
	M[l1-1][i] = M[l2-1][i]
	M[l2-1][i] = aux

print('\nMatriz atual:\n')

for i in range(lin):
	for j in range(col):
		print(M[i][j], end=' ')
	print()