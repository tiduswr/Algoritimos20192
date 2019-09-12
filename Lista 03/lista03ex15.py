print('Verifique se seu numero é primo!')
primo = True
valor = int(input('\nDigite um numero inteiro: '))
for i in range(2,valor,1):
	if valor%i == 0:
		primo = False
if primo:
	print('\nSeu numero é primo! ')
else:
	print('\nSeu numero não é primo! ')
	