print('Saiba quantos numeros pares e inpares existem\nentre 0 ao numero que você digitar: \n')
num = int(input('Digite um numero: '))
par = 0
inpar = 0
for i in range(1,num+1,1):
	calc = i % 2
	if calc == 0:
		par = par + 1
	elif calc != 0:
		inpar = inpar + 1
print('\n'' Quantidade de Pares: ',par,'\n','Quantidade de Inpares: ',inpar)