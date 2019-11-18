print('MATRIZ IDENTIDADE:\n')
ordem = int(input('Ordem: '))
print()
m = []
for i in range(ordem):
		m.append([0]*ordem)
for i in range(ordem):
	m[i][i] = 1
for i in range(ordem):
	for j in range(ordem):
		print(m[i][j], end = ' ')
	print()