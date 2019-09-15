print('Inverta seu Numero!\n')
num = input('Digite um inteiro: ')
numstr = str(num)
leng = len(numstr)
somastr = ''
for i in range(0, leng):
	leng = leng - 1
	somastr = somastr + numstr[leng]
print('\n',somastr)
