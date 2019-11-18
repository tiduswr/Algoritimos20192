ordem = int(input('Qual a Ordem? '))
matriz = []

print()

for i in range(ordem):
	for j in range(ordem):
		matriz[i][j] = int(input('Elemento: '))

print()

for i in range(ordem-1):
	for j in range(i+1, ordem):
		matriz[i][j] = 0

print()

for i in range(lin):
	for j in range(col):
		print(matriz[i][j], end=' ')
	print()