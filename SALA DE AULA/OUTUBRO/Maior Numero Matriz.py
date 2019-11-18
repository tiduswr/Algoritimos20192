lin = int(input('Linhas: '))
col = int(input('Colunas: '))
M = []

for i in range(lin):
	M.append([0] * col)

print()

for i in range(lin):
	for j in range(col):
		M[i][j] = int(input('Matriz[{}][{}]: '.format(i+1,j+1)))