num = int(input('Digite um valor (0 para interromper): '))
cont = 1
soma = 0
while num != 0:
	soma = soma + num
	num = int(input('Digite outro valor (0 para interromper)'))
	cont = cont + 1
cont = cont - 1
med = soma / cont
print('Foram digitados', cont,'valores.')
print('A média dos numeros digitados é igual a: ',med)