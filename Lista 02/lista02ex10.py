print('CALCULADORA DE EQUAÇÃO DO SEGUNDO GRAU\n-------------------------------------------\n\nForma da Equação:\n\naX^(2)+bX+c=0\n\n-------------------------------------------\n')
a = float(input('Digite o valor de "a":'))
b = float(input('Digite o valor de "b":'))
c = float(input('Digite o valor de "c":'))
print('')
if a == 0:
	print('Se "a" for igual a zero, \na equação se torna de primeiro grau! ')
if a > 0 or a < 0:
	bq = b ** 2
	delta = bq - 1*(4 * a * c)
	raizdelta = delta ** (1/2)
	bneg = -1 * b
	x1 = (bneg + raizdelta) / (2 * a)
	x2 = (bneg - raizdelta) / (2 * a)
	if delta < 0:
		print('Quando Delta é menor que zero, a equação não\nterá raizes para X!')
	elif delta > 0:
		print('Sua equação possui duas\nraizes, que são:\nX1 : {:.0f}\nX2 : {:.0f}!'.format(x1,x2))
	elif delta == 0:
		print ('Sua equação possui apenas\numa raiz que é {:.0f}!'.format(x1))