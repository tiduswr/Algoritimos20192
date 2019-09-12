valor = int(input('Insira um valor para o calculo de Fatorial: '))
parcial = 1
for aux in range(valor,1,-1):
	parcial = parcial * aux
print(parcial)