print('='*50)
print('{:.^50}'.format('Lojas Tabajara'))
print('='*50)
prod = 1
soma = 0
i = 1
while prod != 0:
	prod = float(input('Produto {}: R$ '.format(i)))
	i = i + 1
	soma = soma + prod
print('Total a pagar: R$',soma)
valpago = float(input('Quanto o cliente pagou? '))
if valpago > soma:
	troco = valpago - soma
	print('Ele recebera R$ {:.2f} de troco.'.format(troco))
else:
	print('Não será necessario troco!')
print('='*50)
print('{:.^50}'.format('Obrigado!'))
print('='*50)