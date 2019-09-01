print('{:=^55}'.format('INVESTIGAÇÃO'))
print('Serão feitas algumas perguntas para você, reponda da\nsegiuinte forma:\n\n*Use 1 para SIM\n*Use 2 para NÃO\n\n')
qtdsim = 0
p1 = int(input('Você Telefonou para a vitima? '))
p2 = int(input('Esteve no local do crime? '))
p3 = int(input('Mora perto da vítima? '))
p4 = int(input('Devia para a vítima? '))
p5 = int(input('Já trabalhou com a vítima? '))
if p1 == 1:
	qtdsim += 1
if p2 == 1:
	qtdsim += 1
if p3 == 1:
	qtdsim += 1
if p4 == 1:
	qtdsim += 1
if p5 == 1:
	qtdsim += 1
if qtdsim >= 1:
	print('\nVocê respondeu positivamente a {} perguntas!'.format(qtdsim))
elif qtdsim == 0:
	print('\nVocê respondeu negativamente a todas as perguntas!')
if qtdsim == 2:
	print('\nVocê é suspeita de estar envolvida no crime!')
elif qtdsim > 2  and qtdsim < 5:
	print('\nVocê esta enquadrado(a) como Cumplice! ')
elif qtdsim == 5:
	print('\nVocê é culpado(a)!!')
else:
	print('\nVocê é inocente! ')
print('\n{:=^55}'.format('FORMULARIO ENCERRADO'))
