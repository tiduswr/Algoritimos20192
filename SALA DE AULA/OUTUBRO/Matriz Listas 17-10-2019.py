linhas = int(input('Linhas: '))
colunas = int(input('Colunas: '))
matriz = []
for i in range(linhas):
	matriz.append([0]*colunas)
for i in range(linhas):
	for j in range(colunas):
		matriz[i][j] = int(input('Matriz Posição [{}] [{}]'.format(i+1, j+1)))
linV = 0
colV = 0
mai = matriz[0][0]
for i in range(linhas):
	for j in range(colunas):
		if matriz[i][j] > mai:
			mai = matriz[i][j]
			linV = i
			colV = j
print('Maior Valor: {} - Linha {} e Coluna {}'.format(mai, linV, colV))