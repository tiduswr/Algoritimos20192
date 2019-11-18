def potencia(base, expoente):
	AUX = 1
	for i in range(expoente):
		AUX = AUX * base
	return AUX

print('Modelo de Equação: \nX^(A) + X^(B)\n\nRepasse os Valores:')

x = int(input('X: '))
y = int(input('Y: '))
a = int(input('A: '))
b = int(input('B: '))

res = potencia(x, a) + potencia(y, b)

print('\n', 'Resultado = ',res)
