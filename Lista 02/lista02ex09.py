print('Informe o dia da semana baseado na tabela abaixo:\n\n1 - Domingo\n2 - Segunda\n3 - Terça\n4 - Quarta\n5 - Quinta\n6 - Sexta\n7 - Sabado\n ')
num = int(input('Digite um valor: '))
while num <= 0 or num  > 7:
	num = int(input('Por favor, digite um valor especificado na tabela!! '))
if num == 1:
	print('Hoje é Domingo!')
elif num == 2:
	print('Hoje é Segunda')
elif num == 3:
	print('Hoje é Terça')
elif num == 4:
	print('Hoje é Quarta')
elif num == 5:
	print('Hoje é Quinta')
elif num == 6:
	print('Hoje é Sexta')
elif num == 7:
	print('Hoje é Sabado')