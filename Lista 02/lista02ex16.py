print('='*40)
print('{:^40}'.format('FRUTARIA'))
print('='*40)
print('')
kgmo = float(input('Digite quantos Kg de morangos você\ndeseja comprar: '))
kgma = float(input('Digite quantos Kg de maçãs você\ndeseja comprar: '))
print('')
kgtot = kgmo + kgma
if kgmo <= 5:
	valmo = 2.5
elif kgmo > 5:
	valmo = 2.2
	print('*Você ganhou um desconto de 30 centavos\nem cada unidade de morango por comprar\nmais que 5 Kg desta fruta!\n')
if kgma <= 5:
	valma = 1.8
elif kgma > 5:
	valma = 1.5
	print('*Você ganhou um desconto de 30 centavos\nem cada unidade de maçãs por comprar\nmais que 5 Kg desta fruta!\n')
totmo = kgmo * valmo
totma = kgma * valma
valtot = totmo + totma
if kgtot > 8 or valtot > 25:
	valtot = valtot - (valtot * 10/100)
	print('Você ganhou mais 10% de desconto por ter\ncomprado mais que 8Kg de frutas!')
print('\n Você deverá pagar R$ {:.2f} ao caixa! \n'.format(valtot))
print('='*40)
print('{:^40}'.format('Volte Sempre!'))
print('='*40)
print('')