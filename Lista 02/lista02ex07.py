name = input('Insira seu nome por favor: ')
print('Olá {}, insira qual o turno que você estuda se baseando nos seguintes termos: '.format(name))
print('\nM - Matutino\nV - Vespertinoo\nN - Noturno')
turno = input(str('\nDigite a letra correspondente ao seu turno: '))
if turno == 'M' :
	print('Bom Dia, {}! '.format(name))
if turno ==  'V' :
	print('Boa Tarde, {}! '.format(name))
if turno == 'N' :
	print('Boa Noite, {}! '.format(name))