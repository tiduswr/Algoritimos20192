pal1 = input('Palavra: ')
pal2 = input('Outra Palavra: ')
while pal1 <= pal2 and pal2 != 'fim':
	pal1 = pal2
	pal2 = input('Outra palavra: ')
if pal2 == 'fim':
	print('Parabéns você acertou. Como foi pedido,\nestamos encerrando o programa.')
else:
	print('Tente outra vez!!')