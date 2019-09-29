print('='*50)
print('{:^50}'.format('CAIXA ELETRÔNICO'))
print('='*50)
cont = 0
total = 0
clientotal = 0
conv = input('Bem vindo ao caixa, digite qualquer tecla para\ncontinuar ou digite "FIM" para encerrar.  ').upper()
while conv != 'FIM':
	print('='*50)
	while conv != 'NAO':
		price = float(input('\nInsira o preço: '))
		cont = cont + price
		conv = input('\nRegistrar mais itens? Digite "NAO" para parar! ').upper()
	print('='*50)
	print('\nO valor total que esse cliente tem de pagar é de\nR$ {:.2f}. '.format(cont))
	print('='*50)
	total = total + cont
	clientotal = clientotal + 1
	cont = 0
	conv = input('\nAperte qualquer tecla para continuar, ou digite\n"FIM" para encerrar o caixa.  ').upper()
print('\nCAIXA FECHADO!!\n\n* Clientes atendidos: {}\n* Total apurado: R$ {:.2f}'.format(clientotal,total))