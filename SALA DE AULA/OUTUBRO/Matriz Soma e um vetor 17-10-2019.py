linhas = int(input('Linhas: '))
colunas = int(input('Colunas: '))
matriz = []
for i in range(linhas):
	matriz.append([0]*colunas)
for i in range(linhas):
	for j in range(colunas):
		matriz[i][j] = int(input('Matriz Posição [{}] [{}]'.format(i+1, j+1)))
vetor = [0] * colunas
for i in range(colunas):
	for j in range(linhas):
		vetor[i] = vetor[i] + matriz[j][i]
print('\nVetor da Soma das colunas da Matriz digitada:\n', vetor)