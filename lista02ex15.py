print('='*40)
print('{:^40}'.format('Abasteça seu Veiculo!'))
print('='*40)
palc = 3.4
pgas = 4.5
cesc = input('Qual o combustivel que você deseja\ncomprar?\n\nDigite "A" para Alcool\nDigite "G" para Gasolina\n\n')
if cesc == 'A' or cesc == 'a':
	print('\nVocê escolheu a opção Alcool!\n ')
	cqtd = float(input('Quantos litros você deseja colocar? '))
	if cqtd <= 20:
		valalcb = cqtd * palc
		valalc = valalcb - (valalcb * 3/100)
		print('\nVocê recebeu um desconto de 3% na sua\nconta de R$ {:.2f}, o novo valor é\nR$ {:.2f}. '.format(valalcb,valalc))
	if cqtd > 20:
		valalcb = cqtd * palc
		valalc = valalcb - (valalcb * 5/100)
		print('\nVocê recebeu um desconto de 5% na sua\nconta de R$ {:.2f}, o novo valor é\nR$ {:.2f}. '.format(valalcb,valalc))
if cesc == 'G' or cesc == 'g':
	print('\nVocê escolheu a opção Gasolina!\n')
	cqtd = float(input('Quantos litros você deseja colocar? '))
	if cqtd <= 20:
		valgasb = cqtd * pgas
		valgas = valgasb - (valgasb * 4/100)
		print('\nVocê recebeu um desconto de 4% na sua\nconta de R$ {:.2f}, o novo valor é\nR$ {:.2f}. '.format(valgasb,valgas))
	if cqtd > 20:
		valgasb = cqtd * pgas
		valgas = valgasb - (valgasb * 6/100)
		print('\nVocê recebeu um desconto de 6% na sua\nconta de R$ {:.2f}, o novo valor é\nR$ {:.2f}. '.format(valgasb,valgas))
else:
	print('Você não digitou um valor valido! ')
print('')
print('='*40)
print('{:^40}'.format('Obrigado por comprar conosco! '))
print('='*40)