n = int(input('Quantos fatoriais? '))
for numero in range(n):
	parcial = 1
	for i in range(numero,1,-1):
		parcial = parcial * i
	print(numero, '! =', parcial)