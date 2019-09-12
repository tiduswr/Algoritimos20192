print('Saiba quanto você gastou em sua coleção de CDs\n')
cdqt = int(input('Quantos CDs você tem em sua coleção? '))
soma = 0
print('')
for i in range(cdqt):
	price = float(input('Preço do CD: '))
	soma = soma + price
media = soma / cdqt
print('\nVocê gastou aproximadamente R$ {:.2f} em cada CD!'.format(media))
	