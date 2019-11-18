def insertM(lin, col, matriz):
	for i in range(lin):
		matriz.append([0] * col)
	return matriz

def SvalM(lin, col, matriz, func, MatrizNum):
	for i in range(lin):
		for j in range(col):
			matriz[i][j] = func(input('Matriz {} [{}][{}]: '.format(MatrizNum, i+1, j+1)))
	return matriz
	
def printM(lin, col, matriz):
	for i in range(lin):
		for j in range(col):
			print(matriz[i][j], end = ' ')
		print()

def somM(lin, col, m1, m2, m3):
	for i in range(lin):
		for j in range(col):
			m3[i][j] = m1[i][j] + m2[i][j]
	return m3

#---------------------------------------------------------------------------------------------

matriz1 = []
matriz2 = []
matrizS = []
print('=' * 50)
print('{:^50}'.format('Exercicio - Q01(13-11-2019)'))
print('=' * 50)

ordem = int(input('Ordem da Matriz: '))

print('\n*Valores Matriz 01:\n')

matriz1 = insertM(ordem, ordem, matriz1)
matriz1 = SvalM(ordem, ordem,matriz1,int, 1)

print('\n*Valores Matriz 02:\n')

matriz2 = insertM(ordem, ordem, matriz2)
matriz2 =SvalM(ordem, ordem,matriz2,int, 2)

print('\n*Resultado da Soma das Matrizes:\n')

matrizS = insertM(ordem, ordem, matrizS)
matrizS = somM(ordem, ordem, matriz1, matriz2, matrizS)

printM(ordem, ordem, matrizS)
