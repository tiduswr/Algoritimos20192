parcial = 1
valor = int(input('Insira uma valor para o calculo de fatorial: '))
while valor > 1:
	parcial = parcial * valor
	valor = valor - 1
print('O fatorial é igual a ', parcial)
	