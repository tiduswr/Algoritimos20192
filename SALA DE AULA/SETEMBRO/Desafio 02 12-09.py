val = float(input('Insira um valor: '))
soma = val
pos = 0
neg = 0
while val != 0:
	if val > 0:
		pos = pos + 1
	if val < 0:
		neg = neg + 1
	val = float(input('Insira um valor: '))
	soma = soma + val
print('Soma: ',soma)
print('Positivos: ',pos)
print('Negativos: ',neg)
	