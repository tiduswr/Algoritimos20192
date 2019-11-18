lin = 3
col = 4
mtz1 = []
mtz2 = []
mtzsom = []
for i in range(lin):
	mtz1.append([0] * col)
	mtz2.append([0] * col)
	mtzsom.append([0] * col)
for j in range(lin):
	for k in range(col):
		mtz1[j][k] = int(input('Matriz 01 Posição[{}][{}]: '.format(j+1, k+1)))
print()
for j in range(lin):
	for k in range(col):
		mtz2[j][k] = int(input('Matriz 02 Posição[{}][{}]: '.format(j+1, k+1)))
for j in range(lin):
	for k in range(col):
		mtzsom[j][k] = mtz1[j][k] + mtz2[j][k]
print()
for j in range(lin):
	for k in range(col):
		print('|', mtzsom[j][k], '|', end = ' ')
	print()