total = 0
for den in range(1,51,1):
	numerador = den * 2 - 1
	total = total + numerador / den
print('Soma: {:.2f}'.format(total))