lin = 4
col = 5
mtz = []
for i in range(lin):
	mtz.append([0] * col)
mtz[1][2] = 9

for i in range(lin):
	for j in range(col):
		print(mtz[i][j], end = ' ')
	print()